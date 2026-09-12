# Rooms Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Rooms-Configuration-Overview.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Rooms-Configuration-Overview.htm`
- **Ingestion Date:** `2026-09-11 22:12:56`

---

# Rooms Configuration

Use the Rooms setup to tellG3 RMShow to manage your room types. The steps in this setup are grouped into one process because they depend on each other.For example, when you create a new Room Class, you must also define its position in price ranking and upgrade paths.Use the following steps in this order:
- Room Class: group room types with similar demand and pricing into a Room Class.
- Cost of Walk:G3 RMSconsiders the values that you set up for its overbooking calculations.
- Room Type: define settings at the Room Type level that match your business processes, like Overbookingor Special Use Room Types.G3 RMSoverbooks to ensure that you can maximize revenue.
- Price Ranking and Upgrade Path: define a pricing hierarchy and what happens when demand is higher than capacity for some Room Classes and lower for others.
- Group Price Ranking and Upgrade Path:  set this up in the rare case where it differs for group business.
- Minimum Price Differential: set it up if two Room Classes must be priced apart by at least a certain amount.
- Display Preferences: determines the order that your Room Classes display inG3 RMS.
G3 RMSautomatically saves your changes when you move between steps. Review each step when you work with the module to ensure consistent, correct settings, particularly afterG3 RMSbegins managing decisions for your property.

## Master Class

The Master Class determines which Room Class decisionG3 RMSshows when there is only space to show one. For example, the default pricing decision on theSummarytab of the Business Analysis Dashboard is for the Master Class. Typically, the lowest priced Room Class with the largest inventory is selected as the Master Class.
