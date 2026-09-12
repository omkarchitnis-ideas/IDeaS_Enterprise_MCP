# Calculation and Use of Wash

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Demand-Wash/Wash-Use-Calculation.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Demand-Wash/Wash-Use-Calculation.htm`
- **Ingestion Date:** `2026-09-11 22:14:41`

---

## Calculation and Use of Wash inthe RMS

Wash is the drop in occupancy due to cancellations, no-shows, group cut-offs, and so on. For future dates, it is the expected drop inTotal DemandThe combination of the rooms on books and the remaining unconstrained demand.. For past dates, it is the expected wash as of the last optimization. For example, for yesterday the last optimization was at 1 pm when the system expected 4 rooms wash out of 40 rooms on books. Final Wash shows as 10%. To maximize revenue,the RMSuses overbooking to make up for the loss caused by wash. Reviewhowthe RMScalculates overbooking.
To forecast wash for all Forecast Groups,the RMSlooks at their historical wash patterns. For the wash of individual groups, the system also searches for patterns in:
- Booking lead time (days between the booking and arrival date).
Booking lead time (days between the booking and arrival date).
- Days prior to arrival (between today and arrival date).
Days prior to arrival (between today and arrival date).
- Peak vs. shoulder block.
Peak vs. shoulder block.
- Length of stay.
Length of stay.
- Size of group block.
Size of group block.
- Market segments.
Market segments.
If needed, override the group wash. For example, for a group block of 100 rooms,the RMSexpects 10% wash, but you expect 20%, meaning a final pickup of 80 rooms. Mostclientsoverride Wash by Individual Group. If you have many groups and don't want to manage overrides for each group, considerGroup Occupancy Forecast Overrides.
Note: If your subscription doesn't include  Wash overrides,  you can improve the Wash forecasts with good business practices, for example, how youmanage cancellations and no-shows.
The RMSforecasts wash for each group that is on books, both for picked up reservations and for available block. It uses the Forecast Group wash patterns, group-specific data like picked up versus total group block and, if available, cut-off date. SeeOverriding Wash for Individual Groups.
Note: Data issues can lead to Wash by Individual Group overrides being unavailable, seeinconsistent group block practices.
With Group Occupancy Forecast Overrides, you enter the expected final pickup by Forecast Group and letthe RMSdistribute the wash to all groups in that Forecast Group. For example, you add a 200 room Group Occupancy Forecast Override to a Forecast Group, andthe RMSdistributes that to all groups in that Forecast Group. The system calculates the Wash percentage for each group and the remaining group demand for that Forecast Group.
This type of wash override isn't as precise as at the individual group level, but for someclients, the gain in efficiency due to fewer overrides outweigh that downside. To learn more about the steps, setup and best practices, reviewGroup Occupancy Forecast Override.
