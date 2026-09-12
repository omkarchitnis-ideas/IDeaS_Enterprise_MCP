# Best Practices for Competitive Market Position Constraints

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/BP-Competive-Market-Position-Constraints.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/BP-Competive-Market-Position-Constraints.htm`
- **Ingestion Date:** `2026-09-11 22:14:32`

---

# Best Practices for Competitive Market Position Constraints

Review these best practices andscenarioswhen you set up Competitive Market Position Constraints under Rate Shopping.

## Understand How Competitive Market Position Constraints Work

Watch this short video or read the explanation below.
Your browser does not support the video tag.
Without constraints, whenthe RMSpicks the price that results in the highest revenue, it considers the full price range that you set up. But with a constraint, for example,Mid Range, the system can only pick  from those prices that meet that constraint. That might mean that it can't select the price 
	 that would result in the highest revenue.
The Mid Range constraint and your pricing setup limit the prices available tothe RMSto the ones between the two dotted red lines. The optimal price would be higher.
The Maximum Market Percentile is set at 50, so to the lower half of competitors. The constraint (the two dotted red lines) and your configured price range limit the prices available tothe RMSto the ones in the green area, between 110 and 125. The optimal price would be higher.
Competitive Market Position Constraints impact the demand becausethe RMSunderstands the relationship between price and demand. If the constraint forces higher pricing versus the competitive set, theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).tends to be lower. If the constraint forces lower prices, the Occupancy Forecast tends to be higher.
To determine the impact of a constraint,the RMScompares competitors' prices against a weighted average of all room types in themapped Room Class.

## Scenarios

These examples show when Competitive Market Position Constraints are the right choice.
After a renovation, your property wants to reposition itself after a renovation and change from a pricing position in the middle of the competitive pricing set to a position near the top. You can quickly change your pricing, but  the buying behavior of your guests likely doesn't change quickly.the RMSmight continue to price in the middle of the market until it sees the change in demand andprice sensitivity.
If you don't want to wait for a gradual pricing change, or you think that you can predict the price sensitivity of the market, use aHigh Rangeconstraint to ensure the higher pricing position untilthe RMSadjusts. We recommend that you monitor the demand forecast and the pricing decisions closely.
For example, your full service hotel is surrounded by limited service hotels. Without a constraint,the RMSmight propose lower prices that impact your long-term position and brand. Thus, you use a constraint to ensure your property's market position at the top.
If your property uses Synthetic Data because it opened or changed flags, you might  know little about your competitors' pricing. You can use a constraint likeHigh Rangeuntil you know more.
Some properties want to build a base occupancy before they focus on maximizing room revenues. For example because they get a large share of their revenues from ancillary sources like casinos. Or because those properties have much larger inventory than their competitors. In that case, use an Occupancy-Based constraint to keep pricing below a number of competitors until you reach a certain occupancy On Books.
