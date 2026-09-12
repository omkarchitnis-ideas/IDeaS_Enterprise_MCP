# Best Practices for Setting Up Inventory Groups

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Property/BP-Business-Views-Inventory.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Property/BP-Business-Views-Inventory.htm`
- **Ingestion Date:** `2026-09-11 22:14:18`

---

# Best Practices for Setting Up Inventory Groups

## Select a Base Room Class

For each Inventory Group, you select a Base Room Class. Similar to aMaster Class, the decision for the Base Room Class is the one that displays in fields where only a single decision can display. For example, when you filter by an Inventory Group on the Summary tab of the Business Analysis dashboard, the LRV decision that displays in the table is for the Base Room Class of that Inventory Group. For Inventory Groups with more than one Room Class, many clients select the Room Class with the largest inventory.

## Don't Create a Property-Level Inventory Group

Create Inventory Groups that contain one or more Rooms Classes. You don't need to create an Inventory Group with all Room Classes since Inventory Group filters have a "Property" view option.

## Scenario: Properties with Mixed Inventories

You manage a property with mixed inventory. Examples are residences and non-residences or managing multiple buildings as one property inthe RMS. In those cases you may want to see performance data only for Room Classes that contain one type of inventory. For example, you create one Inventory Group for residences and one for non-residences so that you can see On Books and the Occupancy Forecast only for your non-residence Room Classes.
