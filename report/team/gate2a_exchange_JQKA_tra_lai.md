# Hồ sơ trao đổi duyệt chéo Gate 2a · Nhóm JQKA (Lớp L3B)

> Tài liệu tóm tắt toàn bộ bằng chứng A–E phục vụ trao đổi duyệt chéo lúc 17:00 (file tạm ngoài `report/team/`, không dùng để nộp thay bộ hồ sơ chính).

- **Repo nhóm:** `https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics`
- **Hồ sơ chính (1 trang):** `report/team/ho_so_launch_v0.md`
- **File chi tiết:** `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`

---

## 1. Tóm tắt 7 mục cốt lõi (Nhiệm vụ A–E)

| Mục | Con số chính và bằng chứng | Trạng thái | Phụ trách |
| --- | --- | --- | --- |
| **1 · Chi phí mỗi việc thành công** | Toàn mẫu (`978/1.200` TC): **`4.472 đ/việc`** (`simulated`, gấp `16,3×` hoá đơn `274,7 đ/YC`). Phạm vi `noi_dia + hang_nang` (`900/982` TC): **`3.414 đ`** biến đổi; cộng cố định `40 triệu đ/tháng` đạt **`4.599 đ` (`0,38×`)** ở `45.000d YC/tháng` (`5.784 đ = 0,48×` ở nửa khối lượng) `[simulated]`. | Giả lập | PM trợ lý hoàn phí |
| **2 · Ba yếu tố nhạy nhất** | 1. Số ca làm lại `×2`: **`6.787 đ` (`+51,8%`)** · 2. Tỉ lệ xem lại `×2`: **`6.292 đ` (`+40,7%`)** · 3. Lương NV `+25%`: **`5.506 đ` (`+23,1%`)** `[simulated]`. Giờ nhân viên chiếm `92,5%` tổng chi phí; giá token `×2` chỉ tăng `+5,6%`. | Giả lập | PM trợ lý hoàn phí |
| **3 · So với 12.000 đ (nhân viên tự làm)** | Toàn hệ thống (gộp `222` ca lỗi × `12.000 đ`): **`5.865 đ/YC = 0,49×`** `[simulated]`. Theo loại: `noi_dia` **`0,22×`** (`2.696 đ`), `hang_nang` **`0,69×`** (`8.221 đ`), `doi_tac` **`0,85×`** (`10.215 đ`), `quoc_te` **`1,88×`** (`22.515 đ`, chạy lại tụt `30,0% → 11,4% → 2,2%`). **Bất lợi B4 (xem lại 100%):** **`11.743 đ = 0,98×`** (`9` phút làm lại) hoặc **`12.414 đ = 1,03×`** (`15,3` phút làm lại) `[simulated]`. | Giả lập | Giám đốc vận hành LogiX-VN |
| **4 · Chỉ số & Telemetry** | Trong đợt chạy thử (chưa đối chứng): Chính **`82,83%`** (`994/1.200`), Dùng (bỏ qua gợi ý) **`27,12%`** (`48/177`), An toàn (mở lại 7 ngày) **`4,25%`** (`51/1.200`; trong phạm vi pilot **`3,97%`**). Đã thêm `2` chỉ số pilot (`assistant_opened / request_assigned`, `refund_amount_audit`) và **`13` event có `trace_id`** + bảng kiểm tra chéo. | Xong, có bằng chứng | PM trợ lý hoàn phí |
| **5 · Phân loại lỗi (Google PAIR)** | TV3 & TV4 gắn độc lập `20` ca → đồng thuận **`18/20 = 90%`** (`≥ 80%`), quy tắc phân biệt cho Ca 6 (`Do người dùng`) và Ca 16 (`Ngữ cảnh`), thống nhất `20/20` ca và `5` biện pháp phát hiện đo được cho `5` loại (`9, 7, 18, 4, 17`). | Xong, có bằng chứng | Trưởng nhóm CSKH |
| **6 · Kế hoạch pilot** | Chia cụm theo **20 nhân viên/nhóm** (phân tầng `12` depot, `seed = 20261125`), rollout `[0.10, 0.25, 0.50]`, rollback `30 phút`, `decision_date: 2027-01-05`. **Bất lợi thống kê:** `c/ICC = 1.000 < 1.251`, nên chấp nhận **MDE `+6 điểm`** (`n_per_arm = 859`, `m ≥ 299`, `DE = 6,96`), làm **power ở `+5 điểm` còn `0,64`**. Có **`4` luật dừng** đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ`. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| **7 · Rủi ro kinh tế** | Làm lại `×2`: `6.787 đ` (`+51,8%`); xem lại `×2`: `6.292 đ` (`+40,7%`); xem lại `100%`: `11.743–12.414 đ` (`0,98×–1,03×`); nửa khối lượng: cố định `+2.370 đ/việc` (`5.784 đ`) `[simulated]`. | Giả lập | Giám đốc vận hành LogiX-VN |

---

## 2. Đề xuất của JQKA: `Go có điều kiện`

- **Phạm vi pilot:** Chỉ `noi_dia` và `hang_nang` (`900/982` YC thành công); loại `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`, có điều khoản riêng).
- **4 điều kiện bắt buộc trước/khi chạy:**
  1. **Sửa lỗi nghiêm trọng (Ca 7, Ca 20):** Kỹ sư trưởng agent bổ sung khoá chống trùng và chỉ báo `"đã hoàn"` khi `refund_ledger_write` trả `ok` (trước khi mở pilot).
  2. **Ký duyệt pilot & chấp nhận đánh đổi power:** Giám đốc vận hành ký duyệt `pilot_plan.yaml` (`20 NV/nhóm`, MDE `+6 điểm` / power `0,64` ở `+5 điểm`, `4` luật dừng, rollback `30 phút`) trước 17:00 ngày `25/11/2026`.
  3. **Bật telemetry & đo phút thực:** Kỹ sư trưởng agent bật đủ `13` event có `trace_id`; Trưởng nhóm CSKH thay phút `simulated` bằng phút xem lại/làm lại đo thật sau tuần 1 pilot.
  4. **Lộ trình giảm xem lại theo bậc:** PM trợ lý hoàn phí thiết kế kế hoạch giảm xem lại (khi `sua + bo < 15%` và chỉ số an toàn đạt ngưỡng), vì xem lại `100%` đẩy chi phí lên `11.743–12.414 đ/việc` `[simulated]`, không còn tiết kiệm.

---

## 3. Tin nhắn trao đổi & Bài trình bày 1 phút

### Tin nhắn gửi nhóm bạn (copy & paste)
> **Nhóm JQKA · Lớp L3B** gửi hồ sơ Gate 2a:
> - **Repo:** `https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics`
> - **Hồ sơ chính:** `report/team/ho_so_launch_v0.md`
> - **Bằng chứng đối chiếu:** `report/team/pilot_plan.yaml`, `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/chi_so.md`
>
> Cho nhóm mình xin **link repo** hoặc các file hồ sơ (`ho_so_launch_v0.md`, `pilot_plan.yaml`, `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md`) của nhóm bạn để hội đồng chấm nhé!

### Kịch bản trình bày 1 phút (TV4 đọc lúc duyệt chéo)
> Nhóm JQKA đề xuất **Go có điều kiện** cho pilot giới hạn `noi_dia` và `hang_nang` (`900/982` việc thành công; `0,22×` và `0,69×` mức `12.000 đ` `[simulated]`, gộp cố định `40 triệu/tháng` đạt `4.599 đ = 0,38×` ở `45.000 YC/tháng`). Chúng tôi loại `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`).
> Về **bất lợi và rủi ro**: giờ nhân viên chiếm `92,5%` chi phí; nếu phải xem lại `100%` thì chi phí vọt lên `11.743–12.414 đ/việc` (`0,98×–1,03×`, `[simulated]`), xoá sạch lợi ích; đồng thời với `20` nhân viên/nhóm, nhóm chấp nhận MDE `+6 điểm` (`859 YC/nhóm`, `m ≥ 299`), làm power ở `+5 điểm` giảm còn `0,64`.
> Pilot chỉ mở khi đủ 4 điều kiện: sửa Ca 7 & Ca 20; Giám đốc vận hành ký duyệt `pilot_plan.yaml` với `4` luật dừng và rollback `30 phút`; bật đủ `13` event có `trace_id` và đo phút thật ở tuần 1; có lộ trình giảm tỉ lệ xem lại theo bậc.

---

## 4. Checklist nhận & chấm nhóm bạn (điền vào `report/team/phieu_cham.md`)

- **Xin từ nhóm bạn:** Tên nhóm, lớp, link repo, `ho_so_launch_v0.md`, `pilot_plan.yaml`, `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md`.
- **Chấm C6–C8 (`0 / 5 / 10`):**
  - **C6:** Đề xuất khớp số? Có nêu rõ con số bất lợi (B4 xem lại `100%`, power `0,64` ở `+5 điểm`) và cách xử lý?
  - **C7:** Đã gắn nhãn `simulated`/`Giả lập` ở mọi số từ `_simulated`? Phạm vi có thu hẹp bằng số? Có lọt từ cấm?
  - **C8:** Có đối chứng cùng thời gian + ngẫu nhiên + `≥ 20` cụm/nhóm (hoặc nêu rõ đánh đổi)? `≥ 3` luật dừng đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ` (lưu ý: đặt ngưỡng mở lại `3%` sẽ dừng ngay tuần đầu vì nền đang `4,25%`)?
- **Ghi lại ngay sau phần hỏi đáp:**
  1. Câu trả lời của đội trình → `report/team/phieu_cham.md`
  2. Điểm và quyết định hội đồng chấm **JQKA** → Mục 4 của `report/team/group_report.md`

---

## 5. Kết quả DMTG chấm JQKA

Hội đồng DMTG đã đối chiếu hồ sơ chính và các file chi tiết trong repo JQKA.

| Tiêu chí | Điểm | Bằng chứng |
|---|---:|---|
| C6 · Đề xuất khớp bằng chứng | **10/10** | Đề xuất Go có điều kiện, thu hẹp phạm vi và nêu rủi ro xem lại 100% là 11.743–12.414 đ/việc cùng power 0,64 nếu tác động thật +5 điểm; có điều kiện xử lý các rủi ro này. |
| C7 · Số giả lập và phạm vi | **5/10** | Phạm vi có lý do bằng số (`noi_dia` 0,22×, `hang_nang` 0,69×, loại `quoc_te` 1,88×), và các số chi phí có nhãn. Tuy nhiên 82,83%, 27,12%, 4,25% trong `chi_so.md` chưa được ghi rõ là số chạy thử giả lập. |
| C8 · Pilot ra được quyết định | **10/10** | Có đối chứng đồng thời, chia ngẫu nhiên theo nhân viên, phân tầng depot, 20 cụm/nhóm, 859 mẫu hiệu dụng/nhóm, 299 yêu cầu/nhân viên và 4 luật dừng có ngưỡng/thời hạn/người phụ trách; rollback 30 phút. |
| **Tổng** | **25/30** | |

**Quyết định của hội đồng DMTG:** Go có điều kiện.  
**Điều kiện khuyến nghị:** gắn nhãn `simulated` rõ cho ba chỉ số chạy thử nêu trên và giữ các điều kiện an toàn, telemetry, đo phút thực trước khi mở pilot.

## 6. Phiếu để JQKA chấm DMTG

- **Nhóm được chấm:** DMTG · L3B
- **Repo:** https://github.com/TDM414/K5-L3B-DAY13-NhomDMTG-LaunchEconomics
- **Hồ sơ chính:** `report/team/ho_so_launch_v0.md`
- **Bằng chứng chi tiết:** `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`

| Tiêu chí | Điểm JQKA (0/5/10) | Lý do có số/bằng chứng |
|---|---:|---|
| C6 · Đề xuất khớp bằng chứng | ____ | ____ |
| C7 · Số giả lập và phạm vi | ____ | ____ |
| C8 · Pilot ra được quyết định | ____ | ____ |
| **Tổng** | **____ / 30** | |

**Quyết định của JQKA:** Go / Go có điều kiện / No-go: ____  
**Lý do:** ____  
**Một câu hỏi cho đội trình:** ____  
**Câu trả lời của DMTG:** ____
