# Restriction Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/Restriction-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/Restriction-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:12:55`

---

# Restriction Configuration

Use Restriction setup if yourSelling SystemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.can't use theLast Room Value (LRV)to decide if a yieldable rate is available for a given stay pattern. Examples include:
- Some selling systems don't support controlling yieldable rates with the LRV.
Some selling systems don't support controlling yieldable rates with the LRV.
- Other selling systems can accept LRV but can't translate it for other selling channels that don't accept LRV, like the Online Travel Agent (OTA) channel Booking.com or anypush channelChannels that automatically receive inventory availability and pricing from the PMS or CRS. Restrictions translate Last Room Value (LRV) into controls that these channels can understand..
Other selling systems can accept LRV but can't translate it for other selling channels that don't accept LRV, like the Online Travel Agent (OTA) channel Booking.com or anypush channelChannels that automatically receive inventory availability and pricing from the PMS or CRS. Restrictions translate Last Room Value (LRV) into controls that these channels can understand..
- SomeG3 RMSsubscriptions don't include controlling yieldable rates with the LRV.
SomeG3 RMSsubscriptions don't include controlling yieldable rates with the LRV.
In these cases,G3 RMSneeds to translate the LRV into Minimum Length of Stay (MinLOS) or Full Pattern Length of Stay (FPLOS) restrictions. And to do that, the system needs to know the  value of your yieldable rate codes. Use Restriction setup to add this information if theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.doesn't send the rate codes and their rate details toG3 RMS.Or useMass Restrictionto set this up with an Excel workbook.
If yourreservation systemallows you to import rate codes and their values automatically, verify and edit the import. For example, rate codes that are derived off other rate codes in yourreservation systemdon't import at all or don't import as derived. Enter or edit them manually in Restriction setup.

### What Help Do You Need with Configuring Restrictions?

- Show me anoverview videoabout Restriction setup.
- What are the steps to addRate HeadersandRate Details?
- How do I know if I need Restriction setup and what are thebest practicesfor setup?
- I useLinked Products, how canG3 RMSuse those values for the Restriction setup?
- Show meexamples of the calculationfor converting LRV to Restrictions.

### See an Overview Video

Your browser does not support the video tag.

## Setup Steps

The setup consists of two steps: first, add Rate Headers (or rate plans), then add values and seasons for each rate in theRate Detailstab.
If you choose to use Mass Restriction setup to set up Restrictions using an Excel workbook, click theMass Restriction Configurationlink. SeeMass Restriction setupfor steps and considerations.
- Click, thenDecisions, and thenRestrictions.The Rate Header tab displays.
- Click the add icon.
- Enter aNamefor the rate plan. If you want to automate delivery of these restrictions, the name must match the rate code or rate category in the selling system.
- Enter aDescription.
- Select aStart Dateusing the calendar 
	 icon. The Start Date must be greater than or equal to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
- Select anEnd Dateusing the calendar 
	 icon. The End Date must be greater than the System Date and cannot be earlier than the Start Date.
- Select theDo Not Generate Restrictionscheckbox for rate codes for which you don't wantG3 RMSto prepare and send restrictions.Selected rate codes also don't display in theRestriction Report.Only use this option for rate codes that were imported automatically. If you have to load your rate codes manually, there is no need to add rate codes that you can't restrict.
- Select theTypeas a fixed value or an offset from the BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) decision. This selection applies to all room types and days of the week for the rate plan:Fixed: The rate is a fixed value for all dates.Derived: The rate is an increase or decrease off the BAR decision for all dates:Value: The rate is a fixed value off the BAR decision. For example, if the BAR decision is 100 and the Value offset is -20, the derived rate plan is 80. If the Value offset is 20, the derived rate plan is 120.Percentage: The rate is a percentage value off the BAR decision. For example, if the BAR decision is 200 and the Percentage offset is -10, the derived rate plan is 180. If the Percentage offset is 10, the derived rate plan is 220.
- Fixed: The rate is a fixed value for all dates.
- Derived: The rate is an increase or decrease off the BAR decision for all dates:Value: The rate is a fixed value off the BAR decision. For example, if the BAR decision is 100 and the Value offset is -20, the derived rate plan is 80. If the Value offset is 20, the derived rate plan is 120.Percentage: The rate is a percentage value off the BAR decision. For example, if the BAR decision is 200 and the Percentage offset is -10, the derived rate plan is 180. If the Percentage offset is 10, the derived rate plan is 220.
- Value: The rate is a fixed value off the BAR decision. For example, if the BAR decision is 100 and the Value offset is -20, the derived rate plan is 80. If the Value offset is 20, the derived rate plan is 120.
- Percentage: The rate is a percentage value off the BAR decision. For example, if the BAR decision is 200 and the Percentage offset is -10, the derived rate plan is 180. If the Percentage offset is 10, the derived rate plan is 220.
- Select theIgnore PMS/CRS Updatescheckbox if you wantG3 RMSto ignore updates to the rate code that are sent by the PMS or CRS.Some of our clients select this option because they use Mass Restriction setup to load all rates intoG3 RMSand don't want PMS/CRS updates to overwrite those values.
If you select Ignore PMS/CRS Updates, you take control of the rate code setup and must keep it up to date when changes are made in the PMS/CRS.
- Click the save icon.
- Continue adding rate plans until all required plans are represented. Select theApply first Rate Header Start and End Datecheckbox to apply the same date range as the first Rate Header to all new rate plans.
You can only change the dates for which a rate plan is defined if the changes meet certain criteria. If the Start Date is in the past, then only the End Date can be edited. If seasons are defined for the rate plan in Rate Details, the Start Date cannot be changed to be later than the earliest Start Date in its seasons. The End Date cannot be changed to be earlier than the latest End Date in its seasons.
- Click, thenDecisions, and thenRestrictions.The Rate Headers tab displays.
- Click the edit iconfor the Rate Header to be edited.
- Edit theName, if needed.
- Edit theDescription, if needed.
- Edit theStart DateandEnd Date, considering the criteria listed above.
- Select theDo Not Generate Restrictionscheckbox for rate codes for which you don't wantG3 RMSto prepare and send restrictions.Selected rate codes also don't display in theRestriction Report.
- Edit theType, if needed, considering thatG3 RMSremoves the Rate Details for all future seasons when you change the Type. If you change the Type (Fixed or Derived) for an existing rate plan,G3 RMSremoves the Rate Details for all future seasons.
- Click the save icon.
- Click, thenDecisions, and thenRestrictions.The Rate Headers tab displays.
- Click the delete iconfor the Rate Header to be deleted. Rate Plans with a Start and End Date in the past can't be deleted.
- ClickOKin the confirmation window.
- The dates for seasons within Rate Details must fall within the dates defined by the Rate Header.
The dates for seasons within Rate Details must fall within the dates defined by the Rate Header.
- Seasonal dates can't overlap. If you add a new season with dates that overlap an existing season, the new season takes over the existing one.G3 RMSadjusts the dates of the existing season to accommodate the new season, following these rules:When the new season falls within the date range of an existing season, the existing season is split into two seasons. The new season falls in the middle, and date ranges are adjusted accordingly. The rates by room type for the split season are maintained.When the Start Date of a new season is set to include dates at the end of an existing season, the existing season is adjusted to end on the date prior to the Start Date of the new season.When a new season includes all the dates of an existing season, the new season replaces the existing season.
Seasonal dates can't overlap. If you add a new season with dates that overlap an existing season, the new season takes over the existing one.G3 RMSadjusts the dates of the existing season to accommodate the new season, following these rules:
- When the new season falls within the date range of an existing season, the existing season is split into two seasons. The new season falls in the middle, and date ranges are adjusted accordingly. The rates by room type for the split season are maintained.
When the new season falls within the date range of an existing season, the existing season is split into two seasons. The new season falls in the middle, and date ranges are adjusted accordingly. The rates by room type for the split season are maintained.
- When the Start Date of a new season is set to include dates at the end of an existing season, the existing season is adjusted to end on the date prior to the Start Date of the new season.
When the Start Date of a new season is set to include dates at the end of an existing season, the existing season is adjusted to end on the date prior to the Start Date of the new season.
- When a new season includes all the dates of an existing season, the new season replaces the existing season.
When a new season includes all the dates of an existing season, the new season replaces the existing season.
- Where gaps exist in the dates  between seasons, the gap is considered a season with an undefined rate.
Where gaps exist in the dates  between seasons, the gap is considered a season with an undefined rate.
- Click, thenDecisions, and thenRestrictions.
- Click theRate Detailstab.
- Click the open iconbefore the Name.
- Choose a method for adding seasonal rates:Notes:You must enter rates for at least one Room Type in a season.To view the rates in past seasons, select thePastcheckbox.If available, select toInclude Discontinued Room Types. They display with a null symbol Ã.Copy all future seasons and offset the rates from another rate. This option is available only for rates without any seasons and when at least one other rate with a season and shared dates exists:Select theOffset fromcheckbox.Select a rate from the menu.Enter a positive or negative value to adjust the rates of the copied seasons.ClickApply. The new season displays with the copied dates and  rates adjusted with the offset value.Click the open iconfor the season to view and edit the populated rates for each room type and day of the week, as needed.You must enter rates for at least one Room Type in a season.Copy another season from the same rate. This option is available only when at least one season already exists in the rate.Click the add icon.Select aStart DateandEnd Dateusing the calendar 
	 icons.Select theOffset fromcheckbox.Select a season from the menu.Enter a positive or negative value to adjust the rates of the copied season.ClickApply. The new season displays, with copied rates adjusted with the offset value.Click the open iconfor the season to view and edit the populated rates for each room type and day of the week, as needed.Enter a new season:Click the add icon.Select aStart DateandEnd Dateusing the calendar 
	 icons.Add values to the season, depending on the type of rate:Fixed:Enter a rate in the first field following a room type. The rate displays for all days of the week for that room type.Continue to add rates as needed for other room types.Derived:Enter theOffsetvalue for the season. The offset is either a value or a percentage off the BAR decision, depending on your Derived setting in the Rate Headers tab.ClickApply. The value populates all room types and days of the week.Edit the populated offsets for each room type and day of the week, as needed.
Notes:
- You must enter rates for at least one Room Type in a season.
You must enter rates for at least one Room Type in a season.
- To view the rates in past seasons, select thePastcheckbox.
To view the rates in past seasons, select thePastcheckbox.
- If available, select toInclude Discontinued Room Types. They display with a null symbol Ã.
If available, select toInclude Discontinued Room Types. They display with a null symbol Ã.
- Copy all future seasons and offset the rates from another rate. This option is available only for rates without any seasons and when at least one other rate with a season and shared dates exists:Select theOffset fromcheckbox.Select a rate from the menu.Enter a positive or negative value to adjust the rates of the copied seasons.ClickApply. The new season displays with the copied dates and  rates adjusted with the offset value.Click the open iconfor the season to view and edit the populated rates for each room type and day of the week, as needed.
- Select theOffset fromcheckbox.
- Select a rate from the menu.
- Enter a positive or negative value to adjust the rates of the copied seasons.
- ClickApply. The new season displays with the copied dates and  rates adjusted with the offset value.
- Click the open iconfor the season to view and edit the populated rates for each room type and day of the week, as needed.
- Copy another season from the same rate. This option is available only when at least one season already exists in the rate.Click the add icon.Select aStart DateandEnd Dateusing the calendar 
	 icons.Select theOffset fromcheckbox.Select a season from the menu.Enter a positive or negative value to adjust the rates of the copied season.ClickApply. The new season displays, with copied rates adjusted with the offset value.Click the open iconfor the season to view and edit the populated rates for each room type and day of the week, as needed.
- Click the add icon.
- Select aStart DateandEnd Dateusing the calendar 
	 icons.
- Select theOffset fromcheckbox.
- Select a season from the menu.
- Enter a positive or negative value to adjust the rates of the copied season.
- ClickApply. The new season displays, with copied rates adjusted with the offset value.
- Click the open iconfor the season to view and edit the populated rates for each room type and day of the week, as needed.
- Enter a new season:Click the add icon.Select aStart DateandEnd Dateusing the calendar 
	 icons.Add values to the season, depending on the type of rate:Fixed:Enter a rate in the first field following a room type. The rate displays for all days of the week for that room type.Continue to add rates as needed for other room types.Derived:Enter theOffsetvalue for the season. The offset is either a value or a percentage off the BAR decision, depending on your Derived setting in the Rate Headers tab.ClickApply. The value populates all room types and days of the week.Edit the populated offsets for each room type and day of the week, as needed.
- Click the add icon.
- Select aStart DateandEnd Dateusing the calendar 
	 icons.
- Add values to the season, depending on the type of rate:Fixed:Enter a rate in the first field following a room type. The rate displays for all days of the week for that room type.Continue to add rates as needed for other room types.Derived:Enter theOffsetvalue for the season. The offset is either a value or a percentage off the BAR decision, depending on your Derived setting in the Rate Headers tab.ClickApply. The value populates all room types and days of the week.Edit the populated offsets for each room type and day of the week, as needed.
- Fixed:Enter a rate in the first field following a room type. The rate displays for all days of the week for that room type.Continue to add rates as needed for other room types.
- Enter a rate in the first field following a room type. The rate displays for all days of the week for that room type.
- Continue to add rates as needed for other room types.
- Derived:Enter theOffsetvalue for the season. The offset is either a value or a percentage off the BAR decision, depending on your Derived setting in the Rate Headers tab.ClickApply. The value populates all room types and days of the week.Edit the populated offsets for each room type and day of the week, as needed.
- Enter theOffsetvalue for the season. The offset is either a value or a percentage off the BAR decision, depending on your Derived setting in the Rate Headers tab.
- ClickApply. The value populates all room types and days of the week.
- Edit the populated offsets for each room type and day of the week, as needed.
- Continue to add seasons, as needed.
- ClickSave.
- Click, thenDecisions, and thenRestrictions.
- Click theRate Detailstab.
- Click the open iconfor the season to edit.
- Edit the rates by room type and day of the week, as needed.
- ClickApply.
- ClickSave.
- Click, thenDecisions, and thenRestrictions.
- Click theRate Detailstab.
- Click the open iconfor the season to delete.
- ClickDeleteand thenYesto confirm the deletion. The season is marked with a remove iconX. Note that Rate Details with a Start and End Date in the past can't be deleted.
- ClickSave.
