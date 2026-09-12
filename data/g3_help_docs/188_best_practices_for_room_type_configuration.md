# Best Practices for Room Type Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/BP-Overbooking-Room-Type.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/BP-Overbooking-Room-Type.htm`
- **Ingestion Date:** `2026-09-11 22:14:14`

---

# Best Practices for Room Type Configuration

Review the following general best practices for overbooking, those forRoom-TypeandRun-of-Houseoverbooking, orscenarios.

## General Best Practices for Overbooking

### Allow Overbooking

Overbooking past your property's capacity ensures that your property can sell out and maximize revenue.The RMScalculates overbooking to make up forWashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization.and to maximize revenue through upgrades, while considering the risks (walking guests).
View this video to understand why you should allow overbooking.
Your browser does not support the video tag.

### Be Careful with Restricting Overbooking

You can restrict overbooking through setup or overrides. But that can have unintended, negative consequences.
First, the total property overbooking can never be more than the sum of the overbooking of all room types. Thus, when you limit room type overbooking, you might also limit the overall property overbooking, which has a big impact on the systemâs forecasts and other decisions like pricing, sincethe RMSoptimizes all decisions together.
Restricting overbooking means keepingthe RMSfrom offsetting the forecasted wash. If the system can't overbook enough to offset wash, it might forecast occupancy to be below capacity, despite demand well above capacity. And it might increase pricing andLRV, because the optimal revenue for the lower occupancy might consist of accepting more higher-priced demand.
Watch this video to understand what happens when you limit overbooking at a property.
Your browser does not support the video tag.

### Consider Wash

Do you want to limit the overbooking because you see days with overbooking decisions that seem too high? The high overbooking is likely due to an equally high wash forecast. That wash forecast is based on actual past wash patterns. Review yourgroup business processesto ensure that they are consistent. For example, loading groups at the contracted amount versus at the amount that you expect them to pick up, or deciding how and when group blocks are cut off. Whatever processes you establish, follow them consistently. That keeps the uncertainty low and  enables the system to produce the best possible  forecasts.
The RMSonly forecasts wash if it observed actual wash in the past. For example, you might feel uneasy about overbooking your Suites because there is no higher ranked room type to which you could upgrade. However, Suites might have a higher wash than standard rooms if guests book them because no lower priced rooms are available, then cancel them when cheaper alternatives become available. In this case, allowing to overbook the Suites might be the best option. However, not allowing overbooking might be the right option for the highest priced, accessible room.

### Consider Cost of Walk

Before you limit overbooking, review the configuredCost of Walk.Cost of WalkCost of Walk happens if your property is unable to provide the confirmed room to a guest and has to relocate, or walk, the guest to another hotel. In that situation, costs might include the hotel room at the other hotel, a taxi, etc. 
Cost of Walk influences the overbooking level: the RMS weighs the risks of overbooking, represented by Cost of Walk, against its benefits, which are the additional revenues from selling another room. The higher the Cost of Walk, the lower the RMS tends to overbook.influences the overbooking level.
- Cost of Walk impacts overbooking much less than Wash.
- Changing Cost of Walk to a very low value likely increases the overbooking significantly, because it means a very low risk when overbooking.
- Changing Cost of Walk to a high value likely doesn't result in zero overbooking because of the expected wash. As an extreme example, if the system expects 100 cancellations, then overbooking by 10 is still a low-risk approach, since it only offsets 10% of expected wash.

## Best Practices for Overbooking by Room Type

### Ensure Overbooking Supports Your Upgrade Path

Your overbooking setup must support yourUpgrade Path. The Upgrade Path is meant to handle scenarios when the demand for your Room Classes does not align with the available capacity. For example, in your Upgrade Path configuration, you allowed Standard rooms to borrow unsold inventory from Deluxe rooms if there is no demand for Deluxe but more demand than capacity for Standard. For that upgrade to occur,the RMSneeds to overbook Standard rooms. If you do not allow overbooking for some Standard room types, you might block the Upgrade Path configuration, which leads to unsold rooms despite demand. For more details and examples, reviewHow Overbooking Configuration Supports Upgrade Paths.
Your browser does not support the video tag.

### Allow Overbooking for At Least One Room Type in each Room Class

This enablesthe RMSto share the wash of restricted room types with other room types in the Room Class. Why is this sharing important?
The RMScalculates overbooking for a room type based on its expected wash. That wash doesn't change when you restrict the room type's overbooking through configuration, ceiling default, or a ceiling override. And when the system calculates property overbooking, it must consider the wash ofallroom types.
Thus,the RMSshares the wash of a room type with restricted overbooking, adding it to the overbooking of other room types in the same Room Class. This sharing  only works if the receiving room type allows overbooking without any ceiling. Seescenarios for Overbookingfor examples.

### Use Wash or Cost of Walk Overrides Before Restricting by Season

Before restricting overbooking for a season, review and, if necessary, override the wash for that period first. Also, if you think the overbooking should be different during this season due to a higher cost of relocating guests, use a Multiday Cost of Walk Override instead. For a single event or a short period of time, it is easier to use the override functionality for Cost of Walk and overbooking inOverbooking Management.

### Decide If You Need to Set Up Special-Use Room Types

Special-Use Room Types are room types that you don't sell publicly or that don't sell easily due to their features, like accessible rooms (for other examples, seeRoom Class). By allowing  to distribute their unsold capacity as overbooking to the other room types in the same Room Class, you helpthe RMSoptimize overbooking. Select Special-Use Room TypeandDistribute Unsold Capacity if you can move guests into Special-Use Room Types, if needed.
Donotselect Distribute if moving guests into Special-Use rooms might cause issues and complaints.
Note: If you select Special-Use Room Types but not Distribute Unsold Capacity,the RMStreats those room types the same as when you don't select Special-Use and don't allow overbooking for them.

### Decide ifthe RMSShould Reduce Overbooking Based on Closed Competitors

Some properties are in a market where, during high-demand periods, they have few or no appropriate options to walk  (or relocate) guests to, should they need to. Meaning, if their shopped competitors are sold out, they might not be able to walk guests.If market data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section., such properties can reduce the risk of walking by havingthe RMSautomatically reduce overbooking based on a certain % of competitors being unavailable.
If you select that option, you define the % of closed competitors. Whenthe RMSsees in the publicly available data that this threshold is reached, it reduces overbooking and displaysinOverbookingand in theSummarytab. If no competitor has a price available for a one-night length of stay, the system reduces property overbooking to zero. If competitors open up again,the RMSincreases overbooking too. You can set up aNotificationto monitor overbooking changes.
Note: Learn about the possibleunintended consequencesof this option which, like overrides, restricts overbooking.
Whenthe RMSapplies the % threshold, it considers:
- Only competitors checked for Use Rate Shopping Data or Use in Competitive Market Position Constraints.
Only competitors checked for Use Rate Shopping Data or Use in Competitive Market Position Constraints.
- Only competitors not set to Ignore Competitor Data.
Only competitors not set to Ignore Competitor Data.
- A competitor with no price for a one-night stay for any room type or any channel. For example, if there is a price for only 1 room type and 1 Channel, but not others,the RMSconsiders the competitor open.
A competitor with no price for a one-night stay for any room type or any channel. For example, if there is a price for only 1 room type and 1 Channel, but not others,the RMSconsiders the competitor open.

## Best Practices for the Run-of-House Overbooking Option

### Understand How Run-of-House Works

Run-of-house overbooking assigns all overbooking to the selected room type. If you choose a second run-of-house room type, all overbooking is split between the two selected room types relative to their capacity.the RMSconsiders washand your Upgrade Pathto determine the room type overbooking values. See asimplified scenario.
Run-of-house overbooking can limit your revenue potential, because all higher priced room types are never overbooked. It can be the right option for some limited-serviceclientsbecause it is simpler to set up and manage:
- Only select the Run-of-House room type. All other overbooking setup is fixed, for example, no option to vary by season.
- YourUpgrade Pathis fixed and all higher-priced Room Classes accept upgrades from lower-priced ones.
- You apply overbooking overrides only at the property, not the room type level.
Note that if you have more than one Room Class, the selected run-of-house room type (or types) should be in the lowest Room Class. If you have more than two Room Classes, the room type should be in the Room Class that typically has excess demand.

### Use Upgrades to Balance Your Inventory

Using run-of-house overbooking, one or two room types can potentially get overbooked up to a high level. You need to balance your inventory through upgrades or upsells, either at or shortly before check-in. Therefore, select a room type from which you can easily upgrade without causing operational challenges.
While a large number of upgrades or upsells might be an operational issue, it is not an issue for the system's unconstrained forecasts. The system can track the demand both at the booked and the stayed room type level. For example, when a guest books a Standard room and, at check-in, gets upgraded for free to a Suite because it is the last room, thenthe RMSunderstands that this demand represents Standard and not Suite demand.  SeeComplimentary Upgradesfor more information about business practices for upgrading guests and for more details about booked versus stayed data.

## Scenarios

### Scenarios for Overbooking by Room Type

When you select to not allow overbooking for a room type,the RMSproportionately allocates the room type's expected wash to other room types in the same Room Class, based on their capacity, as long as the receiving room types allow overbooking.The receiving room type depends on the Upgrade Path configuration inPrice Ranking and Upgrade Path.
The examples below illustrate howthe RMShandles the expected wash in the Room Class while balancing the expected wash at the room type level. These examples only apply to hotels that have a mixture of room types in a Room Class, some that allow overbooking and others that do not.

#### Example 1

In this example, one Room Class in the hotel has 100 Rooms. The majority of them are Twins. This Room Class is the lowest valued in the hotel.
The RMSallocates additional overbooking based on the expected wash from the Accessible room type. Its allocation is proportionate to the percentage capacity represented by the room type.

#### Example 2

In this example, one Room Class in the hotel has 100 Rooms. The majority of them are Twins. This Room Class is the lowest valued in the hotel. Only the Twin room type is set up without any limit and can receive any shared wash. The Double room type has overbooking allowed but has a ceiling. Therefore, its wash is not shared.The RMSallocates only the additional overbooking from the Accessible room type to the Twin room type.
The property overbooking decision is constrained, because two rooms of wash from the Double are not considered.

#### Example 3

In this example, one Room Class in the hotel has 60 rooms. The majority of them are Twins. This Room Class is the lowest valued in the hotel.
In this case, both room types have an overbooking ceiling applied in Overbooking Management.
The RMSconsiders the wash for each room type separately (because both room types have a limit), meaning that the system can't consider the wash in the Accessible room. In this scenario, limiting the room type overbooking directly impacts the total property level overbooking, since  total property overbooking decision is never higher than the sum of the overbooking of all room types.

### Run-of-House Scenario

You have two Room Classes, Standard and Suite. Standard includes your Run-of-House room type, STKG. For all room types combined,the RMSexpects 10 rooms of wash, so property overbooking is 10 rooms.
STKG receives the overbooking of all room types. Additionally, overbooking considers the Upgrade Path. That means that if the system expects 5 Suites to remain unsold for a date, the STKG overbooking is 15, 10 to offset the wash plus 5 rooms thatthe RMSexpects you to upgrade to fill the Suites.
