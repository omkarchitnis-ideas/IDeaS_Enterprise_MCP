# Best Practices for Setting Up My Forecast

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Budget-Forecast/BP-My-Forecast.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Budget-Forecast/BP-My-Forecast.htm`
- **Ingestion Date:** `2026-09-11 22:14:22`

---

# Best Practices for Setting Up My Forecast

## If Possible, Enter the Data at the Property Business View Level

### Understand How Property Business Views Help You

To enter the budget or My Forecast at the Property Business View level, you need to first set up yourProperty Business Views. Unlike Forecast Groups, whichthe RMScreates from your market segments for analytical purposes, you set up Property Business Views based on your business needs and how you want to view your data inthe RMS. Group your market segments the same way that you group them when you prepare your budget and forecast. Then, add your budget or forecast data for each Property Business View.

### If Needed, Resolve Errors in Property Business Views

A warning icondisplays at the top of the page if all your market segments inthe RMSare not assigned to a Property Business View or you have a Property Business View with no market segments. Unassigned market segments mean that you could see an incorrect comparison between Property Business View data and other data within the system that includes that market segment data. For an accurate data comparison, be sure you assign all market segments inthe RMSto a Property Business View.

## Select the Entry Method That Is Best For You

### When to Use the  Table

The table is the best option if you prepare your budget or forecast data as a summary total by month or week, not for each occupancy date.  In the table, you can enter the data at a monthly, fiscal period, or weekly level. The table includes a feature to distribute the data from months to weeks and days, then change the data for specific dates, if needed. As soon as you save the data, you can view it by day in dashboards and reports.
If you upload daily budget or forecast data using the Excel template, the table summarizes it to show weekly and monthly totals. If needed, you can use the table in the system to edit your uploaded values.

### When to Use the Template

If you define your budget or forecast data by day, you can import an Excel workbook with that data.
Begin by selecting the dates and exporting the template. Upload the completed workbook after you add your data. You can add to or change imported data by exporting a new workbook or by using the table in the system.

### With RevPlan, Send the Data toG3 RMS

If your property uses RevPlan, use the Export option there (under Admin click Submission, then Schedule) to update the Budget and Forecast data inG3 RMS. To use the Export from RevPlan you must:
- Enable Budget and My Forecast.
- Define both at the Business View level.
Note: If  the names of your Property Business View don't match  the Market Segment PMS description names in RevPlan, you map them in RevPlan. To ensure matching names you can also  use theAuto-Createoption.

## Fix the Issues that Cause Upload Errors

### Include Valid Data

- Rooms values are whole numbers. Revenue values include up to two decimal places.
- The date column must include valid dates.
- No rows are incomplete. Each occupancy date must have both rooms and revenue. Add "0" as a placeholder, if needed.
- For Business Type: use only Transient and Group and include each once for each occupancy date.
- For Business View:In the Business View column, use only names from the Property Business View page.Include each Business View only once for each occupancy date.
- In the Business View column, use only names from the Property Business View page.
- Include each Business View only once for each occupancy date.
- The sum of the rooms for all Business Views does not exceed the property's physical capacity for an occupancy date.

### Don't Change the Template Columns

- The column order and titles for columns A-E are the same as in the original, exported template.
- The Property ID has not changed and matches the property to which the file is being uploaded.
- If needed for your own work, you can enter data on other columns or worksheets in the My Forecast workbook that do not contain template data.The RMSignores this extra data when you import the workbook.
