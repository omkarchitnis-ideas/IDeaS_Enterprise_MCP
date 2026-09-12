# Rate Shopping

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping.htm`
- **Ingestion Date:** `2026-09-11 22:12:46`

---

# Rate Shopping

Withmarket data  enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.,G3 RMSunderstands that your demand is not only impacted by your pricing but also by the pricing of your competitors. Use Rate Shopping setup to control howG3 RMSuses the competitive pricing data that is publicly available. It includes steps to manage which competitors' prices impact your pricing decisions and how channels display in the system.

### What Help Do You Need With Setting Up Rate Shopping?

- I want an overview of the topic.What are the steps and benefits of setting up Rate Shopping?
- I want to know more details.How doesG3 RMSuse rate shopping data?
- I need to ensureG3 RMScompares my competitors' room types to our equivalent Room Classes.How do I complete Room Class Mapping?
- I need to manage how channels display.What are the steps for Channel Settings?
- I need to define howG3 RMSuses our competitors' pricing.How do I complete Competitor Settings?
- I need to ensureG3 RMSdoesn't use outdated rate shopping data.What are the steps to set up the Rate Shopping Schedule?
- My property needs to maintain a certain pricing position in the competitive set.How do Competitive Market Position Constraints work?
- My property is switching to a new rate shopping vendor.What are the steps for Vendor Mapping?
- My property subscribes to the Reputation Management module.What are the steps for Competitor Mapping â Reputation?
- I need to see the most recent data from all my competitors and all channels. Where can I see myCompetitor Details?

### Understand How to Set Up Rate Shopping for the Best Forecast and Decisions

Your browser does not support the video tag.

## Use of Competitors' Data

If enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.,G3 RMSuses your competitorsâ rate shopping data to improve its forecasts and decisions. By being able to use rate shopping data the system knows what you know.
SeeRate Data Advantage and Standard Rate Shoppingto learn about how the use of data differs between them.

##### Reference Price

G3 RMSuses rate shopping to understand how your pricing influences demand relative to your competitors. To do that, the system uses and calculates a Reference Pricefor the primary priced product and, if used, for any independently priced product. It considers:
- Your historical  pricing (for the market segments with theBase Productattribute).
- Thefloor, orlowest value,of the available price range, includingfloor overrides.
- Your competitorsâ historical pricing position and how that compares to their current pricing (excluding dates when current pricing greatly deviates from historical pricing).
- Whether any competitorsâ pricing is closed, indicating compression.
- How much impact the competitor has on your demand. For example,G3 RMSfound that whenever Hotel A lowered its prices in the past, there was significant negative impact on your demand. But Hotel Bâs price changes in either direction had little impact.
With the Reference PriceG3 RMSalso usesprice sensitivity, in other words, how much more or less demand exists if the price changes.

#### Example of how rate shopping data impactsG3 RMS:

G3 RMSforecasts 100 rooms of remaining demand for a certain date, based on the current rate shopping information. Next, a competitor whose pricing has historically had a big impact on your demand raises its price. With the new price difference,G3 RMSnow expects 110 rooms of demand at your current price point, because it knows how your pricing influences demand relative to your competitor.
G3 RMScould also suggest to raise your price to a higher level, at which it expects only 90 rooms. The system would make this choice if the optimization shows that the revenue gain from the higher price offsets the revenue loss from the lower demand.
Note thatG3 RMScalculates price sensitivity and Reference Price also for business that is linked to BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.). Thatâs because the pricing for BAR  is often much higher than the discounts linked to BAR. Linked demand is a large factor in pricing, seePricing Calculationfor more details.
You can also set up Competitive Market Position Constraints that forceG3 RMSto maintain a specific positioning of your rates against the rates of your competitors. These constraints limitG3 RMSin finding the optimal pricing decision, so they are not enabled by default. SeeCompetitive Market Position Constraintsfor more information.
View this video to learn more about howG3 RMSuses rate shopping data.
Your browser does not support the video tag.

## Data Not Shopped

To optimize demand,G3 RMScreates a grid of competitor prices for each arrival date and length of stay (LOS). To do that, the system needs at least LOS1 data, but it uses all available data, for any LOS and any Room Class. If needed, it completes  unavailable data with approximations, see the following details:

### If You Shop Only for LOS1

For properties that useBAR by Day pricing,G3 RMSuses rate shopping data for a one-night length of stay (LOS1). For properties that use BAR by LOS pricing, however, an LOS1 price is very different from a LOS3 price. For these properties,G3 RMSlooks for available rate shopping data for other LOS. If the system does not find this data, it uses LOS1 for each date, and uses averages of the LOS1 data to influence the BAR by LOS decisions.

### If You Shop for Only One Room Class

If you rate shop for only one Room Class, the pricing recommendations for your other Room Classes, which are not mapped to competitive room types, are influenced by the competitor rates shopped for the one mapped Room Class.G3 RMSdoes not rely only on the Room Classes that are shopped.
For the Room Classes that are not mapped to competitor room types, the system infers a representative value of competitor rates, based on the known price gaps between Room Classes.
For example, you shop for the Standard Room Class, but your competitors also have Deluxe and Suite Room Classes similar to yours. In this case,G3 RMScalculates your other Room Classes based on the Standard Room Class and the known gaps between it and the other Room Classes.

## Your Own Rate Data

G3 RMSneeds to include the rate shopping data from your property to compare to competitors' data. For this reason, the system includes your property by default inCompetitor Settings. You cannot change this setup.
The system looks at your propertyâs historical rate shopping data (where available) against the competitorsâ prices charged at the same time to estimate price sensitivity for the property. In each snapshot,G3 RMSestimates the difference between your final sale prices and the competitorsâ rates in the shopped information.
G3 RMSdoes not use your property's rate shopping data on a forward-looking basis. Rather, the system optimization selects the optimal price and uses it for estimating future demand.

## Data Requirements

G3 RMSneeds to learn how much a competitor's pricing impacts your demand. If your rate shopping vendor provides 90 days of historical data,G3 RMSmeasures the impact right away. Without historical data, the system measures the impact 90 days after it received the first rate shopping data file (it needs at least two files).
Competitive Market Position Constraintsdonât require historical data for a new competitor. If you have enabled this feature, a new competitor may impact your pricing immediately.
