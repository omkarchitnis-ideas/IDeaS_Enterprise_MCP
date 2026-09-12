# Synthetic Data for Inventory Change

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/LDB/LDB-for-Inventory-Change.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/LDB/LDB-for-Inventory-Change.htm`
- **Ingestion Date:** `2026-09-11 22:14:05`

---

# Synthetic Data for Inventory Change

Use Synthetic Data for Inventory Change to ensure the best possible forecasts and decisions forG3 RMSproperties with renovations that change their room types, their number of rooms, or both. For example, a property adds a new wing or divide suites into smaller rooms. In those cases,G3 RMScan't immediately know the demand for new or changed inventory.
With Synthetic Data for Inventory Change,G3 RMSuses booking patterns and history of unchanged room types, together with sales projections, to forecast demand. Once the system learns  the patterns of the new room types, it turns off Synthetic Data and uses historical data and patterns from all room types.
With Synthetic Data for Inventory Change, you set up two tabs:

### Select Room Types

Tell the system which room types are new or changed. For those, you provide the below sales projections.

### Projections

Complete expected rooms sold and revenue for the selected room types, by market segment. The projections replace the missing historical demand data for the changed or new room types. You also define the first date whenG3 RMScan start usingMaster ClassThe occupancy, revenue or ADR that the property achieved, once the day is in the past. Actual occupancy is also called Final Rooms Sold.data of the new room types, together with your projections, to forecast demand.

## Setup Steps

### Select Room Types

- Click, thenForecasts, and thenSynthetic Data.
- In theSelect Room Typestab, select theUse Projected Datacheckbox for the room types that lack 365 days of historical data.
- ClickSave.

### Projections

- Click, thenForecasts, and thenSynthetic Data.
Click, thenForecasts, and thenSynthetic Data.
- Click theProjectionstab.
Click theProjectionstab.
- Select the first date when the final rooms sold data is "normal." SeeBest Practicesfor how to select the date.
Select the first date when the final rooms sold data is "normal." SeeBest Practicesfor how to select the date.
- ClickSave.
ClickSave.
- Enter theStart DateandEnd Dateof the period for which you provide projections.
Enter theStart DateandEnd Dateof the period for which you provide projections.
- Add projections data by uploading daily values using an Excel worksheet. ClickDownload.
- Save the workbook to a location on your computer.
Save the workbook to a location on your computer.
- Complete or review the values in theProjected Dataworksheet. SeeData Detailsbelow for a description of the values.
Complete or review the values in theProjected Dataworksheet. SeeData Detailsbelow for a description of the values.
- If you made changes, save the modified file in an XLSX format.
If you made changes, save the modified file in an XLSX format.
- ClickUpload.
ClickUpload.
- Navigate to and select the saved workbook.
Navigate to and select the saved workbook.
- ClickOpen. The system confirms when the projections are successfully uploaded.
ClickOpen. The system confirms when the projections are successfully uploaded.
- To overwrite the values, repeat the process.
To overwrite the values, repeat the process.

### Run a Synthetic Data Build

- If necessary, complete other set up for the selected room types, for example mapping them to Room Classes in Rooms setup.
- Ask IDeaS to run the Synthetic Data build. In the process,G3 RMSuses your projections to simulate the missing Actual data for the selected room types, by market segment. If you have more than one Room Class, the system distributes projections to them primarily according to their capacities. For distributing the revenue projections, your pricing structure and Price Ranking also matter.G3 RMSthen uses the simulated historical data, the history, and booking patterns of unchanged room types to create forecasts and decisions for all room types. After the process completes, the Projections tab is unavailable. IDeaS tells you when you can continue with the next step.
- Review the forecasts and decisions. If you need to change your projections, contact IDeaS support to unlock the tab and to request a re-build.
- OnceG3 RMShas 365 days of historical data  for the new room types, you can contact IDeaS to switch from a Synthetic Data to a Standard build.

## Data Details

### Projections

SeeBest Practicesfor help with selecting the values.

#### Projected Rooms and Revenue Excel Worksheet

## Best Practices

### Determine the Date When Business Patterns Are "Normal"

How can you select the first occupancy date when business for the new or changed room types closes with "normal" patterns? Imagine that the date is past, and you review itsMaster ClassThe occupancy, revenue or ADR that the property achieved, once the day is in the past. Actual occupancy is also called Final Rooms Sold.occupancy and revenue. Those values match what you expect from similar "normal" days in the future. For example, if you added a new room type, the demand for it might be lower until more guests are familiar with it or until reviews about it are posted. The amount and type of business is "normal" only when those initial impacts are gone.
Because you think that business of that date and all following dates is "normal," you wantG3 RMSto use historical data to forecast demand for the new room types. Therefore, starting with the date you select, the system uses each day's Actual data together with projected data to forecast future demand forallroom types. Until that date, the system ignores the actual rooms and revenue data for the new room types and uses projected data for forecasts.

### Select the Correct Start and End Date for Your Projections

The system auto-populates the dates based on available data and the minimum required date range.
Start by selecting thefirst date with "normal" final rooms sold data. After you enter it, the Start Date defaults to that date. The End Date defaults to the Start Date plus 365 days. Adjust the dates, if needed, depending on your situation.
G3 RMSrequires at least 365 days of data, so the End Date should equal the Start Date plus 365 days. Note that the End Date doesn't date automatically when you change the Start Date. You can download and upload the Excel worksheet for shorter periods. You can set up 730 days of projections.

#### New room types are being sold and guests are staying in them

If your new or changed room types are already welcoming guests, the Start Date should be the current System Date.

#### New room types are being sold, but the first arrival date is in the future

The Start Date should be the first date that the property is expecting arrivals.

#### New room types are not yet being sold

The Start Date should be the first date that the property is expecting arrivals for the new or changed room types.

#### Usable History is Available

Your 365 days of data can be a combination of your projections and, if available, usable history. Usable history means that the first date with "normal" final data is in the past. The days between that date and theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.count towards the 365 days.
For example, Actual data is available inG3 RMSfrom January 1, 2025 to March 31, 2025. You entered February 1, 2025 as the first date with normal final rooms sold data, because the month of January didn't provide representative data. In this case, your Start Date is April 1, 2025, becauseG3 RMSis missing data from this date. Your End Date is February 1, 2026, 365 days after the first date with normal final rooms sold data.

### Create Projections that Reflect Typical Business

For the room types that are unchanged and that have historical data,G3 RMSuses all demand history as an input into itsunconstrained demand calculations. With Synthetic Data for Inventory Change, your projections replace the demand history. That means the system uses your projections, and any available usable history, to simulate the missingMaster ClassThe occupancy, revenue or ADR that the property achieved, once the day is in the past. Actual occupancy is also called Final Rooms Sold.data for the past year. That simulated history, the booking patterns of unchanged room types, and on books data are the basis for the system's forecasts and decisions.
Therefore, your projections shouldnotbe an exact forecast of the upcoming year. Instead, projections should reflect the typical business of a year that you want the system to use for forecasting the upcoming year. For example, don't enter exceptional demand for Special Events in your projections. SeeManage Demand for Special Events with Overridesfor details.

### Manage Demand for Special Events Using Overrides

In the Synthetic Data build,G3 RMScreates forecasts based not only your projections, but also on booking patterns and business on books. Thus, the system likely ignores days in your projections when demand greatly differs from normal patterns (day of the week, seasonal). That includes Special Events with exceptional demand.
Let's use a simplified example. Your projections include a Special Event on a Saturday three months from now. You expect higher than normal transient demand for it and include that in your projections for that day. The date is an outlier from other trends, meaning that demand for other Saturdays in the same season is much lower. In that case,G3 RMSlikely forecasts that day lower than your projections, closer to the normal demand for Saturdays.
Therefore, we recommend that you enter normal, not high or low, demand for Special Events in your projections. Next, enter a Special Event for the date. After youCreate and Commit Forecast Groups, monitor and, if needed, override demand.

#### Recurring Events

If the Special Event is recurring, create only future, not past, instances. This applies even if the past instance is part of the historical data thatG3 RMSuses to forecast (in other words, even if it occurs after the first date with "normal" final rooms sold data).
For example, today is June 1 and your projections include the recurring "New Yearâs Eve" Special Event. Your first date with "normal" final rooms sold data is November 1 of last year. When this year's New Year's Eve happens, last year's instance falls into the historical data that the system uses, after November 1. However, because the future instance is in the period of your projections,G3 RMSlikely ignores the past instance and uses normal demand patterns to forecast this year's instance. Therefore, monitor and, if needed, override the demand for this year's instance.
Once all your future Special Events instances occur after the period of your projections, follow theBest Practices for repeat events.

### Fix the Issues that Cause Import Failures for the Worksheet

If the worksheet has data or format issues, the import fails. To avoid that, ensure the following:
- The Property Name and Property Code rows are unchanged and appear exactly as they did when you exported the workbook.
- No columns are added, deleted, moved, or renamed.
- The name of the Projected Data tab is unchanged.
- The file type is XLSX.
- No gaps exist in dates between the start and end date.
- No market segments are missing for a date.
- The total projected rooms sold for any date doesn't exceed the capacity.
- For each row, if the Projected Room Revenue is greater than 0, the Projected Rooms Sold is also greater than 0.
- No cells are blank. Enter 0.00 as placeholders if there are no projected rooms sold or revenue values for a date.
- No formulas are added to cells.
