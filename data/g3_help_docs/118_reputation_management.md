# Reputation Management

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reputation/Reputation-Management.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reputation/Reputation-Management.htm`
- **Ingestion Date:** `2026-09-11 22:13:27`

---

# Reputation Management

Reputation Management is an optional feature that combines rate shopping with reputation management data, helping you improve your performance by visualizing your market position. Use  Reputation Management to:
- Find opportunities for improving your reputation score and for increasing your pricing, seeReputation Quadrant.
Find opportunities for improving your reputation score and for increasing your pricing, seeReputation Quadrant.
- Understand how your reputation score impacts your performance, see theReputation Performancechart.
Understand how your reputation score impacts your performance, see theReputation Performancechart.
- Improve the system's pricing, seeunderstand the impact onG3 RMSpricing(ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.).
Improve the system's pricing, seeunderstand the impact onG3 RMSpricing(ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.).
If you are interested, review the following data requirements.

### Data Requirements

To use Reputation Management, your property must have the following:
- A subscription to the Reputation Management module inG3 RMS.
- A subscription to a certified reputation management data feed for your property and your competitors. This vendor collects the review history from review sources, calculates reputation scores, and sends that information toG3 RMSduring daily extracts. See the time of the last extract inImportant Information.
- Rate Shoppingdata inG3 RMS.
- At least three matching competitors from rate shopping and reputation data (which can include your property). SeeCompetitor Mapping â Reputationabout how to match the hotels.
- TheUse Rate Shopping Datachecked inCompetitor Settings. A competitor that is not checked doesnotimpact pricing, even if its reputation data is available.
- A minimum of 90 days with both rate shopping and reputation data from matching competitors. Pricing inG3 RMSis not influenced by reputation data until this minimum requirement is met.

## Best Practices

### Understand How Reputation Data ImpactsG3 RMSPricing

When you enable Reputation Management,  the reputation data influences the system's pricing decisions  (ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.).G3 RMSstill produces a single pricing decision for each day (and for each LOS, if applicable).
G3 RMSuses the data to adjust the effect of publicly available competitor prices. The system's analytics evaluate where your property is positioned competitively and identify opportunities to increase rates, accounting for recent trends and day of week patterns. For example, if your competitors have poor reputation scores,G3 RMSconsiders that their guests are less likely to pay higher rates.  At a result, the system might determine that your property can charge higher rates.
Reputation-influenced pricing will not reduce your price due to negative reviews or ratings. Using pricing to address a low average reputation score can have a long-term impact on the rates that you can expect to achieve. Instead, the system's analytics help drive rates when there is an opportunity to do so based on the position of your property against its competitive set, with respect to rate and reputation.
If your  reputation scores are poor, address the issue outside of pricing within your operational teams.  Use theReputation Performancechart to quantify how an increase in your reputation score impacts your property's performance.

### Make SureG3 RMSReceives Reputation and Rate Shopping Data

Reputation Management data extracts are processed on a daily basis. Similar to rate shopping, IDeaS is dependent on the reputation management vendor for daily delivery of the data extract. IfG3 RMSdoes not receive a reputation or rate shopping extract, the system calculates reputation-influenced pricing based on the latest available data.

### Contact IDeaS Before Changing Vendors

Changing reputation management vendors requires re-integration work and historical data from the new vendor. Contact IDeaS support before changing vendors to ensure that they have a certified integration with IDeaS.

### Understand How Reputation Management Handles Data

- Reputation Management considers the overall guest rating, not by specific types, like leisure versus corporate.
- Reputation Management removes the data of Special Events as outliers, replacing it with the typical values of neighboring dates.
- Reputation data is provided at the property level, even if your property shops for rates by Room Class.G3 RMStreats reputation data equally for all Room Classes.
