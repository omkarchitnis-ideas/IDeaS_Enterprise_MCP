# Data Differences between IDeaS Systems

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Transitions/Data-Differences.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Transitions/Data-Differences.htm`
- **Ingestion Date:** `2026-09-11 22:13:30`

---

# Data Differences between IDeaS Systems

## Pace Differences

Read this topic if you are switching from IDeaS RMS, Pricing System (PS), or FMS toG3 RMSand found Same Time Last Year (STLY) pace data differences between the old and new systems. These differences are due to the different types of pace data in each system.
IDeaS RMS, PS, and FMS build pace and STLY data by observing the business on the books from each daily data extract. UntilG3 RMSreceives a full 365 days of daily data extracts, like the other IDeaS systems, it creates one year of pace from historical data, which reduces system implementation time. This historical data has limitations for measuring pace, which we describe below.
These data differences lead to the pace discrepancies that you might see between IDeaS RMS, PS, or FMS andG3 RMS. At any point, IDeaS RMS, PS, and FMS can see the exact business that was on books for the same time the previous year.G3 RMSwill not see this data until it has been capturing data for a full year. Due to the constraints of the data available toG3 RMS, STLY inG3 RMSis an indication and not an exact STLY position as is available from direct observation of daily data extracts.

### IDeaS RMS, PS, and FMS: Pace Data from Daily Extracts

To build pace, IDeaS RMS, PS, and FMS use a daily data extract captured from yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.. This data is created from summary level data only (rooms sold by market segment). In booking pace calculations, IDeaS RMS, PS, and FMS compare this data from one Business Day End extract to another. This method allows the systems to show exactly what was on books by market segment at a given point for transient and group business. For group blocks, the extracts include the exact date the block appears as on books, in a status where it is deducting from inventory. It includes any changes to the group block, like rooms added or removed. The same applies to any transient reservations in which the length of stay is increased or reduced.
This method means that when properties are initially built in IDeaS RMS, PS, or FMS, the systems can only show STLY pace after capturing 365 days of daily data snapshots from thereservation system. There is a 90-day period during system implementation in which IDeaS captures data to build an understanding of the hotelâs booking patterns to apply forwards.

### G3 RMS: Pace from History

InG3 RMS, we prefer to reduce system implementation time and build seasonal booking patterns beginning with the initial system build. To do so, we developed the ability to create booking patterns from a historical data extract from the reservations system. For both transient and group business, we use 365 days of reservations and group blocks from prior occupancy dates to build an indication of booking patterns, including booking pace.   This method providesG3 RMSanalytics with the data required to understand booking patterns and allowsG3 RMSto display an indication of STLY data on dashboards and reports.

### Transient Pace Data inG3 RMS

Two items are not available toG3 RMSfor transient reservations:
- For past bookings,G3 RMSonly receives the final status of a reservation. The system does not know if changes to the reservation took place. For example, if a reservation was booked with an incorrect market segment and was later changed,G3 RMSonly sees the reservation with its final market segment.G3 RMSalso does not receive adjustments to the number of nights. In these cases,G3 RMSbuilds pace that reflects reservations based on their final details. For all bookings received from daily data extracts, the system sees such changes due to the difference between an extract and the next day's extract.
- G3 RMSalso adjusts for canceled and no-show reservations. These are generally delivered to the system with a room revenue of 0.00. When the reservations were confirmed, they did carry a value. Therefore, for optimal system performance,G3 RMSshould treat them as holding a value between the booking and cancellation date. All properties built or re-built after January 16, 2016 use the Rate Value as an approximation of the Room Revenue value. This approximation is not a perfect proxy for the Room Revenue value. However, it is more valid than assuming these transactions held a 0.00 value, which dilutes metrics such as Average Daily Rate (ADR).

### Group Pace Data inG3 RMS

For group business,G3 RMSdoes not receive two items that improve creating booking pace patterns from the historical group block data:
- The date the group moved between status codes. Currently,G3 RMSonly has the block entry date available. However, the block might have been held on a status code where it was not deducting from inventory for a period before moving to a deduct status, or the block might have been held as deduct confirmed for a period before moving to canceled.
- The changes during the booking cycle, like block increases or decreases. Any block changes from the date the block moved from deduct to non-deduct or deduct to canceled until the day of arrival are generally not available toG3 RMS. The system only has this information available after the system begins capturing the data through daily data extracts.

### Example of Differences in Group Pace Data

This example shows the differences between the group data that IDeaS RMS andG3 RMShave available, whenG3 RMSis built from a historical extract:
The illustration shows the following:
- A group was blocked as Tentative (Non-Deduct) at 88 days to arrival.G3 RMSshows the rooms as on books from this point.
- The group signed a contract, and the block moved from Tentative (Non-Deduct) to Confirmed (Deduct) at 54 days to arrival. IDeaS RMS now shows the group as on books in the daily data extracts.
- At 53 days to arrival, the number of rooms changes from 14 to 18. IDeaS RMS sees this change in the daily data extracts, butG3 RMSdoes not have the change available.
- At 41 days to arrival, extra rooms are added to the block temporarily. IDeaS RMS see this change in the daily data extracts, butG3 RMSdoes not have the change available.
- IDeaS RMS sees that the block gradually washes and ends at 13 rooms.G3 RMS, however, only sees the drop-off to the final rooms sold on the Day of Arrival.
Thus, to determine group booking patterns from historical data,G3 RMSknows only that the block was booked at 14 rooms and ended at 13.
When data capture begins,G3 RMSuses the actual observed pick-up and wash patterns, based on the group block extracts. As the volume of data thatG3 RMScollects grows, the system is able to improve its understanding of group booking patterns. After the initial year of data capture,G3 RMShas a more accurate picture of the STLY business conditions
For more information about this process, seeOverview of Building Pace from History.

## BAR by Day Calculations

If your property transitioned from IDeaS G2 RMS toG3 RMS, you might want to understand the important differences between the way the two systems determine BAR by Day.

### G2 RMS

IDeaS RMS produces the BAR by Day decision based on the expected volume of demand for a 1-night LOS, for each individual arrival date.
For example, when it produces the System BAR decision for 28 June, IDeaS RMS considers the demand for a 1-night stay arriving on 28 June.
For longer LOS bookings, the system sums the LOS1 rates. For properties with a higher average length of stay, this method may not always be optimal.

### G3 RMS

For its BAR by Day and Continuous Pricing methods,G3 RMSproduces one pricing decision for each arrival date. To maximize the potential revenue for each arrival date, the system also considers how much demand will stay through that date.
For example, when pricing Sunday, 3 July, the system considers the entire effect of the pricing:
- How many guests arrive and stay just one night versus how many arrive on Sunday and stay multiple nights (Sunday for 2 nights, 3 nights,  etc.).
- How many guests arrive prior to Sunday and stay through (Thursday for 4 nights, Friday for 3 nights, etc.).
Even if the demand for Sunday overall is low, but it is surrounded by high demand dates and has some longer LOS demand staying through the date, you might see  higher pricing for Sunday night.
For properties with higher average LOS, it is important to select the most appropriate pricing methodology. For more information, review thePricing Methodsfor which is best for your property. BAR by LOS may more reliably reflect the demand profile. However, if your property does select BAR by Day pricing or is constrained to BAR by Day,G3 RMSaccounts for the impact of longer lengths of stay, which is a benefit in capturing optimal revenues.
