# Báo cáo cá nhân — Đinh Lê Thịnh-2A202603953

## 1. Thông tin thành viên

- Họ tên: Đinh Lê Thịnh
- MSSV: 2A202603953
- Email: dinhlethinh137@gmail.com
- Vai trong nhóm: Người viết code và kiểm số cho Checkpoint 4

## 2. Phần việc phụ trách

- Hoàn thiện nhiệm vụ D, gồm tính cỡ mẫu, kiểm tra khả năng tách tác động của trợ lý và lập kế hoạch pilot cho Gate 2a.

## 3. Đóng góp cụ thể

- Bổ sung 5 phép tính D1 cho các phương án chia theo yêu cầu, nhân viên và depot. Tính thêm tỷ lệ mở lại và bỏ qua gợi ý từ dữ liệu chạy thử. [`src/lab13.py`](../../src/lab13.py)
- Hoàn thiện D2–D3 cho phạm vi `noi_dia` và `hang_nang`, với phân bổ ngẫu nhiên theo nhân viên, đối chứng đồng thời, lịch thu mẫu và 4 luật dừng về mở lại, hoàn trùng, chi phí và mức độ sử dụng. [`pilot_plan.yaml`](pilot_plan.yaml)

## 4. Bằng chứng

- Chênh lệch 5 điểm phần trăm cần 1.251 yêu cầu hiệu dụng mỗi nhóm. Với 20 nhân viên mỗi nhóm và ICC 0,02, cỡ mẫu hiệu dụng luôn dưới 1.000.
- Phương án đã chọn cần 299 yêu cầu mỗi nhân viên, tức 5.980 yêu cầu gốc mỗi nhóm. Chia cho hệ số thiết kế 6,96 cho khoảng 859,20 yêu cầu hiệu dụng mỗi nhóm, đạt mục tiêu thiết kế cho chênh lệch 6 điểm phần trăm.
- Chạy thử ghi nhận 51/1.200 yêu cầu mở lại trong 7 ngày (4,25%). Trong phạm vi pilot, tỷ lệ là 39/982 (3,97%), dùng để đối chiếu với trần an toàn 6%.
- `python lab13.py` chạy hết và cả 3 phép thử A1 đạt. `yaml.safe_load` đọc được kế hoạch và cả 4 luật dừng đủ bốn vế. [Checklist nộp bài](../../SUBMISSION.md#checklist)

## 5. Công cụ AI đã dùng

Dùng Codex để đọc đề và rubric, hỗ trợ triển khai phép tính D1, soạn kế hoạch pilot và rà tiêu chí nộp. Kết quả được kiểm chứng bằng cách chạy `lab13.py`, đếm lại số yêu cầu mở lại trực tiếp từ CSV, kiểm tra rằng 298 yêu cầu mỗi nhân viên chưa đủ cỡ mẫu và dùng `yaml.safe_load` để đọc kế hoạch.

## 6. Tự đánh giá

Phần CP4 đã có phép tính tái lập và luật dừng đo được. Giới hạn cần trình bày tại Gate 2a là power chỉ khoảng 64,2% nếu tác động thật là 5 điểm phần trăm. Khả năng thu đủ 299 yêu cầu mỗi người cần được kiểm tra theo lưu lượng từng nhân viên trước khi mở pilot.
