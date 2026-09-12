# ManagingG3 RMSDuring Demand Disruptions

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/About/Demand-Disruption.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/About/Demand-Disruption.htm`
- **Ingestion Date:** `2026-09-11 22:13:14`

---

# ManagingG3 RMSDuring Demand Disruptions

Follow these recommendations if you need to manageG3 RMSduring times of large and sudden changes in demand, from events like pandemics, acts of violence, political disruptions, or extreme weather.  This topic includes what to do if your hotel is closed, how to place rooms out of order, and how the system handles the demand disruption.
- Monitoring and Adjusting the Forecast
- Using Special Events
- Managing Full or Partial Closures
- Managing Pricing
- Managing Rate Shopping Data
- Managing Recovery
- Returning from Demand Disruption
The steps that you take can vary based on the disruption's size, duration, and length of the recovery. In these circumstances, work withIDeaSsupport to determine the best mix of actions.

## Monitoring and Adjusting the Forecast

If adjustments to demand made byG3 RMSor IDeaS don't meet your expectations, or you need to make immediate changes, useMultiday Demand Overrides.
Reviewing forecasts and decisions is important during a disruption, since booking volume and patterns change quickly and often.

### Short Term

Share withG3 RMSwhen you know something that the system doesn't. For example, tell the system if you think the drop in demand or the wash is stronger than it expects.

### Longer Term

Beyond 90 days, reviews are important too. However, consider the high uncertainty before making changes. It's difficult to predict the demand and speed of recovery. If you aren't sure about an override, monitor regularly.
G3 RMSregularly checks its demand patterns and will react to large changes in demand in the recent past (within 14 days). If the system sees significant changes, it likely applies this to future forecasts for the impacted Forecast Groups. That meansG3 RMSchanges its demand forecast for future months now, instead of waiting until it expects pick up for that month.
For example, it's March and you have low occupancy on books for May. Based on normal pick up patterns,G3 RMSmight not expect bookings for May until mid-April and would forecast normal demand for May. But based on current, disrupted demand patterns, the system has a low forecast. If this applies to a period far in the future that you expect to be very strong and not impacted by the disruption, you can override demand. Keep in mind that it's difficult to know when the disruption will end and how demand will change.
SeeUnconstrained Demand Calculationfor more details.
There are two key items thatG3 RMSlooks for when checking for demand changes:
- Business on books is less than expected.
- Change is statistically significant, such as a shift between forecast groups or a big drop in business.
For example, five days to arrival, the system expects 50 rooms for a market segment and room type. If it sees that only five rooms are on books,G3 RMSreacts quickly and drops the forecast. The same applies to large losses, like a group cancellation.
For dates further in the future, the system applies recent trends, not on books. That's because the business on books might not be indicative. For example, 50 days to arrival the system might expect only three rooms on books. If only one room is on books, that alone is not a good indication to drop the forecast.

#### Rooms are not Out of Order for Closed Properties

G3 RMSonly knows that a hotel is closed if 100% of the capacity is out of order. Otherwise, the system reacts day by day, as business on books doesn't match the expected business. SeeRestricted Inventoryto learn more.

#### A Special Event Is Added

You added a Special Event for the demand disruption, but not as Informational Only. SeeWhy Add a Special Event as Informational.

#### âââââââData for the Disrupted Period Is Excluded

- You requested via your support contact thatG3 RMSignores the dates.
- You use Synthetic Data, and you define the date whenG3 RMSstarts using data.
- You resolved anOut of Order RoomsAlert withC) Don't use the data to forecast - Out of Order rooms constrain the performance. SeeManaging Out of Order.

#### G3 RMSHas Only One Year of Data or Less

In this case, the system can't compare to last year to detect if this is regular seasonality or a change. With at least 13 months of data, the system can detect a statistically significant change and apply it to future demand.

#### Strong Seasonality

If your property has strong seasonality, it is more difficult for the system to differentiate seasonality from a shift in patterns. This is especially true whenG3 RMShas less than two years of historical data.

#### G3 RMSis Reacting by Booking Window

If the system sees  evidence of a downward trend and reduced business on the books, it should use that to adjust the demand forecast. It likely applies changes less aggressively outside of the main booking window, so you will see less reduction further out.
If you believe the reasons above do not apply and are not comfortable with howG3 RMSis reacting to the disruption,open a case.We'llreview if the patterns are consistent or if any other concerns exist.
Follow best practices foroverriding demandby applying a reasonable percentage to decrease the demand  that matches the observed loss of business. Monitor and, if needed, update the overrides.
For example, if all Forecast Groups lost 30% of their demand, you might adjust by the same percentage for the future period that you expect to be impacted. This could be based on impact on travel to your region, impact on the region of your main guest markets, or the impact on your primary markets and key accounts.
As always, share withG3 RMSonly what you know and override the demand only for the period that you know is significantly impacted. If you are unsure about which period to override, start with a short period that you are certain about. If needed, expand the period once you know more.
If you manage multiple properties and don't agree with the forecast for several of them, contact yourIDeaSrepresentative.
Based on the amount of disruption, shouldn'tG3 RMSstart with a blank slate from a data perspective? No,  because the 13 (or more) months of history help the system.
Consider the following example. The blue line shows Occupancy On Books. The system compares March 2019 to March 2020 (in the red frame). If it determines that this is a significant drop and that it is not a seasonal change, it adjusts future forecasts (the green line in the frame on the right) accordingly.
This same process helps the system react quickly when business recovers. SeeHow the System Reacts to Recent Changesfor details.
You might provide complimentary or highly discounted rooms to essential workers or displaced persons. In that case, ensure this business is coded to the correct rate code and market segment in yourreservation system. That helpsG3 RMSsee the disruption-related shift in business and the rate trending down. After the disruption is over, IDeaS can exclude this period. That avoids a lasting impact of this one-time business on future forecasts.
Properties withSynthetic Datashould monitor the situation. Short-term,G3 RMSreacts stronger to recent changes. Longer-term and once it's clear that the disruption is over, extend the period for Projected Rooms Sold and Revenues. Ensure that the property continues with Synthetic Data until twelve months of stable historical data is available.
As with all properties, IDeaS can ensure thatG3 RMSignores the patterns from the disruption and doesn't use them to forecast the recovery period.
If your property has completed using Synthetic Data, it should have twelve months of stable historical data. Therefore, it should have enough data to forecast normal periods, and the system uses the recent past to forecast the current, disrupted period.

## Using Special Events

### Adding Special Events for the Disrupted Period

How you create the Special Event depends on your closure status. For an overview of the process, seeDecide how to set up a Special Event.
- If your property is closed 100%, enter aSpecial Eventfor the closure period immediately.
- If your property remains open or partially open, enter a Special Event for that period after the demand disruption ends. If you want to enter a Special Event before the disruption ends, enter it asInformational Use Only.
- When the  disruption is over, remove the Informational Use Only setting and update the event dates. That ensures thatG3 RMSdoesn't use that data to forecast the normal demand of the recovery period.
If the impacted or closure period is longer than 60 days, enter two consecutive events.
There are two issues:
- If you don't set the Special Event as Informational Use Only,G3 RMSconsiders the period of the demand disruption as exceptional and not as an indication of future demand. But until the demand disruption ends, the current data is typical.G3 RMSshould use it to forecast demand.
- Let's say you enter a non-recurring Special Event that covers the entire period of the demand disruption. It covers not only the past dates but also the future remaining days of disrupted demand.G3 RMSforecasts these remaining days based on the patterns of the completed past days of the Special Event. In other words, if the past dates of the event had very low demand, the system forecasts very low demand for the remaining dates.
You might not know enough about the amount of demand and the duration of the remaining period to letG3 RMSforecast accordingly. That's why we suggest you create an informational Special Event.

### Managing Special Events during the Disruption

Follow thebest practiceand remove the instances  of recurring Special Events if they happen during the demand disruption and if they are unusual. Remove them after each impacted Special Event or all at once when the demand disruption is over. If needed, add the removed instance as a separate, Informational Use Only Special Event and override demand.
For an overview of the process, review the following recommendation.
Follow this decision tree to understand how to manage Special Events that occur within the disruption period.

## Managing Full or Partial Closures

### Full Closure

If the disruptions cause your property to close completely, follow the process forRestricted Inventory. Note that the process includes continued running of night audits. Also, ensure that the appropriate controls (for example,Close) are in place in all selling and distribution systems.

### Partial Closure

If only portions of your property close, use Out of Service or a similar status that doesn't reduceEffective CapacityThe property's physical capacity minus the out of order rooms.. If yourreservation systemdoesn't have an Out of Service or similar non-deduct status, useOut of Order Overrides. Otherwise the existing demand with the restricted capacity might cause aggressive controls.
G3 RMScalculates Last Room Value based on remaining demand compared to remaining capacity. If capacity is constrained or, in the case of a closure, zero (due to the out of order rooms) and there is remaining demand, the system raises LRV because there is no capacity to accept the remaining demand. SeeLRVfor more details.
If you put more than 20% of inventory out of order, you get anOut of Order Rooms Alertafter seven days. See thescenarios for restricted inventoryto understand how to resolve the Alert.

#### What if I Mistakenly Selected Option C) Don't use the data to forecast?

If you select the optionC) Don't use the data to forecast - Out of Order rooms constrain the performance, the system ignores the recent data from the out of order period. Instead, it uses the normal demand data from before the out of order period to forecast, when demand was strong. That might lead to overly aggressive forecasts, not appropriate for this time of decreased demand.
If you think that you resolved the out of order Alert withC) Don't use the data to forecastby mistake, enter acaseor contact your IDeaS representative. Let us know what period you marked incorrectly, so we can make the necessary corrections.
You might place a room out of order  for a couple of days after a guest checks out to deep clean it. That limits the number of rooms that you can sell. Therefore, place the room out of order (OOO). Seerestricted inventoryfor more information.

## Managing Pricing

Demand disruptions might cause a dramatic slowdown in new reservations. Lowering pricing might seem like a logical answer. However, we recommend that you maintain your pricing strategy and avoid drastic changes in pricing. Here are a few reasons why:
- Lower prices donât bring in more customers because there is no additional demand to attract.
- Lowering prices might attract customers that are not appropriate for your business.
- Widespread discounting can have a negative effect on your perceived value in the market.
Our recommendations:
- Any promotions should be fenced, opaque, and only available through specific channels.
- Instead of general discounting, identify which channels, sources, and markets are still booking and target those segments.
- Packaging is another alternative to overall discounting,  especially if leisure business returns first.
During disruptions, some properties stop selling rates that require full advance payment or that can't be canceled. Instead, they only sell rates with a flexible cancellation policy, like Best Available Rate (BAR). If this is a general trend in your market, customers likely welcome it if you make the same switch. If you switch, note thatG3 RMSobserves a swing fromLinked to BAR ProducttoEqual to BAR Product Forecast Groups.
Countries with tax inclusive pricing may lower taxes temporarily to offset the negative impacts from a disruption. How you manage that inG3 RMSdepends on whether you want to lower prices for customers or keep current pricing (and pay less tax on these prices):
- Lower your pricing:your current price is â¬200 Room Only and the VAT is 10%.G3 RMSand the PMS see net revenue as 181.82. If the VAT drops to 7%, and you change the tax in the system, then the system might drop the price to 194.54 before rounding.
- Keep current pricing:if you keep the tax inG3 RMSat 10%, then the price remains at â¬200. The PMS deducts only 7%, so the net revenue for your property is higher, at 186.91.
In both cases, keep in mind that the system optimizes pricing net of tax. This is because you can only take that revenue to the bank.G3 RMSadds tax before it sends prices to theselling system. And the Property Management System (PMS) deducts the tax from the revenue.
If you lower the tax in the system, use theSeasonal Tax functionality.
If your property uses the OXI integration, contact your Client Relationship Manager. For OXI properties, all tax changes need to be applied by IDeaS Teams.

## Managing Rate Shopping Data

The following applies if youenabled the use of market dataBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section..
What if you don't drastically lower prices, but your competitors do? In that case, ensure that your pricing range is still competitive.
- In the Business Analysis dashboard, count how many times your pricing is at the lowest price point. If the number exceeds 50 in the next 90 days, and you are priced 30% or more above your competitors, consider expanding your price range to remain competitive.
- If you useCompetitive Market Position Constraints, avoid the Low Range option. It can drive overall market pricing down and lower revenues. If Low Range is your typical price position, verify that it's still appropriate.
- Exclude closed competitors (if you are open) and  those that price much lower than normal and that drive down your price.
Tell the system to ignore the rate shopping data of closed competitors. To do that, clickConfigureandRate Shopping, then use theIgnore Competitor Datafeature in theCompetitor Settingstab.
Competitors that price erratically or discount heavily can negatively impact your pricing. To avoid that, tell the system to ignore the rate shopping data of those competitors. To do that, clickConfigureandRate Shopping, then use theIgnore Competitor Datafeature in theCompetitor Settingstab.

## Managing Recovery

Use theChecklist for Returning from Demand Disruption.
- UsePickup/Change,Performance Comparisonreports, or Notifications to look for return of business on the books and a slowing of cancellations.
- Use market data sources, like  recent STR performance reports, adjustments to STR market forecasts, orDemand360.
- Look for improvements in competitor pricing in Rate360.
- Use tools like Agency360, which can  show recovery of business from particular client accounts.
These tools are only relevant if your competitive set is representative; in other words, all competitors have a similar business mix.
Once demand recovers, monitor how quickly it recovers. Consider your inbound and outbound markets, your business segmentation (corporate clients, contracts), and the travel restrictions or concerns about travel in these countries, markets, and organizations.
Review howG3 RMSreacts to changes in demand and booking patterns. For example, does the system expect the same high wash as during the peak of the disruption? The system learns the new patterns but might need your help if patterns change faster (or slower) than expected.
Follow the steps forrestricted inventoryand ensure available capacity in each Room Class is proportional to enable theUpgrade Path. For example, a 100-room property has 60 Standard, 30 Junior Suites, and 10 Executive Suites. If they can only open 10% of their capacity, that should be 6 Standard rooms, 3 Junior Suites, and 1 Executive Suite. This also ensures that you can accommodate demand for higher-priced Room Classes, see the similar recommendations aboutcomplimentary upgrading.
Monitor room types with constrained bedding types, for example, a family room type. It might be more difficult than normal to walk guests or upgrade them.
Focus on your current customer base and explore what segments still travel. Useloyalty programofferings and focus on your repeat business segments. Investigate consumer behavior, and look for changes in who travels or is allowed to travel.
