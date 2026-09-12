# Business Analysis Pace Data

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/BAD/Business-Analysis-Pace-Data.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/BAD/Business-Analysis-Pace-Data.htm`
- **Ingestion Date:** `2026-09-11 22:13:54`

---

# Business Analysis Pace Data

The Pace Data tab helps you compare the current year to last year's pace for up to 330 days. You can view pace for occupancy and either ADR or revenue. The booking pace curve shows the number of rooms and how that number changes as the arrival day approaches. The graph is similar to the one in theAt a Glancedashboard but offers more options, like viewing pace at the Forecast Group instead of only at the property level.
For more information, view:
- Best practices for comparing pace data.
Best practices for comparing pace data.
- Theoverview of all Business Analysis tabs.
Theoverview of all Business Analysis tabs.
- Investigating data  differencesbetween systems.
Investigating data  differencesbetween systems.

## Chart Steps

- Clickand thenBusiness Analysis.
- Click thePace Datatab. Property level pace is displayed for the current month or fiscal period.

#### View by Inventory Group

If you set upInventory Groups, you can select one to see the data only for its defined Room Classes. The default selection is Property, or all Room Classes. You can change the default selection inPreferences.

#### Remove Excluded Segments

Select toRemove Excluded Segmentsand the data to exclude business from specific market segments. This option is available if you defined the excluded segments inProperty Information. And with Inventory Groups, you must select the Property level.
- Change the monitored period, for example, the upcoming month of April. Seehow to use the period filter.
- Select how manyDays to Arrivalyou want to view pace. For example, to view 90 days of pace for April.Note: with these selections, to see any current pace for April, April 1 must less than 90 days from today.
- Enter a number of days forShow Expected Booking Pace as of. A  dotted line displays in the graph to help you understand changes in the system's forecast.Compare today's expected pace against the expectation from that number of days ago. The larger the difference is between the current and the previous expected booking pace, the likelier it is that the system changed the remaining demand forecast.
- Occupancy pace displays by default. Select to add eitherADRorRevenue.
- Click the filter iconto set filters for the displayed data, as needed. Property is selected as the default level. To view data at a more granular level, select either Business Types, Forecast Groups, Market Segments or Business Views.
- If you compare many data points, each with a pace curve for current, past year and forecast, the graph might look crowded. Hide a curve by clicking its colored square icon in the legend below the chart. Click that icon again to restore the curve.
To read the booking pace curve, work from left to right. On the x-axis you see the curve starts at the selected number of Days to Arrival, measured from the beginning of the selected period. For example, today is the first of the month, and you select 60 Days to Arrival and the full next month to monitor.G3 RMSdisplays the current year booking pace curve from 60 days to arrival to about 30 days to arrival. At about 30 days to arrival, the solid curve ends at the black vertical line that indicates the System Date. A dotted curve to the right of the System Date line indicates the expected booking pace.Note: Expected pace is available only at Property and Forecast Group level and for maximum of 120 days ago.
The curve reaches zero days to arrival when theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.is past the start date of the monitored period. The Days to Arrival then shows negative values, meaning the occupancy values contain both actual occupancy (for past days) and on books occupancy (for future days). The number of days to arrival with negative values depends on the length of your monitored period.
The y-axis displays the occupancy expressed in number of rooms. Point to the pace or forecast curve to see the exact occupancy value for the corresponding number of days to arrival.
