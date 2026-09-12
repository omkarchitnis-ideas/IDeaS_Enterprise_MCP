# Room Type Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Rooms-Room-Type.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Rooms-Room-Type.htm`
- **Ingestion Date:** `2026-09-11 22:13:03`

---

# Room Type Configuration

Use the Room Type Configuration page for settings at the Room Type level, like Overbooking or Special Use Room Types.

### What Help Do You Need With Room Type Configuration?

- I want ashort overviewof the setup for overbooking and Special-Use Room Types.
I want ashort overviewof the setup for overbooking and Special-Use Room Types.
- I need thestepsto set up my Room Type Configuration.
I need thestepsto set up my Room Type Configuration.
- I want to understand the benefits ofallowing overbookingand how to ensure itsupports the Upgrade Path.
I want to understand the benefits ofallowing overbookingand how to ensure itsupports the Upgrade Path.
- I need to understandhow to decideif I need to set up Special Use Room Types.
I need to understandhow to decideif I need to set up Special Use Room Types.
- I want to seeexamplesof howG3 RMShandles the expected wash if some room types in a Room Class allow overbooking and others don't.
I want to seeexamplesof howG3 RMShandles the expected wash if some room types in a Room Class allow overbooking and others don't.

#### Allow Overbooking by Room Type:

Thesetup stepsallow you to vary the overbooking by room type, based on features,  upgrade options, and number of rooms.  For example, allow overbooking for your common Standard King room type, but not for the Standard Accessible King with just two rooms and no upgrade option. For details, see why you shouldallow overbookingandhowG3 RMScalculates overbooking.
Note: Some properties with less complex characteristics enable Run-of-House overbooking. With this optionG3 RMSassigns all overbooking to the one or two Run-of-House room types that you select. All other room types are not overbooked. Beforesetting up this option, understandhow Run-of-House overbooking works.For some subscriptions Run-of-House is the only overbooking option.

#### Special-Use Room Types

Consider this option for room types that you don't have onselling systemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.(like connector rooms for suites) or room type that don't sell easily due to their specific features, like accessible rooms.G3 RMScan improve overbooking by distributing their unsold capacity, see decide if you need to set upSpecial-Use Room Typesfor more.

## Setup Steps

### Accessing Room Type Configuration

- Click, thenInventory, and thenRooms Configuration.
- ClickNext, then clickNextagain in the Room Class and the Cost of Walk tabs. The Room Type tab opens.

### Setting Up Overbooking by Room Type

Mostclientsuse this option. If you use Run-of-House overbooking, see thesteps  to enable it.
- SelectSpecial-Use Room Typeif that applies to any of your room types. SeeHow do I decide?for questions.G3 RMSadds two columns, Special-Use Room Types and Distribute Unsold Capacity.
- If you selected Special-Use Room Type, also selectDistribute Unsold Capacity.
- Click the iconfor every Special-Use Room Type. The icon changes to.
- In the Allow Overbooking column, clear the checkbox  for any room type that you don't wantG3 RMSto overbook. Special-Use Room Types are cleared automatically.
Allow overbooking for at least one room type in each Room Class. See thisBest Practicefor more details.
- To control overbooking by day of week or with seasonal exceptions, select theAdvanced Settings - Overbookingcheckbox. For the detailed steps, see Setting Up by Day of Week and Season below.
- If you have very few competitors to walk to, consider selecting theReduce Overbooking for when more than % of competitors are sold outand entering a percentage value. Review thebest practicesbefore selecting this option.
- ClickNext. Continue to complete all the steps in Rooms Setup.

### Setting Up by Day of Week and Season

Note: Seasonal overbooking setup overrides anyCeiling Defaultvalues. If you use both for a room type,G3 RMShonors the seasonal overbooking setting rather than the Ceiling Default.
- Select theAdvanced Settings - Overbookingcheckbox. Columns for each day of the week display.
- Clear the checkboxfor the days when you don't want to allow overbooking for a room type.
- Click the add iconfollowing a room type if you need to add a season. The Add Season window opens.
- Click theStart DateandEnd Datecalendars to select the seasonal date range.
- In theOverbookingrow, select the checkbox for the days of the week for which you want to allow overbooking for the season.
- ClickApply.
- Continue to add seasons following the steps above until you set up all your required seasons.
- ClickNext. Continue to complete all the steps in Rooms Setup.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.

### Setting Up Run-of-House Overbooking

IfG3 RMSconfigured Overbooking for you, it selects the room type with the largest capacity in theMaster ClassThe Room Class for which a value displays if there is only space in the RMS to show one, for example, when you see only one price on a page..
- Click theEnable Run of Houselink.
- For theAdd Run-of-House Room Typeoption, select the Room Class that contains the room type to receive all overbooking. The room type that you select for run-of-house overbooking should belong to the lowest-priced Room Class to support upgrades.
- Select theRoom Type. This room type receives all the overbooking, up to the systemâs calculated total property overbooking level.
- If necessary, select theAdd second Run-of-House Room Typecheckbox to add a secondary room type. Select the secondaryRoom ClassandRoom Type.
- ClickNext. Continue to complete all the steps in Rooms Setup.
