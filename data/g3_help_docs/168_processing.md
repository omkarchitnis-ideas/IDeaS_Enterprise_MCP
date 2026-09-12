# Processing

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Optimization/System-Processing.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Optimization/System-Processing.htm`
- **Ingestion Date:** `2026-09-11 22:14:01`

---

# Processing

Processing is when data transfers between a property'sReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.andG3 RMS.  During processing,G3 RMSreceives  anextractFiles with new and changed booking data that the RMS receives from the reservation system. It includes reservations, group blocks, and inventory summary data. Also called Snapshots or Daily Extracts.with new and changed data and then:
- Updates the forecast.
- Runs anOptimizationThe step in the RMS Processing when the system uses the demand forecast (volume and value), the available capacity to sell, your configuration, and your interactions (like events, overrides) to calculate the outputs that maximize your revenues or profits. Outputs include pricing for the primary priced product, LRV, and overbooking. An Optimization also updates the constrained Occupancy Forecast..
- Sends the decisions to theselling system.
- Monitors the results.
For pricing and overbooking,G3 RMSsends only differential decisions, meaning only values that changed in the last processing.For LRV the system sends full decisions, meaning changed and unchanged values.

### What Help Do You Need With Processing?

- I want to learn more about  thetypes of processing.
I want to learn more about  thetypes of processing.
- I can't wait for the next scheduled Processing and want to know if can I use anOn Demand Optimization.
I can't wait for the next scheduled Processing and want to know if can I use anOn Demand Optimization.
- I need to know the limitations during each Processingstatus.
I need to know the limitations during each Processingstatus.
- I want to learn about the relatedSyncandWhat Ifoptions that are available after changes, like overrides.
I want to learn about the relatedSyncandWhat Ifoptions that are available after changes, like overrides.
- I need to send pricing overrides to myreservation systembefore the next Processing withManual Upload.
I need to send pricing overrides to myreservation systembefore the next Processing withManual Upload.

## Processing Types

If you need to react to significant changes, and you can't wait until the next scheduled processing, useOn Demand Optimization.

## Status of Processing

During processing, you see spinning arrowsin the top right. Additionally, two icons tell you about specific phases:
Processing impacts only some pages and some only briefly, so you can use most pages normally. When you see the Read Only icon, it means that you can't save any changes.  Before Read Only begins,G3 RMSnotifies you  in the Pricing,Demand and Wash, Group Floor, and Group Wash by Group pages so that you can save any overrides.
The amount of timeG3 RMSremains in Read Only mode depends on many factors, for example, the number of room types, the number of decision changes, and whether you made setup changes and started a Sync. On average, Read Only Mode lasts five minutes and should not take longer than 30 minutes.
WhileG3 RMSis sending decisions to yourselling system, an upload icondisplays next to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.. You can fully use the system, but you may see discrepancies between decisions inG3 RMSand yourselling system. Click the icon to view theselling systemto whichG3 RMSis currently uploading decisions. After decisions are sent, the upload icon clears and new decisions are available in yourselling system.

## Best Practices

### Impact on Data

During processing,G3 RMScollects on-books data, updates the forest, and sendsdifferential decisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case.. Thus, the forecast, decisions and on-books data that display inG3 RMSreflect the most recent values from either the nightly or the daytime processing.
Daytime processing, however, does not update pace data. Booking curve information, for example, in thePace Datadashboard or theBooking Pacereport, updates only during nightly processings, based on final rooms sold data.
When a report compares to a current value, the previous value is from the last nightly, or BDE, processing. Only thePickup/Changereport can compare between daytime processings.

### Impact on Alerts, Exceptions and Notifications

Data conditions that trigger most Alerts and Exceptions are based on data from the nightly processing. Therefore, there are typically no new Alerts or Exceptions between nightly processings. Note that the New Market Segments Alert and New Room Types Alert are the exception to this rule. SeeAlertsfor more information.
Notifications are available to set up for changes since the last nightly optimization or since the last optimization.
