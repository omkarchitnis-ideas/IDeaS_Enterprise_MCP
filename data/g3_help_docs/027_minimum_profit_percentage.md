# Minimum Profit Percentage

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Pricing/Group-Pricing-Minimum-Profit.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Pricing/Group-Pricing-Minimum-Profit.htm`
- **Ingestion Date:** `2026-09-11 22:12:25`

---

# Minimum Profit Percentage

Use Minimum Profit Percentage to define a profit value that a group must meet when you run an evaluation. For example, if your property has heavy group demand, you might only want to accept groups that  result in a Net Profit of 20% or greater.
You can vary the profit value by day of week and by  days to arrival. If needed, you can create seasons in which the profit values override the default values. For example, during your high demand season, you set a higher minimum profit percentage than during the rest of the year.

### Run of House Evaluation Constraint

G3 RMSapplies minimum profit percentages only to Run of House evaluations. To meet a minimum profit for Room Class evaluations, use Adjust Evaluation Results.

### HowG3 RMSApplies Minimum Profit Percentages

For a multiday evaluation with different minimum profit percentages by day of the week,G3 RMSuses a weighted average based on the number of rooms by day.
Note that an adjusted recommended rate can exceed the Ceiling value defined inCeiling/Floor.

### Group Evaluation Results

In the evaluation results you can see the following:
- If the recommended rate results in a Net Profit percentage equal to or greater than the minimum profit percentage that you set up, the evaluation results display as:Acceptable Rate.
- IfG3 RMSadjusts the rate to achieve the minimum profit percentage, the results display as:Rate has been adjusted to meet the minimum profit threshold. The same status displays if the rate exceeds the group pricing Ceiling.

## Setup Steps

### Accessing Minimum Profit Percentages

- Click, thenDecisions, and thenGroup Pricing Configuration.
- Click theMinimum Profit Percentagetab.

### Adding Minimum Profit Percentages

- ClickConfigure Days to Arrivalto set the days to arrival ranges.
- In the Days to Arrival Configuration window, define the ranges of days to arrival in which you want to enforce specific minimum profit percentages. Select one of two options:SelectFull Forecast Windowto enforce the same minimum profit percentages for the entire Forecast Window, and clickApply.ClickAddto add days to arrival ranges. You can define up to four ranges. Enter anEnd Dayvalue to specify the cut-off day for each range. For example,  add the End Days of 30, 60 and 90 for days to arrival ranges of 0-30, 31-60, 61-90 and 91+.
- SelectFull Forecast Windowto enforce the same minimum profit percentages for the entire Forecast Window, and clickApply.
- ClickAddto add days to arrival ranges. You can define up to four ranges. Enter anEnd Dayvalue to specify the cut-off day for each range. For example,  add the End Days of 30, 60 and 90 for days to arrival ranges of 0-30, 31-60, 61-90 and 91+.
- In theValuecolumn, type a minimum profit percentage for each Days to Arrival range. The value must be between 0 and 100. The value displays for each day of the week.
- Edit the minimum profit percentage for each day of week, as needed.
- ClickSave.

### Adding Seasons

- Click the add icon.
- Add aSeason Name. You can refer to this name later if you want to copy a season to create another.
- Type or select theStart Datefor the season.
- Type or select theEnd Datefor the season.
- Change the minimum profit percentages for each Days to Arrival range and day of the week, as needed. If you already created a season, you can also use theCopy Frommenu to copy the values from an existing season.
- ClickApply.
- Repeat the steps as needed to add additional seasons.
- ClickSave.
