# Room Class Capacity Ratio

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Rooms-Room-Class-Capacity-Ratio.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Rooms-Room-Class-Capacity-Ratio.htm`
- **Ingestion Date:** `2026-09-11 22:13:03`

---

# Room Class Capacity Ratio

If your property usesGroup Occupancy Forecast Overrides, use Room Class Capacity Ratio to letG3 RMSadjust the remaining demand and wash of a Forecast Group by Room Class. SeeHowG3 RMSDistributes Group Occupancy Forecast Overridesfor details.
For a summary of all the steps in Rooms setup and the importance of completing them together, seeRooms Configuration Overview.

## Setup Steps

- ClickNextafter you complete Minimum Price Differential setup.
- By default, the Room Class ratios are based on their capacity. For example, you have two Room Classes: 70 rooms in Standard and 30 in Suites. The default ratio is 0.7 for Standard and 0.3 for Suite.
- If needed, change the ratio for a Room Class. For example, the pickup of your groups is higher than 70% in the Standard Room Class. Therefore, you change the Standard value to 0.9 and Suites to 0.1. Applying a Group Occupancy Forecast Override forcesG3 RMSto change the Wash and Remaining Demand for a Forecast Group. The system uses the 9 to 1 ratio to apply demand and wash to the two Room Classes.
- Turn off the togglefor a Room Class that you don't want to receive any wash or remaining demand.
- ClickNextto save your changes and continue.
