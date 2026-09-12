# Best Practices for Setting Up  Room Classes

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/BP-Rooms-Room-Class.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/BP-Rooms-Room-Class.htm`
- **Ingestion Date:** `2026-09-11 22:14:30`

---

# Best Practices for Setting Up  Room Classes

## Group Room Types with Similar Demand

Group room types with similar demand and pricing into a Room Class, while considering the effort of monitoring. See theCreating Room Classesvideo for examples.
The RMSassumes that demand is transferable between room types of the same Room Class. Therefore, combine room types with similar prices into one Room Class only if you can easily transfer from one to the other and upgrade to the next Room Class.
To explain, let's look at some examples.

### Example 1: Demand for the 2 Doubles is low, mostly single occupancy

In this example, you have two room types, one with 1 King, the other with 2 Doubles, both priced similarly.
You can move reservations for the King room type to the 2 Doubles with little or no resistance. There is high demand from families on weekends that you can't transfer to the King, but if that demand exceeds capacity, you can accommodate guests in the next higher Room Class without issues.
Recommendation: Assign both room types into one Room Class if they are similarly priced. If necessary, restrict overbooking for 2 Doubles on weekends.

### Example 2: Demand for the 2 Doubles is high, mostly triple occupancy or more

This example uses the same two room types as above, one with 1 King, the other with 2 Doubles, both priced similarly.
The demand for Kings is mostly for double occupancy from couples. You can't move either demand to the other room type without complaints. The next higher Room Class can accommodate only 2 guests, and you need to upgrade excess demand for 3 or more guests to the third highest Room Class.
Recommendation: Separate the room types into two Room Classes, each with its own upgrade path, seeScenario 4 in Advanced Price Ranking and Upgrade Path. Note that separate Room Classes is the right choice regardless of the number of guests, if you wantthe RMSto be able to price the 2 Doubles much higher than the Kings based on demand.

### Example 3: Room Types with Different Characteristics

The same concept of transferable demand applies to  other characteristics, like differences in smoking preference, view or accessibility.
For example, for a city property, guests might perceive a Deluxe room type that is considerably larger than the Standard room type as more valuable. If so, put the Deluxe room type into a separate Room Class.
The size difference likely matters much less to guests in a suburban or rural property. If so, put both Standard and Deluxe room types  in one Room Class.
Guests at a resort might perceive a room type with a view of the parking lot as inferior to a smaller ocean-view room type. That means you can't upgrade from an ocean-view room type to a larger parking lot-view room type. In this case, put the similarly sized room types with different views into separate Room Classes.

### Example 4: Negotiated Contracts

Your ability to transfer demand between room types can also be impacted by negotiated accounts.
Let's say you have several accounts with a rate negotiated for the Standard Queen room type. Other room types in the same Standard Room Class are not available for the accounts to book. Whenthe RMSsees more demand from that market segment than the available capacity of the Standard Queen, it assumes the demand is transferable to the other Standard room types. In reality, bookings from the accounts stop when there are no more Standard Queens left to book. In this case, create a separate Room Class for the Standard Queen room Type.

## Group Similarly Priced Room Types

Combine two room types with similar demand into one Room Class only when the ADR difference between them is less than 20%. Otherwise, you negatively impact the system's ability to optimize pricing and LRV and to forecast ADR for the Room Class.
To assist you with grouping similarly priced room types,the RMSdisplays the ADR for each room type from the past year in Rooms setup. The ADR updates during eachBusiness Day End Processing. If the data is provided by yourreservation system(usually PMS or CRS), the ADR refers to booked, not stayed. Booked means thatthe RMSignores if the reservation is upgraded from the initially booked room type. If you don't know whetherthe RMSis using booked or stayed data, click Important Informationin the top right corner and look forData Used for Forecasting and Optimization.
Let's look at two examples.

### Example 1: Two Suites with Significantly Different Pricing

You combine two suites into one Room Class. The ADR for room type Suite A is 1000, for Suite B 5000. You set up a pricing difference of 4000 between them. For room types with such different pricing and ADR, how canthe RMSknow theValue of Demandfor this Room Class and find one optimal price? With the price difference that is set up, the room types are either priced too high or too low. Same for the ADR forecast. In this case, the suites should not be in the same Room Class.

### Example 2: Controlling the Price Differences Between Room Types

What if you want control over the price differences between room types? Let's say you have two room types that have the same size but vary greatly in guest perception: one with a highly-priced ocean view, the other with an undesirable parking lot view. Both can be upgraded to the next higher Room Class.
One option is to put both into one Room Class and set up pricing so that ocean view is always more expensive. In this scenario, the hotel controls the price difference between ocean view and city view.
You could also put them in two different Room Classes and letthe RMSprice them independently. Here, the system decides on the price difference between the two Room Classes, based on demand and willingness to pay. With this setup, you can still ensure that ocean views are always priced higher than city views
From a revenue maximization perspective, the second option is likely the better one. However, you might select the first option to ensure pricing clarity for guests and to protect brand image. For example,  what ifthe RMSchooses  much lower pricing for city view than ocean view? Does that make the city view rooms appear significantly inferior? If so, you might want to avoid the second option.

## Keep Low Capacity Room Types in Their Own Room Class

What if you have a room type that is priced and perceived very differently from other Room Classes, but that contains only 5 rooms or less. This can apply to Signature Suites or a single room like a Presidential Suite.
Generally, we recommend that you keep such a room type in its own Room Class, due to the price difference.If you plan to set up such a low capacity Room Class, contact your IDeaS representative.
Expect higher forecast fluctuation in this Room Class because a Room Class with low capacity has very little booking data at that  level.The RMScan deal with such situations, but it results in higher uncertainty. That means higher forecast fluctuations compared to forecasts for a Room Class with large amounts of booking data. For example, one unexpected booking of a Standard room type rarely ever causes a change to the forecast of the Standard Room Class. But one unexpected booking of the Presidential Suite (in its own Room Class) likely causes changes to the forecast, especially the revenue forecast.

## Consider the Effort of Monitoring

The more Room Classes, the more forecasting levels you need to monitor. For example, if you have 10 Forecast Groups and 10 Room Classes, you have 100 forecasting levels, one for each combination.The RMScan easily forecast, optimize, and produce controls at that many levels. But it might be cumbersome for you to review and, if necessary, override the forecast and decisions at that many levels.

## Manage Zero Capacity  Room Types

Under certain circumstances,the RMSreceives a room type with a capacity of zero. Follow one of these guidelines, depending on the circumstance:
- Discontinued Room Type with a New Equivalent: For example, you renamed the room type or its capacity moved to another room type. Assign the discontinued room type to its new equivalent room type.
- Discontinued Room Type with No Equivalent: For example, you removed the room type completely or it changed after a renovation. Without a matching Room Class there is no benefit to assigning it. In theunassigned zero capacity room type Alert, selectKeep the new room type unassignedso thatthe RMSexcludes it from forecasting and optimization.
- Component Room Type: If you are using the Component Rooms module, assign the room type to a Room Class if it represents a Component Room Type. SeeSelect Component Rooms.
- Pseudo Room Type: Pseudo room types typically do not appear in Rooms setup. If they do, leave them unassigned. If you assign them to a Room Class,the RMSmight get the wrong impression of the value of demand for that Room Class.
After you assign a room type to a Room Class, it must remain in a Room Class. All Room Classes must have a capacity of at least one room. You can't assign all  zero capacity room types to a separate Room Class.

## Manage Room Types That You Don't Sell Publicly or That Rarely Sell

There are two examples for this:
- Rooms that often remain unsold due to their features, for example, accessible rooms.
Rooms that often remain unsold due to their features, for example, accessible rooms.
- Rooms not sold on yourselling systemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.. This could be rooms of a lesser quality which you sell only to groups or contracts. They might be in a separate building and harder to access, thus difficult to sell to individuals but not to a group that reserves all of them. Other examples are a connector room for a suite or a specialty suite that you only assign to specific guests.
Rooms not sold on yourselling systemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.. This could be rooms of a lesser quality which you sell only to groups or contracts. They might be in a separate building and harder to access, thus difficult to sell to individuals but not to a group that reserves all of them. Other examples are a connector room for a suite or a specialty suite that you only assign to specific guests.
If you have either of these room types, assign them to a Room Class with other room types of a similar  value.The same applies to setting upPricingfor such room types. If you instead consider a Room Class that contains only such room types,first review the options to set upspecial-use room types.

## Be Careful When You Change Room Classes

You might need to change Room Classes after the initial setup. For example,a renovation moves a room type from one Room Class to another orthe capacity changes for room types. Such changes impactthe RMS. And when the system is inDecision DeliveryA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system., the impact is larger than in the initial setup.
Follow thesestepsto avoid issues like processing disruption, occupancy discrepancies or, in the worst case, a costly and time-consuming rebuild ofthe RMS. Due to the severity of the impact, we suggest in many cases that you stop Decision Delivery until you have reviewed the revised forecast and decisions.

### Impact of Room Class changes on Forecasts and Decisions

Most changes to Room Classes impact forecasts and decisions, andthe RMSneeds to re-synchronize data. In that case, you see theSyncflag iconin the menu bar. The impact depends on the type of change:
- New room types: Sincethe RMShas no historical data for a new room type, the system needs to begin learning about patterns like seasonality. Therefore, closely monitor forecasts and decisions for Room Classes with new room types untilthe RMSlearns the new patterns.
- Moved room types: When you move an existing room type to a different Room Class,the RMShas historical data to create new, changed forecasts and decisions for the impacted Room Classes. The magnitude of changes depends on the affected room typeâs capacity and its impact on the old and new Room Classes. As a guideline, if the inventory shift between Room Classes is 15% or more of the total hotel capacity, the system's forecast and decisions might change significantly.
