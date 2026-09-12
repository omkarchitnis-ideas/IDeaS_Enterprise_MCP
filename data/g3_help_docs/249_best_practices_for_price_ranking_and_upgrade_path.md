# Best Practices for Price Ranking and Upgrade Path

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/BP-Rooms-Price-Ranking-Upgrade-Path.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/BP-Rooms-Price-Ranking-Upgrade-Path.htm`
- **Ingestion Date:** `2026-09-11 22:14:55`

---

# Best Practices for Price Ranking and Upgrade Path

Review these best practices for setting up Price Ranking andUpgrade Pathor reviewscenarios.

## Best Practices for Setting Up Price Ranking

### Verify the Ranking by ADR Is Correct

By default,the RMSsorts your Room Classes by the historical ADR that is shown in theRoom Classtab.  Verify that the sorting accurately reflects your price ranking.
Almost all properties can use this price ranking with a single column. But some large and complex properties have several distinct types of inventory that they price independently. If that applies to you, consider theAdvanced Settings. Be sure to review the scenarios and best practices before choosing that option.

### Understand the Impact on Pricing Setup

Price ranking directly impacts yourPricing Configuration. By default,the RMSmaintains the price ranking order using the lowest priced room types. Thus, under certain conditions, the highest-priced room type of a lower ranked Room Class might be priced higher than the lowest room type of a higher ranked Room Class. This setting providesthe RMSwith some flexibility to price optimally, while considering the integrity of room type positioning and operational issues. At first glance, this setting might not be intuitive, but consider that a room type from a higher Room Class would only be priced close to, equal to, or lower than a room type of a lower one when there is very little or no demand for it.

## Best Practices for Upgrade Paths

All best practices apply only to Room Type  overbooking, not toRun of House.

### Ensure That Overbooking Setup Supports Upgrade Paths

Overbooking and upgrade paths work together and must be set up accordingly.  The following examples show this relationship:

#### Example: Standard Room Class with No Overbooking

A property sets up the Suite Room Class to accept upgrades from the next lower Standard Room Class, but the property does not allow overbooking for any Standard room types.
In this case, the room type setup invalidates the upgrade path setup. Ifthe RMSforecasts no demand for Suite but excess demand for Standard, the Standard rooms cannot upgrade to the unsold Suite inventory because excess demand is not allowed in Standard rooms.The RMSassumes that the hotel will turn down all the excess Standard demand.

#### Example: Accepting a Group Directly in the Reservation System

What if a hotel accepts a group directly in theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.so that the Standard Room Class is overbooked by five rooms, even when overbooking is not allowed for Standard inthe RMS?
In this case, if the hotel allows upgrades between Standard and Suite rooms, the systemâs optimization assumes the five rooms will be upgraded to Suites and not walked.

#### Example: Deluxe and Suite with No Overbooking

A hotel has three Room Classes: Standard, Deluxe, and Suite.
In this case, Deluxe can receive five rooms from Standard's overbooking.
However, what if the hotel sold all Deluxe rooms, but Suite has 5 rooms of remaining capacity and remaining demand exists only for Standard. There is no wash, so the system only overbooks if there is an available upgrade path.
In this case, the upgrade path from Deluxe to Suites is disabled because overbooking for Deluxe is disabled.The RMScan only overbook Standard if there are available Deluxe rooms. It assumes that the hotel can't accommodate the overbooked Standard rooms in Suites and that it turns away all the excess demand for Standard.

### Be Careful When You Don't Include a Room Class in the Upgrade Path

#### Avoid Missed Revenue Opportunities

A Room Class for which you do not accept any upgrades is like a hotel within a hotel. If there is no demand for the Room Class, it remains empty, even if there is more demand than capacity for the "main" hotel.
You can consider not including a Room Class in the upgrade path if you have a separate Room Class of very expensive suites. This option might be the right choice when you prefer letting those exclusive suites sit empty rather than upgrading lower priced demand to them for free, to preserve the image value.
For many hotels, however, the additional costs from upgrades are negligible, and they prefer to overbook their lower priced room types if there is not enough demand for the more expensive ones. To achieve that inthe RMS, enable the upgrade path between all your Room Classes to ensure maximum revenue and profits.

#### Avoid Forecasting Issues

When the system forecasts demand in excess of capacity for a Room Class that you have not included in the upgrade path, the system considers the excess demand as lost.
For example, you have 50 Standard rooms and 20 Suites, and you do not enable upgrades from Standard to Suite.The RMSforecasts demand for 100 Standard rooms, but none for Suites. To make this example simpler, there is no wash.
In this scenario,the RMSassumes that after the 50 Standard rooms are sold, each guest wanting to book a Standard room will be told that there are no available rooms. If that is not the truth, because in reality you do overbook your Standard rooms and upgrade them to Suites, you should enable upgrades from the Standard Room Class to the Suites. Otherwise, the excess Standard demand is missing from occupancy forecasts, which means the system is under-forecasting compared to your expectations.
When you do not include one Room Class in the upgrade path,  the resulting forecasting issues apply to any Room Class. However, the impact is likely more apparent and more frequent when you do not share a lower priced Room Class, because demand in excess of capacity usually occurs more often and to a stronger degree for lower priced Room Classes than higher priced Room Classes. Therefore, we strongly recommend always including lower priced Room Classes.
Remember that upgrades only occur ifthe RMSdoes not forecast enough demand for the higher Room Class. For example, if you enabled upgrades from Standard to Deluxe and there is enough demand to fill the Deluxe rooms, the system does not share Deluxe inventory with Standard rooms, even if the demand for Standard rooms exceeds capacity. You can review the demand by Room Class inDemand and Wash Management.

### Understand If You Need Advanced Settings

Use Advanced Settings if your property contains two or more distinct types of inventory that each need their own upgrade path,  independent pricing or both. SeeAdvanced Pricing Ranking and Upgradeto learn more.

## Scenarios

All scenarios are for Room Type, notRun of House, overbooking. Remember that upgrades only happen on days when the higher ranked Room Class has less forecasted demand than capacity and the lower ranked Room Class has more demand than capacity.

### Example 1

In this example, the hotel has three Room Classes. The setup below indicates the following:
- Standard is priced less than or equal to Deluxe. Deluxe is priced less than or equal to Suites.
- Upgrades can occur between all Room Classes under appropriate demand conditions.

### Example 2

In this example, the hotel has four Room Classes. The setup shown below indicates the following:
- Standard is priced less than or equal to Deluxe. Deluxe is priced less than or equal to Suites. Signature Suites are priced equal to or greater than Suites.
- Upgrades can occur between Standard, Deluxe, and Suites Room Classes. Upgrades cannot occur from Suites to Signature Suites.
This setting is correct if the property decides to fill the Signature Suites only if there is demand for them. If there is no demand for them but excess demand for the lower Room Classes, the property prefers to leave the Signature Suites empty rather than accept upgrades.

### Example 3

In this example, the hotel has four Room Classes. The setup shown below indicates the following:
- The price ranking works the same as in the above examples.
- The Two Twins are higher than the One Double because there is strong demand for two separate beds, which is expressed in the higher ADR.
- The One Double Room Class cannot be upgraded to any other Room Class. Upgrades can occur only from Two Twins upwards.
Consider the following with this setup:
- Whenever there is excess demand for the One Double Room Class,the RMSconsiders the excess demand as turned away and lost. In a worst case scenario, when there is no demand for the top three Room Classes but more demand than capacity for the One Double Room Class, the upper three Room Classes would remain unsold.
- We do not recommend such a setup where a low-priced Room Class is not included in the Upgrade Path. SeeImpact of Not Including a Room Class in the Upgrade Pathabove.
- What if the intent of the property is to allow upgrades from One Double to Family, but not from One Double to Two Twins? This might be the case if the property always experiences guest complaints when upgrading overbooked demand from the One Double to the Two Twins Room Class, because guests perceive the Two Twins as a downgrade from the One Double due to the smaller bed size. In that case, the property needs two separate upgrade paths and could achieve this with the use of an Advanced Price Ranking and Upgrade Path.
Delete this text and replace it with your own content.
