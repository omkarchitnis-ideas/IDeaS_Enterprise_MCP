# At a Glance Summary

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/AAG/At-a-Glance-Summary.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/AAG/At-a-Glance-Summary.htm`
- **Ingestion Date:** `2026-09-11 22:13:51`

---

# At a Glance Summary

Use the Summary pane to quickly compare key metrics of a full month to other periods, with variances for easy comparison. For example, how the occupancy and On Books of this month compare to at the same time 2 years ago (ST2Y). Or the forecast compared to how that month finished last year. Variances display as a percentage (%) or, for Occupancy %, as percentage points (ppt).
If setup, you see thefiscal calendarinstead of monthsbudget. For more granular comparisons of shorter periods to last year and adjusted by day of week, useBusiness Analysis Data Details. Or click to see anoverview of all panels of the dashboard.
Displays if you set upBudget and My Forecastvalues. You can compare your budget and forecast to on books and the system's forecast. The title of these rows differ if you customized the names. The data does notRemove Excluded Segmentsif you select that checkbox.
With an integration forSmith Travel Research (STR)STR is a global provider of competitive benchmarking, information services and research to the hotel industry. STR reports provide property performance data compared to its competitive aggregate and general market, allowing you to follow trends in occupancy, average daily rate (ADR), revenue per available room (RevPAR).or Benchmarking Alliance, you can see Market Performance data in the table. This helps you understand how your Occupancy %, ADR, and RevPAR compare to your competitors' historical data.
For past months or fiscal periods, compare this year's and last year's Market Performance data to your actuals. For the current or future months, you see past Market Performance data from the same time last year, adjusted by day of week. If data is missing or if you only receive STR market level data, you see --.
The values display in the currency you receive from STR.
If you enabledProfit Optimization, you can view Profit metrics:
- Profit: the calculation depends on data that you provide.G3 RMScan consider profitability of guest rooms (based on servicing, channel costs, etc.) and profitability of other revenue streams. For current dates,G3 RMSestimates the profit based on occupancy on books andOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).. For past dates, the system estimates the profit based on the final number of rooms occupied.
- ProPOR: profit per occupied room. ProPOR equals the profit divided by the number of occupied rooms and is comparable toADRAverage Daily Rate. Room revenue divided by the number of rooms of occupancy..
- ProPAR: profit per available room. ProPAR equals the profit divided by capacity (based on property's selection, eitherPhysical CapacityThe total number of guest rooms at a property, including out of order rooms.orEffective CapacityThe property's physical capacity minus the out of order rooms., and is comparable toRevPARRevenue Per Available Room. The total room revenue divided by the total number of rooms (capacity).
See the Property Information topic for the capacity definition..
If you haveExtended Stay Forecasting and Optimizationenabled,  you see a separate summary for that business type. It represents rooms on the books with a length of stay (LOS) greater than 7 nights or, withIndependent Products, based on their configured min and max LOS.
- ALOS represents the average length of stay across all rooms on the books for the selected month.If a reservation begins in one month and ends in the next month, the full LOS impacts the ALOS calculation in both months.
ALOS represents the average length of stay across all rooms on the books for the selected month.
If a reservation begins in one month and ends in the next month, the full LOS impacts the ALOS calculation in both months.
- Short Stay Occupancy % represents the occupancy on the books with a LOS up to 7 nights. If your property uses Independent Products, this value represents the occupancy on the books with a LOS up to the minimum LOS configured for the product. For example, if the minimum LOS for your independent product is 15 nights, then the Short Stay Occupancy % includes all reservations up to 15 nights.
Short Stay Occupancy % represents the occupancy on the books with a LOS up to 7 nights. If your property uses Independent Products, this value represents the occupancy on the books with a LOS up to the minimum LOS configured for the product. For example, if the minimum LOS for your independent product is 15 nights, then the Short Stay Occupancy % includes all reservations up to 15 nights.
- Extended Stay Occupancy % (ESOCC %) represents the occupancy on the books with a LOS of 8 nights or more, expressed as a percentage of rooms. For properties with independent products, this value represents the configured min and max LOS for each product.
Extended Stay Occupancy % (ESOCC %) represents the occupancy on the books with a LOS of 8 nights or more, expressed as a percentage of rooms. For properties with independent products, this value represents the configured min and max LOS for each product.
By default, Short Stay Occupancy % and Extended Stay Occupancy % values use the Physical Capacity for the total number of rooms, which includes out of order rooms.A property (or a corporate office for an enterprise) can contact IDeaS to switch this to use Effective Capacity, which excludes out of order rooms.

## Summary Steps

- Clickand thenAt a Glance.
- Scroll down the page to the Summary pane.
- Select theRemove Excluded Segmentscheckbox if you want the metrics to exclude business from specific market segments. You must define your excluded market segments inProperty Information.The exclusions do not apply to Budget and My Forecast values.
- Click the open 
	 iconin the upper right corner to display the table in full screen view. Close the window to return to the full dashboard.
