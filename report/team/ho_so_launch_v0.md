# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: **DMTG** · Lớp: **L3B**

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Phạm vi `noi_dia` + `hang_nang`: **4.599 đ/việc** gồm phân bổ chi phí cố định ở 45.000 yêu cầu/tháng; **5.784 đ** nếu khối lượng bằng nửa (giả lập). A2 trực tiếp: 4.472 đ/978 việc thành công, chưa gồm chi phí cố định. | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: **+51,8%** (6.787 đ); xem lại ×2: **+40,7%** (6.292 đ); lương +25%: **+23,1%** (5.506 đ), trên cơ sở A2 (giả lập). | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | A4 đầy đủ phạm vi: **4.599 đ so với 12.000 đ** (0,38×) ở 45.000 yêu cầu/tháng (giả lập). Toàn mẫu gồm chuyển nhân viên: 5.865 đ/yêu cầu (0,49×), cũng giả lập. | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: chính **994/1.200 = 82,83%**; bỏ qua **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%** (giả lập, không có nhóm đối chứng). | Giả lập | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận **18/20 = 90%**; đủ 5 loại lỗi, mỗi loại có cách phát hiện đo được và vai trò phụ trách. | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | 20 cụm nhân viên mỗi nhóm; 299 yêu cầu/người, 5.980 yêu cầu gốc/nhóm, 859 hiệu dụng/nhóm; MDE 6 điểm phần trăm. Nếu tác động thật +5 điểm, power khoảng **64,2%**. | Xong, có bằng chứng | Người viết code và kiểm số (CP4) |
| 7 · Rủi ro kinh tế | Xem lại 100%: **11.743–12.414 đ/việc** (giả lập); khối lượng giảm nửa làm chi phí cố định tăng thêm **1.185 đ/việc** so với quy mô đầy đủ. | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện cho pilot, không phải mở rộng vận hành.** Trước 2026-12-06, Kỹ sư trưởng agent phải kiểm thử khoá chống hoàn trùng và đối soát sổ cái; PM phải bật đủ event có `trace_id`, xác nhận đủ 299 yêu cầu/nhân viên ở bước 0,50 và thay số phút giả lập bằng thời gian đo thật sau tuần đầu; Giám đốc vận hành phải ký chấp nhận MDE 6 điểm và power 64,2% nếu tác động thật chỉ 5 điểm. Bắt đầu `noi_dia`; chỉ thêm `hang_nang` nếu chi phí mỗi việc thành công không vượt 8.000 đ trong hai tuần liên tiếp và luật an toàn đạt. Nếu điều kiện chưa đạt, không mở pilot theo lịch 2026-12-07.
