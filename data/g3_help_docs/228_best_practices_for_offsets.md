# Best Practices for Offsets

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BP-Offsets.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BP-Offsets.htm`
- **Ingestion Date:** `2026-09-11 22:14:41`

---

# Best Practices for Offsets

## Consider Other Values That Impact the Setup of Offsets

## Understand How to Enter Offsets

- The RMSprices the Base Room Type's 1 Adult occupancy. Your task is to use the offsets to price:The Base Room Type for Double occupancy, Extra Adult, and optional child age groups if you useOccupant Grouping.Other room types in the same Room Class:Single Occupancy: if the room type is priced above or below the Base Room Type, see the STDD room type in thescenarios.Double Occupancy, Extra Adults, and Extra Child occupancies: enter the difference to the single occupancy price, so you likely use the same offsets as for the Base Room Type.
The RMSprices the Base Room Type's 1 Adult occupancy. Your task is to use the offsets to price:
- The Base Room Type for Double occupancy, Extra Adult, and optional child age groups if you useOccupant Grouping.
The Base Room Type for Double occupancy, Extra Adult, and optional child age groups if you useOccupant Grouping.
- Other room types in the same Room Class:Single Occupancy: if the room type is priced above or below the Base Room Type, see the STDD room type in thescenarios.Double Occupancy, Extra Adults, and Extra Child occupancies: enter the difference to the single occupancy price, so you likely use the same offsets as for the Base Room Type.
Other room types in the same Room Class:
- Single Occupancy: if the room type is priced above or below the Base Room Type, see the STDD room type in thescenarios.
Single Occupancy: if the room type is priced above or below the Base Room Type, see the STDD room type in thescenarios.
- Double Occupancy, Extra Adults, and Extra Child occupancies: enter the difference to the single occupancy price, so you likely use the same offsets as for the Base Room Type.
Double Occupancy, Extra Adults, and Extra Child occupancies: enter the difference to the single occupancy price, so you likely use the same offsets as for the Base Room Type.
- Fixed and percentage offsets can be positive or negative (-).
- Offsets are cumulative, so the double occupancy price is calculated by adding the Single + Double offsets to the Optimal Price. SeeCalculations for the Pricing Decisionbelow.
For an overview and all setup steps, seePer Person Pricing.
- The RMSprices the Base Room Type's 2 Adults occupancy. Your task is to use the offsets to price:The Base Room Type for 1 Adult, Extra Adults, and Extra Child occupancies (more  if you useOccupant Grouping).Other room types in the same Room Class:2 Adults: if the room type is priced above or below the Base Room Type, see the QN room type in thescenarios.1 Adult, Extra Adults, and Extra Child occupancies: enter the difference to the 2 Adults price, so you likely use the same offsets as for Base Room Type.
The RMSprices the Base Room Type's 2 Adults occupancy. Your task is to use the offsets to price:
- The Base Room Type for 1 Adult, Extra Adults, and Extra Child occupancies (more  if you useOccupant Grouping).
The Base Room Type for 1 Adult, Extra Adults, and Extra Child occupancies (more  if you useOccupant Grouping).
- Other room types in the same Room Class:2 Adults: if the room type is priced above or below the Base Room Type, see the QN room type in thescenarios.1 Adult, Extra Adults, and Extra Child occupancies: enter the difference to the 2 Adults price, so you likely use the same offsets as for Base Room Type.
Other room types in the same Room Class:
- 2 Adults: if the room type is priced above or below the Base Room Type, see the QN room type in thescenarios.
2 Adults: if the room type is priced above or below the Base Room Type, see the QN room type in thescenarios.
- 1 Adult, Extra Adults, and Extra Child occupancies: enter the difference to the 2 Adults price, so you likely use the same offsets as for Base Room Type.
1 Adult, Extra Adults, and Extra Child occupancies: enter the difference to the 2 Adults price, so you likely use the same offsets as for Base Room Type.
- Extra adult offsets are cumulative, so the price for an Extra Adult occupancy includes the price for the maximum adults + Extra Adult offsets. SeeCalculations for the Pricing Decisionbelow.
- Child offsets are the exact price for the number of children in the room (1 Child, 2 Children, etc.). SeeCalculations for the Pricing Decisionbelow.
- Since Child offsets are the exact price, the value can't be negative. Other offsets can be positive or negative (-).

## Scenarios for Pricing Calculations

Review the following  examples. To understand the options for entering offsets, review thisbest practice.
In this example, STKG and STDD are in the same Room Class. STKG is the Base Room Type for the Standard Room Class. Offsets add an extra charge for double occupancy and  extra adults in each room type.
In this example, all offsets are percentages of Optimal Price. Occupant Grouping was used to add child age groups:
The following example shows pricing calculations when non-roomSupplementsare included. Note that offsets are cumulative, but Supplement values are not cumulative.
Review the following  examples. To understand the options for entering offsets, review thisbest practice.
In this example, KNG and QN are in the same Room Class, and KNG is the Base Room Type. You set up Occupant Grouping so that you can define the prices for up to 4 Adults and charge Extra Adults above that. And you charge for every Extra Child. You set up Maximum Occupants for the KNG as 3 (2 Adults and 1 Child) and 5 (4 Adults and 1 Child) for QN.  Offsets are fixed values off Final Price:
In the next example, all offsets are percentages of Final Price.Occupant Groupingwas used to add more adult and child occupancy levels. The maximum occupants you can set up is 4 adults before the additional adult supplement applies.
In this example, offsets are fixed values off Final Price, andOccupant Groupingwas used to set up child age groups.
In the offset setup example below, the group recommended rate for the STD-King and STD-Lakeview King room types are offset from the Base Room Type rate in the same Room Class:
If you don't include the Base Room Type in a group evaluation, the group's recommended rate uses the offsets for the included room types. In the following example, the Base Room Type (STD-Double) isn't selected, but the other room types in the Room Class (STD-King and STD-Lakeview King) are included:
