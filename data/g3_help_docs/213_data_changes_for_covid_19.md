# Data Changes for COVID-19

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/About/Covid-Data-Changes.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/About/Covid-Data-Changes.htm`
- **Ingestion Date:** `2026-09-11 22:14:31`

---

# Data Changes for COVID-19

This page lists the data changes that IDeaS made during the COVID-19 pandemic. These changes ensured thatG3 RMS:
- Did not include data from the demand disruption to forecast the recovery period or normal demand.
- Could quickly detect when recovery began.
The changes are listed from the most recent to the oldest.
To see if data exclusions applied to your property, reviewExcluded Datesin the Forecast Investigator.

### July 2024: Removing Most Remaining Changes

With most markets at or near full recovery and with enough normal demand data, we remove most remaining changes to ensure forecasts and decisions remain optimal. We keep the features that allowG3 RMSto quickly adapt to demand disruptions.

### July 2022: Using 2019 and Recent Data; Changes to Data Exclusions

#### Using 2019 and Recent Data

G3 RMSbegan using recent and 2019 data for forecasting to ensure that it could react quickly to the strong performance seen in many markets.

#### Data Exclusions

- IDeaS excluded all data from February 2020 to September 2021. Previously exclusions were  through January 2021.
- Group booking patterns were excluded from March 2020 to June 20, 2022.G3 RMSused groups after those dates.
We began applying these changes to properties on Tuesday, July 5, 2022. We excluded properties with Synthetic Data, those that did not have or use 2019 data, and those that performed better in June to September 2021 than in the same months of 2019.

### February 2022: Changes to Data Exclusions and to April 2021 Refinements

#### Changes to Data Exclusions

- Because group business had not recovered for most hotels, we extended the August 2021 exclusion of group booking patterns (originally for March 2020 to December 2021) to June 30, 2022.
- Transient Booking cancellations had increased for some hotels. To minimize the impact on wash and overbooking for those hotels, we excluded the transient booking data from December 1, 2021 to January 31, 2022.
- In April 2021, we excluded all data for February 2020 to January 30, 2021 for hotels in which the rooms sold for July to December 2020 was less than 80% of the rooms sold for the same period in 2019. In February 2022, we applied the same change to properties that previously did not qualify for it.

#### Changes to the April 2021 Refinements

To maintain forecast stability after excluding so much data in 2020 and 2021,IDeaSadjusted the April 2021 refinements. For example,G3 RMSbegan using booking patterns from the past 365 days instead of only the recent past. We applied these changes to all properties that received the April 2021 refinements and to all previously excluded properties.
We did not apply these changes to properties that used Synthetic Data, had been closed on 30 of the previous 60 days (as of January 15, 2022), or that had less than 10% occupancy on books.

### August 2021: Expansion of the April 2021 Refinements; Extended Group Data Exclusion

#### Expansion of the April 2021 Refinements

We applied  the April 2021 refinements to those properties that were excluded at that time, including properties that newly qualified for them or that started using the system since.
We did not apply the refinements to properties that used Synthetic Data, were closed for 31 or more of the previous 60 days (as of August 15, 2021), or that had less than 10% occupancy on books.

#### Extended Group Data Exclusions

We extended the January 2021 group data exclusion (originally set to ignore group data from March 1, 2020 toâ¯June 30, 2021) to December 31, 2021 because group business had not yet recovered for most hotels.

### May 2021: Refinements for Properties with the Full Ignored Period

This change was applied to properties whereG3 RMSignored all data from February 1, 2020 to January 30, 2021 (see April 2021). This change made the system's forecasting more stable when itupdated its demand models.

### April 2021: Refinements and Ignore All Data

IDeaS made the following changes for qualifying properties. See exclusions below.

#### Refinements

- Revised calculation for thereference price, so it would change less often and better handle large year-on-year changes.
- Improved forecasting to better handle day-of-week pattern changes. These pattern changes were very common due to the change in business mix and travel patterns.
- Updated booking patterns to use the recent past more quickly.
- Projected booking pace changes to future dates of the same day of week. Typically transient bookings for an occupancy date influence the remaining demand for that date. With this change,G3 RMSused the future bookings of earlier occupancy dates to influence the remaining demand for later occupancy dates. This enabled the system to react faster to aggressive booking pattern changes during the COVID-19 recovery.

#### Ignore All Data

We set upG3 RMSto exclude all data from February 1, 2020 to January 30, 2021. This change ensured that the system ignored the most disrupted period and used the difference between 2019 and the recent past. This change replaced the changes made in June 2020. The group booking pattern changes from January 2021 remained active.

#### Exclusions

We did not apply these changes to properties that used Synthetic Data or  that had been closed on 30 of the last 60 days (as of April 12, 2021).
Only the refinement changes were applied to properties where the rooms sold percentage for July to December 2020 was greater than 80% of those in the same period in 2019. The ignored periods  remained the ones made in June 2020.

### January 2021: Ignored Group Booking Patterns

G3 RMSignored the group booking patterns from March 1, 2020 to June 30, 2021.
During this time, the impact of COVID-19 was larger on group business than transient. Transient cancellations and no-shows happened mostly around theclosure periods, for whichG3 RMSignored the data. But group business continued to cancel or have high wash. This causedG3 RMSto expect high wash, including for groups that remained on books. And groups that did not cancel likely had lower wash thanG3 RMSexpected.

### June 2020: Booking Patterns

G3 RMSignored the booking pace data so the data would not affect booking patterns,reference price, and price-sensitivity.
The changes were applied to March 1, 2020 to June 15, 2020 for all properties outside of China and Hong Kong. They were applied to January 15, 2020 to June 15, 2020 for properties within China and Hong Kong.
This change ensured that the system ignored irrelevant data like higher levels of cancellations and no-shows, lower levels of reservations, and unusual pricing practices. We did not exclude the final rooms sold, soG3 RMScould react quickly to signs of recovery that spanned at least 14 days.

### March 2020: Used Recent Change and Booking Patterns

These changes were made to all properties, including those using Synthetic Data:
- Set all properties to react to recent changes in demand (the last 14 days).
- MadeG3 RMSmore sensitive to changes in business on books.
