# Pickup/Change and Differential Control Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Pickup-Change-Differential-Control-Report.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Pickup-Change-Differential-Control-Report.htm`
- **Ingestion Date:** `2026-09-11 22:13:40`

---

# Pickup/Change and Differential Control Report

The two versions of this report help you answer different questions:
- ThePick 
	 Up Reportshows the change in performance metrics for a selected analysis period and over a selected activity period. For example, how much revenue did I pick up during the last 7 days (the activity period) for each arrival date in the next month (the analysis period)?
- TheChange Reportshows you the change in performance data and decisions for a selected analysis period since a selected activity date. For example, how much did revenue and pricing for the next month (the analysis period) change since the last nightly optimization (the activity period)?Seeexamplesto understand the differences.
Use rolling dates, like the next 30 days, toschedulethe report, seescenarios. And if you often run the report with the same selections, you cansavethat version. If you use rolling dates, you must use them for both the analysis and the activity periods. To learn about the options for activity dates, seeBest Practices.

## Reporting Steps

- Click, thenReports, and thenPick Up/Change and Differential 
	 Controls.
- Select the desired report version. See the descriptions above.
- Click theAnalysis Start DateandAnalysis End Dateto define the analyzed period by using one of the following options:Enter a date in theSelectionfield and clickApply.SelectSpecific Datefrom the menu. On the calendar, click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar and clickApply.Use flexible dates by selectingRolling Datefrom the menu:Select theSystem Date,Start of Month(the first day of the System Date month) orEnd of Month(the last day of the System Date month). For the Analysis End Date, you can also selectEnd of Year.Optionally, choose to offset that date by selecting the option with either-or+. For System Date, the offset is number of days. For Start of Month and End of Month, the offset is the number of months.Enter the number of days or months to offset the date in theSelectionfield.ClickApply.
- Enter a date in theSelectionfield and clickApply.
- SelectSpecific Datefrom the menu. On the calendar, click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar and clickApply.
- Use flexible dates by selectingRolling Datefrom the menu:Select theSystem Date,Start of Month(the first day of the System Date month) orEnd of Month(the last day of the System Date month). For the Analysis End Date, you can also selectEnd of Year.Optionally, choose to offset that date by selecting the option with either-or+. For System Date, the offset is number of days. For Start of Month and End of Month, the offset is the number of months.Enter the number of days or months to offset the date in theSelectionfield.ClickApply.
- Select theSystem Date,Start of Month(the first day of the System Date month) orEnd of Month(the last day of the System Date month). For the Analysis End Date, you can also selectEnd of Year.
- Optionally, choose to offset that date by selecting the option with either-or+. For System Date, the offset is number of days. For Start of Month and End of Month, the offset is the number of months.
- Enter the number of days or months to offset the date in theSelectionfield.
- ClickApply.
- Set theActivity Start DateorActivity End Dateusing the same date selection method that you used to define the Analysis period:Click the default date.Complete one of the following options:If you selectedSpecific Dateto define the Analysis period, select the date from the calendar.If you selectedRolling Dateto define the Analysis period, select a previous optimization. SeeSetting the Activity Start Dateabove.ClickApply.
- Click the default date.
- Complete one of the following options:If you selectedSpecific Dateto define the Analysis period, select the date from the calendar.If you selectedRolling Dateto define the Analysis period, select a previous optimization. SeeSetting the Activity Start Dateabove.
- If you selectedSpecific Dateto define the Analysis period, select the date from the calendar.
- If you selectedRolling Dateto define the Analysis period, select a previous optimization. SeeSetting the Activity Start Dateabove.
- ClickApply.
- Select a filter underData Selectionfor the business level that you want to see in the report.
- Select theParametersfor the data that you want to include in the report. The available data options depend on the Report Style and the business level that you selected in Data Selection.For example, if you select room types, you can select products other thanthe primary priced product.
- If you do not select Total Property or Business Types as the Data Selection, then you can select theShow Aggregated Valuescheckbox to show summarized date (for example, for all Room Classes versus each Room Class individually).You are limited in the number of selections and a counter aboveData Selectionshows you how many elements you selected out of the maximum number.
- For the Change Report and at the Total Property level, you can selectCompetitorsto include in the report results.	PressCtrl+click to select multiple competitors.
- Select a reportFormat:
- SelectOn Screento open the report in a new browser window. Use the paging 
			 buttons on the top of the window to page through multiple 
			 windows of data.
- SelectExcelto open or save the report as an Excel spreadsheet.
- Note:if you select a large date range,G3 RMSemails you the report. This allows you to continue to work in the system.
- ClickGenerate.
Seeexporting 
			and printing reportsfor how to manage report downloads 
		in your browser. If you selected rolling dates and have the permissions, you also see theSchedulebutton, seescheduling reports.

### Steps to View Profit Data

If you enabledProfit Optimization, you can select Profit metrics as Parameters (step 7):
- Profit: the calculation depends on data that you provide.G3 RMScan consider profitability of guest rooms (based on servicing, channel costs, etc.) and profitability of other revenue streams. For current dates,G3 RMSestimates the profit based on occupancy on books andOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).. For past dates, the system estimates the profit based on the final number of rooms occupied.
- ProPOR: profit per occupied room. ProPOR equals the profit divided by the number of occupied rooms and is comparable toADRAverage Daily Rate. Room revenue divided by the number of rooms of occupancy..
- ProPAR: profit per available room. ProPAR equals the profit divided by capacity and is comparable toRevPARRevenue Per Available Room. The total room revenue divided by the total number of rooms (capacity).
See the Property Information topic for the capacity definition..

## Best Practices

### Understand the Impact of Setting the Activity Dates

For the Pick Up Report, choose:
- Last updated dateto show activity from the current day'sNightly ProcessingAlso known as Business Day End or BDE. The standard daily system update that runs during overnight hours after the end of the business day..
- Last updated date -to define the number of days prior to the last Nightly Processing. For example, Last updated date-1 is yesterday's nightly processing.
For the Change Report, you have an additional option:
- Last Optimizationshows changes since  either the last nightly orintraday processingAbbreviated IDP, it's a system update that occurs between nightly updates. For details search for the Processing topic. Also known as Current Day Processing (CDP).. This selection can show intraday data changes, if your property has more than one dailyprocessing.
To view examples using the Change Report, see Scenarios below.

## Scenarios

### Change Report Example

A property with two intraday processings has three activity periods: nightly processing to intraday processing 1, intraday processing 1 to intraday processing 2, and intraday processing 2 to nightly processing.

### Change Report Example Using On Books Values

Using the previous property, what does the Change Report show with these metrics? Today is October 24 and the current Occupancy On Books is 170.  The Booking Pace Report shows Occupancy On Books at the end of each business day:
The Change Report for October 24 (Analysis Start and End Date = System Date) shows:

### Scenarios for Using Rolling Dates in the Change Report

#### Changes in the Next 90 Days since Yesterday

You want to see what has changed in the next 90 days since yesterday.
- Analysis Start Date: System Date
- Analysis End Date: System Date+90
- Activity Start Date: Last updated date-1

#### Measure Change since Start of Day Yesterday

You want to see what changed since for today since yesterday, when scheduled prior to an intraday processing.
- Analysis Start Date: System Date
- Analysis End Date: System Date
- Activity Start Date: Last updated date-1

#### Measure Change from Friday to Monday (on Monday Morning)

You need to review the data for today from the nightly processing on Thursday night to the current date.
- Analysis Start Date: System Date
- Analysis End Date: System Date
- Activity Start Date: Last updated date-3

#### Measure Same Day Change for Today from the Last Optimization to the Current

You need to review the data from the last daily processing to the current data.
- Analysis Start Date:System DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.
- Analysis End Date: System Date
- Activity Start Date: Last optimization
