# Booking Pattern

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/LDB/LDB-Booking-Patterns.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/LDB/LDB-Booking-Patterns.htm`
- **Ingestion Date:** `2026-09-11 22:13:06`

---

# Booking Pattern

With Synthetic Data, you provideG3 RMSwith two pieces of information to replace the missing historical data: Booking Patterns and your rooms and revenueProjections.
By selecting patterns, you helpG3 RMSunderstand theBooking PaceMeasures how the occupancy changes as the arrival date approaches. It shows the speed at which reservations are booked.andWashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization.of each market segment. In other words, how your business picks up and cancels and when. Because the system can't derive booking patterns from historical data, you select another source. For example, you can choose a generic property with similar booking curves. When your property has enough usable historical data, you switch to using your own data.

## Setup Steps

- Click, thenForecasts, and thenSynthetic Data.
- Click theBooking Patterntab.
- Select the source of the property's booking patterns. SeeBest Practicesfor help with this selection.If you created the projections using similar properties and,in this step, chose to use the same properties for booking patterns, theA specific similar property optionis selected for you.
If you created the projections using similar properties and,in this step, chose to use the same properties for booking patterns, theA specific similar property optionis selected for you.
- ClickSave.
- If the pattern source is My property, you are done. Otherwise, use theSpecific Similar PropertyorGeneric Propertytopics in the Data Details section to complete all fields.

## Data Details

### A Specific Similar Property

Complete the row for each Market Segment following these steps, then clickSave.
If you created the projections using similar properties and,in this step, chose to use the same properties for booking patterns,G3 RMSmatched each of your Market Segments to the most Similar Market Segment of the most Similar Property. To find the best match the system uses  the name and attributes of the market segments. Review the selection and, if you know a better match, change the system's selections.

### A Generic Property

Select a booking curve for each Market Segment, then clickSave.

## Best Practices

### Select the Optimal Source for Your Booking Patterns

The available sources of booking patterns vary by property. The options below are sorted by preference, with the optimal source first.
- My property: this option is available whenG3 RMShas received more than 110 days ofdata extractsFiles with new and changed booking data that the RMS receives from the reservation system. It includes reservations, group blocks, and inventory summary data. Also called Snapshots or Daily Extracts.with pace. If that's the case, you see a message above the pattern options. This can occur either before or afterthe firstSynthetic Data buildruns. Your own data provides the best patterns, and we recommend using this option when it is available. If you select this option after using other sources, the system stops using the other sources, and those other options are no longer available in the tab.
- A specific similar property: if your property belongs to a large company, this option might be available. SeeData Details for the options.
- A generic property: if neither of the other sources are available, select a fabricated property. You choose the booking curves that best match your property's business for each of your market segments. You also set up the average length of stay and no-show % for each market segment. See the Data Details for how toSet up a Generic Property.

### Select Realistic Booking Patterns

For many Synthetic Data properties it takes some time before business behaves normally. If you expect a slow build up phase, select the appropriate booking patterns. For example, your group business books more than six months before the arrival date. If you pick a booking pattern with such a long-term pick-up, any groups staying during the first six months of operation would have to be already on books or there are none, since their expected booking window is already past. If needed, select a booking pattern with shorter pick-up window and change it later.
