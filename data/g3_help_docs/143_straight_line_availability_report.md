# Straight Line Availability Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Straight-Line-Availability-Report.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Straight-Line-Availability-Report.htm`
- **Ingestion Date:** `2026-09-11 22:13:44`

---

# Straight Line Availability Report

Use the Straight Line Availability report to see occupancy dates when a room type does not have availability for more than one room and for a stay of two to seven nights, even though its Room Class has continuous availability considering its other room types.
For example, your Standard Room Class contains two room types: Queen and King. For Tuesday you only have one Queen left to sell. For Wednesday, you have only one King. A guest who wants to book a Standard room for Tuesday for two nights sees no availability for your property, even though you have availability at the Room Class level.
TheStraight Line Availability Exceptionautomatically looks for a lack of straight line availability for one room for an occupancy date. Use the report only when you want to look for availability for more rooms for a specific period.  For example, a group needs 12 rooms and you want to know if you should adjust reservations to make a room type available for their entire stay.
When straight line, or stay through, availability doesn't exist for lengths of stay up to seven days, the report displays the dates and the Room Class. You can then decide if you want to move reservations between room types in theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.to free up space and create straight line availability. In the example, it might be more profitable to upgrade or move one Standard Queen reservation on Wednesday to a King to free up availability for two nights in the Standard Queen.

## Reporting Steps

- Click, thenReports, and thenStraight Line Availability.
- Select theArrival Start Dateand theArrival End Datefor the period to investigate.Click the default date.Complete one of the following options:Enter a date in theSelectionfield.SelectSpecific Datefrom the menu. Click the left or right  arrows to navigate between months; click the double arrows to navigate between years. Click the appropriate date in the calendar. ClickApply.SelectRolling Datefrom the menu. Select theSystem Dateor choose to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.by a defined number of days by selecting eitherSystem Date -orSystem Date +. Enter the number of days to offset the System Date in theSelectionfield.ClickApply.
- Click the default date.
- Complete one of the following options:Enter a date in theSelectionfield.SelectSpecific Datefrom the menu. Click the left or right  arrows to navigate between months; click the double arrows to navigate between years. Click the appropriate date in the calendar. ClickApply.SelectRolling Datefrom the menu. Select theSystem Dateor choose to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.by a defined number of days by selecting eitherSystem Date -orSystem Date +. Enter the number of days to offset the System Date in theSelectionfield.
- Enter a date in theSelectionfield.
- SelectSpecific Datefrom the menu. Click the left or right  arrows to navigate between months; click the double arrows to navigate between years. Click the appropriate date in the calendar. ClickApply.
- SelectRolling Datefrom the menu. Select theSystem Dateor choose to offset theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.by a defined number of days by selecting eitherSystem Date -orSystem Date +. Enter the number of days to offset the System Date in theSelectionfield.
- ClickApply.
- Enter theNumber of Roomsthat you want to investigate for straight line availability for the period.
- ClickGenerate. The occupancy dates display for which there is a lack of straight line availability for the evaluated number of rooms.
- Click theIssue Datelink to see details for the displayed occupancy date.
Click the export iconto export the report to a spreadsheet and use the data to make adjustments in thereservation system.
If you ran the report to see more details about an Exception, return to Information Manager to resolve the Exception.
SeeExporting and Printing Reportsfor more information about managing report downloads 
		in your browser.

## Data Details

Starting with the Arrival Start Date,G3 RMSchecks if room types are available for stays of more than one night for your requested number of rooms. If all room types are available for seven nights, thenG3 RMSconsiders that the associated Room Class has straight line availability for this period and starts to check the next seven-day period.
If a room type cannot be sold for a length of stay between two and seven nights, even though its Room Class has continuous availability considering all room types for the same period,G3 RMSdisplays an Issue Date.
The Issue Date is the date when straight line availability is interrupted. In the window the Issue Date displays the available rooms for this room type in red.
For example, you enter June 1 through June 8 as the period to investigate for a group that requires 12 rooms.G3 RMSchecks the period starting on June 1. It finds that for a two-night and three-night stay, the STB room type has availability to accommodate the 12-room request, but it does not have availability on the fourth night stay. For June 5, the Room Class for the STB room type has no availability in any room type.
In this case, June 4 displays available rooms values in red. June 5 does not display because there is no opportunity on this date to move reservations to another room type.
If the group requires a four-night stay, you can choose to move reservations on June 4 to another room type to accommodate the group in the STB room type.
