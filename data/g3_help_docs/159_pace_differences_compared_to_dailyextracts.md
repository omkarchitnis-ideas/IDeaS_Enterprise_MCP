# Pace Differences Compared to  DailyExtracts

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/BAD/Pace-Data-Discrepancies.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/BAD/Pace-Data-Discrepancies.htm`
- **Ingestion Date:** `2026-09-11 22:13:55`

---

# Pace Differences Compared to  DailyExtracts

InG3 RMS, you might notice pace differences in data from same time last year (STLY) to other systems, like size changes of a group block. These scenarios explain why you might see such discrepancies.

## Pace Built from History

When initially building a property,the RMScan use up to 365 days of historical reservation and group block data to build booking pace. By building pace from history, the system reduces its  learning time and quickly understands the booking patterns for a full year without having to collect a full year ofdailydata extractsFiles with new and changed booking data that the RMS receives from the reservation system. It includes reservations, group blocks, and inventory summary data. Also called Snapshots or Daily Extracts.. View the effects of building pace from history in the scenarios below.
the RMSuses this historical data to build a full year of seasonal booking patterns, including booking pace, for both transient and group business.the RMSuses these booking patterns to understand how business picks up and washes within each season across the year, which is particularly beneficial to properties that see different seasonal materialization.
To build pace from history for transient business,the RMSuses the original booked date from the individual reservation. For group business,the RMSuses the booked date and the originally contracted room nights compared to the final picked-up room nights from the group block reservation.

## Differences in Same Time Last Year (STLY) Data

When a property is built using historical data,the RMScreates an indication of pace for the same time last year, which it displays in dashboards and reports. Using this method,the RMSallows you to see an indication of the business on books at the same time last year, without waiting to gather each dailysnapshotfrom yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.for 365 days.
You should view STLY data as a representation of your status at the same time last year. Due to the constraints of the historical data available tothe RMS, the data  does not show your exact position at the same time last year like you have available from your daily dataextracts. After the initial year of capturing daily dataextracts,the RMShas a more accurate picture of the STLY business conditions.

### STLY for Transient Business

For transient business from history,the RMSbases STLY on the volume of individual reservations on books as of the same number of days prior to arrival, accounting for bookings made and canceled. For past bookings,the RMSonly receives the final status of a reservation. The system does not know if changes to the reservation took place. For example, if a reservation was booked with an incorrect market segment and was later changed,the RMSonly sees the reservation with its final market segment.the RMSalso does not receive adjustments to the number of nights. In these cases,the RMSbuilds pace that reflects reservations based on their final details. For all bookings received fromdaily data extracts, the system sees such changes due to the difference between an extract and the next day's extract.
the RMSalso adjusts for canceled and no-show reservations. These are generally delivered to the system with a room revenue of 0.00. When the reservations were confirmed, they did carry a value. Therefore, for optimal system performance,the RMSneeds to treat this value as a holding a value between the booking and cancellation date. All properties built or re-built after January 16, 2016 use the rate value as an approximation of the room revenue value. This approximation is not a perfect proxy for the room revenue value. However, it is more valid than assuming these reservations held a 0.00 value, which dilutes metrics such as Average Daily Rate (ADR).

### STLY for Group Business

This scenario applies if your implementation began after May 2016.
When pace data is built from history, it is more difficult to get a full picture of group booking patterns than with transient business. That is because, whenthe RMSinitiallyextractsdata, the group block only shows original room nights and the final picked-up room nights for past blocks.the RMSdoes not receive information about changes during the booking cycle, like block increases or decreases. Any block changes from the date the block moved from deduct to non-deduct or deduct to canceled until the day of arrival are generally not available tothe RMS. The system only has this information available after the system begins capturing the data throughdaily data extracts.
Thus, when pace is built from history, the STLY statistics for group blocks inthe RMSmight differ from thePMSduring the first year. These differences in Group Booking Pace occur because thePMS, unlikethe RMS, knows about changes to group status, blocked rooms sold and revenues.
Some reservations systems don't send the booking dates of past group blocks forthe RMSto understand group booking patterns and to show an indication of STLY. In this case,the RMSdisplays STLY only collecting 365 days of daily data.SeeGroup Pace Initialization Periodfor more information.

#### Group Pace Data Comparison

The following example illustrates the differences between the group data observed from daily dataextractscompared to data when pace is built from history:
The illustration shows the following:
- A group was blocked as Tentative (Non-Deduct) at 88 days to arrival. Historical data shows the rooms as on books from this point.
- The group signed a contract, and the block moved from Tentative (Non-Deduct) to Confirmed (Deduct) at 54 days to arrival. The daily dataextractsnow record the group as on books in thedaily snapshots.
- At 53 days to arrival, the number of rooms changes from 14 to 18.Daily data extractsrecord this change, but the historical data does not include this change.
- At 41 days to arrival, extra rooms are added to the block temporarily. Again,daily data extractsrecord this change, but the historical data does not include this change.
- Daily data extractsrecord that the block gradually washes and ends at 13 rooms. Historical data, however, only records the drop-off to the final rooms sold on the Day of Arrival.
Thus, to determine group booking patterns from historical data,the RMSknows only that the block was booked at 14 rooms and ended at 13.
When data capture begins,the RMSuses the actual observed pick-up and wash patterns, based on the group block extracts. As the volume of data thatthe RMScollects grows, the system can improve its understanding of group booking patterns. After the initial year of data capture,the RMShas a more accurate picture of the STLY business conditions.

#### Impact on Group Forecasting

To understand the impact on group forecasting, consider the data thatthe RMSuses for forecasting group:
- Past group blocks, based on the variance between original blocked and final picked-up rooms
- Booking patterns, including the blocked rooms, the blocked date and how far in advance bookings were made
- Actual pick-up and wash patterns for future groups, including original number of rooms, final number of rooms and all changes in between
Each day after data capture begins,the RMSlearns more about the pace and pattern of groups, which helps improve the forecasting. If property has very few groups, andthe RMShas not learned enough by the time it begins sending decisions,  we recommend ongoing group forecast reviews and, if necessary, group demand overrides.

## Suboptimal Business Practices

Some group business practices can result in missing or incorrect pace. SeeGroup Block Business Practicesfor more information.

## Afterthe RMSHas Daily Data

Even afterthe RMScaptures a full year ofdaily extracts, and summary level (market segment by room type) data is available, you could still see minor data discrepancies for these reasons:
- the RMSbreaks down market segments into attributed market segments, using functionality inMarket Segmentssetup.  Since there is no summary level data available at the attributed market segment level,the RMSpopulates some pace from the reservations. Where yourreservation systemprovides summary level data, there might be some differences when comparing summary to transactional data.
- Pseudo room types are removed fromthe RMS. This removal isn't likely to have a significant impact because most pseudo revenue is raised against these room types on the day, rather than held to be posted on a future date or rolling basis, as is the case with normal reservations.
