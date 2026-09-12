# Howthe RMSDetermines Pricing

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BAR-Calculation.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BAR-Calculation.htm`
- **Ingestion Date:** `2026-09-11 22:14:56`

---

Understand HowG3 RMSDetermines Price

# Howthe RMSDetermines Pricing

The RMSperforms the price optimization together with the inventory optimization. This means that it maximizes revenue, not average daily rate. It uses an all-around optimization approach with many variables, granular data, and complex analysis to determine that best mix between Pricing, Last Room Value, and Overbooking. In Pricing, you can see the pricing decision thatthe RMSproduced.

## Key Factors Thatthe RMSConsiders

View the video in Resources on the right for a visual summary of the key factors thatthe RMSconsiders.
Your setup  is the primary input to pricing, since the system must pick the optimal pricing decision from the price spectrum that you defined. Therefore, it's important that you usePricing setup toshare your pricing strategywiththe RMS.
For pricing Room Classes, the system also considers anyMinimum Price Differentialthat you set up as part of your Rooms Configuration.
If you use linked products, seeUnderstanding Howthe RMSPrices Linked Products.
- The volume of demand, or how many rooms are on books, how many are still expected, and how much of that demand is expected to wash. Review thedemand and wash forecast, or learn more abouthowthe RMSforecasts unconstrained demand.
- The value of demand. A strong indicator of that value is the historical Unqualified ADR. Competitors' pricing, especially if they are pricing a lot higher, is another big factor.
- The uncertainty of the demand to come. For example, far into the future uncertainty is high andthe RMSmight price lower.You can see uncertainty in theActual versus Expected On Booksdata in the Investigator.Another example is the impact on LRV. A 0.00 LRV day has the same impact on restrictions as a 0.01 LRV day, but the uncertainty might be very different: for the 0.00 day,the RMSis certain that demand is not enough to fill the property. But with 0.01 LRV, there is still some uncertainty about the volume of demand. There might be a chance that demand reaches or surpasses capacity as the arrival date approaches and asthe RMSreceives more data.
- Available Capacity to Sell, which is the Physical Capacity plus Overbooking, minus On Books, and minus Out of Order. Setup settings like overbookingor the upgrade pathmight affect that capacity. Therefore, they also impactthe primary priced product.
Often called willingness to pay, price sensitivity measures howthe primary priced productaffects demand, and vice versa. The system calculates the overall price sensitivity of the unqualified and the linked qualified demand based on the actual booking patterns that it receives from theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.. The system monitors the volume ofthe primary priced productreservations and models price sensitivity by season, day of week, and time left to arrival.  All price sensitivity models are then used to calculate the expected demand volume for each price point.
The system considers the impact on all demand that is attributed asLinked to Base Productwhen selecting the optimal price. Therefore, pricing might result in very little ofthe primary priced productbusiness itself, but because of the impact on demand that is linked tothe primary priced product, it is still the pricing that produces the maximum revenue.
A qualified discount that is 10% offthe primary priced productis considered linked since a change in pricing changes the price of this qualified discount. The system assumes the same applies to all unqualified demand, sothe primary priced product-linked demand includes all unqualified business and all Linked to BAR qualified business.
The RMScalculates the remaining capacity and the remaining demand for all lengths of stay (LOS). If your system is set up for BAR by Day,the RMSconsiders all demand that stays over an occupancy day and finds the optimal pricing decision for that one day. With a BAR by LOS setup ,the RMScalculates price decisions by arrival date and for each LOS between 1 and 8 nights.
With BAR by LOS pricing, the blended price might differ from the sum of the individual days. This example shows the BAR prices for a Monday 3-night stay and for the equivalent 1-night stays:| Length of Stay | Monday's Price | Tuesday's Price | Wednesday's Price | Total |
| --- | --- | --- | --- | --- |
| 3 Nights | 175 | 175 | 175 | 525 |
| 1 Night | 225 | 225 | 100 | 550 |In sum, the 1-night stays are $25 more than the 3-night stay. In this case,the RMSdetermined that pricing the 3-night stay lower than the separate 1-night stays maximizes revenues, due to variations in demand or price sensitivity.
In sum, the 1-night stays are $25 more than the 3-night stay. In this case,the RMSdetermined that pricing the 3-night stay lower than the separate 1-night stays maximizes revenues, due to variations in demand or price sensitivity.
Ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.the RMSanalyzes how you priced in the past compared to your competitors. And it measures how much impact each competitor had on your demand. Based on that, the system calculates the impact of future competitor prices on your demand.
For more on how rate shopping data helps the system generate better demand forecasts and pricing decisions, viewHowthe RMSUses Competitors' Data.
When calculating the pricing decision,the RMSdoes not consider contracted Group Rates, meaningthe RMSmight pricethe primary priced productbelow an already contracted group rate. If necessary, useFloor Overridesto alignthe primary priced productwith group rates.
