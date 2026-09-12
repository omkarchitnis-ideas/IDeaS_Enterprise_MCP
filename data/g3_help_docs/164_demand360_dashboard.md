# Demand360 Dashboard

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Insights/Demand360.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Insights/Demand360.htm`
- **Ingestion Date:** `2026-09-11 22:13:58`

---

# Demand360 Dashboard

Demand360 is an optional competitive market data tool available to allG3 RMSclients. It includes pace information by market segment, giving you insight into future demand. The optional feature to include Demand360's data inG3 RMSoffers two benefits:
- A Demand360 dashboard allows you to compare market occupancy to your occupancy and forecast.
- G3 RMSuses the market data to improve its forecast and decisions (if enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.). SeeHowG3 RMSUses the Datafor details.

## Dashboard Steps

- Clickand 
	 clickDemand360.
- Click the filter iconto change the displayed dates. The largest available date range is System Date - 30 days to the System Date + 60 Days.
- ClickTableorGraphto switch between the tabular and chart views of the data.
- In the Graph view, click any item in the legend to hide its bar or line in the chart.
- Click the export iconto export the details to a spreadsheet.

## Data Details

The following data 
	 elements display for the selected dates, in the graphical and tabular views:

## Best Practices

### Ensure ThatG3 RMSHas Data Files for 30 Days

If your property was already using the Demand360 service,G3 RMSreceives up to a year of historical Demand360 final data. If your property was not using Demand360 prior to signing up for this feature,IDeaSwill not receive any historical data. In that case,G3 RMSbegins considering Demand360 data for its forecast and decisions after receiving data files for 30 days, sinceG3 RMSmust understand the pace of this data. The 30-day period applies regardless of any competitor changes during that period. The time for setting up Demand360 inG3 RMSis typically completed in one to two weeks.

### Understand HowG3 RMSUses Demand360 Data

Demand360 sendsG3 RMSoccupancy on books data for your market, typically weekly. From the history of the occupancy pace,G3 RMSlearns how much a change in market occupancy influences your own occupancy.  Based on the size of the impact and future market pace information, the system can adjust your transient unconstrained demand forecast. With Demand360 data and ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.,G3 RMScan react to market trends earlier than if it has only your on books data.
Other considerations:
- G3 RMSmeasures if historical Demand360 occupancy is a reliable indicator of market demand, by days to arrival. The system only uses the data if it helps explain the market demand. The system reconsiders this each time it updates its forecast patterns. SeeSelf-Learningfor details.
- G3 RMSdoesn't use Demand360 group data. This is based on our research that high group demand at one property doesn't automatically mean high group demand for other properties. And if a property increases transient prices due to high group demand,G3 RMSlearns that from rate shopping data.
- G3 RMSconsiders combined transient Demand360 data, not each segment. If the system adjusts the forecast due to Demand360 data, it distributes the change at the Forecast Group and Room Class level.

### Understand HowG3 RMSHandles Your Competitive Set

Your propertyâs Demand360 competitive set does not have to match the Rate Shopping competitive set.
Changes to the competitive set in Demand360 have no impact onG3 RMS. The analytics inG3 RMSwere developed to account for comp set changes because such changes might occur at any time and even if you didn't instigate them (for example, because a comp set property no longer reports data).
The analytics inG3 RMSconsider business type mix (transient or group) of competitive bookings.
