# Báo cáo cá nhân — Nguyễn Xuân Dương-2A202603955

## 1. Thông tin thành viên

- Họ tên: Nguyễn Xuân Dương
- MSSV: 2A202603955
- Email: xuanduong20050808@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (CP3, CP5)

## 2. Phần việc phụ trách

- CP3: gắn nhãn độc lập 20 ca lỗi với vai trò người gắn nhãn 2 và cùng nhóm đối chiếu, thống nhất quy tắc phân loại.
- CP5: tổng hợp chỉ số, event và rủi ro kinh tế; hoàn thiện hồ sơ launch v0 và báo cáo nhóm.

## 3. Đóng góp cụ thể

- Tham gia bộ nhãn độc lập của người gắn nhãn 2 trong `report/team/bang_loi.md`; kết quả đối chiếu ghi nhận 18/20 ca trùng (90%) và có giải thích hai ca không trùng.
- Tính và ghi rõ các chỉ số chạy thử giả lập: chỉ số chính 994/1.200 = 82,83%; tỉ lệ bỏ qua 48/177 = 27,12%; tỉ lệ mở lại 51/1.200 = 4,25%.
- Hoàn thiện danh sách event có `trace_id`, ánh xạ event với chỉ số và ghi ba rủi ro kinh tế có số đo trong `report/team/chi_so.md`.
- Tổng hợp bảy mục và đề xuất Go có điều kiện trong `report/team/ho_so_launch_v0.md`, nêu rõ MDE 6 điểm, power 64,2% nếu tác động thật là 5 điểm, cùng điều kiện an toàn và chi phí.
- Hoàn thiện thông tin nhóm và phần tổng hợp CP5 trong `TEAM.md` và `report/team/group_report.md`.

## 4. Bằng chứng

- Các file CP5: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`.
- Đối chiếu CSV bằng pandas: chỉ số chính 994/1.200; quyết định sửa/bỏ 48/177; mở lại 51/1.200. Phạm vi `noi_dia` + `hang_nang`: mở lại 39/982 và bỏ qua 27/128.
- Đã chạy `python lab13.py`: ba phép thử A1 đạt; các kết quả A2, A3, B1–B3, D1 và D3 được in đầy đủ. Lần xác minh đầu tiên dừng vì thiếu `statsmodels`; sau khi cài phụ thuộc đã chạy thành công đến hết.

## 5. Công cụ AI đã dùng

Đã dùng Copilot để tra cứu yêu cầu trong README, checkpoint, rubric và hướng dẫn; hỗ trợ tính/diễn giải chỉ số từ CSV và rà soát sự nhất quán giữa hồ sơ. Tự kiểm tra các số đếm trực tiếp bằng pandas, đối chiếu với công thức và số trong hướng dẫn, đồng thời chạy `python lab13.py`. Không tạo nhãn lỗi hoặc kết quả duyệt chéo thay cho dữ liệu thực tế.

## 6. Tự đánh giá

Đã hoàn thiện phần tổng hợp CP5 và ghi rõ giới hạn của dữ liệu giả lập, không có đối chứng. Đã duyệt chéo nhóm JQKA: 30/30 (C6 10, C7 10, C8 10), quyết định Go có điều kiện; câu trả lời của nhóm chưa có trong hồ sơ trao đổi.
