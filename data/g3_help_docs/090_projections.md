# Projections

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/LDB/LDB-Projections.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/LDB/LDB-Projections.htm`
- **Ingestion Date:** `2026-09-11 22:13:08`

---

# Projections

With Synthetic Data,G3 RMSreplaces the missing historical data with your Projections  andBooking Patterns. Use the Projections tab to enter  your rooms and revenue projections for a typical year and to select the dates that these projections apply to.

### What Help Do You Need with Projections?

- I need to determine thedates for the projections.
I need to determine thedates for the projections.
- What are thesteps to add the projections?
What are thesteps to add the projections?
- I need to determine if I usemonthly or daily projectionsdata.
I need to determine if I usemonthly or daily projectionsdata.
- I need to determine what typical business means for the upcoming year, seeProjections replace history.
I need to determine what typical business means for the upcoming year, seeProjections replace history.
- I import projections - how do Iprevent upload issues?
I import projections - how do Iprevent upload issues?
- How doesG3 RMSuse my projectionsin aSynthetic Data build?
How doesG3 RMSuse my projectionsin aSynthetic Data build?

## Setup Steps

- Click, thenForecasts, and thenSynthetic Data.
Click, thenForecasts, and thenSynthetic Data.
- Click theProjectionstab.
Click theProjectionstab.
- Select theOpening Dateand theNormalization Date. For their definition and examples, seeSelect the Dates.
Select theOpening Dateand theNormalization Date. For their definition and examples, seeSelect the Dates.
- ClickSave.
ClickSave.
- TheProjections Startdefaults to the Opening Date that you entered. SeeSelect the Datesto learn if you should change it.
TheProjections Startdefaults to the Opening Date that you entered. SeeSelect the Datesto learn if you should change it.
- Unless you changed the Projections Start date, theProjections Enddate defaults to the Projections Start date plus the required minimum number of days, 365. You can add up to 730 days of projections, seeSelect the Datesfor details.
- Based onwhat data you have available, select toEnter Data By:Dayif you have daily projections data, for example, because your property uses RevPlan.Monthif you have monthly projections data, or if you are part of a large company andwant to create projections from similar properties (also requires the Projections Builder option in next step).
Based onwhat data you have available, select toEnter Data By:
- Dayif you have daily projections data, for example, because your property uses RevPlan.
Dayif you have daily projections data, for example, because your property uses RevPlan.
- Monthif you have monthly projections data, or if you are part of a large company andwant to create projections from similar properties (also requires the Projections Builder option in next step).
Monthif you have monthly projections data, or if you are part of a large company andwant to create projections from similar properties (also requires the Projections Builder option in next step).
- Select theEntry Type. Your options vary based on your selection in the previous step.
Select theEntry Type. Your options vary based on your selection in the previous step.
- If enabled, select theSource.
- ClickApply.
ClickApply.
- Continue with one of the following steps based on your selected entry type:Downloading and Uploading an Excel Worksheet.Use Projections Builderto enter your own data.Create Projections from similar properties.
Continue with one of the following steps based on your selected entry type:
- Downloading and Uploading an Excel Worksheet.
Downloading and Uploading an Excel Worksheet.
- Use Projections Builderto enter your own data.
Use Projections Builderto enter your own data.
- Create Projections from similar properties.
Create Projections from similar properties.
If your property uses RevPlan, download your Rooms and Room Revenue Forecast data in RevPlan. Then go toStep 4to upload the file. To use the download from RevPlan, you must ensure that:
- The Synthetic DataProjectionspage is unlocked. Contact your IDeaS representative if your screen is locked and you need to make an update.
- You  assigned attributes at the market segment and not at the rate code level. In that case, your Market Segments page looks likethis.
- After you clicked to download the file, save the workbook to a location on your computer.
- Complete or review the values:For daily projections, use theProjected Data Templatesheet.Note: You can add market segments in the file instead of adding them in theMarket Segmenttab, but don't delete any market segments. And if you add an invalid Market Segment by mistake, you can't delete it.For monthly projections, the following sheets apply:Period: This first sheet defines the dates for which you provide projections. The Start Date is usually theopening date. If that date is in the past, use today's date. The End Date is typically 365 days after the date whenbusiness patterns are normal.Note: don't change the Property Name or ID. It is one of theissues that cause upload failures.TheRoomsandADRsheets contain your projections by Market Segment and month. You must add values for all months.If you useComponent Rooms, enter the ADR for each Room Class.Note: The market segments attributed asEqual to BARhas a big impact on forecasts. An  ADR lower than theconfigured Floorcan result in unexpectedly low forecasts.Use theDOW patternsto tellG3 RMShow to distribute the monthly values. Enter positive, whole numbers, and the total percentage must equal 100. See an example ofhow the system uses your patterns.For ADR (monthly) and Projected Room Revenue (daily) values:Exclude taxes and commissions.For all-inclusive resorts, enter values based on the total price, inclusive of all services that your quoted prices cover.
- For daily projections, use theProjected Data Templatesheet.Note: You can add market segments in the file instead of adding them in theMarket Segmenttab, but don't delete any market segments. And if you add an invalid Market Segment by mistake, you can't delete it.
- For monthly projections, the following sheets apply:Period: This first sheet defines the dates for which you provide projections. The Start Date is usually theopening date. If that date is in the past, use today's date. The End Date is typically 365 days after the date whenbusiness patterns are normal.Note: don't change the Property Name or ID. It is one of theissues that cause upload failures.TheRoomsandADRsheets contain your projections by Market Segment and month. You must add values for all months.If you useComponent Rooms, enter the ADR for each Room Class.Note: The market segments attributed asEqual to BARhas a big impact on forecasts. An  ADR lower than theconfigured Floorcan result in unexpectedly low forecasts.Use theDOW patternsto tellG3 RMShow to distribute the monthly values. Enter positive, whole numbers, and the total percentage must equal 100. See an example ofhow the system uses your patterns.
- Period: This first sheet defines the dates for which you provide projections. The Start Date is usually theopening date. If that date is in the past, use today's date. The End Date is typically 365 days after the date whenbusiness patterns are normal.Note: don't change the Property Name or ID. It is one of theissues that cause upload failures.
- TheRoomsandADRsheets contain your projections by Market Segment and month. You must add values for all months.If you useComponent Rooms, enter the ADR for each Room Class.Note: The market segments attributed asEqual to BARhas a big impact on forecasts. An  ADR lower than theconfigured Floorcan result in unexpectedly low forecasts.
- Use theDOW patternsto tellG3 RMShow to distribute the monthly values. Enter positive, whole numbers, and the total percentage must equal 100. See an example ofhow the system uses your patterns.
- For ADR (monthly) and Projected Room Revenue (daily) values:Exclude taxes and commissions.For all-inclusive resorts, enter values based on the total price, inclusive of all services that your quoted prices cover.
- Exclude taxes and commissions.
- For all-inclusive resorts, enter values based on the total price, inclusive of all services that your quoted prices cover.
- Save any changes to the file in an XLSX format.
- Click to Upload the Daily or Monthly File.
- Navigate to and select the saved workbook.
- ClickOpen. The system confirms when the projections are successfully uploaded.
- To overwrite the values, repeat the process.
- After you clickApplyto use the Projections Builder, the Projected Rooms by Month table appears.
- In the first tab,Rooms, enter the expected monthly rooms in the field following the market segment name. The value displays for all months for that market segment.
- Review the monthly totals at the top, ensuring they make sense. If needed, edit values. Complete the projections for all market segments, which are defined in theMarket Segmenttab. If needed, scroll to see all months and market segments.
- ClickSave
- Click theADRtab. The Projected ADR by Month table appears.
- Complete the projected monthly ADR values by market segment and month.If you useComponent Rooms, enter for each Room Class.
- ClickSave.
- Click theDOW Patterntab. The Projected Rooms Pattern by DOW table appears.
- Enter the percentage value for each day of the week. The value in the first field  displays for all days of the week, change any day, as needed. See an example ofhow the system uses your patterns.
- Ensure that the last column with the sum of the percentages equals100%.
Ensure that the last column with the sum of the percentages equals100%.
- Complete the percentage values for all market segments.
Complete the percentage values for all market segments.
- ClickSave. Review your projections. If you want others to review, you can download a monthly file.You can't make changes after this step, so, if needed, make corrections now.
- ClickGenerate. Based on the monthly values and day of week distribution, the system overwrites your monthly projections with a file containing daily projected rooms and revenue (for the dates defined by theStart Dateand theEnd Date.Note:G3 RMScreates this file but doesnotupload it. You do that in the next step.
- Follow the steps toDownload and Upload an Excel Worksheet. Use the worksheet to review the daily projections.Note: The total number of rooms might not match what you entered becauseG3 RMSmakes changes to ensure that rooms projections never exceed capacity.
You can only use this option if your company has a minimum of three similar properties from which it can create projections.
- After you clickApply, the Select Properties window displays.
- If you know which of theAvailable Propertiesyou want to select, continue to step 11. Otherwise, clickFilter By.
- Change theRMS Currency(used byG3 RMSto optimize) from the defaultMy CurrencytoAllif you want to select  properties with different currencies  than the Synthetic Data property.
- The default forSizeis All. Select Range to define the size with a minimum and maximum number of rooms.
- UseDistanceto limit the hotels to those within a certain number of kilometers or miles.
- If your company usesattributes, selectUse Property Attributes.If selected, add the attributes that you want to filter by.ClickView Attributesfor the selected property so that you can chose similar attributes. Attributes that apply to the property display this icon:.G3 RMSselects those attributes, but you can change them.
- If selected, add the attributes that you want to filter by.
- ClickView Attributesfor the selected property so that you can chose similar attributes. Attributes that apply to the property display this icon:.G3 RMSselects those attributes, but you can change them.
- Select theBusiness Mixbetween Transient and Group. For example, to find properties that have between 60 to 70% Transient and 30 to 40% Group.
- Select theADR Rangeat the property level by defining a minimum and maximum value.
- Click toApplyyour filter criteria to the available properties.
- Select theAvailable Propertiesthat you want to use for building projections. Select a maximum of five.Enter a character string in the Search field to filter the list.Select a single property or press Ctrl+click to select multiple properties.Note: You see[Business Mix]and[ADR Range]next to properties that match your selections.G3 RMSdoesn't remove properties that don't match those criteria.
- Enter a character string in the Search field to filter the list.
- Select a single property or press Ctrl+click to select multiple properties.
- Click>to move the 
	 selected properties to theSelected Propertiespane or click>>to add all the properties.G3 RMSdisplays the minimum and maximum number.
- SelectUse Selected Properties for Pattern Configurationif the booking patterns of the properties that you selected are also a good match for the Synthetic Data property. In theBooking Patternstab,G3 RMSfinds the best match from those properties.
- ClickBuild Projections. The suggested projections appear in the Rooms, ADR, and DOW Pattern tabs.
- In the Rooms tab, review and, if needed, change the values for each month and each market segment. Click toSaveyour progress if you want to come back later:Review the totals at the monthly level, for example, theOccupancy %row in the Rooms tab . If you disagree with a month's total value, enter a new value.G3 RMSdistributes the value to all market segments based on the patterns it found in the selected properties.Then review at the market segment level, both by number of rooms and the segment's % share. If you disagree with a market segment's values for all months, enter a new value in the first column to use that number for all months. Then change specific months, if needed.Note: If you disagree with all values, clickto change the filter sections, select different properties and then clickBuild Projectionsagain.
- Review the totals at the monthly level, for example, theOccupancy %row in the Rooms tab . If you disagree with a month's total value, enter a new value.G3 RMSdistributes the value to all market segments based on the patterns it found in the selected properties.
- Then review at the market segment level, both by number of rooms and the segment's % share. If you disagree with a market segment's values for all months, enter a new value in the first column to use that number for all months. Then change specific months, if needed.Note: If you disagree with all values, clickto change the filter sections, select different properties and then clickBuild Projectionsagain.
- ClickSave.
- Repeat your review of the suggested values in theADRand theDOW Patterntab. Ensure you agree with the values before you continue. You can't make changes after the next step.
- ClickGenerate. Based on your monthly values and day of week distribution, the system calculates the daily projected rooms and revenue for each market segment and for each occupancy date defined by theStart Dateand theEnd Date. Note that your monthly projections are erased and you can't change them anymore.
- To review the daily projections, download an Excel worksheet, seedownloading and uploading values.Note: The total number of rooms might not match what you entered becauseG3 RMSmakes changes to ensure that rooms projections never exceed capacity.

## Best Practices

### Select the Correct Dates for Your Projections

The Opening Date is when the first guests occupy your hotel and is the first arrival date for whichG3 RMSforecasts demand. It must be earlier or the same as theNormalization Date. For new hotels, this date is typically in the future. For hotels with guests already in house, the date could be theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..G3 RMSuses the date:
- As the suggestedstart date for your Projections.
As the suggestedstart date for your Projections.
- To warn you of incomplete Synthetic Data configuration when you change dates.
To warn you of incomplete Synthetic Data configuration when you change dates.
- To determine the period from your Projections that it uses when itruns the nextBuild process.
To determine the period from your Projections that it uses when itruns the nextBuild process.
Update this date if the opening date changes for a new hotel, for example, due to construction delays. This way,G3 RMSadjusts the period that it uses from your Projections in the next Build process, resulting in the best possible forecasts and decisions.
This date is the first occupancy date when business displays normal patterns andG3 RMScan useActualsThe occupancy, revenue or ADR that the property achieved, once the day is in the past. Actual occupancy is also called Final Rooms Sold.to forecast demand. To determine this date, imagine that the date is past, and you review its actual occupancy and revenue. Those values match what you expect from similar normal days in the future. For example, if you recently opened or re-branded your property, occupancy and ADR might be negatively impacted. Or your market segment mix might be impacted by one-time discounts. Business patterns are normal only when you no longer see those impacts in theForecast Investigator. Therefore:
- Before that date,G3 RMSignores your property's actual rooms and revenue and uses projected data to forecast future demand.
Before that date,G3 RMSignores your property's actual rooms and revenue and uses projected data to forecast future demand.
- On that date, the system starts using each day's Actual data together with projected data for forecasts.
On that date, the system starts using each day's Actual data together with projected data for forecasts.
The date selection depends on why your property uses Synthetic Data:

##### Newly Opened Property

For a newly opened hotel, you might have offered special discounts to attract business during an early, or soft, opening period. These one-time discounts impact the value, volume, and mix of business. So normal may mean that the achieved occupancy and revenues are not impacted by these discounts anymore, and business is consistent with what you expect in the future. In this scenario, the date is likely in the future, after the soft opening date.

##### Re-branded Property or New System

If your property was already open, and you lost historical data because you switched brands and systems, business may already be normal. In this case, the date is in the past. The date is in the future if business is not yet normal because of a delay in recording all reservations in the new system or because demand is irregular due to a brand transition.
You can load between 365 (minimum required) and 730 days of projections. You can select dates for less than 365 days if you want to download and upload the Excel worksheet more than once. For example, one worksheet for January 1 to June 30 and one for July 1 to December 31.
Note that if you load 730 days of projections,G3 RMSuses only 365 days, beginning with the system date. WhenG3 RMSre-runs the Synthetic Data build, the system uses the next 365 days of projections, beginning with the system date. This also applies if you ask IDeaS to extend the forecast window from the default contracted 365 to 730 days. In that case, the system uses historical and on books business to forecast beyond 365 days, which might not match your expectations. For questions, contact your IDeaS representative.
Here are some scenarios for how to select the dates:

##### Property is open and welcoming guests

If your property is open and already welcoming guests, the Start Date should be the current System Date.

##### Property is not yet open or, it is open and selling rooms, but the first arrival date is in the future

G3 RMSdefaults the Start Date to thefirst date that the property is expecting arrivals.

##### Usable History is Available

Your 365 days of data can be a combination of your projections and, if available, usable history. Usable history means that the first date with normal final data is in the past. The days between that date and theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.count towards the 365 days.
For example, Actual data is available inG3 RMSfrom January 1 to March 31 of this year. You entered February 1, this year, as the first date with normal final rooms sold data, because the month of January did not provide representative data. In this case, your Start Date is April 1 of this year, becauseG3 RMSis missing data from this date. Your End Date is February 1, next year, 365 days after the first date with normal final rooms sold data.
Note that if you move the normalized date (when business patterns are normal) further into the future, you need to extend your projections as well.

### Select How You Enter Projections Based on Your Available Data

Select the option based on your available projections data.

#### Monthly Data

Many of our Synthetic Data clients have monthly, but not daily, projections data by market segment. In that case, enter your monthly values and the day of week patterns, using theProjections Builderor anExcel workbook.
You select 20% for Monday, Tuesday and Wednesday. The four other days are at 10%, so 100% for the week. Your projections for February are for 1,000 rooms. With 28 days or four weeks in the month, that means that each week receives 250 rooms. Of the 250 rooms, each Monday, Tuesday and Wednesday receive 50. Each other day, 25 rooms.
And you select the monthly Projections Builder option if you are part of a company with other similarG3 RMSproperties and want to create projections based on those. Reviewthe stepsfor details.

#### Daily Data

If you have daily projections data available, download the Excel workbook and enter those values.Or, if your property uses RevPlan, download the data in RevPlan.Once complete, import the workbook with the data intoG3 RMS. If you used theProjections Buildertool, use the download function to review the daily values. If needed, make changes in the workbook and upload to overwrite the previous values.

### Create Projections that Replace Historical Data

With a Standard build,G3 RMSuses the available history to calculate theunconstrained demand. With Synthetic Data, your projections replace the history. That means the system uses your projections, and any available history, to simulate the missingactualThe occupancy, revenue or ADR that the property achieved, once the day is in the past. Actual occupancy is also called Final Rooms Sold.data for the past year. The system uses that simulated history, the booking patterns, and on books data for its forecasts and decisions.
And because your projections are only one of several inputs, they shouldnotbe an exact forecast of the upcoming year. Instead, projections should reflect the typical business of a year that you want the system to use for forecasting the upcoming year. For example, don't enter exceptional demand for Special Events in your projections. SeeManage Demand for Special Events with Overridesfor details.

### Manage Demand for Special Events with Overrides

In the Synthetic Data build,G3 RMScreates forecasts based not only your projections, but also on booking patterns and business on books. Thus, the system likely ignores days in your projections when demand greatly differs from normal patterns (day of the week, seasonal). That includes Special Events with exceptional demand.
Let's use a simplified example. Your projections include a Special Event on a Saturday three months from now. You expect higher than normal transient demand for it and include that in your projections for that day. The date is an outlier from other trends, meaning that demand for other Saturdays in the same season is much lower. In that case,G3 RMSlikely forecasts that day lower than your projections, closer to the normal demand for Saturdays.
Therefore, we recommend that you enter normal, not high or low, demand for Special Events in your projections. Next, enter a Special Event for the date. After youCreate and Commit Forecast Groups, monitor and, if needed, override demand.
For a recurring Special Event, create only future, not past, instances. This applies even if the past instance is part of the historical data thatG3 RMSuses to forecast (in other words, even if it occurs after the first date with normal final rooms sold data).
For example, today is June 1 and your projections include the recurringNew Yearâs EveSpecial Event. Your first date with normal final rooms sold data is November 1 of last year. When this year's New Year's Eve happens, last year's instance falls into the historical data that the system uses, after November 1. However, because the future instance is in the period of your projections,G3 RMSlikely ignores the past instance and uses normal demand patterns to forecast this year's instance. Therefore, monitor and, if needed, override the demand for this year's instance.
Once all your future Special Events instances occur after the period of your projections, follow theBest Practices for repeat events.

### Prevent Issues that Cause Import Failures

- No changes to the Property Name and Property ID rows.
- No columns are added, deleted, moved, or renamed.
- No changes to the names and order of tabs.
- The file type is XLSX.
- For daily values:No market segment is missing for a day.Days with room revenue also have rooms sold greater than 0.There are no gaps in dates between the start and end date.
- No market segment is missing for a day.
- Days with room revenue also have rooms sold greater than 0.
- There are no gaps in dates between the start and end date.
- The total projected rooms don't exceed the capacity.
- No rows or cells are blank. Enter 0.00 as placeholders if there are no projected rooms or revenue values for a date.
- No changes in cell formatting for numbers, including no formulas in the cells.

### Review Your Projections

Perform regular reviews inInvestigator - Forecastto ensure that your projections remain accurate. For revenue projections, click the PDF button below for the detailed review process.
By Forecast Group, compare the values for Occupancy On Books and Occupancy Forecast against your projections. If the On Books with the booking patterns align with your projections, the systemâs forecast will likely be close to your projections. If the forecast differs from your projections, consider if you need to change the projections or the booking patterns.
For example, for a date in two months and for Group you projected 30 rooms, five are on books, and the forecast is for 10. That can mean that your projections were too high or that you chose a booking pattern where, two months before arrival, 100% is picked up.
We recommend reviewing the entire period of your projections at least monthly. Depending on your property characteristics, review your immediate booking window more frequently. If you need to change your projections, contact IDeaS support to unlock the tab and to request a re-build.
