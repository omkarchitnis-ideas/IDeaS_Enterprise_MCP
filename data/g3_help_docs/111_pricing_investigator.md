# Pricing Investigator

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Investigator.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Investigator.htm`
- **Ingestion Date:** `2026-09-11 22:13:22`

---

Understand HowG3 RMSDetermines Price
Understand How Demand Impacts Pricing

# Pricing Investigator

Use Pricing Investigator to review what influencedG3 RMSwhen it selected a specific price.

### What Help Do You Need with the Investigator?

- Show me thestepsto interact with the Pricing Investigator.
- I need to gain confidence and trust in the pricing. Show me how to review key drivers of the price in theProperty Overview.
- I need to review the price for a specificRoom Class:I need to review ifPrice Rankingimpacts the demand and the price of another Room Class.I need to check if setup of Floor and Ceiling keepsG3 RMSfrom pricing as high as myCompetitors.I need to understandhow much specific factors influence the price.
- I need to review ifPrice Rankingimpacts the demand and the price of another Room Class.
- I need to check if setup of Floor and Ceiling keepsG3 RMSfrom pricing as high as myCompetitors.
- I need to understandhow much specific factors influence the price.
- I need to explain to a colleague or supervisor why a price override often isn't the best solution. Show mehowG3 RMSdetermines pricing.
- I need to understand howG3 RMSdetermines thepricing between Room Classes.
- I need to investigate theLRVfor a specific date and Room Class.

## Investigation Steps

- Clickand thenInvestigator. The default selection isPricing.
Clickand thenInvestigator. The default selection isPricing.
- Click the calendarto select the date to investigate. The data for that date loads automatically.
Click the calendarto select the date to investigate. The data for that date loads automatically.
- Click the back arrowor forward arrowto move to the previous or next occupancy date.
- Click the noteto view and add notes for the date. A check markindicates that a note already exists.
- Click the PDF iconto save the results to a PDF file.Attach the PDF file whenever you create a case forIDeaS Supportabout pricing.
- ClickGo to Pricingto review pricing information for the same occupancy date.

#### Interacting with the Graphs and Tables

- Point to elements in the charts, like bubbles or lines, to see numerical values.
- Click an item in the legend to hide the item from the chart. Click it again to restore it.
- In the Pricing Details table, select theRoom ClassandRoom Typefor which you want to see Occupancy Forecast, pricing and LRV data.
- Click theprice linkin the Pricing Details table to drill down to the Room Class level data.
Your browser does not support the video tag.

## Investigate the Property Overview  Details

When you disagree with the system's price,  first review thedemand forecast. That is because the volume and value of all demand compared to capacity impacts theprice calculation.
Use theOccupancy Forecastgraph to review the demand forecast, and then theBooking Pacegraph to compare the On Books against the average On Books of the previous weeks (for the same day of week).
The Occupancy Forecast chart  shows occupancy on books, and the unconstrained and constrained forecasted occupancy, all compared to capacity.
Use the Booking Pace chart to compare the booking pace of the last 30 days against the average On Books of the previous weeks with the same day of the week. To see more pace data, review thePace Data tab.

## Investigate the Pricing Details

The Pricing Details display below the property overview graphs and shows pricing data by Room Class for the selected date and the three days before and after it.
This table helps you to understand how the system optimizes pricing for an entire period and Room Class hierarchy.
Click the  link to openCompetitor Detailsand view the data from all competitors and all channels. Review this data to understand how competitors' prices influence your price (ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.).
Check the remarks to ensure that you view comparable prices.  For example, if you comparethe primary priced productto the competitorsâ discounted Loyalty Program price, thenG3 RMStends to price lower.
The data in Competitor Details changes depending on the Room Class that you selected above the table:
- All Room Classes: Shopping data for all Room Classes that are mapped to a competitor room type.
- Single Room Class: Shopping data for that single Room Class, if it is available.

## Investigate the Room Class Details

In the Pricing Details table, click a price link for a room type to open pricing details for the selected date and Room Class. The details  show you more granular data than the property level data at the top of the Investigator page.
For properties in countries withTax-inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., the values for Final Price, Floor, Ceiling, Historical Price (Projections BAR for Synthetic Data) and the competitor prices include the tax percentage that you set up.
G3 RMSconsiders many factors when it calculates the price. The indicators show you three factors, demand, competitors (if  enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.), and LRV, and which of those push the prices for the selected Room Class higher or lower. If you enabledProfit Optimization, they also display for channel costs, service costs, and ancillary revenues.
For example, forDemand Priceyou see this indicator. That means that the forecasted demand and the price sensitivity (without considering your competitors' pricing) is a big influence in suggesting higher price. If the needle is in the yellow (pointing up), there is little impact. If it points to the red on the left, Demand Price is a big factor for lower prices.G3 RMSalso points out strong influences with a pricing explanation.
These factors help you understand the different influences. They don't represent the complexity of the system's calculations.
Some  data conditions are so meaningful for pricing thatG3 RMSpoints them out to you with a light bulb icon and a short explanation. If there are multiple explanations, click each bulletto read all of them. For example:
- When the system selects the highest possible price. If you observe this condition repeatedly, it might mean that you need to expand your price range setup.
- When the system selects a price that doesn't meet the Minimum Price Differential for this Room Class. It means that your pricing setup  and price ranking don't allowG3 RMSto select a value that meets the Minimum Price Differential.
- The  occupancy forecast percentage, at the property level.
- The percentage change in the booking pace compared to the same day of the week from the five prior weeks, excluding Special Event days. As an example for the pace comparison, the number of rooms on books for arrival date Saturday December 29 compared against the average on books of the preceding Saturdays, December 22, 15, 8, 1, and November 24. Note that Special Event days are excluded, so if November 24 was a Special Event the system adds November 17 to the comparison group.
- The lowest and highest price points that you set up inPricingand your competitors' lowest and highest price points from rate shopping data. Both are for the selected Room Class and occupancy date.
- TheHistorical Pricefor the Room Class and date  ( for Synthetic Data properties: Projections BAR).
- TheAvailable Capacity to SellPhysical Capacity plus Overbooking minus On Books and minus Out of Order. This value is the number of rooms that the RMS can sell before the property or room type is sold out.for the Room Class. It's calculated as Capacity plus Overbooking minus Out of Order minus On Books. This value is the number of rooms that the system can sell before the property or room type is sold out.
- TheRemaining DemandThe remaining unconstrained demand for a date in the future. This value is either generated by the RMS or, in case of an active user demand override, the user override value plus or minus a possible system adjustment. The RMS adjusts a demand override according to the booking pace, so the override remains accurate after its implementation.for the Room Class and for market segmentsattributedas Unqualified or Qualified, Linked to BAR and Yieldable.
- The Remaining Demand for the Room Class for all other market segments.
- Whether there is enough demand to fill the Room Class, and if it can accept demand from a lower-ranked Room Class due to theUpgrade Path. Use this to review theLRV. ClickSee more detailsand compare the Remaining Demand - Total against theAvailable Capacity to SellPhysical Capacity plus Overbooking minus On Books and minus Out of Order. This value is the number of rooms that the RMS can sell before the property or room type is sold out.for the selected Room Class. If remaining demand is larger, then there is enough demand to fill andG3 RMSuses LRV to restrict demand. You can also view the remaining demand by Forecast Group to analyze its mix.
Use the Price Ranking chart to understand how the value and type of demand versusEffective CapacityThe property's physical capacity minus the out of order rooms.affects pricing for the selected day and the three days before and after that day. Review the data for the selected Room Classand, based on the upgrade path, the neighboring Room Classes,and for shoulder days.
For an example of demand impact across Room Classes, seeInvestigate LRV across Room Classes.
If you have anAdvanced Price Ranking and Upgrade Path, move the charts to view the neighboring towers that connect to the selected Room Class.
Use the Competitors chart to see the relationship between your price, the price range that you gave to the system, the publicly available prices of your competitors,  the LRV, and the Historical Price (for Synthetic Data properties: Projections BAR).
For properties in countries withTax-inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., the values for Final Price, Floor, Ceiling, Historical Price (Projections BAR for Synthetic Data properties) and the competitor prices include the tax percentage that you set up.
The Pricing Pace chart shows how your price (as of each nightly processing) changed in the last 30 days. Compare that to how your competitors' prices have changed over the same period.
This chart shows theOccupancy DemandThe remaining price-able unconstrained demand that will stay over an occupancy date in the future. It is limited to market segments that are impacted by pricing changes (all unqualified and all linked qualified market segments) and only applies to the selected Room Class or Room Type.for theOptimal Price, or thesystem's selected price point, compared to the demand for the neighboring higher and lower price points. The chart helps you understand how theprice sensitivityof the demand is influencing the systemâs price. A steep curve shows that price sensitivity is very elastic. A shallow curve shows that price sensitivity is inelastic.
ClickPricing Configurationto see a summary of pricing setup for the Room Class and occupancy date. The Pricing setup summary shows the following data:
- Base Room Typefor all Room Classes
Base Room Typefor all Room Classes
- Rounding Rulesfor the Final Price
Rounding Rulesfor the Final Price
- TheCeiling/Floorfor all Room Classes and days of week that include the investigated date
TheCeiling/Floorfor all Room Classes and days of week that include the investigated date
- Offsetsfor all room types in the Room Class for all days of the week that include the investigated date
Offsetsfor all room types in the Room Class for all days of the week that include the investigated date
- Supplements, if enabled, for all room types in the Room Class
Supplements, if enabled, for all room types in the Room Class

## Pricing at the Room Class Level

Demand levels vary by Room Class and the pricing needs to reflect that. While demand might vary by Room Type,G3 RMSdoesn't price at the room type level because it's often not the best solution:
- There is more data at the Room Class vs. the room type level, leading to lower uncertainty.
- Pricing each room type means more decisions, which means more complexity when you set up and monitor pricing.
- Many properties need to  control the differences between room types, for example, that a Standard Two-Doubles room type is always priced higher than Standard King.
If your reservation system doesn't support different pricing by Room Class, theMaster Class PriceMaster Class price  applies to all other Room Classes.
Demand  varies by Room Class and thereforeG3 RMSprices by Room Class. The difference in pricing between Room Classes mainly reflects the difference in  remaining "price-able" demand (all unqualified and qualifiedLinked to BARbusiness). For example, if the remaining demand for your Suites is low, but the remaining demand for Standard rooms is high, the price difference  tends to be smaller. If there is plenty of demand for Suites, the price difference is larger.
Note that Room Class pricing also considers anyMinimum Price Differentialthat you set up as part of your Rooms Configuration. For all inputs into pricing, seeHowG3 RMSDetermines Pricing. Use theInvestigatorto review how Room Class demand impacts your price.
HowG3 RMSlooks at remaining "price-able" demand depends on thePricing Method:
- BAR by LOS properties:G3 RMSlooks at remaining demand for a given arrival date and LOS. In the system this demand is calledArrival DemandIn G3 RMS, the remaining price-able unconstrained demand that will arrive on a date in the future. It is limited to market segments that are impacted by pricing changes (all unqualified and all linked qualified market segments) and only applies to a selected length of stay and room class..
- BAR by Day or Continuous Pricing properties:G3 RMSconsiders all demand staying through a particular date (since only one price point is set). CalledOccupancy DemandThe remaining price-able unconstrained demand that will stay over an occupancy date in the future. It is limited to market segments that are impacted by pricing changes (all unqualified and all linked qualified market segments) and only applies to the selected Room Class or Room Type..
G3 RMSdoesn't account for upgrade fees on or around the date of arrival. However, you can still use Room Class pricing as an indicator to determine the supplement for upgrades. The price difference between Room Classes indicates what the system expects. Whether the difference in Room Class pricing is low or high at a point close to arrival is a strong consideration for setting upgrade supplements.
This relative difference is especially important where the remaining demand is high, andG3 RMSmight look for opportunities to sell a Room Class rather than offering discounted upgrades. Where remaining demand is low, the Room Class pricing difference may be lower. You might want to offer lower priced paid upgrades, particularly where lower Room Classes are overbooked. In this case,G3 RMSalso plans for required upgrades to maximize revenue from available inventory across Room Classes.

## Feedback and Support

At the bottom of the page, you can send IDeaS your feedback about Investigator. Click the star icons to provide a rating and click theTell us morefield to send feedback details.
If Investigator did not answer your questions about the system's price, clickExport Investigationto save the page as a PDF file. When you open acase, attach the PDF to the case. Sending us this information helps our support team understand the system settings and forecast conditions at that time.
