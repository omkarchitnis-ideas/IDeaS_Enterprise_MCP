# Best Practices for Setting Ceiling and Floor Values

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BP-Ceiling-Floor-Values.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BP-Ceiling-Floor-Values.htm`
- **Ingestion Date:** `2026-09-11 22:14:17`

---

# Best Practices for Setting Ceiling and Floor Values

## Consider Howthe RMSCalculates the Suggested Values

The suggestions use your historical pricing (bookings with theEqual to BAR attributefrom up to 730 past days) and, if available andenabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section., rate shopping data (how your pricing differed from your competitors in the past and how competitors price for future dates). The system also creates a season for each time period and for each Special Event where pricing differs from the default values.
The RMSsuggestions already consider the following best practices, for example, using historical prices. If your current price range is more constrained than your historical range, the suggested values might be higher or lower than you expect.

## Use Historical Prices to Determine Your Range

Add Ceiling and Floor values that are within a reasonable range of your highest and lowest historical prices, by season, and if significant patterns exist, by day of week. For example, if your historical range has been 100 to 200, do not load 70 to 250. As a general rule, if you would not sell a price value in a manual environment, do not make it available in the price range.
The RMSlearns price sensitivity for each price point from past reservations. In the example of a historical range from 200 to 300, the system has learned the price sensitivity for these prices from past guest behavior. Because you have never sold rooms at 450, the system has not learned the price sensitivity for that price point yet.  Untilthe RMScan learn from actual behavior, it assumes the price sensitivity is the same as for the closest known price point (300, in this case).
If your property uses aSynthetic Data build, projections replace the missing historical data. Make sure that the ADR in the projections aligns with the price range that you set up.
The system learns quickly, so use small increments if you want to explore a lower or higher pricing strategy than in the past. In the above example with a historical range of 200 to 300, don't change the range to 100 to 450 or 70 to 400. Instead, start with 170 or 330, and let the system learn while you monitor the forecast and decisions. Then, if successful, expand the range.
If you used a price point in the past for only a handful of dates (for example,  only during high-demand special events), do not make it the default Ceiling value for the year. Instead, set up a season when that price point is the Ceiling value. The reason is the same as why you should start with your historical prices, namely how the system learns price sensitivity. If you use the highest price as the Ceiling for the full year,the RMSlikely will use it over other dates with less demand until it learns the true price sensitivity over non-peak demand dates.

### Consider Other Factors That Impact Ceiling/Floor Values

Setting the Ceiling and Floor values is the key step to define your pricing strategy. Butthe RMSalso considers  other setup when  producing the Final Price that your guests see.
The following areas impact your Ceiling and Floor values:
