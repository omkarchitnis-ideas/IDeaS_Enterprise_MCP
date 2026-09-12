# Forecast Groups

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Market-Segments/Market-Segments-Forecast-Groups-Configure.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Market-Segments/Market-Segments-Forecast-Groups-Configure.htm`
- **Ingestion Date:** `2026-09-11 22:12:29`

---

# Forecast Groups

Use this tab for the last step ofMarket Segmentssetup, when you Create and Commit Forecast Groups  andG3 RMScreate forecasts and decisions for you. It includes these steps:
- Create Forecast Groups.G3 RMScombines market segments into Forecast Groups, based on attributesandbooking patterns. For example, two market segments with the same attributes are in two different Forecast Groups because of their booking patterns. One books much earlier than the other.
- Review Forecast Groups. In rare cases you might make changes. For example, if you assigned incorrect attributes to a market segment, or for low volume market segments that you are certain belong in a different Forecast Group.
- Commit Forecast Groups.G3 RMSstarts a full optimization and goes into Read Only mode. After the optimization completes, forecasts and decisions display in the system.
- Rename Forecast Groupsto a name that's meaningful to you.
You can alsoview this courseabout how to create and commit your Forecast Groups.

## Steps to Set Up Forecast Groups

### Creating Forecast Groups

- Click, thenForecasts, and thenMarket Segments.
- Click theForecast Groupstab.
- ClickCreate Forecast Groups.
- Check the system's setup message. It confirms that you meet the required criteria for creating Forecast Groups. All criteria in the confirmation message must show a check mark icon.
- ClickCreate Forecast Groupsto continue if you meet the criteria.
- ClickCancelif you didn't meet the criteria, then correct the issues.Note: There are issues that you can't correct. For example, ifG3 RMSlacks historical or pace data, it needs more time to get enough data.
The process of creating Forecast Groups can take several minutes. When it completes, a list of the Forecast Groups displays in the left pane of the Forecast Groups tab. Newly created Forecast Groups are flagged with a check mark icon. The Market Segment number indicates how many market segments the system included in the Forecast Group.

### Resolving Unapproved Forecast Group Alerts

After your Forecast Groups are created,G3 RMSgenerates anUnapproved Forecast Group Alertin Information Manager. It  informs you that you need to commit the Forecast Groups. The Alert includes a link to the Forecast Groups tab.

### Reviewing Forecast Groups

G3 RMScreates the best possible Forecast Groups, based on the attributes and a pattern analysis. You can't validate the systemâs complex pattern analysis, so typically you commit the system-proposed Forecast Groups.But in some cases you might know something that the system doesn't, so look for the following:
- Check that you correctly assigned attributes to market segments.
- Review low volume market segments.

### Checking Market Segment Attributes

- Select each Forecast Group in the left pane.
- Verify its market segments, displayed in the right pane.
- If the market segments in a Forecast Group don't make sense, check if they have an incorrect attribute. If so, click toReject FGs(Forecast Groups). Correct the attributes in theMarket Segmentstab. Then, click to againCreate Forecast Groups.

### Reviewing Low Volume Market Segments

Look for Forecast Groups that are flagged with a low volume icon.
This icon indicates that the Forecast Group contains low volume market segments. For those,G3 RMScan't make strong recommendations. Due to the low volume of bookings, the analysis of patterns is difficult. In this case, the system selects the most logical Forecast Group based on the available information.
Ideally, you have few low volume market segments. If you have many, it's likely because you split many market segments and the splits don't have enough business, seeclean and dirty market segmentsfor details.
We recommend that you leave low volume market segments in the suggested Forecast Group. Note these exceptions:
- You changed the names of your market segments. And you have a "new" and an equivalent "old" market segment in different Forecast Groups. In that case, the old and new market segments should be in the same Forecast Group.
- You have a very new market segment with few bookings so far.  And you know that the new market segment will behave very similarly to another market segment which is in a different Forecast Group. In that case, you can move it.
Note: The low volume icon does not appear for market segments with the Forecast Type of "None" or "Wash". The same applies to market segments attributed asEqual to BARattribute.

### Moving Low Volume Market Segments

- Select a Forecast Group with the low volume icon. The included market segments and their attributes display in the right pane.
- Click the low volume iconfor the market segment that you want to move. TheMove Market Segment towindow opens.
- You can only move low volume  market segments into Forecast Groups with the same attributes. If Forecast Groups are available, select the one that you want to move the market segment to. If none are available, clickxto close the window.
- ClickSave.

### Committing Forecast Groups

You must commit the Forecast Groups thatG3 RMScreates from your market segments. Otherwise,G3 RMSdoesn't complete the creation of Forecast Groups. That means that it doesn't create forecasts or that they might be inaccurate.
- Click, thenForecasts, and thenMarket Segments.
- Click theForecast Groupstab.
- ClickCommit FGs. A confirmation window opens.
- ClickYesto confirm.
After you commit the Forecast Groups,G3 RMSstarts anoptimizationThe step in the RMS Processing when the system uses the demand forecast (volume and value), the available capacity to sell, your configuration, and your interactions (like events, overrides) to calculate the outputs that maximize your revenues or profits. Outputs include pricing for the primary priced product, LRV, and overbooking. An Optimization also updates the constrained Occupancy Forecast.and goes into Read Only mode. That takes five to ten minutes. After the optimization completes, forecasts and decisions display on the relevant pages. TheCommit FGsbutton is disabled.

### Renaming Forecast Groups

G3 RMScreates default names based on the attributes of the included market segments. For example, Unqual EB for unqualified market segments that have theEqual to BARattribute. Change that to a name that is  meaningful to youand your team, like BAR or Retail.
- Click, thenForecasts, and thenMarket Segments.
- Click theForecast Groupstab.
- Select the Forecast Group 
	 in the left pane.
- Click the edit icon.
- Change the Forecast Group name in the open field. The name can consist of alphanumeric characters and the symbols _ ( )
- Click the save icon.
