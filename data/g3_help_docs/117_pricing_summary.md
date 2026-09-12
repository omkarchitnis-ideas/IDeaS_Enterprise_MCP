# Pricing Summary

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Pricing-Summary.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Pricing-Summary.htm`
- **Ingestion Date:** `2026-09-11 22:13:27`

---

# Pricing Summary

The Pricing Summary helps you  understand whyG3 RMSrecommends the price for the selectedselected Room Class and occupancy date.  Use the data to quickly review key inputs to pricing, including the impact of your own setup.

## Steps to Review

- Clickand thenPricing.
Clickand thenPricing.
- Calendar View displays if it's set up as the default inPreferences. Otherwise click.
Calendar View displays if it's set up as the default inPreferences. Otherwise click.
- You can access the Summary tab using the following options:Click theSummaryiconfor an occupancy dateClick the Final Price value for a room type and then click theSummarytab
You can access the Summary tab using the following options:
- Click theSummaryiconfor an occupancy date
Click theSummaryiconfor an occupancy date
- Click the Final Price value for a room type and then click theSummarytab
Click the Final Price value for a room type and then click theSummarytab
- Click the back arrowor forward arrowto move to the previous or next date. This is limited to your date selection on the Pricing screen.
- Review the selected arrival date and Room Class.
- If needed, change the selectedRoom Class. The options are limited by your Room Class selection on the Pricing screen.
- My Priceis theFinal PriceThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing.for theBase Room TypeThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class., or the final pricing decision thatG3 RMSsends to theselling system. The arrow next toMy Priceindicates an increaseor decreasesince the last processing. Point to the arrow to see the previous price.
- Click the PDF iconto download the results to a PDF file.
- Click the binoculars iconto open theInvestigatorand review more data. The page opens to theRoom Class Leveldetails, showing you more information about your setup, occupancy, demand and the factors that influence pricing.
- Point to elements in the charts, like bubbles or rings, to see numerical values.
- Click an item in the legend to hide the item from the chart. Click it again to restore it.
- In the Competitors bubble chart, click and drag over an area of the chart to zoom in. ClickReset zoomto reset the view.

## Data Details

In most cases,G3 RMSpresents the data for your review. But the system considers some data conditions so meaningful that it points them out to you with an  icon and a short explanation at the top of the window, for example:
- When the system selects the highest possible pricing decision. If you observe this condition repeatedly, it might mean that you need to expand your price range setup.
- When the system selects a pricing decision that does not meet the Minimum Price Differential for this Room Class. It means that your pricing setup  and price ranking do not allowG3 RMSto select a value that meets the Minimum Price Differential.

#### Learn More about Pricing Calculations

HowG3 RMSDetermines Pricing
The Competitors bubble chart shows you the relationship between your price, the price range  that you gave to the system, the publicly available prices of your competitors,  the LRV and the Historical Price (Projections BAR for Synthetic Data properties). If many competitor rates overlap and make it hard to view the data, zoom in by clicking and dragging to define the area you want to see. ClickReset Zoomto return to the default view.
The chart includes the following data:
For properties in countries withTax-inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., the values for My Price, Floor and Ceiling, Historical Price (Projections BAR for Synthetic Data properties) and the Competitor Price include the tax percentage that you set up.

#### Learn More about Pricing Influences

Rate Shopping Data Overview
Last Room Value
Sharing Your Pricing Strategy withG3 RMS
If your property has set upCompetitive Market Position Constraints, this setting displays in greenand you see the constraint value. If you don't use constraints, you seeNone.
The Pricing Pace chart shows your pricing decision as of each nightly processing for the last 30 days.  Use the chart to understand how your price has changed over a 30-day period. If you use Rate Shopping, you can compare the change to how your competitors' prices have changed over the same period.
The Pricing Pace chart shows the following data:
When you disagree with a pricing decision, your first step should be to review the demand forecast for that period. That is because the volume and value of all demand versus capacity is a primary input into the system's pricing decision. The Occupancy Forecast chart  shows occupancy on books, and the unconstrained and constrained forecasted occupancy, all compared to capacity. You can select to view the data either at the property level or at the Room Class level.
The Occupancy Forecast chart shows the following data:

#### Learn More about Reviewing the Forecast

Investigator - Forecast
This chart shows theOccupancy DemandThe remaining price-able unconstrained demand that will stay over an occupancy date in the future. It is limited to market segments that are impacted by pricing changes (all unqualified and all linked qualified market segments) and only applies to the selected Room Class or Room Type.for theOptimal Price, or thesystem's selected price point, compared to the demand for the neighboring higher and lower price points. The chart helps you understand how the price sensitivity of the demand is influencing the systemâs pricing decision. A steep curve shows that price sensitivity is very elastic. A shallow curve shows that price sensitivity is inelastic.
The chart shows the following data:

#### Learn More about Occupancy Demand by Price

Price Sensitivity
