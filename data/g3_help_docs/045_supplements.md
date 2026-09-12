# Supplements

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Supplements.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Supplements.htm`
- **Ingestion Date:** `2026-09-11 22:12:37`

---

# Supplements

Supplements are non-room elements, such as breakfast, that are included in the price of yourprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.or, if used, of yourindependent products. If your property uses supplements, enter their values in this tab to ensure thatG3 RMSknows the true value of the room revenue. If you don't use supplements, skip this tab.

### What Help Do You Need with Supplements?

- I want to learn about theBest Practicesfor how to use supplements.
I want to learn about theBest Practicesfor how to use supplements.
- I need to seescenariosfor howG3 RMSuses Supplements and Offsets to calculate the Final Price.
I need to seescenariosfor howG3 RMSuses Supplements and Offsets to calculate the Final Price.
- I need an overview on how to share my price strategy withG3 RMSinPricing Configuration.
I need an overview on how to share my price strategy withG3 RMSinPricing Configuration.

## Setup Steps

When you change existing supplement values, the changes take effect for all future pricing decisions after the next processing. And changing existing or setting up the initial supplements impacts  the suggested Ceiling/Floor values. Thus, update supplements first, then ask the system to suggest new Ceiling/Floor values.
- Click, thenDecisions, and thenPricing.
- Click to editthe product.
- Click theSupplementstab.
Enter a new or edit an existing supplement value for each room type, occupancy type and day of the week combination. If you have many room types, use theRoom Class Searchto jump to the one that you want to change:
- Select aSupplement Method:Fixed:G3 RMSuses the specific supplement value that you enter.Percentage:G3 RMScalculates the supplement as a percentage of the Optimal Price.
- Fixed:G3 RMSuses the specific supplement value that you enter.
- Percentage:G3 RMScalculates the supplement as a percentage of the Optimal Price.
- Enter the supplement cost in theValuefield. The cost populates each day of the week.
- Press theTabkey to navigate to each day of the week to edit the cost, if needed.
- ClickSave.
- Review that your setup is correct. If necessary, click the Export to Excelicon and review on a spreadsheet.
- Click Addin the Seasons pane.
- Add aName. You can refer to this name later if you need to copy a season to create another.
- Type or select theStart Datefor the season. The Start Date must be greater than or equal to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
- Type or select theEnd Datefor the season. The End Date can be any future date and is not limited by the forecast window.
- Select theSupplement Method, Fixed or Percent.
- Enter the supplement value for each room type, occupancy type and day of the week. You can alsoCopy Fromthe values of an existing season or the default.Enter the supplement cost in theValuefield. The cost populates each day of the week.Press theTabkey to navigate to each day of the week to edit the cost, if needed.
- Enter the supplement cost in theValuefield. The cost populates each day of the week.
- Press theTabkey to navigate to each day of the week to edit the cost, if needed.
- ClickApply.
- Repeat the steps to add additional seasons, as needed.
- ClickSave.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.
- Click Editfor the season that you want to edit.
- Change theSeason Name, if needed.
- Type or select a newStart Datefor the season, if needed. To be changed, the Start Date must be greater than or equal to the System Date.
- Type or select a newEnd Datefor the season, if needed. The End Date can be any future date and is not limited by the forecast window.
- Type new supplement values for the required room type, occupancy type and day of the week, as needed
- ClickApply.
You can completely delete a future season (with a Start Date after the System Date). When you delete a current season,G3 RMSsplits the season and deletes only future dates. You can't delete past seasonsâG3 RMSdeletes them based on thedata retention policy.
- Click Deletefor the season that you want to delete.
- ClickOK.
- ClickSave.
