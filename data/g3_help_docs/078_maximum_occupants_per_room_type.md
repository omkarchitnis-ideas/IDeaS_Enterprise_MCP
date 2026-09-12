# Maximum Occupants per Room Type

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/PPP-Maximum-Occupancy.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/PPP-Maximum-Occupancy.htm`
- **Ingestion Date:** `2026-09-11 22:13:00`

---

# Maximum Occupants per Room Type

If your property uses Per Person Pricing,G3 RMSneeds to know maximum occupancy for each room type because the system optimizes by occupants rather than per room. Use Maximum Occupants per Room to set up the maximum number of guests that each room type can accommodate and specify the maximum number of adults and children.
The maximum occupancy values control how many adults and children you can add in theOccupant Groupingsetup. It also helps the system understand what occupancy patterns could be possible for a Room Type. See anoverview of all Per Person Pricing topics.
The offsets define the supplemental cost thatG3 RMSadds for each of the extra adults and children in a room type to its base pricing decision for two adults in that room type.

## Setup Steps

- Click, thenInventory, and thenRooms Configuration.
- ClickNextthrough the Rooms Setup introduction. The Room Class step displays.
- Click theAdd Maximum Occupancylink.
- Enter the maximum number of occupants for each room type:Max: The maximum number of guests who can occupy the room type. This value can be greater than the sum of Adults and Children and must be at least 2.Adults: The maximum number of adults who can occupy  the room type. The number of adults cannot be greater than the Max and must be at least 2.Children: The maximum number of children who can occupy the room type. The number of children cannot be greater than the Max.
- Max: The maximum number of guests who can occupy the room type. This value can be greater than the sum of Adults and Children and must be at least 2.
- Adults: The maximum number of adults who can occupy  the room type. The number of adults cannot be greater than the Max and must be at least 2.
- Children: The maximum number of children who can occupy the room type. The number of children cannot be greater than the Max.
- ClickSave.
- Complete any remainingRoom Classsetup steps, then clickNextto move on to the next step in Rooms Setup.

## Best Practices

### Complete the Setup

- You must set up the maximum occupancy for all room types.
- You can complete this setup either before or after you map room types to Room Classes, but you must complete it before you can move to the next step in Rooms Setup.
- You must set up a Max occupancy of at least one adult in every room type.
- The Max value can be greater than the sum of the adults and children, but the number of adults or children cannot be greater than the Max. For example, a room may be able to accommodate up to two adults and two children, but a maximum of three people at any one time, meaning the following maximum combinations are possible: 1 adult and 2 children, or 2 adults and 1 child. In this case, the setup would be: Max = 3; Adults = 2; Children = 2.

### Set Up Accurately

This setup must accurately reflect the maximum occupants and patterns that each room type could accommodate. The setup establishes the occupancy types thatG3 RMSwill consider as possibilities when optimizing. For example, a room that can accommodate up to four people (two adults and two children) would have all of the following possible patterns:
- 1 Adult + 0 Children
- 1 Adult + 1 Child
- 2 Adults + no Children
- 2 Adults + 1 Child
- 2 Adults + 2 Children
- 0 Adults + 1 Child
- 0 Adults + 2 Children
However, if you have never sold certain occupancies (using the previous example, let's say you don't allow the two options with 0 Adults), thenG3 RMScan't see any transactions with 0 adults and, therefore, will not consider the possibility of demand with 0 Adults.
