# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Duy Mạnh · Người gắn nhãn 2: Nguyễn Xuân Dương (gắn độc lập, không trao đổi trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Ngữ cảnh | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. (Đồng thuận 90% ≥ 80%, không cần viết lại định nghĩa.)

- **Ca 6 (Do người dùng vs Ngữ cảnh → Do người dùng):** Gốc lỗi là khách chọn sai mục ngay ở đầu vào ("Hoàn phí giao trễ" thay vì hàng vỡ); việc trợ lý chưa đối chiếu mô tả để gợi ý đổi mục là phần cần cải thiện ở cột khắc phục.
- **Ca 13 (Hệ thống vs Giới hạn hệ thống → Giới hạn hệ thống):** Yêu cầu hoàn phí bảo hiểm của công ty đối tác nằm ngoài phạm vi trợ lý nên nguyên nhân gốc là giới hạn hệ thống, kể cả khi trợ lý xử lý giới hạn đó chưa rõ ràng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` với lý do sai định dạng mã; cảnh báo theo ngày khi vượt **2%** tổng yêu cầu | Tự nhận diện mã đơn sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát **mỗi giờ**: đếm tin nhắn báo "đã hoàn" nhưng không có bản ghi `refund_ledger_write` trạng thái `ok` cùng `trace_id`; ngưỡng **0 ca** | Chỉ cho phép gửi thông báo "đã hoàn" khi sổ cái trả `ok`; nếu lỗi 503 quá 3 lần thử thì báo "đang xử lý" và chuyển nhân viên kèm `trace_id` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do thắc mắc số tiền nhưng kiểm tra đối soát thấy tính đúng, theo dõi **hằng tuần**; cảnh báo khi vượt **1%** | Bổ sung công thức tính chi tiết vào mẫu phản hồi (ví dụ: `30.000 đ × 50% = 15.000 đ`) trước khi gửi khách | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` tách theo `loai`, theo dõi **hằng ngày**; cảnh báo khi tỉ lệ chuyển ở nhóm trong phạm vi vượt **5%** | Giữ cơ chế chuyển nhân viên kèm bản tóm tắt đầy đủ; loại nhóm `quoc_te` khỏi phạm vi chạy thử pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm tra mẫu ngẫu nhiên **100 đơn/tuần** so với bảng giá hiện hành; ngưỡng báo động **> 1%** đơn lệch tiền | Vô hiệu hoá bộ nhớ đệm ngay khi bảng giá cập nhật và ghi mã phiên bản bảng giá vào trường metadata của `trace_id` | Kế toán trưởng |
