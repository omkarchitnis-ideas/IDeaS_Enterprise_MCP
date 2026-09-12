# Best Practices for Using the Forecast Investigator

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Demand-Wash/BP-Investigator-Forecast.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Demand-Wash/BP-Investigator-Forecast.htm`
- **Ingestion Date:** `2026-09-11 22:14:37`

---

# Best Practices for Using the Forecast Investigator

Review the following best practices for investigatingthe RMSforecast or viewexamples.

## Review the System's Decisions

If you agree with the system's decisions, but disagree with the forecast, consider first if it's worth investigating the date. If you disagree with the system's forecast, but you aren't certain that you know something thatthe RMSdoesn't, continue to monitor it. If you're certain that you know something thatthe RMSdoesn't know, applydemand overrides.

## Consider the Impact of Demand360

If you subscribe tothe RMSpowered byDemand360, consider that the data from Demand360 can influence the forecast. As a simplified example, unusually high transient bookings for the competitive set will tend to adjust the demand forecast upwards, and the opposite downwards. Changes to demand may then impact decisions.

## Don't Review Occupancy Forecast at the Market Segment Level

We do not recommend reviewing the Occupancy Forecast at the Market Segment level becausethe RMScalculates the unconstrained demand forecast at the Forecast Group and Room Class level, not at the Market Segment level. For the constrained Occupancy Forecast,the RMSdistributes the Forecast Group level data down to the Market Segment level. This distribution is based on historical data and the proportion at which the business materialized under individual Market Segments in the Forecast Group. Ifthe RMSdoes not see past or future bookings for a market segment,the RMSconsiders the market segment discontinued and will no longer produce a forecast for it. For past bookings,the RMSlooks at the historical period for which it initially received data, typically two years.

## Scenarios

Investigator helps you understand the basic principles behindthe RMSforecasting: look for consistent patterns in the past and apply them to the future. Here are some examples.
In this example captured in March 2022, look at the forecast for the first quarter of 2023 (number 1). There are no On Books and the matching 2021 season is  grayed out and excluded. Therefore,the RMSuses the demand level and trend from the same season in 2022 (number 2). Lowest in January, increasing in February and in March (arrows).
To keep it simple we only show the property level, but always verify at Forecast Group level! The patterns might look very different at the Forecast Group level, see the Day of Week Patternsexample.

#### Recent Trends versus Similar Period in the Past

This example also shows how past seasonal trends might not be representative of current demand or the past data is excluded. In this case, the system might rely more on recent demand trends. Look at the forecast for April 2022 (number 3). The matching historical data, April 2021 and 2020, is excluded. Recent On Books is trending upwards since early February 2022 (number 2 and arrow).The RMSfollows that trend  and expects strong demand in April 2022, with many dates with unconstrained demand above capacity.
In this example we zoomed in to see the day of week pattern. At the property level the occupancy increases from the low on Sunday, slight decreases for Wednesday and Thursday and peaks on Friday and Saturday.
Butthe RMSforecasts at the Forecast Group (and Room Class) level, and at that level you see differences. For example, for a corporate Forecast Group, demand is highest on the Tuesday, then decreases.
These examples are for a period that is almost a year into the future. With no or very little On Books (1, 2, and 3) the patterns  look very similar for multiple weeks. Where more On Books exist (arrow), the system varies the forecasts. And if On Books are stronger than the system expected, it might interpret that as stronger demand and increase the forecast.
Patterns can vary for repeat Special Events becausethe RMSuses the patterns of the last occurrence to forecast the next one. In this holiday example, December 21 to 25 is set up as a four-day Special Event. The following shows last year's occurrence when December 24, a Saturday, had higher demand than the other three days.
In the next, upcoming year, visual the green line shows thatthe RMSforecasts the same strong demand for December 24. But this year that date falls on a Friday and the demand for Saturday, December 25, might follow the normal day-of-week patterns and be stronger. If so, adjust the Special Event or override demand.
Look at the below scenario, step one. You might ask why the orange Occupancy Forecast for this Room Class is so high, close to capacity. And why the green System Total Demand is below the Occupancy Forecast. Step 2 shows that in the past, Demand for that Room Class was well below capacity.
To explain, we switch from Booked to Stayed. In step 3 we see that final Occupancy On Books for this Room Class was usually close to capacity. This is due to upgrades, enabled by Room Type Overbooking and theUpgrade Path. The difference between System Total Demand and Occupancy Forecast is becausethe RMSexpects upgrades in the future too.
