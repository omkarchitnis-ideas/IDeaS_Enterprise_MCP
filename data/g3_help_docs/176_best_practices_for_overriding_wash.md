# Best Practices for Overriding Wash

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Wash/BP-Overriding-Wash.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Wash/BP-Overriding-Wash.htm`
- **Ingestion Date:** `2026-09-11 22:14:06`

---

Understand the Process to Decide if a Wash Override is Best

# Best Practices for Overriding Wash

## Understand the Process to Decide If a Wash Override is the Best Solution

Following this overview of the process, click on any of the steps to learn more.Download a PDF of the process in the s.
If theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.doesn't provide a cut-off date tothe RMS, we recommend setting the wash override to expire on the group's cutoff date.
For example, you know that the group expects to pick up very few of their contracted rooms, so a higher wash applies until the cutoff date. After the cutoff, cancels and no-shows are comparable to other groups, so the override should expire and the systemâs wash forecast should apply again.
Maintain consistent 
 group business practices to ensure the best possible wash forecasts. For
 example, you should have an established procedure to load groupseitherat the 
 contracted amountorat the amount you expect them to pick up.
SeeGroup Block Business Practicesfor details.
The RMSforecasts wash for each group that is on books, both for picked up reservations and for available block. It uses the Forecast Group wash patterns, group-specific data like picked up versus total group block and, if available, cut-off date. Mostclientsuse this type.
If you manage many groups, consider using the Group Occupancy Forecast Override to enter the expected final pickup by Forecast Group. Then,the RMScontrols and adjusts the remaining demand and wash for all groups in that Forecast Group.
This type of wash override isn't as precise as at the individual group level, but for someclients, the gain in efficiency due to fewer overrides outweigh that downside. To learn more about the steps, setup and best practices, reviewGroup Occupancy Forecast Override.
The wash percentages are calculated only on the Remaining Demand that the system will accept, not the Remaining Demand that the system plans to restrict because it is too low-priced.
For example, you have zero rooms on books for one Forecast Group, 100 rooms Remaining Demand, theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).is 40 rooms, but only 20% wash. This means that the system is restricting 50 out of the 100 rooms of Remaining Demand because it is unwanted low-priced business. The remaining 50 rooms represent the optimized demand that gets washed by 20%, resulting in the Occupancy Forecast of 40 rooms.
If you question a high wash value for a date far in the future, keep in mind thatthe RMSadjusts the wash forecast depending on the booking window. The wash might be high becausethe RMSexpects high wash for a group on the cut off date, close to arrival.  As the arrival date draws closer,the RMSwill adjust the wash percentage.
The RMSoverbooks to compensate for the loss caused by wash, thus the higher the wash, the higher the overbooking. As part of yourregular tasks, review all your overrides at least weekly to ensure that they remain accurate. Use notes 
 so that you understand in your next review why you added or removed the override and what the conditions were.
