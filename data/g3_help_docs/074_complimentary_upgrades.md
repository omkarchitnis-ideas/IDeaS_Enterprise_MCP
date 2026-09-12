# Complimentary Upgrades

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Complimentary-Upgrades.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Complimentary-Upgrades.htm`
- **Ingestion Date:** `2026-09-11 22:12:57`

---

# Complimentary Upgrades

Complimentary upgrades are free upgrades to a higher room type that you provide to some guests due to overbooking or as a business practice. For example, a frequent guest that books a Standard room type gets a free upgrade to a higher-priced Suite.G3 RMSconsiders this by using booked versus stayed data.

## Booked versus Stayed Data

G3 RMSuses reservation history to understand upgrades and any other change in room type. For transient business, the system tracks the original room type from the history at the time the reservation was made. The room type that the guest initially booked is defined as the booked room type. The stayed room type is the room type where the guest actually stayed. You can see this information in the Booked Room Type column of theBusiness Insightsdashboard.
Knowing the difference between the Booked and the Stayed room types helps the system understand demand by Room Class. In the above example of the frequent guest,G3 RMSunderstands that the guest represents Standard demand, not Suite demand. With that information, the system can improve its unconstrained forecast for Standard and Suite, especially in the case of a large number of upgrades or upsells. For more information, viewbest practices for complimentary upgrades.
G3 RMScan provide benefits to your property without Booked versus Stayed data. But whenever available, the system uses Booked versus Stayed room type data:
- If historical data includes Booked versus Stayed data,G3 RMSis built based on historical demand of the booked room type. This availability depends on thereservation systemthat provides data toG3 RMS.For example, Infor HMS  includes Booked versus Stayed data. With some systems,G3 RMSuses alternate data, for example, with Oracle Opera with OXI, the RTC field in the historical data serves as an indication for Booked versus Stayed.
- If the reservation system doesn't include Booked versus Stayed,G3 RMSstarts collecting the data, for example, when a new or existing reservation is upgraded at check-in. After  365 days of Booked Room Type data is available, you get aSufficient Booked Data Available Alertwhich tells you that you can switch to using Booked instead of Stayed data.Examples of this scenario are Oracle Suite8 and Protel. This scenario also applies to systems that include Booked versus Stayed Data, but not enough, for example, Oracle Opera V5.6 or newer (using an API or Agent) includes only 180 days.
To find out which room type dataG3 RMSuses for your property, click Important Informationnext theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.and look underData Used for Forecasting and Optimization.If you use theextended stay functionalityyour system has to remain on Stayed data.
Even if the historical data contains Booked versus Stayed information,G3 RMSdoes not use the data if it is not clean or meaningful enough. For example,G3 RMScaptured 365 days of history with Booked versus Stayed data for a property. For the first 65 days of that history, less than 2% of reservation records show any difference between Booked and Stayed room type.
At that low level of differentiation,G3 RMSconsiders those first 65 days of Booked versus Stayed history as insufficient and counts only the remaining 300 days (when the difference sometimes exceeds 2%). The 300 days count towards the minimum of 365 days that the system requires to switch to using Booked data. After the initial data capture, the system collects new Booked versus Stayed data from reservation activity during each day of the implementation and adds those days to the 300 days from history.
After 30 days, the property creates and commits Forecast Groups, with forecasts based only on Stayed data. But after another 35 days, the property now has 365 days of Booked versus Stayed data and gets a Sufficient Booked Data Available Alert in Information Manager.
