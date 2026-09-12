# Market Segments Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Market-Segments/Market-Segments-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Market-Segments/Market-Segments-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:12:28`

---

Why do I set up Market Segments?

# Market Segments Configuration

An optimal setup of Market Segments, together withRoomssetup, is the key foundation for the best possible forecasts and decisions inG3 RMS.

### What Help Do You Need with Setting Up Market Segments?

- Anoverview and why I need to set up market segments.
- For the initial setup:Review the attributes thatG3 RMSassigned to market segments.Assign the attributes to market segments.
- Review the attributes thatG3 RMSassigned to market segments.
- Assign the attributes to market segments.
- Understand howG3 RMSuses Default Market Segments.
- Change the existing setup of market segments.
- Understandwhich behavior each  attribute describes.
- Create and commit Forecast Groups.
- My Market Segments page looks like this(we use Synthetic Data or our reservation system doesn't support splitting market segments):

## Steps

Before you set up market segments
- Know what type of business your market segments contain, for example, if a segment is fixed-priced or derived off a rate code. If needed, learn about your market segments, for example,  corporate texts or thereservation systemmight have that information.
- Become familiar with theattributesthatthe RMSuses to define business.
Click, thenForecasts, and thenMarket Segments.
Setting up market segments follows this workflow:
- Your unassigned Market Segments display in the left panel in one of three tabs: Group Business, Market Segment, or Rate Code Level. Select the checkbox for the market segment.
- Select the attributes to assign to the selected market segment.
- The attributed market segment moves from the left to the right panel, andG3 RMSsaves your work automatically.
The attributed market segment moves from the left to the right panel, andG3 RMSsaves your work automatically.
Select one of the following scenarios. Before you start, familiarize yourself withmarket segment attributes.
IfG3 RMSautomatically assigned attributes to your market segments,  review if the attributes are correct. SeeHow the system assigns attributesfor details.
Note: if you have  fixed price rate codes that change to a discount off  BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) when the BAR price is below the fixed price, first ensure the attributes are correct. Seestep 7. Then define the exact pricing of the rate code in theRate Protecttab.
- Click refresh. Any new market segments that the system finds after it assigned attributes display  in the left pane.
- ClickPreview. TheAttribute Assignment Previewwindow opens.
- In the window, click to export to Exceland save the file. We recommend that you complete the review using the Excel file of the Preview and the Assigned Market Segments pane inG3 RMS.
- To enlarge theAssigned Market Segmentspane, click and drag the linebetween the two panes.
- By default, the Assigned Market Segments pane is sorted by theMarket Segmentcolumn. Click any other column to change the sort order.
- Before you review the assigned attributes, ensure that you understand their definition. Review themarket segment attributes.
G3 RMSsplits market segments where it finds that the patterns of some rate codes differ significantly from others. For example, the system split CORP into two market segments. One for the rate codes whose ADR  is linked to the ADR of theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.. And another for rate codes that have a fixed ADR. You can recognize split market segments because their names are followed by abbreviations, such as CORP_DEF (for default, see step 6) and CORP_QYL (Qualified, Yieldable, Linked).
Note:G3 RMSonly splits market segments if the splits have enough business. Therefore, you might notice a market segment that includes a rate code that you know  behaves differently than the market segment. In that case, the rate code is likely too small to make a difference, soG3 RMSkept it in the market segment. Seeclean vs. dirty market segments. Unless you know the rate code's production will become bigger in the future, such as if it's new, don't split it and keep it in the market segment.
G3 RMSassigns the Forecast Type attribute ofDemand and Washto all market segments. Review the attributes in theAssigned Market Segmentspane. If needed, change the attribute, for example, toWashfor contracted business. SeeForecast Typefor all options and best practices.
- Clickto unassign the attributes for a market segment.
- Click toApply Changes to Past and Future Data.
- The market segment moves to the left pane.
- Continue with your review. You assign attributes to all unassigned market segments at the end of the review. Seestep 7.
IfG3 RMSsees in the data that a market segment's ADR follows that of theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration., it assigns theQualified Non-block Linkedattribute. Change the attribute toUnqualifiedif the business represents public rates that anyone can book.  SeeUnqualified Attributesfor all options and best practices.
- Filter the Excel file of the Preview by Attributes.
- Review the segments whose attributes start with: Transient > Qualified Non-block > Linked.
- For any that should be Unqualified, go toG3 RMSand clickto unassign the attributes.
- Click toApply Changes to Past and Future Data.
- The market segment moves to the left pane.
- Continue with your review. You will assign attributes to all unassigned market segments at the end of the review. Seestep 7.
G3 RMSassigns theYieldableattribute to all Transient Qualified Non-block market segments. Change the attribute if Revenue Management doesn't fully control the availability of a market segment or rate code, such as when a corporate rate code has a Last Room Availability (LRA) contract.  SeeQualified Attributesfor all options and best practices.
- Filter the Excel file of the Preview by Attributes.
- Review the segments whose attributes end with Yieldable.
- For any that should be Semi- or Non-Yieldable, go toG3 RMSand clickto unassign  the attributes.
- Click toApply Changes to Past and Future Data.
- The market segment moves to the left pane.
- Continue with your review. You assign attributes to all unassigned market segments at the end of the review. Seestep 7.
Default market segments ensure that new rate codes of a split market segment receive the correct attributes. SeePurpose of default market segmentsfor details.
- Filter the Excel file of the Preview to view default market segments. Their name ends in _DEF, for example, CORP_DEF.
- Verify that the attributes  are correct for the majority of future rate codes in this market segment.  If not, clickto change  the attribute for a market segment.
- Select the correct attributes.
- ClickAssign.
Assign attributes to all segments in the leftUnassigned Market Segmentspane. If needed, click and drag the line between the two panes to enlarge the left one.
Notes:
- If others at your property also review the market segments, you might want to track changes. ClickAuditat the bottom of the page. SeeDetailsto learn about the displayed data.
- If your rate codes follow a certain naming convention, review howAttribute Assignment Rulescan help save you time.

##### a) Market Segment Level tab

In this tab, assign attributes toclean, or mostly clean market segments, such as the small split market segments that you unassigned instep 6because they have less than 5% of the property volume.
- Review the Occupancy Actual value for the market segment:If it is less than 5% of the total property, assign attributes at the Market Segment Level.If it is more than 5%, click the togglenext to the market segment name to verify that the market segment is clean.
- If it is less than 5% of the total property, assign attributes at the Market Segment Level.
- If it is more than 5%, click the togglenext to the market segment name to verify that the market segment is clean.
- Select the checkboxes for all market segments to which you want to assign the same attributes.
- SelectAttributes. 	Based on common sense rules,G3 RMSlimits you to valid attribute combinations. For example,G3 RMSconsiders all Qualified business as Fenced, so Fenced is not an option for Qualified business. And you can't change the Forecast Type ofDemand and Washfor Unqualified. Point to each attribute to view its definition or refer toMarket Segment Attributes.Note:if the market segment includes  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first verify the attributes (these rate codes should use the Qualified Non-linked attribute, because the pricing is typically fixed more often than linked).  Then define the exact pricing of the rate code in theRate Protecttab.
Note:if the market segment includes  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first verify the attributes (these rate codes should use the Qualified Non-linked attribute, because the pricing is typically fixed more often than linked).  Then define the exact pricing of the rate code in theRate Protecttab.
- ClickAssign. The Assign Attributes window opens to verify your selections.
- ClickOK. The selected market segments move to the Assigned Market Segments pane.G3 RMSassigns the same attributes to future rate codes from the same market segment.

##### b) Rate Code Level tab

After you assigned attributes at the Market Segment Level, the Rate Code Level tab contains Original Market Segments that need to be split because they are larger than 5% of the property volume and because some rate codes need different attributes than others.
By default, the market segments are sorted by their % share of total property business, in descending order. Change the sort order by clicking any other column header. Sorting applies only to market segments, not rate codes. SeeDetailsfor more information about the data displayed in this tab.
- Click the togglenext to the Original Market Segment code to view all the included rate codes.
- Select the checkboxes  for all rate codes to which you want to assign the same attributes.
- SelectAttributes.G3 RMSlimits you to valid attribute combinations. For example,G3 RMSconsiders all Qualified business as Fenced, so Fenced is not an option for Qualified business. And you can't change the Forecast Type ofDemand and Washfor Unqualified.   Point to each attribute to view its definition or refer toMarket Segment Attributes.Note:if you have  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first ensure that it has the Qualified Non-linked attribute (because the pricing is typically fixed more often than linked). Then define the exact pricing of the rate code in theRate Protecttab.
- ClickAssign. The market segment is split and displays with a new name in the right pane. SeeData Detailsfor the naming convention.
- If you are splitting the market segment for the first time, another Assign Attributes window opens. Assign attributes to its Default Market Segment. ReviewUnderstand the Purpose of Default Market Segmentsfor more details. Select the attributes for the likely future rate codes in this segment.
- ClickAssign. The market segments display in the Assigned Market Segments pane.
- After you assign the Default Market Segment, the Assign to default icondisplays next to the original market segment name. Click it to assign the remaining rate codes to  the Default Market Segment. Or repeat steps 1 to 4 to assign different attributes. If you leave any rate codes unassigned,G3 RMSplaces them in the associated Default Market Segment.
If you made any changes in the review,G3 RMSneeds to update the Forecast Groups that are the basis for forecasting. For more information, seeForecast Groups setup.
- Click theForecast Grouptab.
- ClickCreate Forecast Groups.
- The Forecast Groups Validation window opens. The check marksconfirm that you meet the criteria for creating Forecast Groups.
- ClickCreate Forecast Groups.G3 RMSstarts the process, which can take a few moments.
- When completed, a check markmeans that the Forecast Group has changed or is new.
- ClickCommit FGsto commit the changed Forecast Groups. A confirmation window opens.
- ClickYesto confirm.
- In the window, confirm to Create Forecast Groups.
- G3 RMSapplies the changes:If you used the Unassignoption during your review,G3 RMSrebuilds past data and pace. It does that for all market segments and rate codes that are impacted by the change. After the rebuild,G3 RMScreates new Forecast Groups. This can takes about an hour.If you used only the Changeoption,G3 RMScreates new Forecast Groups. This can take several minutes.
- If you used the Unassignoption during your review,G3 RMSrebuilds past data and pace. It does that for all market segments and rate codes that are impacted by the change. After the rebuild,G3 RMScreates new Forecast Groups. This can takes about an hour.
- If you used only the Changeoption,G3 RMScreates new Forecast Groups. This can take several minutes.
You canrename the Forecast Groupsto ensure they are easily understood by you and your team.
You can skip this step if your rate codes don't follow a naming convention. Otherwise, Attribute Assignment rules can save time.
For example, all rates of the corporate market segment CP start with the letters CL or CN. CL is used for LRA (Last Room Availability) rates that are semi-yieldable. CN is for non-LRA rates that are yieldable. Therefore, you split the CP market segment into two  by assigning different attributes at the Rate Code Level.
Create two Attribute Assignment Rules, one for CL and one for CN. In the futureG3 RMSassigns the appropriate attributes to all new rate codes in the CP market segment. When reservations are booked for them,G3 RMSknows if the rate code belongs to the yieldable or the semi-yieldable market segment. You don't have to assign any attributes.
- On the Rate Code Level tab, click theCreate Attribute Assignment Rulelink.
- In the Rule Parameters pane, click theMarket Segmentmenu.
- Select one of the Unassigned Market Segments.
- Select the filter option for the rate code, eitherContains,Ends with, orStarts with.
- Enter the alphanumeric character(s) by which you want to filter.
- ClickFilter. The list of applicable rate codes displays. Verify that the list is correct.
- SelectAttributes. Refer toMarket Segment Attributes.
- ClickCreate Rule. The window closes, and a verification window opens.
- ClickOK. The selected rate codes display in the Assigned Market Segments pane. Click the togglenext to the name of the Mapped Code. The rule displays in the Rate Code column.
IfG3 RMScan't auto-configure the attributes for you, follow these steps to assign the attributes:
- When you first access this page, you need to initialize the market segments list. ClickInitializeto continue. When you return to the page, click the refresh icon. That ensures that all unassigned market segments display in the left pane.
- Assign attributes to the market segments in each of the three tabs following the steps below.Review the definitions forMarket Segment Attributes.You must assign attributes to at least one rate code in each Market Segment. After you have done that, no market segments display in the Group Business Level or Market Segment Level tabs.Market segments are sorted by their percent share of total property business. Start with the largest market segments at the top. They have the biggest impact.Select the checkbox of multiple market segments or rate codes to assign the same attributes to all.
- Review the definitions forMarket Segment Attributes.
- You must assign attributes to at least one rate code in each Market Segment. After you have done that, no market segments display in the Group Business Level or Market Segment Level tabs.
- Market segments are sorted by their percent share of total property business. Start with the largest market segments at the top. They have the biggest impact.
- Select the checkbox of multiple market segments or rate codes to assign the same attributes to all.
- The following shows the decision process for selecting the attributes.Note: if you have  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first assign attributes. See the Notes in theMarket SegmentsorRate Codesteps. Then define the exact pricing of the rate code in theRate Protecttab.
The following shows the decision process for selecting the attributes.Note: if you have  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first assign attributes. See the Notes in theMarket SegmentsorRate Codesteps. Then define the exact pricing of the rate code in theRate Protecttab.
This tab includes all group market segments, so you can assign attributes to them together. SeeDetailsfor more information about the displayed data. You can't split group market segments at the Rate Code Level. At that level,G3 RMSdoesn't receive data to differentiate between room and non-room revenue (for example, if a group rate includes a package or tax).
- Select the market segments to which you want to assign group attributes. Refer toMarket Segment Attributesfor attribute definitions.
- ClickAssign. The Assign Attributes window opens to verify your selections.
- ClickOK. The selected market segments move to the Assigned Market Segments pane.
In this tab, assign attributes to "clean," or mostly clean market segments. SeeClean vs. Dirty Market Segmentsto understand the difference. SeeDetailsfor more information about the displayed data.
- Review the Occupancy Actual value for the market segment:If it is less than 5% of the total property, assign attributes at the Market Segment Level.If it is more than 5%, click the togglenext to the market segment name to verify that the market segment is clean.
- If it is less than 5% of the total property, assign attributes at the Market Segment Level.
- If it is more than 5%, click the togglenext to the market segment name to verify that the market segment is clean.
- Select the checkboxes for all market segments to which you want to assign the same attributes.
- SelectAttributes. 	Based on common sense rules,G3 RMSlimits you to valid attribute combinations. For example,G3 RMSconsiders all Qualified business as Fenced, so Fenced is not an option for Qualified business. And you can't change the Forecast Type ofDemand and Washfor Unqualified. Point to each attribute to view its definition or refer toMarket Segment Attributes.Note:if the market segment includes  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first assign the attribute (these rate codes should be Qualified Non-linked attribute because the pricing is typically fixed more often than linked).  Then, define the exact pricing of the rate code in theRate Protecttab.
Note:if the market segment includes  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first assign the attribute (these rate codes should be Qualified Non-linked attribute because the pricing is typically fixed more often than linked).  Then, define the exact pricing of the rate code in theRate Protecttab.
- ClickAssign. The Assign Attributes window opens to verify your selections.
- ClickOK. The selected market segments move to the Assigned Market Segments pane.G3 RMSassigns the same attributes to future rate codes from the same market segment.
In the first two tabs, assign attributes to group business and to all clean, or mostly clean, market segments. Assign attributes to as many market segments as possible in the first two tabs. Once completed, the Rate Code Level tab contains only dirty market segments. SeeClean vs. Dirty Market Segmentsto understand the difference. SeeDetailsfor more information about the displayed data.
By default, the market segments are sorted by their % share of total property business, in descending order. Change the sort order by clicking any other column header. Sorting applies only to market segments, not rate codes. If your rate codes follow a certain naming convention, review how to createAttribute Assignment Rules.
- Click the togglenext to the Original Market Segment code to view all the included rate codes.
- The link iconmeans that the market segment shares rate codes with other market segments. Point to the linknext to a rate code to see which other market segments contain the same rate code. In most cases, the icon indicates coding issues. For example, the rate code of a reservation was changed, but the market segment was not updated.
- Select the checkboxes  for all rate codes to which you want to assign the same attributes.
- SelectAttributes.G3 RMSlimits you to valid attribute combinations. For example,G3 RMSconsiders all Qualified business as Fenced, so Fenced is not an option for Qualified business. And you can't change the Forecast Type ofDemand and Washfor Unqualified.   Point to each attribute to view its definition or refer toMarket Segment Attributes.Note:if you have  fixed price rate codes that change to a discount off BAR when the BAR price is below the fixed price, first assign the attributes of Qualified Non-linked, because the pricing is typically fixed more often than linked.  Then, define the exact pricing of the rate code in theRate Protecttab.
- ClickAssign. The market segment is split and displays with a new name in the right pane. SeeData Detailsfor the naming convention.Note: if your property usesExtended Stay Forecastingand if a market segment with the same attributes exists,G3 RMSasks you if you want to add this to the existing or create a new market segment. Ensure that you have different market segments for each of your extended stay products. For example, one market segments for all weekly rate codes, one for bi-weekly,  and one for monthly rate codes.
Note: if your property usesExtended Stay Forecastingand if a market segment with the same attributes exists,G3 RMSasks you if you want to add this to the existing or create a new market segment. Ensure that you have different market segments for each of your extended stay products. For example, one market segments for all weekly rate codes, one for bi-weekly,  and one for monthly rate codes.
- If you are splitting the market segment for the first time, another Assign Attributes window opens. Assign attributes to its Default Market Segment. ReviewUnderstand the Purpose of Default Market Segmentsfor more details. Select the most likely attributes for those future rate codes.
- ClickAssign. The market segments display in the Assigned Market Segments pane.
- After you assign the Default Market Segment, click assignafter the market segment. That assigns the remaining rate codes to the Default Market Segment. If you leave any rate codes unassigned,G3 RMSplaces them in the associated Default Market Segment.
Attribute Assignment rules can save time if your rate codes follow a certain naming convention.
For example, all rates of the corporate market segment CP start with the letters CL or CN. CL is used for LRA (Last Room Availability) rates that are semi-yieldable. CN is for non-LRA rates that are yieldable. Therefore, you split the CP market segment into two  by assigning different attributes at the Rate Code Level. Without the Attribute Assignment Rule, you need to manually select all rate codes and assign the appropriate attributes. Instead, create two Attribute Assignment Rules.G3 RMSassigns the appropriate attributes to all rate codes that start with the letters CL and CN.
This functionality also helps you in the future when you create new rate codes in the CP market segment. When reservations are booked for them,G3 RMSknows if the rate code belongs to the yieldable or the semi-yieldable market segment. You don't have to assign any attributes.
- On the Rate Code Level tab, click theCreate Attribute Assignment Rulelink.
- In the Rule Parameters pane, click theMarket Segmentmenu.
- Select one of the Unassigned Market Segments.
- Select the filter option for the rate code, eitherContains,Ends with, orStarts with.
- Enter the alphanumeric character(s) by which you want to filter.
- ClickFilter. The list of applicable rate codes displays. Verify that the list is correct.
- SelectAttributes. Refer toMarket Segment Attributes.
- ClickCreate Rule. The window closes, and a verification window opens.
- ClickOK. The selected rate codes display in the Assigned Market Segments pane. Click the triangle iconnext to the name of the Mapped Code. The rule displays in the Rate Code column.
Review your attribution before you click Finalize. SeeFinalizefor why this is important. Focus on the market segments with a large share of your business. Those have the biggest impact.
The Equal to BAR attribute directly impacts the pricing decisions. Only use it for business that is booked at the value ofthe selected Base Product, by default,BAR. Don't use it for discounted business, such as advance purchase rates.
- ClickPreview, then export the data by clicking the Excel icon. Sort and filter the data, for example, to view all qualified yieldable market segments at once. Use the preview to make sure that each market segment shows the correct attributes. And ensure that their ADR and % share information match your expectations.
- Run theMarket Segment Mapping Reportin the Excel format. Sort and filter the data to verify that rate codes are assigned to the correct market segments. Then sort by attributed market segments. Verify that they contain only rate codes with the same behavior.
- If you need to fix mistakes:
- Click Editfor minor changes, such as to change  the Forecast Type attributes from Demand and Wash to only Wash or None. Or for an attribute change for a small market segment.
- Click Unassignfor other changes. The market segment moves to the leftUnassigned Market Segmentspanel where you can assign new attributes.
- If several people at your property work in Market Segment setup, you might want to track changes. ClickAuditin the bottom, right corner of the page. SeeDetailsto learn about the displayed data.
ClickFinalizeonly after you complete and review the assigned attributes.You can only click this button once.It is available only after you map at least one rate code for every market segment. In other words, no market segments remain in the Group Business Level or Market Segment Level tabs.
Clicking Finalize means that you wantIDeaSto load transactional data (like the rate code in a reservation) inG3 RMS, based on your attributed market segments.
After the loading step completes, you can see the new market segments in the right pane of theForecast Groupstab. You can also see past and future booking data inG3 RMSmodules.
If you have to define anyRate Protectbusiness, you can do that before or after clicking Finalize. The Rate Protect setup doesn't impact the loading of data or the last step, Create and Commit Forecast Groups.
AfterIDeaS loads the data, you set up other areas inG3 RMS:
- Room Classes
- Pricing
- Rate Shopping
Once you complete these setup tasksand IDeaS tells you to go ahead, continue to the last step. Use theForecast Groupstab to create and commit the Forecast Groups. The result is the system's first forecast.
You canrename the Forecast Groupsto ensure they are easily understood by you and your team.
If you manage a live property inDecision DeliveryA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system., you might need to update the market segment setup. Be sure that you understand theimpact of changes to market segments and Forecast Groups. Here are common scenarios:
A new market segment was created and needs attributes. You receive anUnassigned Market Segment Alertif this occurs.
- Follow the Alert link to the Market Segments tab.
- Select the market segment and assign attributes. See thedetailed steps here.
- ClickAssign.
- Click theForecast Groupstab.
- ClickCreate Forecast Groups. The updated Forecast Group is flagged with a green check mark.
- ClickCommit FGsto commit the changed Forecast Groups. A confirmation window opens.
- ClickYesto confirm.
If you create a new rate code for a clean market segment (that  you attributed at the Market Segment Level), you don't need to update anything. AfterG3 RMSgets the first reservation, it uses the attributes of the existing market segment. The same applies to a rate code that falls under anAttribute Assignment Rule.
The steps differ when a new rate codes belongs to a split market segment (that you attributed at the Rate Code Level). Unless you set up an Attribute Assignment Rule,G3 RMScan't know which attributes to use.
- The property gets anUnassigned Rate Code Alertfor the new rate code. Follow the link in the Alert to the Market Segments tab.
- ClickRefresh.
- Click the togglenext to the Original Market Segment name to open it and review the rate code.
- Select and assign attributes to the new rate code, using the below decision process:
- Click theForecast Groupstab.
- ClickCreate Forecast Groups. The updated Forecast Group is flagged with a green check mark.
- ClickCommit FGsto commit the changed Forecast Groups. A confirmation window opens.
- ClickYesto confirm. Note that if you donât commit the Forecast Groups, the rate code reverts to unassigned in the next processing.G3 RMSstarts an optimization and goes into Read Onlymode
- ClickUnassign.
- TheUnassign Attributeswindow opens. Your steps depend on the reason for the change:Incorrect attributes or a big change in the attributes:The assigned attribute of a clean or split market segment is incorrect.A corporate rate with high production, roughly more than 2% of the total property business, changes from Fixed and Yieldable to Linked to BAR and Semi-Yieldable. In such case, it's better to link the rate to the history (even if it's not a perfect match in behavior) than forG3 RMSnot to have any history to use for forecasts. SelectApply Changes to Past and Future Data. The market segment moves to the left pane.If you don't see two options for how to apply the changes, your reservation system doesn't support a rebuild inG3 RMS. In that case, the RMS applies changes to future dates only. If you made an attribute mistake and the impacted market segments contain more than 2% of total property production, contact IDeaS. We review the impact and suggest how to correct the mistake.A change in Forecast Type attributes from Demand and Wash to only Wash or None. Or an attribute change for a small market segment. SelectApply Changes to Future Data Only. The market segment moves to the left pane.
- Incorrect attributes or a big change in the attributes:The assigned attribute of a clean or split market segment is incorrect.A corporate rate with high production, roughly more than 2% of the total property business, changes from Fixed and Yieldable to Linked to BAR and Semi-Yieldable. In such case, it's better to link the rate to the history (even if it's not a perfect match in behavior) than forG3 RMSnot to have any history to use for forecasts. SelectApply Changes to Past and Future Data. The market segment moves to the left pane.If you don't see two options for how to apply the changes, your reservation system doesn't support a rebuild inG3 RMS. In that case, the RMS applies changes to future dates only. If you made an attribute mistake and the impacted market segments contain more than 2% of total property production, contact IDeaS. We review the impact and suggest how to correct the mistake.
- The assigned attribute of a clean or split market segment is incorrect.
- A corporate rate with high production, roughly more than 2% of the total property business, changes from Fixed and Yieldable to Linked to BAR and Semi-Yieldable. In such case, it's better to link the rate to the history (even if it's not a perfect match in behavior) than forG3 RMSnot to have any history to use for forecasts. SelectApply Changes to Past and Future Data. The market segment moves to the left pane.
- If you don't see two options for how to apply the changes, your reservation system doesn't support a rebuild inG3 RMS. In that case, the RMS applies changes to future dates only. If you made an attribute mistake and the impacted market segments contain more than 2% of total property production, contact IDeaS. We review the impact and suggest how to correct the mistake.
- A change in Forecast Type attributes from Demand and Wash to only Wash or None. Or an attribute change for a small market segment. SelectApply Changes to Future Data Only. The market segment moves to the left pane.
- Assign the correct attribute.
- Click theForecast Grouptab.
- ClickCreate Forecast Groups.
- In the window, confirm to Create Forecast Groups.
- G3 RMSapplies the changes:If you applied the changes to future data only, the system updates the attributes for future dates only. Your forecasts and decisions might change.If you selected to Apply Changes to Past and Future Data,G3 RMSrebuilds past data and pace. It does that for all market segments and rate codes that are impacted by the change. The rebuild lasts about an hour.
- If you applied the changes to future data only, the system updates the attributes for future dates only. Your forecasts and decisions might change.
- If you selected to Apply Changes to Past and Future Data,G3 RMSrebuilds past data and pace. It does that for all market segments and rate codes that are impacted by the change. The rebuild lasts about an hour.
- If you selected a rebuild, review the possible impacts:Your forecasts and decisions might change.In reports and dashboards, the Pace for Same Time Last Year (STLY)  is rebuilt for all impacted segments. For details on the impact on the STLY values, seePace Built from History.G3 RMSdeletes Demand Overrides for impacted Forecast Groups. Overrides of pricing and overbooking are not impacted.The system removes Group Evaluations if a market segment is no longer classified as group.
- Your forecasts and decisions might change.
- In reports and dashboards, the Pace for Same Time Last Year (STLY)  is rebuilt for all impacted segments. For details on the impact on the STLY values, seePace Built from History.
- G3 RMSdeletes Demand Overrides for impacted Forecast Groups. Overrides of pricing and overbooking are not impacted.
- The system removes Group Evaluations if a market segment is no longer classified as group.
If you addindependent productsto an existingG3 RMSproperty:
- ClickUnassignfor the market segment  that represents the business of the independent product.
- TheUnassign Attributeswindow opens.
- SelectApply Changes to Past and Future Data. The market segment moves to the left panel.
- Select the checkbox  for the market segment.
- Select theUnqualified,Equal to Base Product, andDemand and Washattributes.
- ForBase Product, selectIndependent Product.
- ClickAssign. A confirmation window opens.
- ClickOkto confirm that you understand when to use the Equal to Base Product attribute. TheIndependent Product Namewindow opens.
- Enter the name of the independent product, using the same name as it appears in yourselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data..
- ClickOk.
- Repeat steps 1 to 10 for market segments that areLinked tothe pricing of the independent product. Seeattributesfor examples.
- Click theForecast Grouptab.
- ClickCreate Forecast Groups.
- In the window, confirm to Create Forecast Groups.
- G3 RMSapplies the changes. It rebuilds past data and pace. It does that for all market segments and rate codes that are impacted by the change. The rebuild lasts about an hour.
- After the rebuild, review the possible impacts:Your forecasts and decisions might change.In reports and dashboards, the Pace for Same Time Last Year (STLY)  is rebuilt for all impacted segments. For details on the impact on the STLY values, seePace Built from History.G3 RMSdeletes Demand Overrides for impacted Forecast Groups. Overrides of pricing and overbooking are not impacted.
- Your forecasts and decisions might change.
- In reports and dashboards, the Pace for Same Time Last Year (STLY)  is rebuilt for all impacted segments. For details on the impact on the STLY values, seePace Built from History.
- G3 RMSdeletes Demand Overrides for impacted Forecast Groups. Overrides of pricing and overbooking are not impacted.
- Continue setting up the independent product in Pricing:Definition,Ceiling/Floor,Offsets, and, if needed,Supplements.
When you make attribute changes, those to market segments with a large share of your business have the biggest impact on forecasts and decisions. And ensure that you use the Equal to Base Product attribute correctly, since it directly impacts the pricing decision. Only use it for business that is booked at the value of the selected Base Product. Don't use it for discounted business, such as advance purchase rates.

## Data Details

Following are definitions for each tab. If needed, review theanswers to common data questions.
This tab displays market segments from the historical data that belong to one or more group blocks or group block headers.
These tabs contain business from two sources:
- The historical transactional data, for example, the details of a reservation.
- The summary level data, for example, the actual revenue totals  by market segment for a date.
