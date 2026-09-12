# Data Level Differences

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/BAD/Data-Level-Discrepancies.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/BAD/Data-Level-Discrepancies.htm`
- **Ingestion Date:** `2026-09-11 22:13:53`

---

# Data Level Differences

InG3 RMS, you might notice data differences between different reporting levels, like the property level compared to the market segment level. For example, Revenue On Books at the property level may not equal the sum of Revenue On Books for all Forecast Groups. These data discrepancies may exist within a dashboard or report or compared to yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system..
It's important to understand thatthese data discrepancies are reporting challenges only.They have no impact on your forecast and decisions, whereG3 RMSuses market segment and room type level information as the basis for its optimization.

## Occupancy and Revenue for Property, Market Segment, or Forecast Group

Most discrepancies in data can be explained by the fact that some values shown inG3 RMSare based on summary data and others on transactional data. Both are received directly from thereservation system. An example of summary data is the total number of rooms sold by market segment. Transactional data is all the details from all individual reservations booked under that market segment.
G3 RMSdisplays the occupancy and revenue on books values at the property level based on summary level data from thereservation system. For the market segment or Forecast Group level,G3 RMScannot use the market segment summary data from yourreservation system. Instead,G3 RMSneeds to add up transactional data from individual reservations. The original market segments from yourreservation systemdiffer from the market segmentsG3 RMSuses because you used attributes to modify the original market segments to provideG3 RMSwith the best data for forecasting and optimization.
These are a few other scenarios when the general differences between summary and transactional data lead to data differences inG3 RMS:

### Multiday Reservations

Discrepancies can occur when multiday reservations include rate amounts or rate codes and market segments that differ between the days. For example, a three-night reservation consists of a corporate rate code for the first and last night and a Package code for the second. The transactional rate code data counts the second night as Package. The summary property level data uses the corporate rate code for all three nights, as determined by the last night's data. Similarly, if a three-night reservation was priced at daily rates of $100, $150 and $200, the Business Analysis Dashboard shows a rate of $150 for all nights because it averages the rates and attributes the data based on the last nightâs market segment, rate code, etc.

### No Show Revenue Codes

Thereservation systemmay send No Show revenue toG3 RMS. Categorizing it as room revenue may result in data discrepancies, depending on whether it was booked against a physical room type or a pseudo room type.

### Pseudo Room Types

Revenue posted to paymaster/pseudo room types is not reflected in the Forecast Group level data, whereG3 RMSexcludes pseudo room types. If the property level data from the reservations system, however, is a direct summation of all room types, it could include revenue posted to pseudo room types.

### Re-Attribution or Removal of Rate Codes

Rate codes that are re-purposed or deleted impact the revenue values at theG3 RMSmarket segment level, which is combined to produce the Forecast Group level summary.

## Pickup for Rate Code and Market Segment

You might  see differences in the pickup between rate code and market segment levels, becauseG3 RMSmaintains pace only at the market segment level.  To determine pickup at the rate code level,G3 RMSadds up individual reservations, inferring the pickup based on the booked date of the reservation. The following are a few scenarios that cause these differences:

### Pace Maintained only from Nightly Processing to Nightly Processing

G3 RMSdoes not maintain intraday booking pace to record incremental bookings between nightly processing and intraday processing. Booking pace is only stored from one day to another, from one business day end to the next.
Consequently, rate code level pickup (based on the booking date of each reservation) may feature rooms booked during an intraday processing.  However, at the market segment level, this pickup is reflected in the next dayâs Nightly Processing.

### Modification of Arrival Date or Length of Stay

When the arrival date or length of stay changes for a reservation,G3 RMStreats it as a new booking.
While this does not impact the actual pace recorded at the market segment level, the booked date reflected in the new reservation is used to derive rate code level pickup. The âtrueâ booking date not being reflected on the updated reservation leads to discrepancies between the rate code and market segment level pickup.

### Group Blocks with Incomplete Pickup

As group blocks appear, the rooms sold are appropriately recorded at the market segment level.
However, until the reservations arrive with actual pickup against the block, no rate code level information can be recorded. This will lead to discrepancies between the market segment and rate code level wherever group blocks are greater than the picked up rooms on the block.
These discrepancies are more likely further from the day of arrival, where there is more pickup pending on group blocks.
