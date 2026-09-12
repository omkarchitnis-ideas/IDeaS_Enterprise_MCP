# Profit Optimization

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Profit/ProfitOptimization.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Profit/ProfitOptimization.htm`
- **Ingestion Date:** `2026-09-11 22:14:36`

---

# Profit Optimization

For most clientsG3 RMSmaximizes room revenue. This means that the system bases its decisions likeLRVA control that blocks lower-valued yieldable business when the RMS thinks that your property might sell out. It ensures that you accept only the most valuable demand. For example, a $150 LRV means that guests can book a Flexible Rate product at $160, but not a discounted PrePay&Save product at $140. The RMS optimizes LRV by Room Class.only on the forecasted room revenue and number of sold rooms. Properties like casinos or resorts also consider ancillary revenue streams, like gaming, retail, or food and beverage outlets. For example, a casino might prefer a complimentary room of a high-value gambler over a high-priced room with low ancillary revenues.
Similar to howG3 RMSevaluates group business, Profit Optimization can consider other revenues and their profit percentage, plus any associated costs, like channel and servicing costs. Thus, with profit optimization,G3 RMS:
- Forecasts demand by Room Class and Forecast Group, and forecasts net revenues, profits, and costs associated with those Forecast Groups.
Forecasts demand by Room Class and Forecast Group, and forecasts net revenues, profits, and costs associated with those Forecast Groups.
- Optimizes the forecast by selecting the business mix from that demand that is most profitable.
Optimizes the forecast by selecting the business mix from that demand that is most profitable.
- Controls the business with profit-optimized pricing and LRV. For an example, seescenario 2.
Controls the business with profit-optimized pricing and LRV. For an example, seescenario 2.
- Monitors the results of the controls and adjusts the forecast as needed. You view specific profit metrics, seemonitoringfor details.
Monitors the results of the controls and adjusts the forecast as needed. You view specific profit metrics, seemonitoringfor details.
Note: to use Profit Optimization, a property must have:
- Representative spending data for each optimized  ancillary revenue stream, by room type and market segment.
Representative spending data for each optimized  ancillary revenue stream, by room type and market segment.
- A selling system that supports restrictions based on profit.
A selling system that supports restrictions based on profit.
See the following Profit Optimization workflow to understand howG3 RMSuses the additional data to calculate profit. See thescenario 1for an example.
Note: In this diagramG3 RMSuses all possible data options, but this varies by client. For example, Profit Optimization for an extended stay property might use only Servicing Costs (their single largest cost). A very complex property, like a casino, uses all options. If you're unsure about  your property setup, contact your corporate revenue management team or your IDeaS representative.

## Steps to Set Up, Manage, and MonitorG3 RMS

With Profit Optimization, there are some differences in how you set up and manageG3 RMS. Note that your property's Profit Optimization version might not include all configuration options listed in thepreceding workflow:

### Channel Configuration

If you are not already using the Channel Forecast dashboard, complete thissetup.

### Servicing Cost by LOS Configuration

Follow the steps and best practiceson this pagefor this setup, used only for Profit Optimization.

### Rate Shopping Configuration

Some Profit Optimization properties, for example, casinos that rely on ancillary revenues, want to build a base occupancy before they focus on maximizing room revenues. If that applies to your property, considerOccupancy-Based Constraints.

### Market Segment Configuration

Your market segments attribution was likely set up after consultation with IDeaS. For any questions about the specific setup, contact your IDeaS representative.
Note: when creatingForecast GroupsSimilar market segments combined by the RMS: You characterize market segments by adding attributes. the RMS combines similar market segments into Forecast Groups to ensure sufficient booking data. Forecast Groups with similar characteristics and enough data improve forecasting and optimization performance.,G3 RMScombines market segments not only based on their attributes and similar behavior, but also based on similar profit values.

### Monitoring and ManagingG3 RMS

When youreview forecasts and decisions, use the profit-specific metrics, like Profit per available room, to understand the impact of profit optimization.Note: These metrics exclude revenues from market segments with  theComplimentary attribute.
The metrics vary slightly by page. For an example, review the descriptions for theBusiness Analysis dashboard.
- The Data Details tab of the Business Analysis dashboard.
The Data Details tab of the Business Analysis dashboard.
- The Summary panel of the At a Glance dashboard.
The Summary panel of the At a Glance dashboard.
- The Data Extraction report.
The Data Extraction report.
- The Pickup/Change and Differential Control report.
The Pickup/Change and Differential Control report.
- A What If analysis of an override.
A What If analysis of an override.
- The Pricing Investigator.
The Pricing Investigator.
With full profit optimization,G3 RMSknows the total spend and profits for all market segments. Thus, the system can select the optimal price and LRV based on overall profitability.
As a very simplified example, a guest wants to stay at your casino and has a budget of 1,500 total. If the room price is 500, then they can spend 1,000 in the casino. If the room price is 1,000, they spend only 500 in the casino. Due to the higher profit margins of the casino,G3 RMSselects the 500 price because it is  more profitable overall. For an example of an optimized LRV, seescenario 2.
Before you save an override, especially a pricing override, run What If to compare the profits with and without the override. Viewing the profit changes next to other metrics and decisions can help you understand the system's focus on total profitability, rather than just room revenue. For example, you might see thatG3 RMSprices lower when it expects that this business  has high spending in ancillary revenue streams  and when those revenue streams have a high profit margin.

### Setup - Data from Your Business Intelligence System

Your Profit Optimization might include sending data like fixed costs and profit margins from your business intelligence system to IDeaS (for the full workflow, seethis preceding diagram). If that's the case, ensure that this data remains current and correct. If needed, check with the team responsible for the data transfer, like the IT department. Or, ask your IDeaS representative when the data was last updated.

## Scenarios

### Scenario 1 - Profit Calculation

Review this scenario of a casino to understand howG3 RMScalculates total profit:
- The reservation is for 3 nights with ancillary revenues, including gaming.
The reservation is for 3 nights with ancillary revenues, including gaming.
- Open the following workflow to see how the numbered list with the calculations aligns with that process.
Open the following workflow to see how the numbered list with the calculations aligns with that process.
- Expected ancillary revenues and profit margins from the property, based on their tracking of historical data:Profit margin: food = 25%, beverage = 40%, and gaming = 80%.$400 food revenue x .25 = $100.$200 beverage revenue x .4 = $80.$400 gaming revenue x .8 = $320.Thus, total ancillary profit is$500(100+80+320).
Expected ancillary revenues and profit margins from the property, based on their tracking of historical data:
- Profit margin: food = 25%, beverage = 40%, and gaming = 80%.
Profit margin: food = 25%, beverage = 40%, and gaming = 80%.
- $400 food revenue x .25 = $100.
$400 food revenue x .25 = $100.
- $200 beverage revenue x .4 = $80.
$200 beverage revenue x .4 = $80.
- $400 gaming revenue x .8 = $320.Thus, total ancillary profit is$500(100+80+320).
$400 gaming revenue x .8 = $320.Thus, total ancillary profit is$500(100+80+320).
- Room revenues from the Reservation System:The reservation is a $100 per night package that includes $20 breakfast, soG3 RMSreceives a room revenue value of $80 per night from thereservation system. Total room revenue is$240(3x80).
Room revenues from the Reservation System:
The reservation is a $100 per night package that includes $20 breakfast, soG3 RMSreceives a room revenue value of $80 per night from thereservation system. Total room revenue is$240(3x80).
- Channel Costs based on your configuration and the channel and source information from thereservation system:For the booking source or channel of this reservation there is a $2 pass-through fee and a 15%  commission.The 15% applies to $300 total rate value (not just room revenue), so $45. Plus the $2 fee totals$47.
Channel Costs based on your configuration and the channel and source information from thereservation system:
- For the booking source or channel of this reservation there is a $2 pass-through fee and a 15%  commission.The 15% applies to $300 total rate value (not just room revenue), so $45. Plus the $2 fee totals$47.
For the booking source or channel of this reservation there is a $2 pass-through fee and a 15%  commission.The 15% applies to $300 total rate value (not just room revenue), so $45. Plus the $2 fee totals$47.
- Servicing Costs defined in your configuration:Full Turn Cost (when guest checks out): $22.Full Service: $15.Full Service Interval (days between Full Service): Alternate Day.Interim Service Cost (on non-Full Service days): $5.Thus each cost applies once: $5 for Interim Service on day one, $15 for Full Service on day two, and $22 for check out on day three. The total cost is$42(5+15+22).
Servicing Costs defined in your configuration:
- Full Turn Cost (when guest checks out): $22.
Full Turn Cost (when guest checks out): $22.
- Full Service: $15.
Full Service: $15.
- Full Service Interval (days between Full Service): Alternate Day.
Full Service Interval (days between Full Service): Alternate Day.
- Interim Service Cost (on non-Full Service days): $5.Thus each cost applies once: $5 for Interim Service on day one, $15 for Full Service on day two, and $22 for check out on day three. The total cost is$42(5+15+22).
Interim Service Cost (on non-Full Service days): $5.
Thus each cost applies once: $5 for Interim Service on day one, $15 for Full Service on day two, and $22 for check out on day three. The total cost is$42(5+15+22).
- Room Profit:Room Revenue (2. bullet) minus Channel (3.) and Servicing Costs (4.) equals$151(240-42-47).
Room Profit:
Room Revenue (2. bullet) minus Channel (3.) and Servicing Costs (4.) equals$151(240-42-47).
- Total Profit: Room Profit (5.) plus Ancillary Profit (1.) equals$651(151+500).
Total Profit: Room Profit (5.) plus Ancillary Profit (1.) equals$651(151+500).

### Scenario 2 - LRV

Use this simple scenario to compare how the LRV differs between Room Revenue and Profit Optimization:
- Only two rooms remain for sale for this date, andG3 RMSforecasts four rooms of remaining demand.
Only two rooms remain for sale for this date, andG3 RMSforecasts four rooms of remaining demand.
- This demand consists of two Spa Packages and two Room Only rate codes.
This demand consists of two Spa Packages and two Room Only rate codes.
- The property prices inclusive of 10% tax.
The property prices inclusive of 10% tax.
- For simplicity, there are no specific Channel or Servicing Costs, only overall room revenue Profit %.
For simplicity, there are no specific Channel or Servicing Costs, only overall room revenue Profit %.
With Room Revenue Optimization,G3 RMSrestricts the Spa Package demand because it has lower room revenue. It sets the LRV at 455, just above the 454.55 pre-tax value (tax is added before sending LRV toselling system).
With Profit Optimization,G3 RMSalso forecasts ancillary spend and considers profitability, both based on the property's tracked data. Thus it knows that the Spa Package is more profitable and sets the LRV at 251, above the lower Profit Value and, thus, restricting the Room Only demand.
To enable aselling systemto use a profit optimized LRV,G3 RMSneeds to also send yield adjustments. These adjustments reduce the rate code value down to the profit value. In our example, the Room Only rate code's value of 550 is adjusted by 300 to result in a profit value of 250. The Spa Package value of 580 is adjusted by 322.73, thus the profit value is 257.27.
