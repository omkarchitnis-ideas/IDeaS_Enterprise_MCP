# Base Room Type

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Base-Room-Type.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Base-Room-Type.htm`
- **Ingestion Date:** `2026-09-11 22:12:31`

---

# Base Room Type

G3 RMSuses the Base Room Type to:
- For transient, to optimize the price for a Room Class. Then it uses that  optimal price of the Base Room Type together withOffsetsto calculate pricing for other room types and other occupancy levels in the same Room Class.
- For group pricingor function spaceevaluations, to calculate the recommended price.

### What Help Do You Need with Base Room Type Setup?

- I want to know how toexclude Room Classesfrom being priced byG3 RMS.
I want to know how toexclude Room Classesfrom being priced byG3 RMS.
- I need to enforce aMinimum Change Value.
I need to enforce aMinimum Change Value.
- I want to understand thebest practicesfor Base Room Type setup.
I want to understand thebest practicesfor Base Room Type setup.
- I want to understand the process ofsharing my pricing strategy withG3 RMS.
I want to understand the process ofsharing my pricing strategy withG3 RMS.
G3 RMSuses the  lowest priced room type and not the Base Room Type when enforcingPrice Rankingbetween Room Classes.

### Price Excluded
Room Classes

If you do not wantG3 RMSto price a Room Class, select the Price Excluded option. If enabled, the system doesn't optimize pricing for the room types of such a Room Class and instead sends the fixed price, plus any offsets, to theselling system.  For example, many properties select this option for their large specialty suites.
Set the fixed prices for a Price Excluded Room Class in theCeiling/Floortab. You canoverride pricingfor Price Excluded Room Classes.
In Group Pricing Evaluations,G3 RMSincludes the room types of a Price Excluded Room Class and uses the fixed price that you define.

### Minimum Change Value

Minimum Change Value is an optional selection. It is the minimum amount that a pricing decision must increase or decrease beforeG3 RMSsends the new decision. SeeDecide if your property needs Minimum Change Values for details.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click Advanced Settings.
- ClickBase Room Type.
- ClickAssign Base Room Types. If the button isn't available,G3 RMSalready selected the Base Room Types for you. Review and, if needed, change the system's selection.For each Room Class, the system selects the room type that has the highest number of past bookings with theEqual to BAR Product attribute.If your property usesSynthetic Data, manually select the Base Room Types.
- If you have multiple Room Classes, selectPrice Excludedfor a Room Class with a fixed price.
- Optionally, select theMinimum Change Method. You can use a different method and value for each Base Room Type:Fixed: The price must change by a fixed value beforeG3 RMSsends a new decision.Percent: The price must change by a percentage of the current price decision beforeG3 RMSsends a new decision.
- Fixed: The price must change by a fixed value beforeG3 RMSsends a new decision.
- Percent: The price must change by a percentage of the current price decision beforeG3 RMSsends a new decision.
- If you selected a Minimum Change Method, eenter theMinimum Change Valueas the fixed amount or percentage amount that the price must change.
- Select theEnable Supplementscheckbox if your Room Class rates include non-room supplements, like breakfast.
- ClickSave.
When you change pricing setup, a sync flagdisplays in the menu bar to indicate that your changes impact the system's forecast and decisions. SeeSyncfor more information.
