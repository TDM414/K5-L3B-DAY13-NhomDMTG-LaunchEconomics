# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Các số bên dưới là kết quả trên bộ dữ liệu chạy thử **giả lập**, không phải so sánh nhân quả: đợt chạy thử không có nhóm đối chứng.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Tỉ lệ yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng yêu cầu | **994/1.200 = 82,83% (giả lập)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số quyết định `sua` hoặc `bo` / số yêu cầu được xem lại | **48/177 = 27,12% (giả lập)** |
| An toàn | Tỉ lệ yêu cầu mở lại trong 7 ngày | Số yêu cầu `mo_lai_trong_7_ngay = 1` / tổng yêu cầu | **51/1.200 = 4,25% (giả lập)** |
| Dùng (đề xuất thêm) | Tỉ lệ chấp nhận gợi ý đã xem | Số quyết định `giu` / tổng quyết định `giu`, `sua`, `bo` | Chưa tính riêng; ghi qua `staff_review_decision` |
| An toàn (đề xuất thêm) | Tỉ lệ hoàn sai tiền trong mẫu kiểm toán | Số bản ghi kiểm toán có tiền hoàn khác số đúng / tổng bản ghi đã kiểm toán | Chưa có số; ghi qua `audit_sample_checked`, lấy mẫu 100 đơn/tuần |

Trong phạm vi `noi_dia` + `hang_nang`, tỉ lệ mở lại là **39/982 = 3,97% (giả lập)**; tỉ lệ bỏ qua là **27/128 = 21,09% (giả lập)**. Đây là lát cắt phạm vi pilot, khác mẫu số toàn bộ ở hai chỉ số tương ứng.

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mỗi event phải mang `trace_id` xuyên suốt từ yêu cầu đến lần chạy, quyết định nhân viên, sổ cái và ticket.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi nhận yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiển thị |
| `staff_review_decision` | Nhân viên | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên quyết định |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận hoàn tiền |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `request_id`, `trace_id` | Khi đóng ticket |
| `ticket_reopened` | Hệ thống ticket | `reopened_at`, `reason`, `request_id`, `trace_id` | Khi ticket mở lại |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `mismatch`, `trace_id` | Mỗi tuần khi kiểm toán mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` (mẫu số) + `ticket_closed` + `ticket_reopened` (tử số và theo dõi đủ 7 ngày).
- Tỉ lệ bỏ qua và tỉ lệ chấp nhận: `agent_suggestion_shown` + `staff_review_decision`.
- Tỉ lệ mở lại: `refund_request_created` + `ticket_reopened`.
- Chỉ số dùng đề xuất: `agent_suggestion_shown` + `staff_review_decision`.
- Chỉ số an toàn đề xuất: `audit_sample_checked`; chỉ tính khi có đủ mẫu được kiểm toán.

## E2 · Rủi ro kinh tế

Tác động chi phí dưới đây là **giả lập**, lấy từ độ nhạy và B4 trong `bang_chi_phi.md`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **51,8%**, từ 4.472 đ lên **6.787 đ** (giả lập) | Tỉ lệ `staff_rework_completed` theo tuần và phút làm lại; báo động nếu chi phí vượt 8.000 đ trong 2 tuần | Tạm dừng tăng tỉ lệ, rà 20 trace làm lại gần nhất và thu hẹp phạm vi nếu chạm ngưỡng | PM trợ lý hoàn phí |
| Phải xem lại 100% yêu cầu trong phạm vi | **11.743 đ/việc** (0,98× mức 12.000 đ) nếu làm lại 9 phút; **12.414 đ/việc** (1,03×) nếu dùng 15,3 phút làm lại trung bình (giả lập) | Tỉ lệ có `staff_review_decision` / yêu cầu đủ điều kiện và phút xem lại mỗi tuần | Không duy trì xem lại 100%; giảm xem lại theo bậc khi audit và luật an toàn cho phép; giữ chuyển nhân viên cho ca rủi ro | Trưởng nhóm CSKH |
| Khối lượng chỉ đạt một nửa dự kiến | Phần cố định 40 triệu đ/tháng tăng từ **1.185 đ** lên **2.370 đ/việc thành công**, làm tổng chi phí lên 5.784 đ (giả lập) | Số việc thành công mỗi tuần so với kế hoạch 45.000 yêu cầu/tháng | Không tăng phạm vi; PM cập nhật mô hình chi phí và điều khoản chi phí cố định trước quyết định | PM trợ lý hoàn phí |
