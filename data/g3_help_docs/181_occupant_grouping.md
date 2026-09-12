# Occupant Grouping

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Occupant-Value-Grouping.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Occupant-Value-Grouping.htm`
- **Ingestion Date:** `2026-09-11 22:14:10`

---

# Occupant Grouping

Occupant Grouping impacts yourOffsetssetup. Its usage depends on your pricing method:
- If, like most of ourclients,your property usesper room pricing, you can use this feature to vary the extra child charge by age group. For example, you set one offset for children 0 to 6 and another for those 7 to 13 years old.Availability depends on your selling system, seeBest Practices.
- If your property, like many all-inclusive resorts, usesper person pricing, you can also use this feature to price any of your room types differently at higher adult or child occupancies.

### When to Use Occupant Grouping

Use Occupant Grouping if any of your room types meet one of these scenarios:

#### Child Pricing

- Pricing for children is based on their age group. For example, pricing for children aged 0-3, 4-12, and 13-16 is different. If pricing for all children is a flat price regardless of age, you do not need to use Occupant Grouping. This is the only available Occupant Grouping option if you price by room.
- Pricing for children differs based on the number of children in a room, rather than a flat price for each child. For example,  the first child is 20.00, two children are charged at 35.00, etc. If the price increases by 20.00 or 10% for every child (in other words, the extra child offset applies to all children), you do not need to use Occupant Grouping.

#### Adult Pricing

- Pricing for a certain number of adults in a room is fixed, then the extra adult pricing begins. For example, the same rate is charged for 1-4 adults, then the 5th adult is charged an extra adult supplement.
- Pricing is different based on the number of additional adults. For example, the 3rd adult adds 50% to the 2 adult (base) rate, and 4 adults in the room adds 75% (rather than 100%). If pricing for all extra adults increases by 50.00 or 50% (in other words, the extra adult offset applies to all adults beyond the first two), you don't need to use Occupant Grouping.
Completing Occupant Grouping opens up occupancy type rows on theOffsetspage. You then add offset values only to the room types for which the additional occupancy values apply.
The number of rows are defined by the room type'sMaximum Occupancy, seethis best practicefor details.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click Advanced Settings.
- ClickOccupant Grouping.
- To price by child occupancy (if available):Select theExtra Childcheckbox.In the menu, select the number of children for which you need to define a different pricing offset.
- Select theExtra Childcheckbox.
- In the menu, select the number of children for which you need to define a different pricing offset.
- To price children by age group:Select theExtra Child Age Groupcheckbox.Click the add icon.In theMinandMaxfields, type the minimum and maximum age for the group.Continue adding groups until all age ranges are accounted for. At least one group is required.
- Select theExtra Child Age Groupcheckbox.
- Click the add icon.
- In theMinandMaxfields, type the minimum and maximum age for the group.
- Continue adding groups until all age ranges are accounted for. At least one group is required.
- To price by adult occupancy (if available):Select theExtra Adultcheckbox.In the menu, select the number of adults for which you need to define a different pricing offset.
- Select theExtra Adultcheckbox.
- In the menu, select the number of adults for which you need to define a different pricing offset.
- ClickSave.
- Follow the steps toSet up Default Offsetsin Offsets setup .
