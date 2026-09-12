# Offsets

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Offsets.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Offsets.htm`
- **Ingestion Date:** `2026-09-11 22:12:35`

---

# Offsets

For pricing theBase Room TypeThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.of each Room Class,G3 RMSuses the price range from the Ceiling/Floor tab. It uses Offsets to calculate the pricing for:
- Other room types that are in the same Room Class as the Base Room Type.
Other room types that are in the same Room Class as the Base Room Type.
- Other occupancy types, like extra adults, for all room types (if priced differently).
Other occupancy types, like extra adults, for all room types (if priced differently).
You can vary offsets by room type, by day of week, by season, and they can be a fixed amount or a percentage.G3 RMSadds them cumulatively to the Base Room Type value.
For Price Excluded Room Classes, you enter offsets differently. Seethis step.
For Group Pricingor Function Spaceevaluations, the offsetsof the primary priced productdefine how much the recommended rate for non-base room types differs from the recommended rate of the base room type.G3 RMSuses the offsets for the group's arrival date to determine the recommended rate.
Note:G3 RMSuses Offsets only for Room Class, not Run-of-House evaluations.

### What Help Do You Need With Offsets?

- I need to view thestepsto set up Offsets.
I need to view thestepsto set up Offsets.
- I want to learn about thebest practicesfor how to use Offsets.
I want to learn about thebest practicesfor how to use Offsets.
- I need to seescenariosfor howG3 RMSuses  Offsets to calculate the Final Price.
I need to seescenariosfor howG3 RMSuses  Offsets to calculate the Final Price.
- I need an overview on how to share my price strategy withG3 RMSinPricing Configuration.
I need an overview on how to share my price strategy withG3 RMSinPricing Configuration.
- To enable  other Offsets options, like different age groups for children, I need to first set upOccupant Grouping.
To enable  other Offsets options, like different age groups for children, I need to first set upOccupant Grouping.
Note: Forindependent products, you define Offsets separately from the primary priced product Offsets.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click to editthe product.
- Click theOffsetstab.
Offsets impact your suggested Ceiling/Floor values. Before you use Suggest, set up Offsets for the first time or update the existing values.
- For each room typeand occupancy typein a Room Class, select anOffset Method:Fixed:G3 RMSadds the offset value to the Base Room Type price.Percentage:G3 RMScalculates the offset as a percentage of the Base Room Type price.
- Fixed:G3 RMSadds the offset value to the Base Room Type price.
- Percentage:G3 RMScalculates the offset as a percentage of the Base Room Type price.
- Enter the offset value for each room type, occupancy typeand day of the week:Enter the offset value in the first field. The value populates each day of the week.For any room type that you want to price equally to the Base Room Type, leave the default fixed offset with a 0.00 value. If you do not enter any offsets,G3 RMSprices all room types in a Room Class the same.Press theTabkey to navigate to each day of the week to edit each value, if needed.Note: for aPrice ExcludedRoom Class, the Offset Method for the single occupancy of non-Base Room Types isSet. That means that you enter the fixed value instead of an offset value. For example, in the Ceiling/Floor tab, for the Price Excluded Room Class titledSpecialty Suite, you entered 1,000 as the price for the Base Room Type. You charge an extra 200 for the other non-Base Room Type in that Room Class. Therefore, in the Offsets tab you enter 1,200 for single occupancy. For other Occupancy Types you enter the Offsets, not the fixed value.
- Enter the offset value in the first field. The value populates each day of the week.For any room type that you want to price equally to the Base Room Type, leave the default fixed offset with a 0.00 value. If you do not enter any offsets,G3 RMSprices all room types in a Room Class the same.
- Press theTabkey to navigate to each day of the week to edit each value, if needed.
Note: for aPrice ExcludedRoom Class, the Offset Method for the single occupancy of non-Base Room Types isSet. That means that you enter the fixed value instead of an offset value. For example, in the Ceiling/Floor tab, for the Price Excluded Room Class titledSpecialty Suite, you entered 1,000 as the price for the Base Room Type. You charge an extra 200 for the other non-Base Room Type in that Room Class. Therefore, in the Offsets tab you enter 1,200 for single occupancy. For other Occupancy Types you enter the Offsets, not the fixed value.
- ClickSave.
- Check that your setup is correct. If necessary, click the Export to Excelicon and review on a spreadsheet.
Use the upload option if you have a complex setup with many seasons, or you manage pricing data for multiple properties in one place, or both.
- Click Export to Excelto download the template with the current values.Note: Importing replaces the old values, and you can't recover them.
- Save the workbook to a location on your computer.
- Add the new values or change existing values as needed.For details on entering the data, use the Upload Instructions tab in the Excel file.
- Save the modified workbook in an XLSX format.
- Click upload. A warning message displays. ClickYesto continue.
- Navigate to and select the saved workbook, then clickOpen.
G3 RMSchecks the workbook for data and formatting errors. If the system finds no errors, it displays the imported data. If it finds errors, it cancels the import and tells you which rows have errors. Click the export iconto export the error list. Correct the errors, then re-import the workbook.
If you set up optional seasons, they override the default Offsets. For example, you want higher offsets during your high demand season.
- In the Seasons pane, click Add.
- Add aName. You can refer to this name later if you need to copy a season to create another.
- Enter or select theStart Datefor the season. The Start Date must be greater than or equal to the System Date.
- Enter or select theEnd Datefor the season. The End Date can be any future date and is not limited by the forecast window.
- Enter the offset value for any room type, occupancy typeand day of the week that differs from the defaults. Leave those fields empty that are the same as the default. You can alsoCopy Fromthe values of an existing season or the default.Enter the offset values in the first field. The value populates each day of the week.For any room type that you want to price equally to the Base Room Type, leave the default fixed offset with a 0.00 value. If you do not enter any offsets,G3 RMSprices all room types in a Room Class the same.Press theTabkey to navigate to each day of the week to edit each value, if needed.
- Enter the offset values in the first field. The value populates each day of the week.For any room type that you want to price equally to the Base Room Type, leave the default fixed offset with a 0.00 value. If you do not enter any offsets,G3 RMSprices all room types in a Room Class the same.
- Press theTabkey to navigate to each day of the week to edit each value, if needed.
- ClickApply.
- Repeat the steps to add additional seasons, as needed.
- ClickSave.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.
- Enter a new offset value for the required room type, occupancy typeand day of the week. If you have many room types, use theRoom Class Searchto jump to the one that you want to change.
- ClickSave.

#### Impact of Editing Seasons on Pricing Decisions

When you change offsets, the system detects the differences in the resulting price and delivers only those that have changed. Therefore,G3 RMSonly pushes new room type prices tointegrated selling systems.
For example, if you change only the 1 Adult offset for all room types,G3 RMSsees only a change in the 1 Adult values (and subject to setup, possibly changes to the 2 Adult values as well) for all room types.G3 RMSonly sends the price changes impacted by the setup  change tointegrated systemsat the next scheduled decision upload, in addition to any other changes as a result of optimization.

#### Impact on Saved Evaluations

Changesto your pricing setup might impact saved group evaluations, but the results in saved evaluations only change if you run a re-evaluation.
- If necessary, change the selected checkboxes to view onlyPresent orFuture seasons.
- Click Editfor the season that you want to edit.
- Change theSeason Name, if needed.
- Enter or select a newStart Datefor the season, if needed. To be changed, the Start Date must be greater than or equal to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
- Enter or select a newEnd Datefor the season, if needed. The End Date can be any future date and is not limited by the forecast window.
- Enter new offset values for the required room type, occupancy typeand day of the week.
- ClickApply.
You can completely delete a future season (with a Start Date after the System Date). When you delete a current season,G3 RMSsplits the season and deletes only future dates. You can't delete past seasonsâG3 RMSdeletes them based on thedata retention policy.
- Click, thenDecisions, and thenPricing.
- Click to editthe product.
- ClickOffsets.
- Click Deletefor the season that you want to delete.
- ClickOK.
- ClickSave.
When you change Offsets, a sync flagin the top right indicates that the changes impact the forecast and decisions. SeeSyncfor more information.
Note: If you change your offset values,G3 RMSignores theMinimum Change Valueand updates and sends any pricing decisions that changed as a result of the new pricing setup .
