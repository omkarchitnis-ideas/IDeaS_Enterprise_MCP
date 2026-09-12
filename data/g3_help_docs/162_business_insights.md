# Business Insights

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Insights/BusinessInsights.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Insights/BusinessInsights.htm`
- **Ingestion Date:** `2026-09-11 22:13:57`

---

# Business Insights

Use the Business Insights dashboard to analyze transactional, or reservation-level, data from yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.and, if enabled, fromChannel Costssetup.  You can use display options to view the data from multiple perspectives. You can also compare data for a selected date range to the equivalent date range from last year (adjusted by the day of week) to understand year-on-year trends.
The availability of the Business Insights Dashboard depends on yourG3 RMSsubscription.

### Viewing Transactional Details

When you click a data point in the Business Insights chart view, a new window opens. This window displays a table of the available details for the transactions that contributed to the selected data point. The same information displays when you select a data point from last year's data or for future dates. Because all reservation details are not always available from yourreservation system, some data columns might be missing information.

### Using Channel Costs with Business Insights

If you enableChannel Costssetup, the Business Insights dashboard includes additional values that help you understand the overall cost of acquiring business through your sources or channels and how those costs impact other key performance indicators. For example, you can review Total Acquisition Costs, Net Revenue, Net ADR, and NetRevPARRevenue Per Available Room. The total room revenue divided by the total number of rooms (capacity).
See the Property Information topic for the capacity definition., and compare them to last year.
"Net" values are only available to select in the dashboard when you enable Channel Costs. The "Net" values represent ADR, RevPAR, and Room Revenue values after accounting for the Channel Costs that you set up. Channel Costs also control the results for Total Acquisition Costs.
When you change your Channel Cost setup, the values in the Business Insights dashboard update immediately.
Channel Costs are only used for reporting purposes and do not impact the forecast and decisions.

## Reporting Steps

- Clickand thenBusiness Insights.
- Click theStart DateandEnd Datefields to select a date range for the report.Click the default date.Complete one of the following options:Enter a date in theSelectionfield.SelectSpecific Datefrom the menu. On the calendar, click the left or right arrows to navigate between months; click the double arrows to navigate between years. Click the appropriate date in the calendar.SelectRolling Datefrom the menu. Enter the number of days to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.in theSelection: System Date -field.ClickApply
- Click the default date.
- Complete one of the following options:Enter a date in theSelectionfield.SelectSpecific Datefrom the menu. On the calendar, click the left or right arrows to navigate between months; click the double arrows to navigate between years. Click the appropriate date in the calendar.SelectRolling Datefrom the menu. Enter the number of days to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.in theSelection: System Date -field.
- Enter a date in theSelectionfield.
- SelectSpecific Datefrom the menu. On the calendar, click the left or right arrows to navigate between months; click the double arrows to navigate between years. Click the appropriate date in the calendar.
- SelectRolling Datefrom the menu. Enter the number of days to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.in theSelection: System Date -field.
- ClickApply
- SelectFiltersto narrow down the displayed data. For example, you are viewing Arrivals versus Arrivals Last Year but want to see only those  for a specific Room Class, selectRoom Classas a filter and select a Room Class from the list that displays. PressCtrl + clickto select multiple values. Multiple selections display as aggregate data.
- Select a measurement option for theX Axis. If you selectDays to Arrival, enter the number of days, up to 365.
- SelectUse As of Dateif you want to see data as of a specific booking date. Then select the date, using the same date selection method that you used to define the analysis period. This option is not available when you select Days to Arrival for the X axis.
- SelectValuesfrom transactional data to display:PressCtrl + clickto select multiple values.Select a value and its equivalent for last year to compare year-on-year trends (for example, Arrivals compared to Arrivals Last Year).Note that Effective Capacity and RevPAR values are valid only if Occupancy Date, Day of Week or Room Class is selected for the X Axis. If not, the Effective Capacity and RevPAR display as zero.Net values, for example Net Average Daily Rate, consider yourChannel Costs. If you haven't defined those costs, the values equal their base values, for example Average Daily Rate.
- PressCtrl + clickto select multiple values.
- Select a value and its equivalent for last year to compare year-on-year trends (for example, Arrivals compared to Arrivals Last Year).
- Note that Effective Capacity and RevPAR values are valid only if Occupancy Date, Day of Week or Room Class is selected for the X Axis. If not, the Effective Capacity and RevPAR display as zero.
- Net values, for example Net Average Daily Rate, consider yourChannel Costs. If you haven't defined those costs, the values equal their base values, for example Average Daily Rate.
- ClickGenerate.
Use the following features in the tool to adjust the display:
- ClickTableto view the data in a tabular view.
- Click the Excel iconin the tabular view to export the data.
- ClickChartsto return to the chart view.
- In chart view:SelectBar Chart,Column Chart, orLine Chartfrom the list on the top right. The display changes according to your selection.Click a value in the legend to remove that value from the display. Click the value again to restore it.Point to a data point on a bar, column, or line in the chart to view the values in a separate window.Click a data point to open a table of the transactional data that contributed to the value. SeeData Detailsfor information about this data.If you are viewing data by Occupancy Date, click and drag your mouse across a date range in the chart to zoom in on those dates. ClickReset zoomto restore the view.
- SelectBar Chart,Column Chart, orLine Chartfrom the list on the top right. The display changes according to your selection.
- Click a value in the legend to remove that value from the display. Click the value again to restore it.
- Point to a data point on a bar, column, or line in the chart to view the values in a separate window.
- Click a data point to open a table of the transactional data that contributed to the value. SeeData Detailsfor information about this data.
- If you are viewing data by Occupancy Date, click and drag your mouse across a date range in the chart to zoom in on those dates. ClickReset zoomto restore the view.
- Click a data point in the chart view to open the transactional details window.
- Adjust your view:Click a column heading within the details view to sort data by that column.Click theicon on the right side of the headings row. Click a column heading title to hide it from the display. Click the title again to restore it.
- Click a column heading within the details view to sort data by that column.
- Click theicon on the right side of the headings row. Click a column heading title to hide it from the display. Click the title again to restore it.

## Data Details

### Group Block Data

Transactional data does not include group block information, because group blocks do not include actual reservations. Therefore, to include group data for Occupancy on Books for future dates,G3 RMSadjusts the future occupancy using  the difference between the size of the group block and the group pick up.
G3 RMSadds representative transactions for those reservations that are still held in the block to make sure that occupancy data is correctly recorded. These representative transactions are "pseudo" reservations that exist only as placeholders until the block is picked up and are always for a one-night LOS.
Because the group blocks do not contain actual reservations, data columns for the fields specific to a reservation, like the room type, might be missing information.Although they also have a blank channel or source field, these reservations are not included in acquisition costs if you have set up âNot Availableâ costs in Channel Costs setup.
In this example, the transactional data is adjusted to account for group blocks, which do not contain actual reservations. The representative transactions for these "pseudo" reservations display with no Reservation ID, SS for the Individual Status, missing details such as room type or channel, and a one-night LOS.

### Capacity Data

Transactional data also does not includeEffective CapacityThe property's physical capacity minus the out of order rooms.information, but the property's effective capacity displays when you select Occupancy Date, Day of Week or Market Segment  for the X Axis. To display effective capacity values,  rows are added to Transaction Details that include only Room Type, Room Class, and Effective Capacity data. Other fields are blank.

### Transactional Data

View the following data by clicking a data point in the chart view to open the transactional details window.
