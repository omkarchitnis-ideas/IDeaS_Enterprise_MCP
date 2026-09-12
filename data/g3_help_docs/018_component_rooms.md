# Component Rooms

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Component-Rooms/Component-Rooms.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Component-Rooms/Component-Rooms.htm`
- **Ingestion Date:** `2026-09-11 22:12:19`

---

# Component Rooms

If you add the   Component Rooms subscription, you can  maximize your revenues from such guest rooms, meaning from virtual rooms that exist when you combine two or more physical rooms. In yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system., component rooms might be known as Virtual Suites or Component Room Types. Seedefinition and examplefor more.
With Component Rooms enabled,G3 RMSconsiders your component rooms in its forecast and decisions. That helps you decide whether to sell component rooms as separate physical rooms or as combined component rooms.

### What Do You Want to Know about Component Rooms?

- I need to knowhow to get started.
- I want a definition and anexample of Component Rooms.
- I want to check if my property would benefit fromG3 RMSComponent Rooms.What should I do next?
- I need to set up Component Rooms.Give me an overview of the steps.
- What arebest practicesfor setting up and managing Component Rooms?

### Getting Started

If your property is interested in optimizing Component Rooms inG3 RMS, contact your IDeaS representative. You review the required integrations and cost, then you complete the below questionnaire. Then you can have a call with your IDeaS representative to discuss your property's Component Rooms inventory, selling strategy, and data. Together you can ensure that your Component Rooms setup is optimal.
IDeaS Component Rooms Questionnaire
Component rooms consist of two or more physical rooms. The physical rooms are sold individually with the door closed. With the door open, the physical rooms are sold together as a single component room. Selling a component room means that all  its component parts are also sold. Following is an example:
Blue rooms= physical room types
Green rooms= component room types
In this example:
- KING and DBL combine to form component room type KINGSUITE. Selling one KINGSUITE sells the KING and DBL rooms.
- DLX and DBL combine to form component room type DLXSUITE. Selling one DLXSUITE sells the DLX and DBL rooms.
- DBL is shared between all the component room types.
- The two component room types, KINGSUITE and DLXSUITE, combine to form component room type PRESIDENTIAL. Selling PRESIDENTIAL sells the four physical rooms.

## Setup Steps

### 1. Set up Component Rooms

The reservation system doesn't send  all the component room information thatG3 RMSneeds. Use Component Rooms setup to provide  this information. It consists of three steps:
- Select Component Rooms: exclude other zero capacity room types thatG3 RMSmight have imported, like pseudo or paymaster room types.
- Map Component Rooms: define how many rooms of a physical room type can be used to form a component room.
- Shared Physical Rooms: define which room numbers of a physical room type can be used to form a component room.

### 2. Complete Rooms Configuration

Once you have defined your component rooms, youset up all your rooms, for example mapping room types to Room Classes.

### 3. Enter  Out of Order Component Rooms

G3 RMSdoesn't receive out of order details or room numbers for out of order component rooms. Use theComponent Rooms OOOpage to share this information withG3 RMS.

## Best Practices

In general,G3 RMShandles component rooms the same as any other room type. The system accounts for their demand and price sensitivity and includes them in its optimization and decisions.
In some instances,G3 RMSbehaves differently when the Component Rooms module is active. Review these best practices so you understand those differences. For best results, review and follow theComponent Rooms Reservation Practices.

#### Understand How to Map Component Room Types to Room Classes

Follow these rules in theRoom Classsetup:
- Do not place a component room type in the same Room Class as its component parts. Keeping them separate helpsG3 RMSunderstand the demand separately for the component parts and the component room.
- You can combine a physical and a component room type in a Room Class if the physical room type is not part of the component room. As with all room types in the same Room Class, the room types should have similar characteristics.
- You can place component room types that do not share component parts into the same Room Class.

#### Manage Your Overbooking

G3 RMSdoesn't calculate overbooking for component room types becauseselling systemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.usually accept decisions only for physical room types. You can't select the option to allow overbooking for component room types in theRoom Typesetup. For other room types where overbooking is set to None,G3 RMSsends0as the overbooking value. For component room types, the system doesn't send an overbooking value, since a selling system could misinterpret the value.

#### Understand the System's Upgrade Path Rules

Although component room types can't be overbooked,G3 RMSstill considers the possibility that component rooms can be upgraded. The system uses your Upgrade Path to know how to handle wash and not lose demand. The system doesn't allow the following:
- You can't upgrade from Room Classes with only physical room types to Room Classes with only component room types.
- A physical room that is the component part of a component room canât be in a higher ranked Room Class than the component room.
In the following example, you canât upgrade from Room Class 1 to Room Class 2 (indicated by price rank only arrow), because 1 contains only physical room types and 2 contains only component room types.
Properties with component room types are more likely to have small Room Classes and to require theAdvanced Upgrade Path.
Review the best practices below or, for a shorter summary, click the PDF button:

#### Understand Potential Differences in LRV

G3 RMSoptimizes LRV for each Room Class, including those that contain component room types.G3 RMSknows that it can be more valuable to hold component parts to sell as component rooms. In this case,G3 RMSmight raise the LRV abovethe primary priced productfor the component parts, to protect their capacity for sale as component rooms.
Let's use the KINGSUITEexamplefrom the overview and assume its component parts are in a separate Room Class. If there is high demand for KINGSUITE, but low demand for KING, the LRV for KINGSUITE will be higher than KING. The hotel might sell KING, losing the opportunity to sell KINGSUITE. To optimize the demand for the component room,G3 RMSrestricts selling KING by setting the LRV for KING as high as the LRV for KINGSUITE.
Select LRV at the Room Type level in theData Extraction Reportto see where LRV is inflated to protect the capacity of a room type.

#### Use the Sales Forecast to Understand the System's Strategy

When you use the Component Rooms module, you see a Sales Forecast value for each Forecast Group and Room Class in theBusiness Detailswindow of Demand and Wash Management.
Sales Forecast is the number of rooms thatG3 RMSexpects to sell, either component rooms or physical rooms. The Sales Forecast value is important for understanding the systemâs expectations and strategy. Along with Available Capacity to Sell, it helps you make informed overrides.
Using ourexamplefrom the overview again, ifG3 RMSexpects to or attempts to prioritize the sale of KINGSUITE, then the Sales Forecast equals 1 and the Occupancy Forecast (counting the physical rooms that will be occupied) equals 2. If the system expects to sell KING and DBL separately (and not as KINGSUITE), then both the Sales Forecast and the Occupancy Forecast equal 2.
If your Room Classes combine physical rooms and component rooms, you might not know to which of these the Sales Forecast value refers. You can still use the Sales Forecast to understand that demand for that Room Class is whatG3 RMSwants to prioritize.

#### Read Metrics with Component Rooms in Mind

Component rooms present some unique challenges for metrics like rooms and revenues On Books. Let's look at our first example again:
If the component room type  KINGSUITE is sold,G3 RMSreceives one reservation. How should this information be reflected in the rooms sold at the total hotel and room type levels?
At the room type level, you want to know that one KINGSUITE sold. But you also want to know how it impacts the physical room types that are occupied. Because you sold KINGSUITE, you need to know that the KING and the DBL each have one room less capacity. You also want the system to show one room On Books for KING, DBL, and KINGSUITE each. If you add up the On Books at the room type level, you would see three rooms sold  even though you only sold two physical rooms.
On the total hotel level, you want to avoid this double counting and see only the two total physical rooms  sold. You also  want to see the revenue from the single reservation, not from both the physical rooms and the component room.
This simple example shows how important it is for you to understand howG3 RMSaccounts for component rooms differently at different levels. When you view reports and dashboards, you need to know when the data represents physical rooms or both physical and component rooms.
For a more complex example, see theDetailed Scenario.
By default,G3 RMSoptimizes pricing for the component room type separately from the pricing for its physical room types, based on the demand for each. Which means the revenue-optimal price for the component room can be higher or lower than the sum of the prices of the physical parts.
Using thisexample, let's assume there is high demand for suites like the component room type KINGSUITE and low demand for regular rooms like its parts, KING and DBL. In that case,G3 RMSmight price KINGSUITE at 250 and KING and DBL at 100 each.
In some rare cases, a property needs to price their component rooms as the sum of its parts. In our example, if KING and DBL are priced at 100, then KINGSUITE has to be priced as 200. If you think that this applies to your property,G3 RMShas a pricing option for this scenario. It causes some loss in revenue opportunity , so please contact your IDeaS representative to discuss. If the feature is the right solution, IDeaS enables it.
When enabled, a Price as Sum of Parts option displays in the Base Room Type tab of Pricing Configuration. Select that option andG3 RMSprices all component room types of the selected Room Class as the sum of the physical room types. The system doesn't optimize pricing for the selected component rooms, and you can't override their Final Price.
Note: For you to be able to select it, the Room Class must contain only room types that are component rooms. It can't contain parts of component rooms or other room types not used in component rooms.

## Detailed Scenario

This example shows the difference between sold and occupied data when selling component rooms. To simplify this example, all rooms sold are in the same market segment and each room sells for 100.00.

#### Hotel Capacity

#### Room Type and Room Class Structure

#### Room Type Data

The following table shows what you see when three CR1 and eight CR2 are sold. The remainder of the rooms sold in PR1, PR2, PR3, and PR4 are sold at the physical level.
The On Books level is higher for PR1 and PR2 due to sold component rooms. 60 rooms total are sold, including double counting for CR1 and CR2, which are already counted in the component parts.

#### Room Class Data

Room Class reporting shows the following data:
- On Books and Revenue values are double counted.
- On Books and Revenue are disaggregated to the physical room types to support Room Type and Room Class level reporting.

#### Hotel, Market Segment, and Business Type Levels

At this level, solds are not double counted, so only 4,900.00 is On Books, compared to the previous 7,100.00.
