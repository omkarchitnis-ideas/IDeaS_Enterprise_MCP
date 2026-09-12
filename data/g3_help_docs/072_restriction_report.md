# Restriction Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Restriction-Level-Report.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Restriction-Level-Report.htm`
- **Ingestion Date:** `2026-09-11 22:12:56`

---

# Restriction Report

Generate orschedulethe Restriction Report to see the Last Room Value (LRV) and the rate restrictions thatG3 RMSproduces, for example, because you manually deploy restrictions to selling systems. Other scenarios for this report include:
- To help you see how LRV is translated for selling systems that can't accept LRV. For those systems,G3 RMSsends MinLOS or FPLOS restrictions instead of LRV.
- If your property is inDecision CreationA one-way status when the RMS receives data from the reservation system, creates forecasts and outputs (like pricing), but does not send outputs to the selling system.and is not sending restrictions to your selling systems. The report provides the data for you to manually update restrictions in the selling systems. See Decision Configuration for information about decision modes.
- If your property is inDecision DeliveryA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system.and is sending LRV to control rates, the report helps you understand the impact of LRV at the Room Class and rate plan level.
To use the Restriction Report, you must first completeRestriction Setup.

## Reporting Steps

- Click, thenReports, and thenRestriction.
- Select theReport Type:MinLOS: Displays Minimum Length of Stay restrictions.FPLOS: Displays Full Pattern Length of Stay decisions.
- MinLOS: Displays Minimum Length of Stay restrictions.
- FPLOS: Displays Full Pattern Length of Stay decisions.
- Select theStart DateandEnd Datefor occupancy dates that you want to display:Click the date button.Complete one of the following date selections:SelectSpecific Datefrom the menu. Click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar.SelectRolling Date. Select theSystem Dateor choose to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.by a defined number of days by selecting eitherSystem Date -orSystem Date +. Enter the number of days to offset the System Date in theSelectionfield.ClickApply.
- Click the date button.
- Complete one of the following date selections:SelectSpecific Datefrom the menu. Click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar.SelectRolling Date. Select theSystem Dateor choose to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.by a defined number of days by selecting eitherSystem Date -orSystem Date +. Enter the number of days to offset the System Date in theSelectionfield.
- SelectSpecific Datefrom the menu. Click the single left or right arrows  to navigate between months or the double arrows to navigate between years. Click the appropriate date in the calendar.
- SelectRolling Date. Select theSystem Dateor choose to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.by a defined number of days by selecting eitherSystem Date -orSystem Date +. Enter the number of days to offset the System Date in theSelectionfield.
- ClickApply.
- Select theRoom Type. Select a Room Class or click the open iconfor the Room Class to select specific room types.
- Select theReport Style:Full: Displays all decisions for the selected occupancy dates.Differential: Displays only decisions that have changed in your selected time frame for the selected occupancy dates.
- Full: Displays all decisions for the selected occupancy dates.
- Differential: Displays only decisions that have changed in your selected time frame for the selected occupancy dates.
- If you are generating a Differential report, useChanges Sinceto select the date in the past from which you want to see decision changes:Click the date button.Complete one of the following date selections:SelectSpecific Date, and click a past date in the calendar.SelectRolling Date. SelectLast updated dateto view decisions that changed since the last update orLast updated date -to subtract from this date. Enter the number of days to subtract from the last updated date in theSelectionfield.ClickApply.
- Click the date button.
- Complete one of the following date selections:SelectSpecific Date, and click a past date in the calendar.SelectRolling Date. SelectLast updated dateto view decisions that changed since the last update orLast updated date -to subtract from this date. Enter the number of days to subtract from the last updated date in theSelectionfield.
- SelectSpecific Date, and click a past date in the calendar.
- SelectRolling Date. SelectLast updated dateto view decisions that changed since the last update orLast updated date -to subtract from this date. Enter the number of days to subtract from the last updated date in theSelectionfield.
- ClickApply.
- Select a reportFormat:
- SelectOn Screento open the report in the bottom pane.
- SelectExcelto open or save the report as an Excel spreadsheet.
- ClickGenerate.
SeeExporting and Printing Reportsfor more information about managing report downloads 
		in your browser.

## Data Details

The Restriction Report displays the following information:
