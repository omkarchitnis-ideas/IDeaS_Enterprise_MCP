# Overbooking

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Overbooking/Overbooking-Management.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Overbooking/Overbooking-Management.htm`
- **Ingestion Date:** `2026-09-11 22:13:19`

---

# Overbooking

Overbooking ensures that your property can sell out and maximize revenue by accepting reservations beyond the capacity of a room type or overall property.
G3 RMSoverbooks at the property and room type level to offsetWashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization..With multiple Room Classes, the system also needs overbooking at the room type level to enable yourUpgrade Path.
Use Overbooking Management to review and if needed, override Overbooking, Wash, andCost of WalkCost of Walk happens if your property is unable to provide the confirmed room to a guest and has to relocate, or walk, the guest to another hotel. In that situation, costs might include the hotel room at the other hotel, a taxi, etc. 
Cost of Walk influences the overbooking level: the RMS weighs the risks of overbooking, represented by Cost of Walk, against its benefits, which are the additional revenues from selling another room. The higher the Cost of Walk, the lower the RMS tends to overbook..

### What Help Do You Need with Overbooking?

- Show me the options for viewing the overbookingdata details.
- I want to learn about thebest practicesfor overriding overbooking.
- I want to directly influence the overbooking decision byOverriding Wash for Individual Groups.
- I want to override overbookingor cost of walkfor a specific period of time withOverbooking OverridesorMultiday Overbooking Overrides.
- I want to test the impact of overrides before saving them by runningWhat If.
- I want to learnhow overbooking impactsG3 RMS.
- I want to setCeiling Defaultsto limit overbooking forallfuture dates.

## Steps to View Data in Overbooking Management

Clickand thenOverbooking.If you visit this page often, clicknext to the name to add it to the Quick Access menu.
- UnderCalendar Heatmap, switch from the defaultOverbookingThe practice of selling more rooms than are physically present in your hotel to make up for wash (cancellations, no-shows etc.). The goal of overbooking is to maximize revenue by achieving as close to 100% occupancy as possible on any given day.toOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details)., or theTotal DemandThe combination of the rooms on books and the remaining unconstrained demand.view.
- Point to a cell in the heat map to see the property overbooking limit plus the property's total number of rooms for that day, expressed as a percentage of the total number of rooms.Note: By default, this value uses the Physical Capacity for the total number of rooms, which includes out of order rooms.A property (or a corporate office for an enterprise) can contact IDeaS to switch this to use Effective Capacity, which excludes out of order rooms.With Effective Capacity you might see values below 100%. For example, the overbooking for a 100-room property is 10 rooms. With zero out of order rooms the heat map shows 110%. With 10 out of order rooms, the value is 100%.
- Click 
 a month in the heat maps to view that month plus the following in the calendar view below. Click the arrowsto view the next or previous 6 months.
- ClickLegendto see what different Overbooking, Occupancy, or Total Demand levels the colors represent.Customize these settings inHeat Map.
The Overbooking Management calendar displays the overbooking decision and the occupancy forecast. Use the following options to change the calendar display. For example, you might want to find potential sell out days and review the overbooking values for those days.
- Click to filterfor options to focus on  specific days.Select 
	 one or more days of the week to view in the calendars. Days that 
	 you do not select appear grayed out.Use theDates withmenu to select days with an Occupancy Forecast Less Than or Greater Than the 
	 percentage that you type in the % field.Select a checkbox underShow Overridesto highlight only those dates in the calendar that have active overrides.ClickApplyto save the filters. ClickResetto restore the default filters.
Click to filterfor options to focus on  specific days.
- Select 
	 one or more days of the week to view in the calendars. Days that 
	 you do not select appear grayed out.
- Use theDates withmenu to select days with an Occupancy Forecast Less Than or Greater Than the 
	 percentage that you type in the % field.
- Select a checkbox underShow Overridesto highlight only those dates in the calendar that have active overrides.
- ClickApplyto save the filters. ClickResetto restore the default filters.
- Click the date button to select the starting month or click the arrows  to move to the previous or next month.
- Select aRoom Typefrom the left-hand calendar to view two months of data for just that room type.
- Select a differentRoom Typefrom the right-hand calendar to compare two Room Types side-by-side for the same month
- At the property-level view, the calendar displays all overbooking and wash overrides. Point to the override icon to see what level the override applies to.
If set up, you can select theInventory Groupfilter at the top of the calendar. The default selection is Property, or all Room Classes. Change the default selection inPreferences.
Changing Inventory Groups limits the options in the Room Type menu. The selected Inventory Group does not impact the data in the calendar or the heat map.

## Data Details

The following data displays on the calendar dates in Overbooking Management. For data in the Overbooking Override window seeOverrides.
