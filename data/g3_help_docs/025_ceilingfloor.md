# Ceiling/Floor

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Pricing/Group-Pricing-Ceiling-Floor.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Pricing/Group-Pricing-Ceiling-Floor.htm`
- **Ingestion Date:** `2026-09-11 22:12:24`

---

# Ceiling/Floor

Use the Ceiling/Floor tab to define  the highest and lowest prices that you charge to groups:
- The Ceiling is the highest possible price that you quote to a group for the Base Room Type in a high demand period.
The Ceiling is the highest possible price that you quote to a group for the Base Room Type in a high demand period.
- The Floor is the lowest price that you quote to a group.
The Floor is the lowest price that you quote to a group.
G3 RMSchooses from this price range when selecting the recommended guest room rate for a group. You can set different pricing for exceptional periods, see Setting Up Seasons below.

## Setup Steps

The Ceiling and the Floor values apply at the Base Room Type level. Therefore you must set upBase Room Typesbefore you can define Ceiling and Floor values. You can manually enter or upload the values, or, to save time, link the values to yourPrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration., if needed, adjusting them higher or lower.
In the initial setup,G3 RMSuses the Ceiling and Floor values of your Primary Priced Product. The system does that either automatically or after you click that option, see Use the Values ofthe primary priced productbelow. Review and, if needed, change the values.

#### Impact of changes

Changes to your pricing setup might impact existing saved evaluations. However, the results in saved evaluations don't change unless you run a re-evaluation.

### Accessing Ceiling/Floor

- Click, thenDecisions, and thenGroup Pricing Configuration.
- Click theCeiling/Floortab.

### Use the Values ofthe Primary Priced Product

Select this option if your group Floor and Ceiling values are the same or similar as those ofthe primary priced product. Instead of maintaining both, you manage any changes in theCeiling/Floor tabof Pricing setup andG3 RMSapplies the changes to the group Ceiling and Floor values automatically.
- SelectUse BAR Ceiling/Floor.
SelectUse BAR Ceiling/Floor.
- In the Information window, clickYes.
In the Information window, clickYes.
- If needed, select toAdjust Values, for example, to have the group Floor and Ceiling values 5% below transient values.
If needed, select toAdjust Values, for example, to have the group Floor and Ceiling values 5% below transient values.
- If you selected to adjust values, chooseFixedorPercentage, and enter their values for Ceiling and Floor using either a positive or negative number.
If you selected to adjust values, chooseFixedorPercentage, and enter their values for Ceiling and Floor using either a positive or negative number.
- ClickSave.
ClickSave.

### Upload Values

Use the upload option when you:
- Use the same Ceiling and Floor values forthe primary priced productand Group. Downloadthe primary priced productvalues, then upload the file to Group.
Use the same Ceiling and Floor values forthe primary priced productand Group. Downloadthe primary priced productvalues, then upload the file to Group.
- Have a complex setup with many seasons.
Have a complex setup with many seasons.
- Manage pricing data for multiple properties in one place
Manage pricing data for multiple properties in one place
Follow these steps:
- To download a template with the current values, click Export.Note: Importing replaces the old values and you can't recover them. Save a file with the existing values before editing it.
- Add the new values or change existing values as needed.For details on entering the data, use the Upload Instructions tab in the Excel file.
- Save the modified workbook in an XLSX format.
- Click the upload iconand in the warning message, clickYesto continue.
- Navigate to and select the saved workbook, then clickOpen.G3 RMSchecks the workbook for data and formatting errors. If the system finds no errors, it displays the imported data. If it finds errors, it cancels the import and tells you which rows have errors. Click the export iconto export the error list. Correct the errors, then re-import the workbook.

### Manually Adding or Changing Default Rates

- Enter new or change theCeilingandFloorvalues for each Base Room Type and day of the week:Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.Press theTabkey to navigate to each day of the week to edit each value, if needed.
- Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.
- Press theTabkey to navigate to each day of the week to edit each value, if needed.
- ClickSave.

### Setting Up Seasons

After you enter your default Ceiling and Floor values, you can create optional seasons that override the default values. For example, during your high demand season, the lowest rate that you offer groups may be higher than during the rest of the year.
- Click Addunder Seasons.
- Add aSeason Name. You can refer to this name later if you want to copy a season to create another.
- Type or select theStart Datefor the season. The Start Date must be greater than or equal to the System Date.
- Type or select theEnd Datefor the season. The End Date can be any future date and is not limited by the forecast window.
- Change the defaultCeilingandFloorvalues for each required Base Room Type and day of the week. If you have already created a season, you can also use theCopy Frommenu to copy an existing season's values.Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.Press theTabkey to navigate to each day of the week to edit each value, if needed.
- Enter the Ceiling and Floor values in theValuefield. The value populates each day of the week.
- Press theTabkey to navigate to each day of the week to edit each value, if needed.
- Repeat steps 1 - 5 to add additional seasons, as needed.
- ClickSave.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.

### Editing Seasons

You can edit a future season (with a Start Date after the System Date). When you edit a current season,G3 RMSsplits the season, and you can edit only the future dates. You can't edit past seasons.
- If necessary, change the selected checkboxes to view onlyPresent  orFuture seasons. Or use thesearch box to filter by name of the season.
- Click Editfor the season that you want to edit.
- Change theSeason Name, if needed.
- Type or select a newStart Datefor the season, if needed. To be changed, the Start Date must be greater than or equal to the System Date.
- Type or select a newEnd Datefor the season, if needed. The End Date can be any future date and is not limited by the forecast window.
- Type new Ceiling or Floor values for each day of the week, as needed.
- ClickSave.

### Deleting Seasons

You can completely delete a future season (with a Start Date after the System Date). When you delete a current season,G3 RMSsplits the season and deletes only future dates. You can't delete past seasonsâG3 RMSdeletes them based on thedata retention policy.
- Click Deletefor the season that you want to delete.
- ClickOK.

## Best Practices

### Use Offsets for other Room Types and Occupancy Types

G3 RMSprices all room types within a Room Class at the same level as the Base Room Type level. You can useOffsetsto price other room types within a Room Class differently.

### Include Taxes but Exclude Supplements

If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter the ceiling and floor values inclusive of tax. This applies to all pricing setup  values. ViewEntering and Display of Taxes inG3 RMSfor more information. For example, if the lowest room-only price that you want sell is 100, enter 100 as your floor value. If your tax is 20%, that group floor of 100 includes a tax of 20.
Do not include the cost of non-room supplements, if you enabled supplements inBase Room Typesetup.
