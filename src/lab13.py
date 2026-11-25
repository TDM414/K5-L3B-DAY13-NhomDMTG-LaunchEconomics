"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau_hai_ti_le(p1, p2, alpha, power):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ, kiểm định hai phía."""
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    do_lech_gop = math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
    do_lech_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * do_lech_gop + z_power * do_lech_rieng) / (p2 - p1)) ** 2)


def in_ke_hoach_pilot(reqs):
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize

    baseline, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    nhan_vien_moi_nhom, depot_moi_nhom = 20, 6
    yeu_cau_moi_nguoi = 75

    n_5_diem = co_mau_hai_ti_le(baseline, 0.75, alpha, power)
    de_75 = 1 + (yeu_cau_moi_nguoi - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * de_75)
    so_nhan_vien_can = math.ceil(n_theo_nhan_vien / yeu_cau_moi_nguoi)
    tran_nhan_vien = nhan_vien_moi_nhom / icc
    tran_depot = depot_moi_nhom / icc

    n_6_diem = co_mau_hai_ti_le(baseline, 0.76, alpha, power)
    # Giải c*m / (1 + (m - 1)*ICC) >= n hiệu dụng để tìm m tối thiểu.
    m_toi_thieu = math.ceil(n_6_diem * (1 - icc) / (nhan_vien_moi_nhom - n_6_diem * icc))
    de_pilot = 1 + (m_toi_thieu - 1) * icc
    n_thuc_pilot = nhan_vien_moi_nhom * m_toi_thieu
    n_hieu_dung = n_thuc_pilot / de_pilot
    power_5_diem = NormalIndPower().power(
        abs(proportion_effectsize(baseline, 0.75)), nobs1=n_6_diem, alpha=alpha,
    )

    print('\nD1 cỡ mẫu mỗi nhóm')
    print(f'a) Theo yêu cầu, +5 điểm phần trăm: {n_5_diem:,} yêu cầu')
    print(f'b) Theo nhân viên, m={yeu_cau_moi_nguoi}: DE={de_75:.2f}, {n_theo_nhan_vien:,} yêu cầu, '
          f'{so_nhan_vien_can} người, tổng {2 * so_nhan_vien_can} người')
    print(f'c) {nhan_vien_moi_nhom} nhân viên: n hiệu dụng < {tran_nhan_vien:,.0f}')
    print(f'd) {depot_moi_nhom} depot: n hiệu dụng < {tran_depot:,.0f}')
    print(f'e) +6 điểm phần trăm: cần {n_6_diem} yêu cầu hiệu dụng, m tối thiểu={m_toi_thieu}, '
          f'DE={de_pilot:.2f}, {n_thuc_pilot:,} yêu cầu thực, n hiệu dụng={n_hieu_dung:.2f}')
    print(f'   Với tác động thật +5 điểm phần trăm, power xấp xỉ {power_5_diem:.1%}')

    print('\nD3 đối chiếu dữ liệu chạy thử')
    reqs_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    for pham_vi, mau in [('toàn bộ', reqs), ('noi_dia + hang_nang', reqs_pilot)]:
        mo_lai = mau['mo_lai_trong_7_ngay'].sum()
        print(f'Mở lại 7 ngày ({pham_vi}): {mo_lai}/{len(mau)} = {mo_lai / len(mau):.2%}')
    da_xem_lai = reqs_pilot[reqs_pilot['duoc_xem_lai'] == 1]
    bo_qua = da_xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
    print(f'Bỏ qua gợi ý (noi_dia + hang_nang): {bo_qua}/{len(da_xem_lai)} = {bo_qua / len(da_xem_lai):.2%}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3 theo loại yêu cầu')
    for loai in reqs['loai'].unique():
        reqs_loai = reqs[reqs['loai'] == loai]
        runs_loai = runs[runs['request_id'].isin(reqs_loai['request_id'])]
        kq = mo_hinh(runs_loai, reqs_loai)
        print(f'{loai:12s} so_yeu_cau={len(reqs_loai):4d} thanh_cong={kq["thanh_cong"]:4d} '
              f'ti_le={kq["thanh_cong"] / len(reqs_loai):.4f} '
              f'lan_chay={len(runs_loai) / len(reqs_loai):.4f} cps={kq["cps"]:,.0f}')

    print('\nB1 độ nhạy')
    kich_ban = [
        ('gia_token_x2', dict(gia_vao=52, gia_ra=260)),
        ('gia_token_1_2', dict(gia_vao=13, gia_ra=65)),
        ('xem_lai_x2', dict(he_so_xem_lai=2)),
        ('xem_lai_1_2', dict(he_so_xem_lai=0.5)),
        ('lam_lai_x2', dict(he_so_lam_lai=2)),
        ('lam_lai_1_2', dict(he_so_lam_lai=0.5)),
        ('luong_x1_25', dict(luong_phut=2500)),
        ('max_2', dict(max_lan_chay=2)),
        ('max_1', dict(max_lan_chay=1)),
    ]
    for ten, thay_doi in kich_ban:
        kq = mo_hinh(runs, reqs, **thay_doi)
        print(f'{ten:16s} cps={kq["cps"]:,.0f} thay_doi={(kq["cps"] / ket_qua["cps"] - 1) * 100:+.1f}%')

    print('\nB2')
    kq_b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f'gia_token_x2 + xem_lai_x2: cps={kq_b2["cps"]:,.0f} thay_doi={(kq_b2["cps"] / ket_qua["cps"] - 1) * 100:+.1f}%')

    print('\nB3 giới hạn chạy lại')
    for gioi_han in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        chi_phi_he_thong = kq['tong'] + khong_thanh_cong * BASELINE
        print(f'{gioi_han} lan: tong={kq["tong"]:,.0f} khong_thanh_cong={khong_thanh_cong} '
              f'ca_he_thong={chi_phi_he_thong:,.0f} cps={kq["cps"]:,.0f}')

    in_ke_hoach_pilot(reqs)
