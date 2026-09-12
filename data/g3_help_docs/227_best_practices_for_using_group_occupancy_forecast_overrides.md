# Best Practices for Using Group Occupancy Forecast Overrides

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Wash/BP-Group-Occupancy-Forecast-Overrides.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Wash/BP-Group-Occupancy-Forecast-Overrides.htm`
- **Ingestion Date:** `2026-09-11 22:14:40`

---

# Best Practices for Using Group Occupancy Forecast Overrides

## Decide Which Override to Apply

Let's look at a scenario. You have 10 groups on the books for April 1, all with a block of 10 rooms, zero pickup, and belonging to Forecast Group ABC.The RMSforecasts 10%, or one room, wash for each, so the Occupancy Forecast for ABC is 90 rooms. You expect only 70 rooms due to stronger wash of 50% for 5 groups. Let's look at the two ways to share that with the system.
The RMSdoesn't expect any remaining group demand, so we can disregard Wash overrides by Forecast Group. See thenext scenariofor how these overrides can impact remaining group demand.

## Understand Howthe RMSDistributes Group Occupancy Forecast Overrides

Let's use an example to understand what happens when you add a Group Occupancy Forecast Override at the Forecast Group level.
In the Forecast Group ABC, group A has 10 and group B has 40 rooms blocked for April 1.The RMScurrently forecasts 50% wash for both, so the Occupancy Forecast for group A is 5 and for group B 20. The system forecasts zero remaining demand for the Forecast Group, so the total Occupancy Forecast for the Forecast Group is 25 (5+20).
- You add a Group Occupancy Forecast Override of 100 rooms for Forecast Group ABC. That's 50 rooms more than the combined block of 50 (10 group A, 40 group B).The RMSchanges the Wash of the existing block for both groups from 50% to 0%, so the new Occupancy Forecast is 10 for group A and 40 for group B. The system adds the remaining 50 rooms to the remaining demand for the Forecast Group and sets the wash to zero. So the new Occupancy Forecast for the Forecast Group is 100, same as your override (10 and 40 for the existing groups and 50 for the remaining demand).
- The RMSneeds to adjust the wash when you override Forecast Group ABC to 0 rooms. The difference between the current combined block of 50 and your override of 0 is 50 rooms, so the system expects 100% wash for the existing blocks. Note that in the Individual Groups tab, the system doesn't calculate or show the 100% wash, and it grays out the override date.The RMSalso sets the remaining demand for that Forecast Group to 0. That means that the Occupancy Forecast for Forecast Group ABC is zero, same as your override.
- In each processing, the system ensures that the Forecast Group's Occupancy Forecast remains at the value of your override. Based on changes to On Books, it changes the wash % and the remaining demand.
- If group blocks and remaining demand vary by Room Class, the system distributes wash and remaining demand based on the definedRoom Class Capacity Ratio.

## Review Overrides and Use Expiration Dates

Group Occupancy Forecast Overrides are hard overrides and don't adjust as conditions change. For example, two months ago you set an override of 100 rooms for tomorrow, expecting new groups to book and low wash for existing groups. But today, only 50 rooms are blocked for tomorrow.the RMSstill expects 50 rooms to book until tomorrow, a very unlikely scenario. Therefore, we recommend you review your Group Occupancy Forecast Overrides at least weekly, as part of yourregular tasks.
We also suggest that you update the expiration dates of your overrides. By default, the override expires on the date that it is applied for. Many properties change the expiration date to a date that is close to the cut-off date of their groups, usually three or four weeks prior to arrival. That is because, after the cutoff, cancels and no-shows are comparable to other groups and new group bookings are more unlikely, so the override should expire, and the systemâs wash forecast should apply again.
