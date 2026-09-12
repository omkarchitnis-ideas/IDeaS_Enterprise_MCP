# Booking Pace Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Booking-Pace-Report.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Booking-Pace-Report.htm`
- **Ingestion Date:** `2026-09-11 22:13:33`

---

# Booking Pace Report

Use the Booking Pace report to analyze the pace for an arrival date in detail, from property down to the market segment level, and to compare it to theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).. For example, aNotificationtells you that the pace for a date in nine months  is far ahead of this year's pace, and 75% of your property is already booked. You want to investigate what type of 
 business booked and when that business booked.
Alternatively, use thePace Datatab in the Business 
 Analysis dashboard. It displays up to 120 days of expected pace.

## Reporting Steps

- Click, thenReports, and thenBooking Pace.
- Click theArrival Date. Enter a date or select an Arrival Date
	 from the calendar, and clickApply.
- Enter theMaximum Days to Arrival. This value is the number of days of pace to display in the report.  The maximum value that you can enter is the length of the forecast window that you set up.
- Select aReport Byoption for viewing data. All levels display the occupancy on books and Occupancy Forecast
- Total 
			 Groups & Transient: This version of the report
			 also includesPhysical CapacityThe total number of guest rooms at a property, including out of order rooms.andEffective CapacityThe property's physical capacity minus the out of order rooms..
- Forecast 
			 Groups,Market SegmentorBusiness View: 
			 These reports do not include property 
			 totals.
- Room ClassesorRoom Types: These versions include  Effective Capacity andAuthorized CapacityThe Effective Capacity (physical capacity minus Out of Order rooms) plus Overbooking.. They don't include property totals.
- If applicable, select theInclude Discontinued Room Typescheckbox to include historical data for discontinued room types.
- Select theRemove Excluded Segmentscheckbox if you want the Occupancy metrics to exclude business from specific market segments. You must define your excluded market segments inProperty Information.
- Select a reportFormat:
- SelectOn Screento open the report in a new browser window. Use the paging 
			arrows on the top of the window to page through multiple 
			 windows of data.
- SelectExcelto open or save the report as an Excel spreadsheet.
- ClickGenerate.
SeeExporting and Printing Reportsfor more information about managing report downloads 
		in your browser.

### Investigating Pace using the Booking Pace Report

- Run the report using theTotal 
	Groups & Transientoption after entering the Max Days to Arrival with the required 
	 number of days of pace information:
- Review 
			 theOccupancy on Books - Totalcolumn to see the overall pace on the property level. This column shows the total rooms sold as the Capture Date for the selected Arrival Date.
- Review theOccupancy on Books - GroupandOccupancy on Books -Transientcolumns to drill down 
							 to the business type level.
- Review the differentOccupancy Forecastcolumns to see the relationship between booking 
							 pace and the system's forecast. SinceG3 RMSexpects a certain pace for each Forecast Group, 
							 a change in Rooms Sold does not necessarily 
							 mean a change in forecast. Equally, a change 
							 in Occupancy Forecast could be triggered by 
							 other factors than pace, like wash, competitor 
							 prices, or Out of Order rooms.
- Variances betweenHotel CapacityandAvailable 
							 Capacitytell you if Out of Order rooms 
							 impacted the forecast.
- If, after reviewing the pace on the Total 
	 Groups & Transient level, you want to investigate 
	 the pace in more detail, run the report at a more detailed level, for example byForecast 
	 Groups. At the Room Class level, Authorized Capacity helps you understand how overbooking impacts pace. For example, you stopped selling because Occupancy On Books reached Authorized Capacity.

## Data Details

The report displays the following information. 
 The data varies based on the level selected in theReport Byoption.

## Scenarios for Data Discrepancies

If you have questions about differences in the data betweenG3 RMSand other systems,  review one of the following topics:

### Last Year's Booking Pace is Missing

This scenario applies if you're in your first year of system implementation, and yourreservation systemprovides incomplete historical data. When that occurs,  last year's pace looks like a blue triangle with a straight line from zero days to arrival to the final occupancy for the monitored period. For more information, reviewPace Data Missing for Last Year.

### Data Differences between Reporting Levels

If you have questions about variations in data between different levels, for example, between the property and Forecast Group levels or pickup between rate code  market segment level, seeData Level Differences.

### Pace Data Differs betweenG3 RMSand DailyExtracts

If you find data variations between same time last year (STLY) inG3 RMSand  other systems, seePace Differences.

### Pace Data Differs between IDeaS Systems

If you're transitioning from IDeaS RMS toG3 RMS, reviewPace Differences between IDeaS Systems.
