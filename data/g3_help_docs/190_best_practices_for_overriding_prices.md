# Best Practices for Overriding Prices

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BP-Override-Pricing.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BP-Override-Pricing.htm`
- **Ingestion Date:** `2026-09-11 22:14:16`

---

# Best Practices for Overriding Prices

A Pricing override can have unintended consequences and thus is likely the least-used type of override. Instead of focusing on the tactical work of pricing each day, improve the pricing by sharing what you know withthe RMS, like special events, wash, and demand.
Go to the Resources on the right to view a video about when to use pricing overrides.

### Understand the Process to Decide If a Pricing Override is the Best Solution

Following this overview of the process, click on any of the steps to learn more. Download a PDF of the process in the Resources.
We recommend reviewing other factors becausethe RMSoptimizes all decisions together and a price override impacts the other decisions. For example, you use aFlooroverride to push the system's price higher. Based on price sensitivity,the RMSmight expect less demand and less revenue at the higher price. To offset that loss and maximize revenue, the system might lower the LRV to gain more bookings from lower-priced, yieldable demand. So you gain lower-priced demand despite raisingthe primary priced product.
To avoid such unintended consequences, review the following factors before any pricing override. To  understand whythe RMSselected a specific price, use theInvestigator. Or learn more abouthowthe RMSdetermines pricing.
If you disagree with the price because you expect unusual transient demand, add aSpecial Event. If it is a repeating event,the RMSuses  the previous instances to forecast and price optimally. If it's a one-time event, ensure you agree with the remaining demand, see the next point.
The amount of demand and its value are key considerations for pricing, so review the demand forecast. Another consideration is length of stay.The RMSconsiders not only demand for one day, but also the stay-through demand so it can maximize potential revenue for each arrival date. Use theForecast Investigatorto help you understand demand patterns and trends. If a large share of demand comes from groups, review and, if needed, overridegroup wash.
If you disagree with pricing often, review your setup to ensure itreflects your pricing strategy. For example, if pricing often seems too low, ensure that yourFloorvaluesare appropriate.
The RMSoptimizes all decisions together so an override can have unintended consequences on other decisions. Andthe RMSmaximizes revenue overall, not just for a single day, so review Pricing,Demand, andOverbookingoverrides also on surrounding dates. Removing these overrides might adjust the price to a value closer to your expectation.
The RMSconsiders the impact of your competitorsâ prices (if market data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.).  Thus, verify thatyour setupincludes only relevant competitors. For example, the system might price unusually low if you include a competitor that prices very low during a renovation.
The RMSoptimizes pricing to maximize revenue across all Room Classes, not just for a single Room Class. Therefore, a price for a single Room Class might seem wrong, for example, when the price is below the LRV, see thisLast Room Valuescenario.
Use theInvestigator Price Rankingcharts to review how Room Class demand impacts your pricing. And learn more about theprice difference between Room Classes.
You might have to override if you know something specific thatthe RMSdoes not. When you do override, select the appropriate type:
Enter a specific price forthe RMSto use only that price.
Note the following differences  when you apply a Specific override:
- To room types that are not the Base Room Typethe RMSdoesnotcheck if it aligns with your setup, likeOffsets, yourRoom Class Price Ranking, orMinimum Price Differentialsand it doesn't consider the impact of the price on demand, other decisions, and surrounding dates.
To room types that are not the Base Room Typethe RMSdoesnotcheck if it aligns with your setup, likeOffsets, yourRoom Class Price Ranking, orMinimum Price Differentialsand it doesn't consider the impact of the price on demand, other decisions, and surrounding dates.
- To the Base Room Type:the RMSadds the overrides to all room types in the same Room Class, including any applicableOffsets.
To the Base Room Type:the RMSadds the overrides to all room types in the same Room Class, including any applicableOffsets.
- On theTabular Viewor in aMultidayoverride:G3 RMSdisplays  Floor and Ceilinginstead of Specificicons. This is only a display difference, the override functions in the same way for all overrides to Base Room Types: for example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.
On theTabular Viewor in aMultidayoverride:G3 RMSdisplays  Floor and Ceilinginstead of Specificicons. This is only a display difference, the override functions in the same way for all overrides to Base Room Types: for example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.
A Floor override letsthe RMSselect the optimal price at or above, but not below, the value that you set. You can apply a Ceiling or Floor overrides only to the Base Room Type.The RMSuses the adjusted price range to select the Base Room Type price and uses theOffsetsfor other room types.
Note: Floor overrides impact theReference Price, so a floor override to a value higher than the current price might mean that the new price after the next optimization is above the new floor.
A Ceiling override letsthe RMSselect the optimal price at or below, but not above, the value that you set. You can use it together with a Floor override for the same occupancy date. When the system price is lower than the ceiling override, the system's price remains valid.
You can apply a Ceiling override at the Base Room Type level.The RMSselects the price for the Base Room Type based on the adjusted price range and uses the Offsets to price  other room types.
In the rare cases when you need to override pricing for more than just one day at a time, use aMultiday Pricing Override. While it's a convenient option, use it only after reviewingother factorsthat impact pricing. That's because any unintended consequences or a mistake impact a long period.
After you override a price, review the remaining demand, becausethe RMSdisplays the remaining demand for the current price. For example,the RMSprices at $100 and expects 100 rooms of remaining demand. You researched and know the demand is correct, but that you can price at $150. After you override the price to $150, the system lowers the remaining demand to 50, based on price sensitivity. Therefore, you override the demand to 100.
Pricing overrides  can have unintended consequences and are hard overrides thatthe RMSdoesn't adjust. Therefore, as part of yourregular tasks, review your pricing overrides at least weekly to ensure that they remain relevant. When 
 you add, remove, or review and keep an override, add a note 
 so that you understand in your next review why you added or removed the override and what the conditions were.
