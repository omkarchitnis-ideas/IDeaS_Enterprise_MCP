# Best Practices for Setting Up Cost of Walk

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/BP-Rooms-Cost-of-Walk.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/BP-Rooms-Cost-of-Walk.htm`
- **Ingestion Date:** `2026-09-11 22:14:34`

---

# Best Practices for Setting Up Cost of Walk

## Set Up Accurate Cost of Walk by Using and Reviewing the Default Values

For each room type and day of week,the RMScalculates the default Cost of Walk values at 1.5 times the total ADR of the available data, up to 365 past and 365 future days. The system does that automatically in the initial system setup, or when you clickto refresh the values. You review and, if necessary, update the default values.
- During the initial setup, we recommend that you leave the default values unchanged unless they are extreme or clearly incorrect.  After the system produces overbooking decisions, but before it sends them to yourselling system,  review those decisions and, if needed, change Cost of Walk.
During the initial setup, we recommend that you leave the default values unchanged unless they are extreme or clearly incorrect.  After the system produces overbooking decisions, but before it sends them to yourselling system,  review those decisions and, if needed, change Cost of Walk.
- After the initial setup, review the values regularly to keep them accurate. You can click to refreshand replace the values with new defaults based on the ADR of the available data.
After the initial setup, review the values regularly to keep them accurate. You can click to refreshand replace the values with new defaults based on the ADR of the available data.
Note: Ifthe RMSdoesn't find enough historical or future data to create reliable default Cost of Walk values, it warns you with thisAlert. In that case or, if your property uses aSynthetic Data build, review and change the Cost of Walk values to meet your expectations.

## Don't Match Cost of Walk to Your Exact Costs

Don't try to match your Cost of Walk values to the exact costs for your property.   Instead, view the Cost of Walk as an influence on the overbooking decisions. The values inthe RMSrepresent the monetary risk associated with overbooking too much and incurring walks, while at the same time considering the revenue reward for selling an additional room.

## Understand How Cost of Walk Impacts Overbooking

Increasing the Cost of Walk values tends to lower the overbooking decisions without the risks of overriding overbooking.
- Cost of Walk impacts overbooking much less than Wash.
- Changing Cost of Walk to a very low value likely increases the overbooking significantly, because it means a very low risk when overbooking.
- Changing Cost of Walk to a high value likely doesn't result in zero overbooking because of the expected wash. As an extreme example, if the system expects 100 cancellations, then overbooking by 10 is still a low-risk approach, since it only offsets 10% of expected wash.

## Use Overrides Where Needed

UseCost of Walk overridesin Overbooking Management when the values vary from the default. For example, when a large, two-day convention sells out all hotels and your Cost of Walk  increases. If the Cost of Walk varies for a longer period, like during your slowest season, use theMultidayoption.
