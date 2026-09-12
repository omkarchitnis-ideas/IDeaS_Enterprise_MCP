# Ceiling/Floor

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Ceiling-Floor-Transient.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Ceiling-Floor-Transient.htm`
- **Ingestion Date:** `2026-09-11 22:12:32`

---

# Ceiling/Floor

The Ceiling/Floor tab providesG3 RMSwith the minimum and maximum single occupancy prices that you want to sell. The Ceiling value is the highest possible price that you would charge in a high demand period. The Floor value is the lowest price that you are willing to sell.G3 RMSchooses from this range when determining the price.
IfG3 RMShas sufficient data, it can suggest these values, either automatically, or when you clickSuggest. For anyPrice ExcludedRoom Class, you enter the fixed price.

### What Help Do You Need with Ceiling and Floor Values?

- I want to know howG3 RMScalculates the suggested values.
I want to know howG3 RMScalculates the suggested values.
- I want to understand howother factorsimpact the Ceiling/Floor values.
I want to understand howother factorsimpact the Ceiling/Floor values.
- I want to understand the  process ofsharing our pricing strategy withG3 RMSthrough pricing setup.
I want to understand the  process ofsharing our pricing strategy withG3 RMSthrough pricing setup.
- I need to know how to manage my room types that arenot sold publiclyor that rarely sell.
I need to know how to manage my room types that arenot sold publiclyor that rarely sell.
Note: Forindependent products, you define their Ceiling and Floor values separately, but the steps are the same.

## Setup Steps

- Click, thenDecisions, and thenPricing Configuration.
- Click to editthe Primary Priced or Independent product.The Definition page displays.
- Click theCeiling/Floortab.
Before you use Suggest, ensure the Offsets,Supplements,Rounding Rules, Base Room Types, and Special Event setup is correct. Those configurations impact the suggested values.
In this example, it shows how to save the suggested values as a draft. To accept the draft values and replace the values in the Current Configuration tab, clickSave.
Your browser does not support the video tag.
- ClickSuggest. If the Suggest option is not available,enter values manually.The suggestions might take a few minutes, during which you can continue working inG3 RMS.
- After you see a message that the suggestions are ready, click theDrafttab.Review the Ceiling, Floor, and, if applicable, Season values to ensure they meet your business needs. Make changes, if needed. Consider howG3 RMScalculates the suggested values.Note: forPrice ExcludedRoom Classes, no values are suggested, and you enter the fixed price.
- If needed, click Export to Excelto review suggestions on a spreadsheet.
- Continue with any of the following actions:ClickClearto remove all suggestions and enter your own.Clickto delete the Draft completely.ClickSave as Draftto continue your review later.ClickSaveto accept the draft values and replace the values in the Current Configuration tab. The old values are saved as a season. This also deletes the Draft tab.
- ClickClearto remove all suggestions and enter your own.
- Clickto delete the Draft completely.
- ClickSave as Draftto continue your review later.
- ClickSaveto accept the draft values and replace the values in the Current Configuration tab. The old values are saved as a season. This also deletes the Draft tab.
- Enter theCeilingandFloorvalues for each Base Room Type and day of the week:Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.Press theTabkey to navigate to each day of the week to edit each value, if needed.
- Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.
- Press theTabkey to navigate to each day of the week to edit each value, if needed.
- If needed, click Export to Excelto review suggestions on a spreadsheet.
- ClickSave.
- Continue your pricing setup withOffsetsto price other room types within a Room Class differently, if needed.
If you have a complex setup with many seasons, or you manage pricing data for multiple properties in one place, or both, use the upload option.
- Click Export to Excelto download the template with the current values.Note: Importing replaces the old values and you can't recover them.
- Save the workbook to a location on your computer.
- Add the new values or change existing values as needed.For details on entering the data, use the Upload Instructions tab in the Excel file.
- If you made changes, save the modified workbook in an XLSX format.
- Click upload. A warning message displays, clickYesto continue.
- Navigate to and select the saved workbook, then clickOpen.G3 RMSchecks the workbook for data and formatting errors. If the system finds no errors, it displays the imported data. If it finds errors, it cancels the import and tells you which rows have errors. Click the export iconto export the error list. Correct the errors, then re-import the workbook.
If you entered your default pricing setup without suggestions, use the following steps to create optional seasons. For example, during your high demand season, the lowest rate that you want to sell might be higher than during the rest of the year.
- In the Seasons panel, click Add.
- Add aSeason Name. You can refer to this name later if you want to copy a season to create another.
- Type or select theStart Datefor the season. The Start Date must be greater than or equal to the System Date.
- Type or select theEnd Datefor the season. The End Date can be any future date and is not limited by the forecast window.
- Change the defaultCeilingandFloorvalues for each required Base Room Type and day of the week. If you have already created a season, you can also use theCopy Frommenu to copy an existing season's values.Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.Press theTabkey to navigate to each day of the week to edit each value, if needed.
- Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.
- Press theTabkey to navigate to each day of the week to edit each value, if needed.
- ClickSave.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.
WhenG3 RMSsuggests Floor and Ceiling values, it checks and, if needed, creates up to four seasons per year for the next two years where pricing differs from the default values. It also creates a season for each recurring Special Event that had either a higher or a lower pricing structure than normal days. Review and change the season, if needed.
- If necessary, change the selected checkboxes to view onlyPresent  orFuture seasons. Or use thesearch box to filter by name of the season.
- Click Editfor the season that you want to edit.
- Change theSeason Name, if needed.
- Type or select a newStart Datefor the season, if needed. To be changed, the Start Date must be greater than or equal to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
- Type or select a newEnd Datefor the season, if needed. The End Date can be any future date and is not limited by the forecast window.
- Type new Ceiling or Floor values for each day of the week, as needed.
- ClickSave.
You can completely delete a future season (with a Start Date after the System Date). When you delete a current season,G3 RMSsplits the season and deletes only future dates. You can't delete past seasonsâG3 RMSdeletes them based on thedata retention policy.
- Click Deletefor the season that you want to delete.
- ClickOK.
When you change Pricing setup, a sync flagis displayed in the menu bar to indicate that your changes impact the system's forecast and decisions. SeeSyncfor more information.
