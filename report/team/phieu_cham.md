# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): DMTG
- Nhóm được chấm: JQKA · L3B
- Repo: https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics
- Bằng chứng đã xem: `ho_so_launch_v0.md`, `pilot_plan.yaml`, `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md` trong `report/team/`.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất Go có điều kiện giới hạn `noi_dia` + `hang_nang`; nêu chi phí xem lại 100% là 11.743–12.414 đ/việc và power chỉ 0,64 nếu tác động thật +5 điểm, kèm điều kiện xử lý. Nguồn: [hồ sơ JQKA](https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics/blob/main/report/team/ho_so_launch_v0.md). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **5** | Phạm vi được thu hẹp có số: `noi_dia` 0,22×, `hang_nang` 0,69×; `quoc_te` 1,88× bị loại. Tuy nhiên các chỉ số chạy thử 82,83%, 27,12%, 4,25% trong hồ sơ chỉ số chưa ghi rõ nhãn `simulated`, nên chưa đạt mức 10. Nguồn: [chi_so.md của JQKA](https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics/blob/main/report/team/chi_so.md). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Có đối chứng đồng thời, chia ngẫu nhiên theo nhân viên/phân tầng depot, 20 cụm mỗi nhóm; 859 mẫu hiệu dụng/nhóm, 299 yêu cầu/nhân viên. Kế hoạch có 4 luật dừng định lượng, người phụ trách và rollback 30 phút. Nguồn: [pilot_plan.yaml của JQKA](https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics/blob/main/report/team/pilot_plan.yaml). |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện.

**Lý do:** Thiết kế có đối chứng, cỡ mẫu và luật dừng đủ để ra quyết định pilot; đề xuất thừa nhận rủi ro chi phí/power. Trước khi mở pilot, gắn nhãn `simulated` rõ cho các chỉ số chạy thử và xác minh đủ telemetry cùng số phút thực.

**Một câu hỏi cho đội trình:** Nhóm sẽ bổ sung nhãn `simulated` cho ba chỉ số 82,83%, 27,12%, 4,25% như thế nào, và sẽ dùng bằng chứng nào để xác nhận đủ 13 event cùng thời gian xem lại/làm lại thực trước khi mở pilot?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa có câu trả lời trong hồ sơ trao đổi được cung cấp.
