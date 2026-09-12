# Best Practices for Overbooking Overrides

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Overbooking/BP-Overbooking-Overrides.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Overbooking/BP-Overbooking-Overrides.htm`
- **Ingestion Date:** `2026-09-11 22:14:26`

---

When Should I Use Overbooking Overrides?
Understand the Process to Decide if a Overbooking Override is Best

# Best Practices for Overbooking Overrides

Because overbooking overrides can have unintended consequences, we instead recommend that you influence overbooking through wash or cost of walk overrides, whenever possible.

## Understand When to Use Overbooking Overrides

You should override overbooking when you know something thatthe RMSdoes not. For example, a new group with potential for return business requires all the rooms with separate beds in your hotel. In that case, you may want to limit overbooking for that room type to ensure nobody in the group is forced into a room with only one bed. You know that the future revenues from that group outweigh any loss from not maximizing revenues on the arrival day of the group, so share that information with the system.
View the video in Resources on the right to understand when you should override overbooking.

## Understand the Process to Decide If an Overbooking Override is the Best Solution

Following this overview of the process, click on any of the steps to learn more.Download a PDF of the process in the Resources.
If your property uses Run-of-House overbooking setup, some steps don't apply. Learn howthis overbooking setup works.
The RMSoptimizes all decisions together, so overriding overbooking directly impacts other decisions in the system. For example,  by lowering overbooking with an override, you keepthe RMSfrom offsetting wash. The system might forecast occupancy to be below capacity, despite demand that is well above capacity.
That overbooking override might also increase pricing and Last Room Value (LRV) because less capacity means accepting less lower-priced demand. And if an overbooking override blocks the Upgrade Path, then decisions for Room Classes ranked above the one with the override are also impacted.
The RMSprimarily overbooks to offsetWashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization., so first review wash forecasts. You can answer most questions about overbooking by reviewing and, if necessary, overriding wash, seebest practicesto learn more.
If you are concerned about overbooking and wash of a high-priced Room Class, like Suites, reviewthis consideration.
If you agree with the wash forecasts, and you are concerned with the overbooking at the property level, review theCost of WalkCost of Walk happens if your property is unable to provide the confirmed room to a guest and has to relocate, or walk, the guest to another hotel. In that situation, costs might include the hotel room at the other hotel, a taxi, etc. 
Cost of Walk influences the overbooking level: the RMS weighs the risks of overbooking, represented by Cost of Walk, against its benefits, which are the additional revenues from selling another room. The higher the Cost of Walk, the lower the RMS tends to overbook.. Cost of Walk can impact how aggressivelythe RMSoverbooks so, if needed, override Cost of Walk orchange its setup.
- Cost of Walk impacts overbooking much less than Wash.
- Changing Cost of Walk to a very low value likely increases the overbooking significantly, because it means a very low risk when overbooking.
- Changing Cost of Walk to a high value likely doesn't result in zero overbooking because of the expected wash. As an extreme example, if the system expects 100 cancellations, then overbooking by 10 is still a low-risk approach, since it only offsets 10% of expected wash.
If you disagree with overbooking often, review the following setups:
Room Type Configuration:
To ensure that your property can sell out and maximize revenue, your setup should allow overbooking for at least one room type in each Room Class. Otherwise you constrain the total property level overbooking, because the total property overbooking can never be more than the sum of all room type overbooking. Click the above link to learn more.
Upgrade Path:
If you're concerned about a high room type overbooking, for example 30 rooms for the Standard room type in a property of 100 rooms, review your Upgrade Path.
Often there is more demand than capacity for your lower-priced Room Classes and not enough demand to fill the more expensive ones. In this case, the system overbooks lower Room Classes more than what is needed to offset wash, with the expectation that you'll upgrade or upsell, based on your Upgrade Path setup. To see if that's the case, review theRemaining DemandThe remaining unconstrained demand for a date in the future. This value is either generated by the RMS or, in case of an active user demand override, the user override value plus or minus a possible system adjustment. The RMS adjusts a demand override according to the booking pace, so the override remains accurate after its implementation.versus the Occupancy Forecast for each Room Class.
Note that the overbooking at the property level supersedes the  overbooking at the room type level. In the above example, if the property-level overbooking is five, and the property is oversold by five rooms, thenthe RMSdoesn't accept any further reservations, even if the room type level overbooking has not reached the maximum of 30.
Allow overbooking for at least one room type in each Room Class. This way, when you constrain overbooking for a room type (either through room type setup or with an overbooking override),the RMSproportionately allocates the room type's expected wash to other room types in the same Room Class, based on their capacity.  For examples, seeScenarios for Room Type Overbooking.
Overbooking Ceilingsallow you to set a maximum amount of overbooking, while you still let the system optimize the overbooking below that ceiling.The RMScan adjust the overbooking as the conditions change.
- Overbooking Ceiling Defaults apply to all future dates at the property or room type level. Before you use Ceiling Defaults,  review thebest practices.
Overbooking Ceiling Defaults apply to all future dates at the property or room type level. Before you use Ceiling Defaults,  review thebest practices.
- Apply Overbooking Ceiling Overrides instead of a specific value override for the day so thatthe RMScan still optimize the overbooking within the upper limit.
Apply Overbooking Ceiling Overrides instead of a specific value override for the day so thatthe RMScan still optimize the overbooking within the upper limit.
Overbook by a specific number of rooms for the day at the property level. This type of override limitsthe RMSto use that value instead of  its own optimized decision, until you change or remove the override.
In the system's overbooking calculation, Cost of Walk defines the monetary risk from overbooking too much and incurring walks. The system weighs that risk against the revenue reward for selling an additional room. The higher the Cost of Walk, the lowerthe RMStends to overbook. Use a Cost of Walk override when the values vary from the default. For example, when a large, two-day convention sells out all hotels and your Cost of Walk  increases.
In the rare cases when you need to override overbooking for more than just one day at a time, useMultiday Overbooking or Cost of Walk Overrides. While it's a convenient option, use it only after reviewingother factorsthat impact overbooking. That's because any unintended consequences or a mistake impact a long period.
If you feel you have to override overbooking for longer periods, contactyour IDeaS representative or open a case forIDeaS Support.
Overbooking overrides not only can have unintended consequences but they are also hard overrides thatthe RMSdoesn't adjust. Therefore, as part of yourregular tasks, review all your overrides at least weekly to ensure that they remain accurate. Always  add a noteto your overrides,
 in your next review they help you decide if you can  remove them.
