# Best Practices for Group Block Business

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Wash/Group-Business-Practices.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Wash/Group-Business-Practices.htm`
- **Ingestion Date:** `2026-09-11 22:13:17`

---

# Best Practices for Group Block Business

Use these best practices to manage group blocks in theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.to ensure thatG3 RMScan produce the best possible forecasts and outputs (like pricing). You use group blocks for the following business:
- Groups (like tour groups or corporate groups, etc.).
Groups (like tour groups or corporate groups, etc.).
- Allotments, also called allocations (rooms held for a Travel Agent with a rolling cut-off or rooms held for an air crew).
Allotments, also called allocations (rooms held for a Travel Agent with a rolling cut-off or rooms held for an air crew).
Note: Terminology might differ in your reservation system, for example, calling a group block a business block.
Use Group Blocks to manage groups and allocations instead of creating individual reservations.  For issues due to inconsistently using group blocks, see theWash Overrides for Individual Groups are disabled Alert.
The remaining best practices are split into which of  the two parts of a group block in thereservation systemthey apply to:

### Group Block Header

TheGroup Block Headercontains the general information.
For allotments,  or allocations,G3 RMSonly forecasts wash if they are set to deduct from inventory, seeGroup Status Codesfor definitions. Therefore we recommend that you set allotments with significant production to deduct, so that you view the allotments and their wash in the system.
Note that allotments are called Transient Blocks inG3 RMS, for a detailed description seeattributes.
After a group is confirmed, enter the group block as deduct as soon as possible. Delaying the entry impacts howG3 RMSmeasures and forecasts pace.
Follow consistent practices for when you update the status of a group, especially when it moves from a non-deduct to a deduct status. This ensures thatG3 RMSknows the correct number of rooms that it needs to deduct from the available capacity.
The Market Field identifies the appropriate market segment (also sometimes called market code) for the bookings on the block. Ensure that this field is mandatory and the correct market segment is assigned immediately.
Market segments should only contain grouportransient business.G3 RMSneeds market segments that exclusively define group business to ensure the best possible forecasts and decisions, seeinconsistently using group blocks.
Group blocks should also have the same market segment as the individual reservations that are picked up from that block.
G3 RMSneeds to know the net, room only, value of reservations, including of group reservations.
You can set up packages and rate codes many ways in thereservation system. Ensure thatG3 RMSreceives the net rate value for the group block by setting up any included packagesas Add to Rate, if you attach one or more packages to the rate code. This ensures thatG3 RMScorrectly receives the net room revenue.
Group blocks can also be defined by entering the rate value into the group block inventory, instead of having  a specific rate code. In that case attach any package elements and taxes to the group block header to ensure thatG3 RMSsees only net room revenues on group blocks.
If available, use the complimentary room functionality in thereservation systemto account for free rooms, for example, 1 in 50 rooms is free. If no such feature exists,  make individual reservations from the group block and change the rate to zero.
Do not delete group blocks. If you do,G3 RMSmight not receive the deletion and that might even lead to a duplication.

### Group Block Inventory

Group Block Inventory is where room inventory is held and where rates are assigned(unless you used rate codes to define the rate amounts on the Group Block Header).
Ensure that the number of rooms and their rates by occupancy (single, double etc.) and by room type are correct. Communicate with groups to get their current numbers, and make any changes to the group's rooms in a timely manner, similar to updates of a group's status.
Use only physical room types for group blocks, don't use pseudo, house, or run-of-house room types.G3 RMSmanages only physical, yieldable capacity. Therefore, sell only actual, physical rooms as blocks to ensure the system knows what is occupied by room type.
The best practices differ between selling run-of-house or specific Room Types:

##### Run-of-House

Hotels often sell groups a run-of-house room type and then move the block or reservations to specific room types later. However, you should set up all group room inventory only against a physical room type (for example, the Base Room Type like the standard double or twin), even if this means overbooking these room types.G3 RMSunderstands that you will move the block or reservations to available room types later.

##### Room Type

Enter the group block into the room types that you sold, regardless of availability. For example, you sold Standard rooms to a group but Standard rooms are sold out. In that case, don't place the group in the available Deluxe rooms at a Standard price. Instead overbook  Standard and upgrade them later. This helpsG3 RMSunderstand the true demand for Standard.
WhileG3 RMSdoesn't receive cut-off dates from some reservation systems (like Opera PMS), it is important that you apply cut-off procedures consistently.When the cut-off date arrives,eitherkeep the group blocks intact until closer to arrivalorcut blocks off immediately and release them back for general sale.
Both methods work well forG3 RMSbut only if you apply them consistently. Mixing the two methods increases the uncertainty and leads to suboptimal group wash and demand forecasts.
Maintain a consistent procedure to load groupseitherat the 
 contracted amountorat the amount you expect them to pick up. To illustrate, let's say you have two groups, group A and B, both with 40 rooms contracted. You block group A at a pre-washed amount of 30 rooms and group B at the contracted amount of 40 rooms. Both end up with a final pick up of 30 rooms.
BecauseG3 RMSonly sees the amount of rooms that are blocked in yourSales and Catering system, not the contracted amount, it sees 0% wash for group A (30 pick up out of 30 blocked) and 25% wash for group B (30 pick up out of 40 blocked). If the system builds patterns and forecasts wash based on such groups, it will lead to suboptimal wash forecasts that are likely due to the large uncertainty with observed pick-up patterns.
The currency on the group block, including the rate codes on the block header and the currency on the block grid, should be the base currency of thereservation system. This ensures thatG3 RMSis presented with consistent data.
