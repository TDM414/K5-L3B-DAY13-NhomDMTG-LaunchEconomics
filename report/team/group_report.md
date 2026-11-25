# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: DMTG
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí mỗi việc thành công, mức sử dụng, lỗi và thiết kế pilot cho trợ lý hoàn phí LogiX-VN. Nhóm dùng dữ liệu CSV giả lập và công thức của lab; không xem kết quả chạy thử là bằng chứng nhân quả vì chưa có nhóm đối chứng.

## 3. Giải pháp

CP1–CP2: tính mô hình chi phí và độ nhạy trong `src/lab13.py`, ghi kết quả ở `bang_chi_phi.md`. CP3: hai người gắn nhãn độc lập và lập biện pháp khắc phục trong `bang_loi.md`. CP4: chọn phân nhóm theo nhân viên, có đối chứng đồng thời và luật dừng trong `pilot_plan.yaml`. CP5: định nghĩa chỉ số, event, rủi ro tại `chi_so.md`, tổng hợp quyết định tại `ho_so_launch_v0.md`.

## 4. Kết quả

Các số bên dưới là từ bộ dữ liệu giả lập. Chỉ số chạy thử mô tả dữ liệu, không chứng minh trợ lý gây ra thay đổi vì không có nhóm đối chứng.

| Chỉ số | Cách tính và ý nghĩa | Bằng chứng |
|---|---|---|
| **Chính: đóng đúng hạn, không mở lại** | `(dong_trong_24h = 1 và mo_lai_trong_7_ngay = 0) / 1.200` = **994/1.200 = 82,83%**. Một yêu cầu chỉ đạt nếu thỏa cả hai điều kiện; đây là tỉ lệ quan sát, không phải mức cải thiện do trợ lý. | Tính từ hai cột trong [`logix_requests.csv`](../../src/logix_requests.csv); định nghĩa ở [`chi_so.md`](./chi_so.md). |
| **Dùng: bỏ qua gợi ý** | `(quyet_dinh_xem_lai = sua hoặc bo) / duoc_xem_lai = 1` = **48/177 = 27,12%** trên toàn mẫu. Chỉ xét ca nhân viên đã xem gợi ý, không chia cho toàn bộ 1.200 yêu cầu. Riêng phạm vi pilot, số là **27/128 = 21,09%**. | Đếm trực tiếp các cột `duoc_xem_lai`, `quyet_dinh_xem_lai` trong [`logix_requests.csv`](../../src/logix_requests.csv); công thức ở [`chi_so.md`](./chi_so.md). |
| **An toàn: mở lại trong 7 ngày** | `mo_lai_trong_7_ngay = 1 / tổng yêu cầu` = **51/1.200 = 4,25%**; phạm vi pilot là **39/982 = 3,97%**. Đây là tín hiệu cần điều tra, không có nghĩa mọi ca mở lại đều do agent gây ra. | Đếm trực tiếp cột `mo_lai_trong_7_ngay` trong [`logix_requests.csv`](../../src/logix_requests.csv); event theo dõi là `ticket_reopened` trong [`chi_so.md`](./chi_so.md). |
| **Chi phí** | A2: **4.472 đ/việc thành công** = 4.373.585 đ / 978; gồm thời gian xem lại/làm lại giả lập, chưa gồm chi phí cố định. A4 cho `noi_dia` + `hang_nang`: **4.599 đ** = 3.414 đ chi phí biến đổi + 1.185 đ cố định ở 45.000 yêu cầu/tháng, so với 12.000 đ nhân viên tự làm. | Bảng A2/A4 và công thức phân bổ cố định trong [`bang_chi_phi.md`](./bang_chi_phi.md). |
| **Rủi ro độ nhạy** | Nếu chi phí làm lại gấp đôi, CPS tăng **51,8% lên 6.787 đ**; nếu xem lại gấp đôi, tăng **40,7% lên 6.292 đ**. Đây là kịch bản độ nhạy, không phải mức đã quan sát xảy ra. | B1 trong [`bang_chi_phi.md`](./bang_chi_phi.md), tái lập bằng [`lab13.py`](../../src/lab13.py). |
| **Cỡ mẫu pilot** | Chênh lệch +5 điểm cần **1.251 mẫu hiệu dụng/nhóm**, nhưng 20 nhân viên/nhóm với ICC 0,02 có trần dưới 1.000. Vì vậy kế hoạch chấp nhận MDE +6 điểm: **859 mẫu hiệu dụng**, 20 nhân viên × 299 yêu cầu = 5.980 yêu cầu thô/nhóm. Nếu tác động thật chỉ +5 điểm, power khoảng **64,2%** — xác suất phát hiện hiệu ứng ở mức đó theo giả định thiết kế, không phải xác suất pilot thành công. | D1 trong [`pilot_plan.yaml`](./pilot_plan.yaml) và phần D1 khi chạy [`lab13.py`](../../src/lab13.py). |

Đề xuất của nhóm mình là **Go có điều kiện** với phạm vi và luật dừng trong [`ho_so_launch_v0.md`](./ho_so_launch_v0.md). Duyệt chéo JQKA: **25/30** (C6 10, C7 5, C8 10), quyết định **Go có điều kiện**. Điểm C7 bị trừ vì ba chỉ số chạy thử 82,83%, 27,12%, 4,25% trong `chi_so.md` chưa gắn nhãn `simulated`; C6 và C8 khớp bằng chứng về chi phí/rủi ro và thiết kế pilot. Chi tiết ở [`phieu_cham.md`](./phieu_cham.md); câu trả lời của JQKA chưa có trong hồ sơ trao đổi.

## 5. Khó khăn và cách xử lý

Lần chạy xác minh đầu tiên đạt A1, A2, A3, B1–B3 nhưng dừng ở D1 do môi trường chưa cài `statsmodels` (gói đã khai báo trong `src/requirements.txt`). Đã cài đúng phụ thuộc và chạy lại `python lab13.py` thành công đến hết D1 và D3.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Toàn bộ số liệu đầu vào là giả lập; thời gian xem lại/làm lại chưa phải đo thực tế. Chạy thử không có đối chứng, nên không thể kết luận trợ lý làm tăng chỉ số chính. Thiết kế pilot chấp nhận MDE 6 điểm do chỉ có 40 nhân viên; cần xác nhận đủ lưu lượng trước khi triển khai, ghi event có `trace_id`, và chỉ mở rộng phạm vi khi các ngưỡng chi phí/an toàn đạt.

## 8. Tài liệu tham khảo

- `README.md`, `CHECKPOINTS.md`, `RULES.md`, `RUBRIC.md`, `SUBMISSION.md` của Lab 13.
- `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Google PAIR, *People + AI Guidebook*, mục “Errors + Graceful Failure”.
