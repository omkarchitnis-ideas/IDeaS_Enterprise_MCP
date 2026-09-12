# Monthly Booking Pace

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/AAG/At-a-Glance-Monthly-Booking-Pace.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/AAG/At-a-Glance-Monthly-Booking-Pace.htm`
- **Ingestion Date:** `2026-09-11 22:13:48`

---

# Monthly Booking Pace

The Monthly Booking Pace pane helps you compare the property level pace for a full month orfiscal periodto the same period last year. The booking pace curve displays occupancy as the number of rooms sold for 60 days prior to arrival until the last day of that period and how the number of room changes as the day of arrival approaches.
To adjust the monitor period to less than a full month, drill down from the property level, or compare last year's data for the same days of week, useBusiness Analysis Pace Data. Or click to see anoverview of all panels of the dashboard.

## Chart Steps

### Accessing Monthly Booking Pace

- Clickand thenAt a Glance.
- Scroll down to theMonthly Booking Pacepane. The two months or fiscal periods selected in the calendar display in tabs. Select the period to review.
- Click a year in the legend to hide the curve for that year. Click the same year again to restore the curve.

### Reading the Booking Pace Curve

To read the booking pace curve, follow the booking pace or forecast curve from left to right. On the X axis you can see the curve starts 60 days to arrival, measured from the beginning of the selected period. If today is the first of the month and you selected the full next month to monitor,G3 RMSdisplays the current year booking pace curve from 60 days to arrival to about 30 days to arrival. At about 30 days to arrival, the curve ends at the black vertical line that indicates theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
The curve reaches zero days to arrival when the System Date is past the start date of the monitored period. The Days to Arrival then shows negative values, meaning the occupancy values contain both actual occupancy (for past days) and on books occupancy (for future days). The number of days to arrival with negative values depends on the length of your monitored period.
The Y axis displays the occupancy expressed in number of rooms. Point to the pace or forecast curve to see the exact occupancy value for the corresponding number of days to arrival.

## Scenarios for Data Discrepancies

If you have questions about differences in the data betweenG3 RMSand other systems,  review one of the following topics:

### Missing Last Year's Booking Pace

This scenario applies if you're in your first year of system implementation, and yourreservation systemprovides incomplete historical data. When that occurs,  last year's pace looks like a blue triangle with a straight line from zero days to arrival to the final occupancy for the monitored period. For more information, reviewPace Data Missing for Last Year.

### Data Differences between Reporting Levels

If you have questions about variations in data between different levels, for example, between the property and Forecast Group levels or pickup between rate code  market segment level, seeData Level Differences.

### Pace Data Differs betweenG3 RMSand DailyExtracts

If you find data variations between same time last year (STLY) inG3 RMSand  other systems, seePace Differences.

### Pace Data Differs between IDeaS Systems

If you're transitioning from IDeaS RMS toG3 RMS, reviewPace Differences between IDeaS Systems.
