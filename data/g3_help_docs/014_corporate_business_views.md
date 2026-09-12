# Corporate Business Views

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Property/Business-Views-Corporate.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Property/Business-Views-Corporate.htm`
- **Ingestion Date:** `2026-09-11 22:12:16`

---

# Corporate Business Views

Set up a Corporate Business View if you like theProperty Business Viewsand if you manage multiple properties. While Property Business Views vary by property, a Corporate Business View provides one standardized view across all properties. Combined withProperty Groups, you can view data for multiple properties and grouped in the same way on theOccupancy and Revenuechart of the At a Glance dashboard.
For example, your properties have their own Property Business Views which don't align with each other. You want a single view that recreates the market segments from yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.and that your company uses for financial reporting.
You create aFinancial ReportsCorporate Business View. You add Business Groups to the view that match the names of the market segments from yourreservation system. Then you add the appropriateG3 RMSmarket segments to each Business Group. When you select a Property Group on the At a Glance dashboard, the Occupancy and Revenue dashboard displays the data for the included properties in the Corporate Business View. When you switch back from Property Group to a single property, the data is in the Property Business View.

## Setup Steps

### Adding a New Corporate Business View

- Click, thenExternal Data, and thenBusiness Views.
- Click the add icon.
- Enter aNameandDescriptionfor the Business View. Descriptions are used only for informational purposes.
- SelectSet 
	 as default business viewif you want this view as the default.
- ClickSave.
- If you need to change the details, click theEdit Business 
	 View Detailslink in the upper right corner.
- In the Add Business Group pane, type theNameandDescriptionfor the Business 
	 Group.
- In theMarket Segmentsection, select market segments to add to the Business Group.Enter a character string in the empty field to filter the list of available market segments.Press Ctrl+click to select multiple market segments.
- Enter a character string in the empty field to filter the list of available market segments.
- Press Ctrl+click to select multiple market segments.
- Click>to move the 
	 selected market segments to theAdd Business Grouppane, or click>>to add all market segments.
- ClickSave.
- If there are other market segments available, repeat the steps above to create additional Business Groups.
- To change Business Groups, select them in the left pane. Modify them in the right pane, as needed, and save.
- To delete a Corporate Business View or Business Group, click deletenext to it and confirm the deletion.
Your Corporate Business Views display in the left-hand pane. The number of market segments in each Business Groups displays in the Market Segments column.

### Create Rules to Automatically Map New Market Segments

If your market segments follow a naming convention, you canCreate Rulesso thatG3 RMSassigns new market segments to the matching Business View and Business Group. The rules apply only toUnassignedmarket segments, they donât change what you already mapped.
- ClickCreate Rules. TheMapping Ruleswindow opens.
ClickCreate Rules. TheMapping Ruleswindow opens.
- Click to adda rule.
Click to adda rule.
- Select the howG3 RMSselects the market segments for this rule, for example, those with names starting withCOR.
Select the howG3 RMSselects the market segments for this rule, for example, those with names starting withCOR.
- Select theBusiness ViewandBusiness Groupthat the market segments with those names should belong to.
Select theBusiness ViewandBusiness Groupthat the market segments with those names should belong to.
- Savethe rule.
Savethe rule.
- Add all the rules you need and, if needed, changetheir rank. For example, if you have one rule starting with CO and another with COR, rank the COR rule higher than the CO rule.
Add all the rules you need and, if needed, changetheir rank. For example, if you have one rule starting with CO and another with COR, rank the COR rule higher than the CO rule.
- If you change ranking, click toSavethe changes.
If you change ranking, click toSavethe changes.
