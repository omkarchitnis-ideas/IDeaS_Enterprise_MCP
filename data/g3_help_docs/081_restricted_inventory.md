# Restricted Inventory

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Restricted-Inventory.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Restricted-Inventory.htm`
- **Ingestion Date:** `2026-09-11 22:13:02`

---

# Restricted Inventory

If an out of order block covers more than 20% of your total inventory and lasts more than seven consecutive days, review this topic to ensureG3 RMScan produce the best possible forecasts and decisions.
G3 RMSexpects that you  place rooms out of order in yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.when your property has large numbers of rooms unavailable for sale for a longer time. That can be due to room renovations, repairs, or the result of  extremedemand disruption.
Note that reservation systems usually have two out of order statuses (names might vary):
- Out of Order: deducts from available inventory and therefore reduces theEffective CapacityThe property's physical capacity minus the out of order rooms.inG3 RMS.
- Out of Service: doesnât deduct from available inventory and doesnât decrease the Effective Capacity.
Use Out of Order if your property is 100% closed. Also use Out of Order status if your property is partially closed, and you canât make rooms available, for example due to renovation or maintenance.  Viewbest practicesfor using Out of Order.
Use Out of Service or similar status if your property is partially closed, but you can make rooms available. For example, you might close floors during a low demand season. But for some high demand dates within the season, you can put some of the floors back into service. If you use Out of Order in this scenario,G3 RMSsees constrained capacity and might react with LRV and pricing that is too aggressive for a low demand period.
Some reservations systems have limited options to place rooms out of order. If needed, useOut of Order OverridesinG3 RMS.
