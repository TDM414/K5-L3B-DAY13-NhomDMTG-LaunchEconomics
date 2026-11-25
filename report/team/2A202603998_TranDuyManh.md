# Báo cáo cá nhân — Trần Duy Mạnh-2A202603998

## 1. Thông tin thành viên

- Họ tên: Trần Duy Mạnh
- MSSV: 2A202603998
- Email: duymanhtran2004mkc2@gmail.com
- GitHub: TDM414
- Vai trong nhóm: Người gắn nhãn 1 (Checkpoint 3)

## 2. Phần việc phụ trách

- Hoàn thành Checkpoint 3 — phân loại 20 ca lỗi theo 5 nhóm của Google PAIR và xây dựng bảng khắc phục trong `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- Tạo nhánh `manh` từ `origin/hg` (kế thừa phần Checkpoint 1 và Checkpoint 2) và chạy kiểm chứng lại `src/lab13.py` đạt cả 3 phép thử A1 và in đủ kết quả A2–A3, B1–B3.
- Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và tự gắn nhãn độc lập theo 5 loại (`Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`) trước khi đối chiếu với Người gắn nhãn 2 (`Nguyễn Xuân Dương`).
- Đối chiếu hai bộ nhãn, tính tỉ lệ đồng thuận `18 / 20 = 90%`, chốt nhãn thống nhất và viết quy tắc phân biệt nguyên nhân gốc cho 2 ca lệch (`Ca 6` và `Ca 13`).
- Điền bảng khắc phục cho 5 ca đại diện đủ 5 loại (`Ca 9, 7, 18, 4, 17`), bảo đảm mỗi dòng đều có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách cụ thể trong `report/team/bang_loi.md`.

## 4. Bằng chứng

- Commit `885c589` trên nhánh `manh` (`report/team/bang_loi.md`).
- Kết quả đối chiếu hai bộ nhãn độc lập: `18 / 20 = 90%` (vượt ngưỡng tối thiểu `80%`).
- Đã chạy kiểm tra tự động `report/team/bang_loi.md`: đủ 20 dòng nhãn và 5 dòng khắc phục, không còn dấu `...`, không có từ bị cấm và không ghi `"cả đội"` trong bảng.

## 5. Công cụ AI đã dùng

Đã dùng trợ lý AI (Antigravity) để trích xuất danh sách 20 ca lỗi từ tài liệu đề bài, đối chiếu hai bộ nhãn độc lập, tính tỉ lệ đồng thuận, rà soát quy tắc phân biệt và kiểm tra các điều kiện của rubric cho `report/team/bang_loi.md`. Kết quả được tự kiểm tra bằng cách tự đọc và gắn độc lập toàn bộ 20 ca trước khi so nhãn, chạy lại `python -B lab13.py` để xác minh nền CP1–CP2 và kiểm tra trực tiếp bảng kết quả trước khi commit.

## 6. Tự đánh giá

Đã hoàn thành đầy đủ phần việc được phân công ở Checkpoint 3 trên nhánh `manh` đúng quy trình gắn nhãn độc lập và đúng chuẩn rubric. Các checkpoint tiếp theo (CP4, CP5) sẽ tiếp tục được hoàn thiện và gộp vào `main`.
