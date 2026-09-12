# Data Extraction Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Data-Extract.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Data-Extract.htm`
- **Ingestion Date:** `2026-09-11 22:13:35`

---

# Data Extraction Report

Generate orschedulethe Data Extraction Report to exportG3 RMSdata, for example, to work on the data in Excel. For each day of a set period, select:
- The type of data, for example, Number of Arrivals, the Occupancy Forecast, or the Overbooking decision.
- The data level, like  the Occupancy Forecast data at the Property, the Room Class, the Room Type, or all three levels.
- If you want to compare to past data, for example last year.
- If you selected competitors' rate shopping data, choose which competitors to include.
- At the Room Type level, the Product (other thanthe primary priced product) for which to Show Price.
Review thesteps to run the reportor view thedescriptions of all columns.
With an integration forSmith Travel Research (STR)STR is a global provider of competitive benchmarking, information services and research to the hotel industry. STR reports provide property performance data compared to its competitive aggregate and general market, allowing you to follow trends in occupancy, average daily rate (ADR), revenue per available room (RevPAR).or Benchmarking Alliance, you can include Market Performance data in the report. This helps you understand how your Occupancy, ADR, and RevPAR compare to your competitors' historical data.
If you selectShow Market Performance, your date range can be a maximum of 90 days.	This year's and last year's Market Performance data display with your actuals. For current or future dates, you see past STR data from the same time last year, adjusted by day of week.  If data is missing or if you only receive STR market level data, you see --.
Notes:
- The data in the Data Extraction Report is from the daily performance report, rather than the monthly, summary level data that you see on theAt a Glance Summarypage.
The data in the Data Extraction Report is from the daily performance report, rather than the monthly, summary level data that you see on theAt a Glance Summarypage.
- G3 RMSdoesn't use this data in its optimization.
G3 RMSdoesn't use this data in its optimization.
- Click, thenReports, and thenData Extraction.If you visit this page often, clicknext to the name to add it to the Quick Access menu.
- Click the defaultStart Dateand theEnd Dateto define the monitored period by using one of the following options:Enter a date in theSelectionfield and clickApply.SelectSpecific Datefrom the menu. On the calendar, click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar and clickApply.Use flexible dates by selectingRolling Datefrom the menu:Select theSystem Date,Start of Month(the first day of the current month),End of Month(the last day of the current month) orEnd of Year(December 31 of the current year for End Date only).Optionally, choose to offset that date by selecting the option with either-or+. ForSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert., the offset is number of days. For Start of Month and End of Month, the offset is the number of months.Enter the number of days or months to offset the date in theSelectionfield.ClickApply.
- Enter a date in theSelectionfield and clickApply.
- SelectSpecific Datefrom the menu. On the calendar, click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar and clickApply.
- Use flexible dates by selectingRolling Datefrom the menu:Select theSystem Date,Start of Month(the first day of the current month),End of Month(the last day of the current month) orEnd of Year(December 31 of the current year for End Date only).Optionally, choose to offset that date by selecting the option with either-or+. ForSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert., the offset is number of days. For Start of Month and End of Month, the offset is the number of months.Enter the number of days or months to offset the date in theSelectionfield.ClickApply.
- Select theSystem Date,Start of Month(the first day of the current month),End of Month(the last day of the current month) orEnd of Year(December 31 of the current year for End Date only).
- Optionally, choose to offset that date by selecting the option with either-or+. ForSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert., the offset is number of days. For Start of Month and End of Month, the offset is the number of months.
- Enter the number of days or months to offset the date in theSelectionfield.
- ClickApply.
- Select the checkbox of any of theDisplay Options. The available options vary by property:To compare this year to the actual data from the past, select an option likeShow Last Year. The date for past years is adjusted by the day of the week.STRif you licensed STR reports and want to include STR data in the report.Include Account IDif you need to include a unique identifier for your property in your data.Include Discontinued Room TypesandInclude Discontinued Market Segmentsto include their historical data.Remove Excluded Segmentsif you want metrics like Occupancy, ADR, and RevPAR to exclude business from specific market segments. You define such exclusions inProperty Information. Using these exclusions might lead to data variations between different levels, seedata level differences.
- To compare this year to the actual data from the past, select an option likeShow Last Year. The date for past years is adjusted by the day of the week.
- STRif you licensed STR reports and want to include STR data in the report.
- Include Account IDif you need to include a unique identifier for your property in your data.
- Include Discontinued Room TypesandInclude Discontinued Market Segmentsto include their historical data.
- Remove Excluded Segmentsif you want metrics like Occupancy, ADR, and RevPAR to exclude business from specific market segments. You define such exclusions inProperty Information. Using these exclusions might lead to data variations between different levels, seedata level differences.
- Select the checkboxes for the desired data types and levels.Select a checkbox in the topAll Datarow to select all data types for that level.Clear the checkbox  to deselect all data types.Select data types as they apply to certain levels. For example, Special Event only applies at the Property level.
- Select a checkbox in the topAll Datarow to select all data types for that level.
- Clear the checkbox  to deselect all data types.
- Select data types as they apply to certain levels. For example, Special Event only applies at the Property level.
- Select optional data to add to the report:At the Property level, you can selectCompetitorsto include.At the Room Class level, you can selectMarket Segmentsto include.	 For example, use this option to exclude reservations made under House Use or Complimentary market segments.At the Room Type level, you can selectlinked,group, orindependentProductstoinclude.
- At the Property level, you can selectCompetitorsto include.
- At the Room Class level, you can selectMarket Segmentsto include.	 For example, use this option to exclude reservations made under House Use or Complimentary market segments.
- At the Room Type level, you can selectlinked,group, orindependentProductstoinclude.
- Select to filter the data for anInventory Group View, if set up. ReviewSetup Stepsfor details.
- ClickGenerate. The report downloads as an Excel file. Note that if you select a large date range,G3 RMSemails you the report. This allows you to continue to work in the system.Seeexporting and printing reportsfor more information about managing report downloads.
- If you often run the report with the same selections and have the permissions, click toSavethat version.
If you have permissions toschedule reports, you see theSchedulebutton.
Due to the large data volume of this report, you can set up onlyone scheduleper property. You can include up to 13 months of past data and the fullOptimization WindowThe number of days for which the RMS produces outputs (like pricing) and a constrained occupancy forecast. You can view the optimized outputs and occupancy forecast for the Optimization Window, but the system only sends outputs for the Upload Window. The Optimization Window usually matches and can't be longer than the Forecast Window.for future days in the scheduled report.
You can schedule the Data Extraction report with fixed dates, for a range of up to 120 days. You must select future dates.
The columns displayed in the report results depend on your data selections. For example, if you select toShow Last Year, a Last Year Actual column also displays next to the This Year column.
Each tab in the exported spreadsheet displays a selected level: Property, Room Class, Room Type, Forecast Group, Market Segment, or Business View.
The report displays the following data:

### Profit Data Details

If you enabledProfit Optimization, you can also select Profit metrics:
