# Ancillary Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Pricing/Group-Pricing-Ancillary-Revenue.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Pricing/Group-Pricing-Ancillary-Revenue.htm`
- **Ingestion Date:** `2026-09-11 22:12:23`

---

# Ancillary Configuration

If you have ancillary spend data,G3 RMScan use this information for better evaluation results. See theBest Practicesfor the required data. If you have this data, define the values for each Ancillary revenues stream by market segment and to set their profit percentage.
If you are using Function Space rather than Group Pricing, seeFunction Space Ancillary setup.

### What Are Ancillary Revenue Streams?

Ancillary Revenue Streams are additional sources of income that both transient guests and groups can generate, such as restaurant, golf, spa and entertainment. On the Ancillary tab in Group Pricing setup, you define the different Ancillary Revenue Streams and the percentage of profit that your property generates from each.
After you set up Ancillary Revenue Streams, you can create a year-round or seasonal assignment or a combination of both to associate the Ancillary Revenue Streams to specific market segments and dates. For example, a Transient Leisure Market Segment may spend $40 per night at the hotel bar during the two peak months of the year, but only $20 the rest of the year. In that case, set up a $20 year-round assignment and add a season with $40 for the two peak months.

### How DoesG3 RMSUse Ancillary Revenue Streams?

Ancillary Revenue Streams helpG3 RMSgenerate more realistic evaluations, because they provide the system with a better picture of the overall value of a group versus the value of any displaced business.G3 RMSuses ancillary revenue and its associated profit margin to calculate the additional revenue and profit contribution from the group. For example, a group that has meal packages and meetings likely brings more profit than a group that has only accommodation. However, if this group business replaces an equal amount of room revenue from other market segments that generate higher combined profits at your restaurant, bar and spa, you might not want to accept the group.
G3 RMSaccounts for a group's ancillary revenue and its associated profit margin when calculating both the break-even and recommended rates in an evaluation. If a group brings in a higher ancillary profit, you might observe a lower required Break Even and Recommended Rate due to the overall contribution to revenue and profitability from the group.

## Setup Steps

### Accessing the Ancillary tab

- Click, thenDecisions, and thenGroup Pricing Configuration.
- Click theAncillarytab.

### Adding Ancillary Revenue Streams

Use the Ancillary Revenue Streams pane to set up all your property's ancillary revenue streams. You must add these before you can add Ancillary Assignments.
- Click to Adda revenue stream.
- Enter a unique name for theRevenue Stream.
- Enter theProfit %value for the stream. This value is the average percentage of profit  that your property generates from the revenue stream. Its calculation varies, but, if needed, a finance department usually can provide you with this data.
- Click Save.

### Adding Ancillary Assignments by Season

After you set up Ancillary Revenue Streams, you create a year-round  Ancillary Assignment and, if needed, seasonal exceptions of the year-round values. For example, a room from a Transient Leisure market segment spends $40 per night at the hotel bar during the two peak months of the year, but only $20 the rest of the year. In that case, set up a $20 year-round assignment and add a season with $40 for the two peak months.

#### Setting Up Year-Round Values

- If you prefer not to see the revenue streams, close the Ancillary Revenue Streams pane by clicking the toggle icon. Doing so will  enlarge theAncillary Assignments by Seasonpane.
- Click to openYear-round.
- Click to Edit.
- Select aMarket Segmentfor the Ancillary Assignment.
- Select aRevenue Streamfor the Ancillary Assignment.
- ClickAdd.
- Enter theRevenue per Room Nightthat you expect a room from this Market Segment spends on this Revenue Stream per night.
- ClickApply.
- Repeat steps 3 - 10 to add more Ancillary Assignments.
- ClickSave.

#### Setting Up Seasonal Values

- If you prefer not to see the revenue streams, close the Ancillary Revenue Streams pane by clicking the toggle icon. Doing so will  enlarge theAncillary Assignments by Seasonpane.
- Click Addin the Seasons pane.
- Type or select aStart Datefor the season. The date must be greater than or equal to the System Date.
- Type or select anEnd Datefor the season. The End Date can be any future date and is not limited by the forecast window.
- Select aMarket Segmentfor the Ancillary Assignment.
- Select theRevenue Streamfor the Ancillary Assignment.
- ClickAdd.
- Enter the averageRevenue per Room Nightthat you expect a room from this Market Segment spends on this Revenue Stream per night.
- Repeat steps 5 - 8 to add more Market Segment and Revenue Stream combinations for the same season.
- ClickApply.
- Repeat steps 2 - 10 to add additional seasons.
- ClickSave.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.

### Editing Ancillary Revenue Streams

Changes to the Profit % apply to new evaluations. You must re-evaluate saved evaluations if you want to incorporate these changes.
- Click Editfollowing the revenue stream that you want to change.
- Enter a new name for theRevenue Stream, if needed.
- Enter a newProfit %value for the stream, if needed. This value is the average percentage of profit for each day of stay that your property generates from the revenue stream. Its calculation varies, but, if needed, a finance department usually can provide you with this data.
- Click Save.

### Deleting an Ancillary Revenue Stream

You cannot delete an Ancillary Revenue Stream if you use it in Ancillary Assignments by Season. To delete these streams, you must first remove them from the seasons.G3 RMSremoves deleted Ancillary Revenue Streams from existing saved evaluations only if you re-evaluate the group.
- Click Deletefollowing theRevenue Streamthat you want to delete. A confirmation window displays.
- ClickOK.

### Editing Ancillary Assignments by Season

You can edit an Ancillary Revenue Season if the End Date for the season is in the future, or equal to or greater than the System Date. However, if you update a season in which the Start Date is in the past,G3 RMSsplits it into two seasons. The first season includes all past dates, and the second season includes the System Date until the End Date. The past season retains its Market Segment and Revenue Stream information, and you can change the values in the new season. You cannot edit seasons that are completely in the past, where the End Date is less than the System Date.
- If you prefer not to see the Revenue Streams, close the Ancillary Revenue Streams pane by clicking the toggle icon. Doing so will  enlarge theAncillary Assignments by Seasonpane.
- Click  to openthe year-round or season that you want to edit.
- Click Edit.
- Type or select a newStart Datefor a defined season, if needed. To be changed, the Start Date must be greater than or equal to the System Date
- Type or select a newEnd Datefor a defined season, if needed. The End Date can be any future date and is not limited by the forecast window.
- If needed, create new Market Segment and Revenue Stream associations:Select aMarket Segmentto associate with the Revenue Stream.Select theRevenue Streamto associate with the Market Segment.ClickAdd.Enter the averageRevenue per Room Nightthat you expect a room from this Market Segment spends on this Revenue Stream per night and in this season.
- Select aMarket Segmentto associate with the Revenue Stream.
- Select theRevenue Streamto associate with the Market Segment.
- ClickAdd.
- Enter the averageRevenue per Room Nightthat you expect a room from this Market Segment spends on this Revenue Stream per night and in this season.
- Edit the averageRevenue per Room Nightfor existing assignments, if needed.
- ClickApply.

### Deleting an Ancillary Assignment by Season

You can delete a Market Segment and Revenue Stream assignment within a season, or delete an entire defined season, including all Market Segment and Revenue Stream assignments within it. You can't delete the Year-round season in its entirety.
- If you prefer not to see the Revenue Streams, close the Ancillary Revenue Streams pane by clicking the toggle icon. Doing so will  enlarge theAncillary Assignments by Seasonpane.
- Click to openthe year-round or defined season.
- Click Edit.
- To delete a Market Segment and Revenue Stream association for the season, click Deletefollowing in the appropriate row.
- To delete an entire defined season, clickDelete. A confirmation window displays. ClickYes.

## Best Practices

### Ensure You Have Data by Market Segment

Only set up Ancillary Revenue Streams if you have data on average spend by market segment for ancillary revenue streams. You need that data to set up Ancillary Assignments by Season. Without that data you can't give the system a balanced view of the total value of the displaced business. Therefore, if you don't have that spend data by market segment, we suggest you skip this setup altogether.

### Set Up  Ancillary Assignments by Season

Without Ancillary Assignments by Season setup by market segment,G3 RMSonly uses room revenue when calculating the value of displaced transient business. Thus, the balance in an evaluation may be swayed in the groupâs favor, particularly when it has a high ancillary contribution.
If you set up assignments for group market segments,G3 RMSuses those values as default entries when you enter an evaluation, so you only need to review and, if necessary, modify the value.
