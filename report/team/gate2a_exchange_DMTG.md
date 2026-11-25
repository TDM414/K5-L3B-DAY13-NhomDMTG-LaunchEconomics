# Hồ sơ trao đổi duyệt chéo Gate 2a · Nhóm DMTG (Lớp L3B)

> Bản trao đổi gửi JQKA; không thay thế các hồ sơ nộp chính trong `report/team/`.

- **Repo nhóm:** https://github.com/TDM414/K5-L3B-DAY13-NhomDMTG-LaunchEconomics
- **Hồ sơ chính:** [`ho_so_launch_v0.md`](./ho_so_launch_v0.md)
- **File chi tiết:** [`bang_chi_phi.md`](./bang_chi_phi.md), [`bang_loi.md`](./bang_loi.md), [`pilot_plan.yaml`](./pilot_plan.yaml), [`chi_so.md`](./chi_so.md)

## 1. Tóm tắt 7 mục cốt lõi (Nhiệm vụ A–E)

| Mục | Con số chính và bằng chứng | Trạng thái | Phụ trách |
|---|---|---|---|
| **1 · Chi phí mỗi việc thành công** | Toàn mẫu: **4.472 đ** = 4.373.585 đ / 978 thành công (có chi phí phút nhân viên giả lập, chưa gồm chi phí cố định). Phạm vi `noi_dia` + `hang_nang`: **3.414 đ** biến đổi; thêm cố định 40 triệu/tháng đạt **4.599 đ** ở 45.000 yêu cầu/tháng, **5.784 đ** ở nửa khối lượng (`simulated`). | Giả lập | Người kiểm số |
| **2 · Ba yếu tố nhạy nhất** | Làm lại ×2: **6.787 đ (+51,8%)**; xem lại ×2: **6.292 đ (+40,7%)**; lương +25%: **5.506 đ (+23,1%)** so với A2 (`simulated`). | Giả lập | Người viết code |
| **3 · So với nhân viên tự làm** | Nhân viên tự làm: **12.000 đ/yêu cầu** theo giả định lab. Toàn mẫu, tính cả 222 ca không thành công chuyển nhân viên: **5.865 đ/yêu cầu = 0,49×** (`simulated`). A4 trong phạm vi pilot là **4.599 đ = 0,38×** ở quy mô đầy đủ (`simulated`). | Giả lập | Người kiểm số |
| **4 · Chỉ số và telemetry** | Đợt chạy thử: chính **994/1.200 = 82,83%**; bỏ qua gợi ý **48/177 = 27,12%**; mở lại 7 ngày **51/1.200 = 4,25%**. Trong phạm vi pilot: bỏ qua **27/128 = 21,09%**, mở lại **39/982 = 3,97%**. Có **9 event** với `trace_id` trong [`chi_so.md`](./chi_so.md). | Giả lập | Người gắn nhãn 2, kiêm giữ hồ sơ |
| **5 · Phân loại lỗi** | Hai bộ nhãn trong hồ sơ ghi nhận **18/20 = 90%** đồng thuận; có quy tắc cho ca 6 và 13, cùng 5 biện pháp khắc phục đủ năm loại lỗi. | Xong, có bằng chứng | Người gắn nhãn 1 |
| **6 · Kế hoạch pilot** | Chia ngẫu nhiên theo nhân viên, phân tầng depot, **20 cụm/nhóm**; MDE **+6 điểm**, cần **859 mẫu hiệu dụng**/nhóm, **299 yêu cầu/nhân viên** (5.980 yêu cầu thô/nhóm). Power nếu tác động thật +5 điểm: **64,2%**. Có 4 luật dừng và rollback 30 phút. | Xong, có bằng chứng | Người viết code và kiểm số |
| **7 · Rủi ro kinh tế** | Làm lại ×2 làm CPS tăng 51,8%; xem lại 100% có thể lên **11.743–12.414 đ/việc** (`simulated`); giảm nửa khối lượng làm phần cố định tăng từ 1.185 lên **2.370 đ/việc** (`simulated`). | Giả lập | PM trợ lý hoàn phí |

## 2. Đề xuất của DMTG: `Go có điều kiện`

- **Phạm vi:** bắt đầu với `noi_dia`; chỉ đưa `hang_nang` vào khi chi phí mỗi việc thành công không vượt 8.000 đ trong hai tuần liên tiếp và luật an toàn đạt. Giữ `quoc_te` và `doi_tac` ngoài phạm vi pilot.
- **Điều kiện trước/khi chạy:**
  1. Kỹ sư trưởng agent kiểm thử khoá chống hoàn trùng và đối soát sổ cái trước 2026-12-06.
  2. Giám đốc vận hành chấp thuận MDE +6 điểm và power 64,2% nếu tác động thật +5 điểm trước khi mở pilot.
  3. PM bật đủ event có `trace_id`, xác nhận cỡ mẫu/lưu lượng và thay phút giả lập bằng thời gian thực sau tuần đầu.
  4. Chỉ giảm tỉ lệ xem lại theo bậc khi chỉ số an toàn đạt ngưỡng; nếu không, giữ chuyển ca rủi ro cho nhân viên.

## 3. Tin nhắn trao đổi và bài trình bày

### Tin nhắn gửi JQKA

> **Nhóm DMTG · Lớp L3B** gửi hồ sơ Gate 2a:  
> Repo: https://github.com/TDM414/K5-L3B-DAY13-NhomDMTG-LaunchEconomics  
> Hồ sơ chính: `report/team/ho_so_launch_v0.md`  
> Bằng chứng chi tiết: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`.  
> Nhờ JQKA dùng phiếu ở cuối tài liệu để chấm C6–C8 và ghi câu hỏi/câu trả lời sau phần trao đổi.

### Bài trình bày 1 phút

> DMTG đề xuất Go có điều kiện, bắt đầu với `noi_dia`; chỉ thêm `hang_nang` khi CPS không quá 8.000 đ trong hai tuần và an toàn đạt. Mô hình giả lập cho phạm vi pilot là 4.599 đ/việc gồm phân bổ chi phí cố định ở 45.000 yêu cầu/tháng, so với 12.000 đ nếu nhân viên tự làm. Tuy nhiên, nếu xem lại 100% chi phí có thể lên 11.743–12.414 đ, và nếu tác động thật chỉ +5 điểm thì thiết kế pilot có power khoảng 64,2%. Pilot chia ngẫu nhiên theo nhân viên, có 20 cụm mỗi nhóm, 4 luật dừng và rollback 30 phút. Chỉ mở pilot sau khi kiểm thử chống hoàn trùng, bật telemetry và xác nhận đủ mẫu.

## 4. DMTG chấm JQKA

Theo hồ sơ JQKA đã nhận:

| Tiêu chí | Điểm | Lý do |
|---|---:|---|
| C6 · Đề xuất khớp bằng chứng | **10/10** | Có Go có điều kiện, nêu rủi ro xem lại 100% là 11.743–12.414 đ và power 0,64 ở +5 điểm, kèm cách xử lý. |
| C7 · Số giả lập và phạm vi | **10/10** | Phạm vi thu hẹp bằng số (`noi_dia` 0,22×, `hang_nang` 0,69×, loại `quoc_te` 1,88×), và JQKA đã bổ sung nhãn `[dữ liệu chạy thử giả lập, simulated]` cho `82,83%`, `27,12%`, `4,25%` trong `chi_so.md` và `ho_so_launch_v0.md`. |
| C8 · Pilot ra được quyết định | **10/10** | Có đối chứng đồng thời, ngẫu nhiên, 20 cụm/nhóm, 859 mẫu hiệu dụng/nhóm và 4 luật dừng có ngưỡng/thời hạn/người phụ trách. |
| **Tổng** | **30/30** | Go có điều kiện. |

## 5. Phiếu để JQKA chấm DMTG

- **Nhóm được chấm:** DMTG · L3B
- **Repo:** https://github.com/TDM414/K5-L3B-DAY13-NhomDMTG-LaunchEconomics
- **Hồ sơ chính:** [`ho_so_launch_v0.md`](./ho_so_launch_v0.md)
- **Bằng chứng:** các file trong mục 1 và [`phieu_cham.md`](./phieu_cham.md)

| Tiêu chí | Điểm JQKA (0/5/10) | Lý do có số/bằng chứng |
|---|---:|---|
| C6 · Đề xuất khớp bằng chứng | **10** | Đề xuất `Go có điều kiện` khớp số (bắt đầu `noi_dia` `0,22×`, mở `hang_nang` `0,69×` khi ≤ `8.000 đ`); nêu rõ rủi ro xem lại 100% (`11.743–12.414 đ/việc`, `giả lập`), power `64,2%` ở `+5 điểm` và cố định tăng lên `2.370 đ/việc` ở nửa khối lượng kèm điều kiện xử lý trước `2026-12-06`. |
| C7 · Số giả lập và phạm vi | **10** | Mọi số từ `_simulated` và số chạy thử trong `ho_so_launch_v0.md`, `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml` đều gắn nhãn `simulated`/`giả lập`; không có từ cấm; phạm vi thu hẹp bằng số (`noi_dia`, `hang_nang`; loại `quoc_te` `1,88×`, `doi_tac` `0,85×`). |
| C8 · Pilot ra được quyết định | **10** | Có đối chứng đồng thời, ngẫu nhiên theo nhân viên (`seed: 20261207`, phân tầng `depot`), `20` cụm/nhóm (`859` hiệu dụng/nhóm, `299` YC/NV, `DE = 6,96`, `MDE +6 điểm`); `4` luật dừng đủ 4 vế có ngưỡng/thời hạn/người dừng và rollback `30 phút`. |
| **Tổng** | **30 / 30** | |

**Quyết định của JQKA:** Go có điều kiện  
**Lý do:** Hồ sơ đầy đủ bằng chứng, nhãn giả lập nhất quán và thiết kế pilot đủ điều kiện ra quyết định; cần hoàn tất kiểm thử chống hoàn trùng/đối soát sổ cái trước `2026-12-06`, ký chấp nhận power `64,2%` ở `+5 điểm`, và bổ sung `input_validation_failed`, `handoff_to_staff` vào `chi_so.md` để khớp bảng lỗi Ca 9, Ca 4.  
**Một câu hỏi cho đội trình:** Ngưỡng dừng chi phí đặt `> 8.000 đ` trong 2 tuần cho phạm vi có `hang_nang` (CPS gốc riêng `hang_nang` là `8.221 đ` `simulated`), và `bang_loi.md` dùng `input_validation_failed` (Ca 9), `handoff_to_staff` (Ca 4) nhưng 9 event trong `chi_so.md` chưa có 2 event này — nhóm xử lý thế nào trước `2026-12-06`?  
**Câu trả lời của DMTG:** *(ghi lại tại buổi hỏi đáp)*
