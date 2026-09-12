# What If

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Optimization/What-If.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Optimization/What-If.htm`
- **Ingestion Date:** `2026-09-11 22:13:13`

---

# What If

Use a What If to understand the, often unintended, results of adding or removing overrides. For example, the What If for an override lowering the overbooking shows you that it  increases pricing and LRV. That helps you  decide if the override is the best solution, especially for those with a large impact, like pricing or Multiday overrides.
If you can't run a What If, seeUnderstand when What If is available.
- Add or remove aPricing Override,Demand Override, or anOverbooking Override.What If is a simplified preview of anoptimizationThe step in the RMS Processing when the system uses the demand forecast (volume and value), the available capacity to sell, your configuration, and your interactions (like events, overrides) to calculate the outputs that maximize your revenues or profits. Outputs include pricing for the primary priced product, LRV, and overbooking. An Optimization also updates the constrained Occupancy Forecast., comparing the conditions after the override to the ones after the last optimization. If you already saved other overrides since the last optimization and now apply more, a What If compares the impact of all overrides, not just the last one.
What If is a simplified preview of anoptimizationThe step in the RMS Processing when the system uses the demand forecast (volume and value), the available capacity to sell, your configuration, and your interactions (like events, overrides) to calculate the outputs that maximize your revenues or profits. Outputs include pricing for the primary priced product, LRV, and overbooking. An Optimization also updates the constrained Occupancy Forecast., comparing the conditions after the override to the ones after the last optimization. If you already saved other overrides since the last optimization and now apply more, a What If compares the impact of all overrides, not just the last one.
- ClickWhat If. Results open in a new window.Note: the completion time for the What If analysis depends on the number of days it covers. If you saved multiple overrides since the last optimization, What If covers all days impacted by those overrides, including the time in between. The analysis time for this type of scenario may run considerably longer than a single-day override.
- Change the displayed data, as needed:The default Daily Details view shows Pricing values. ClickOverbooking & LRVto display these other decisions.Select theShow Old Valuescheckbox to show values before adding or removing  the override.To hide or show columns, click to open the menuon the right side of the column headers. Click an available column listed in the window to display or hide it. Visible columns are marked with a dot icon.
- The default Daily Details view shows Pricing values. ClickOverbooking & LRVto display these other decisions.
- Select theShow Old Valuescheckbox to show values before adding or removing  the override.
- To hide or show columns, click to open the menuon the right side of the column headers. Click an available column listed in the window to display or hide it. Visible columns are marked with a dot icon.
- Analyze the results. SeeData Detailsbelow. Click the Excel iconto download all the results to a spreadsheet.
- ClickClosewhen your review is complete.
- Return to the page where you placed or removed the override. Decide to save or cancel:If your analysis of the results confirms the need to add or remove the override, clickSaveto finalize the override change. Note that you don't finalize the values displayed in the What If.If you added an override, the new override value displays, and an icon indicates the active override.If you removed an override, the override icon no longer displays, but the old override value remains.Adding or removing overrides impacts forecasts and other decisions only in the next optimization. For example, a demand override leads to a different price. The changed price is sent to yourSelling SystemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.in the nextprocessing. You can send a price override immediately by clickingUpload.If you are no longer certain that the changes are the correct choice, clickCancel. We recommend that you  keep monitoring the situation until you know more, or the situation changes.
- If your analysis of the results confirms the need to add or remove the override, clickSaveto finalize the override change. Note that you don't finalize the values displayed in the What If.If you added an override, the new override value displays, and an icon indicates the active override.If you removed an override, the override icon no longer displays, but the old override value remains.Adding or removing overrides impacts forecasts and other decisions only in the next optimization. For example, a demand override leads to a different price. The changed price is sent to yourSelling SystemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.in the nextprocessing. You can send a price override immediately by clickingUpload.
- If you added an override, the new override value displays, and an icon indicates the active override.
- If you removed an override, the override icon no longer displays, but the old override value remains.
- Adding or removing overrides impacts forecasts and other decisions only in the next optimization. For example, a demand override leads to a different price. The changed price is sent to yourSelling SystemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.in the nextprocessing. You can send a price override immediately by clickingUpload.
- If you are no longer certain that the changes are the correct choice, clickCancel. We recommend that you  keep monitoring the situation until you know more, or the situation changes.

## Data Details

Higher pricing in a What If might also mean lower occupancy forecasts.G3 RMSunderstands that at a higher price point, there may be less demand available than at the lower one.
Match the letters in this example with the corresponding ones in the following list:
- TheNet Variance Summaryshows you  the overall impact of the change for the changed date and the seven days before and seven days after the change. The extended range helps you understand the impact on surrounding days, due to guests staying over.
TheNet Variance Summaryshows you  the overall impact of the change for the changed date and the seven days before and seven days after the change. The extended range helps you understand the impact on surrounding days, due to guests staying over.
- At the top, review the changes at the total property level.
At the top, review the changes at the total property level.
- Below that, view the  Room Class level changes.Keep in mind that the system optimizes all decisions together, so an overbooking override may also change other values like theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).and pricing.
Below that, view the  Room Class level changes.Keep in mind that the system optimizes all decisions together, so an overbooking override may also change other values like theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).and pricing.
- Arrows indicate the changes cause an increase (green) or decrease (red) in the values.
Arrows indicate the changes cause an increase (green) or decrease (red) in the values.
- In the lowerDaily Detailspane you see  the decisions for the override dates.
In the lowerDaily Detailspane you see  the decisions for the override dates.
- If you select toShow Old Values, you can compare those values (prior to adding or removing the override) to the expected New values (after the change).
If you select toShow Old Values, you can compare those values (prior to adding or removing the override) to the expected New values (after the change).
If you enabledProfit Optimization,  the Net Variance Summary also shows the changes in Profit metrics:

## Best Practices

### Understand When What If Is Available

What If is not available:
- If is not included in your subscription.
- When you override wash at the individual group level.
- Whenthe RMSsends decisions to your  selling systems and displays an upload iconnext to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert..
- For overrides ofLinkedorIndependentproducts.

### Use What If to Measure Strategic Goals

- If you know how much extra business a special promotion or marketing campaign delivers, measure that business against what the system currently predicts. Then compare the revenue gain against the marketing costs.
- A similar analysis can review a business mix change to compare the additional revenue from the targeted market segment against the increased cost of sale or displacement of business from other segments.
- You can also use the What If function to examine less frequent situations. For example, use it to help determine the best and worst case scenarios on the impact to your business if a neighboring hotel is going into renovation.
