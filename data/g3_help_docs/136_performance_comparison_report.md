# Performance Comparison Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Performance-Comparison-Report.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Performance-Comparison-Report.htm`
- **Ingestion Date:** `2026-09-11 22:13:39`

---

# Performance Comparison Report

Generate orschedulethe Performance Comparison report to analyze the booking pace of a period over time and to compare it to the pace of a similar period.
For example, the team in your revenue meeting is concerned about the pace for the next month. Use the report to display a chart with the changes in On Books rooms and revenue over the last 90 days, compared to the changes for the same month last year. Start with the Hotel level, then drill down to more details, for example, by Room Class, Forecast Group, or Business View. The report has a chart and table version and also displays the forecasted rooms and revenues.

## Reporting Steps

- Click, thenReports, and thenPerformance Comparison.
- Click theAnalysis Start Dateand theAnalysis End Dateto define the monitored period by using one of the following options:Enter a date in theSelectionfield and clickApply.SelectSpecific Datefrom the menu. On the calendar, click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar and clickApply.Use flexible dates by selectingRolling Datefrom the menu:Select theSystem Date,Start of Month(the first day of theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.month) orEnd of Month(the last day of the System Date month).Optionally, choose to offset that date by selecting the option with either-or+. For System Date, the offset is number of days. For Start of Month and End of Month, the offset is the number of months.Enter the number of days or months to offset the date in theSelectionfield.ClickApply.
- Enter a date in theSelectionfield and clickApply.
- SelectSpecific Datefrom the menu. On the calendar, click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar and clickApply.
- Use flexible dates by selectingRolling Datefrom the menu:Select theSystem Date,Start of Month(the first day of theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.month) orEnd of Month(the last day of the System Date month).Optionally, choose to offset that date by selecting the option with either-or+. For System Date, the offset is number of days. For Start of Month and End of Month, the offset is the number of months.Enter the number of days or months to offset the date in theSelectionfield.ClickApply.
- Select theSystem Date,Start of Month(the first day of theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.month) orEnd of Month(the last day of the System Date month).
- Optionally, choose to offset that date by selecting the option with either-or+. For System Date, the offset is number of days. For Start of Month and End of Month, the offset is the number of months.
- Enter the number of days or months to offset the date in theSelectionfield.
- ClickApply.
- Set the Comparison period. The date range for the Comparison period must include the same number of days as the Analysis period and use the same date selection method.  When you set the Comparison Start Date, the Comparison End Date adjusts accordingly:Click theComparison Start Date.Complete one of the following options:If you selectedRolling Dateto define the Analysis period, selectLast year this dayorLast year start of month. Optionally, choose to offset that date by selecting the option with either-or+. Enter the number of days or months to offset the date in theSelectionfield.If you selected specific dates to define the Analysis period, select the Start Date from the calendar.ClickApply.
- Click theComparison Start Date.
- Complete one of the following options:If you selectedRolling Dateto define the Analysis period, selectLast year this dayorLast year start of month. Optionally, choose to offset that date by selecting the option with either-or+. Enter the number of days or months to offset the date in theSelectionfield.If you selected specific dates to define the Analysis period, select the Start Date from the calendar.
- If you selectedRolling Dateto define the Analysis period, selectLast year this dayorLast year start of month. Optionally, choose to offset that date by selecting the option with either-or+. Enter the number of days or months to offset the date in theSelectionfield.
- If you selected specific dates to define the Analysis period, select the Start Date from the calendar.
- ClickApply.
- Enter the number ofDays of Pacethat you want displayed in the report, limited to 365 days maximum.
- InGraph Options, select the revenue measurement that you want to include in the graphical version of the report. Both revenue measurements are included in the tabular results.
- Select the method to calculate pace:SelectEach Arrival Dateto calculate pace days from each date in the evaluation period.SelectEnd of Selected Periodto calculate pace days from the end date of the period.See anexamplefor how the two methods differ.
- SelectEach Arrival Dateto calculate pace days from each date in the evaluation period.
- SelectEnd of Selected Periodto calculate pace days from the end date of the period.See anexamplefor how the two methods differ.
- Select a data level from theView Bymenu. If applicable, select a sub-level, for example, a Forecast Group name if you select Forecast Groups as the data level.
- Select a single name from theCompetitorsmenu to display its price on the report. This option is only available if the Analysis period is set to a one-day duration (in other words, the Analysis Start Date and the Analysis End Date are the same) and Total Property is selected as the level.
- ClickGenerate.
- If you often run the report with the same selections and have the permissions, click toSavethat version.
SeeExporting and Printing Reportsfor more information about managing report downloads 
		in your browser.

## Data Details

Begin by running the report at the Total Property level to get an overview of the differences. Then drill down further by running separate detailed reports, for example, at the Transient, Group, or a single Forecast Group and even a Market Segment level. The report displays the following information, displayed at the selected levels:

## Scenarios

### Example of the Two Pace Calculation Methods

The Performance Comparison report offers two ways to calculate pace days:

#### 1. End of Selected Period

This option calculates the pace days from the end date of the analysis or comparison period. It shows how many rooms were on books and forecasted a certain number of pace days from the end date. The report totals the rooms and forecast values for a pace point. See the example below.

#### 2. Each Arrival Date

This option calculates the same number of pace days from each date in the analysis period or comparison. It shows how many rooms were on books and forecasted for a certain number of pace days prior to each date in the period. The report then totals the rooms and forecast values for that pace point.
Compare the two method in the following example:
- Analysis Period: June 11, 2021 to June 12, 2021 (Friday and Saturday)
Analysis Period: June 11, 2021 to June 12, 2021 (Friday and Saturday)
- Comparison Period: June 12, 2020 to June 13, 2020 (equivalent Friday and Saturday from previous year)
Comparison Period: June 12, 2020 to June 13, 2020 (equivalent Friday and Saturday from previous year)
- Number of Days of Pace: 30
Number of Days of Pace: 30

### Examples of Data Differences

You might see differences in the data betweenG3 RMSand other systems,  like one of the following:

### Last Year's Booking Pace is Missing

This scenario applies if you're in your first year of system implementation, and yourreservation systemprovides incomplete historical data. When that occurs,  last year's pace looks like a blue triangle with a straight line from zero days to arrival to the final occupancy for the monitored period. For more information, reviewPace Data Missing for Last Year.

### Data Differences between Reporting Levels

If you have questions about variations in data between different levels, for example, between the property and Forecast Group levels or pickup between rate code  market segment level, seeData Level Differences.

### Pace Data Differs betweenG3 RMSand DailyExtracts

If you find data variations between same time last year (STLY) inG3 RMSand  other systems, seePace Differences.

### Pace Data Differs between IDeaS Systems

If you're transitioning from IDeaS RMS toG3 RMS, reviewPace Differences between IDeaS Systems.
