# Best Practices for Mass Restriction Setup

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/BP-Restriction-Configuration-Mass.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/BP-Restriction-Configuration-Mass.htm`
- **Ingestion Date:** `2026-09-11 22:14:57`

---

# Best Practices for Mass Restriction Setup

## Follow the Best Practices for Restriction Setup

The same considerations apply for setting up rate plans when using the exported workbook as when you complete the process within the system. We recommend that you review thebest practices for Restriction setup, regardless of the setup method that you choose.

## Do Not Change the Template Format

- The first row of the file must contain the header names exactly as they appear when you export the workbook. Do not change this content.
- Do not change cell formatting.
- Do not change the order of the columns or remove columns.
- Do not change the name of the Restriction setup worksheet tab.
- The Property ID must be present on every row containing rate plan data.
- The second column (B) contains the Property Name for the property from which you exported the workbook. Do not edit this information.
- The first column (A) contains the Property ID for the property from which you exported the workbook. Do not edit this information.
- The file type must remain .xlsx.
- Do not add blank rows in the worksheet.The RMSconsiders a blank row to be the end of the data.
- You can add additional worksheets for your data and calculations at the end of the workbook.The RMSwill ignore worksheets that you create, so you do not need to remove them before you import your data.
- The RMSreads all data below the yellow highlighted column headers when you import the data. Do not add extra data or calculations in these columns.
- You can add new columns on the right side of the worksheet columns.The RMSignores them when you import your data.

## Add Correct Data

- Use the drop-down menus to choose valid settings.
- Date fields must contain dates entered in "dd-mmm-yyyy" format, for example, "25-Jun-2020."
- You cannot have duplicate records (no duplicate rate plans or room types within a season for a specific day of week).
- You can't enter zero when you use fixed values.
- Modifying the Plan Start Date and Plan End Date will affect any decisions that have already been produced for dates prior to the new start date and dates after the new End Date. New decisions will not be produced for these periods until the next optimization.
- In the worksheet, new seasons within the same rate plan cannot have overlapping start and end dates.
- If you add a new season with dates that overlap a season existing in the system,the RMSadjusts the dates of the existing season to accommodate the new season, following these rules:When the new season falls within the date range of an existing season, the existing season is split into two seasons, with the new season falling in the middle and date ranges adjusted accordingly. The rates by room type for the split season are maintained.When you set a start date for a new season to include dates at the end of an existing season, the existing season is adjusted to end on the date prior to the start date of the new season.When a new season includes all the dates of an existing season, the new season replaces the existing season.
- When the new season falls within the date range of an existing season, the existing season is split into two seasons, with the new season falling in the middle and date ranges adjusted accordingly. The rates by room type for the split season are maintained.
- When you set a start date for a new season to include dates at the end of an existing season, the existing season is adjusted to end on the date prior to the start date of the new season.
- When a new season includes all the dates of an existing season, the new season replaces the existing season.
- Seasons that only have past dates cannot be changed.
- You cannot change the start date for a rate plan to be before the currentSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
- Seasons  must fall within the dates of their rate plan.
- You cannot delete rate plans using this worksheet. If you delete rows, the removed rate plans will not change in the system. You can delete the rows in the worksheet for any rate plans that you do not wish to edit.
- Any rate plans updated using this tool will be marked as "Ignore PMS/CRS Updates." If your primary inbound integration provides rate plan updates tothe RMS, your rate plan setups will not be overwritten. You will manage all Restriction setup withinthe RMSonly.
