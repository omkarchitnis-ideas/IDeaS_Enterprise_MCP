# Best Practices for Demand Override

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Demand-Wash/BP-Demand-Override.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Demand-Wash/BP-Demand-Override.htm`
- **Ingestion Date:** `2026-09-11 22:14:20`

---

Understand the Process to Decide if a Demand Override is Best

# Best Practices for Demand Override

Demand overrides influences the decisions ofthe RMS. Use them when you know something about the demand that the system doesn't and add them at the appropriate level of detail.

### Understand the Process to Decide If a Demand Override is the Best Solution

Following this overview of the process, click on any of the steps to learn more.Download a PDF of the process in the Resources.
The RMSoptimizes all decisions and demand together, so a demand override influences the decisions.
If you question the demand forecast for a date, review anyPricingoverrides, because they directly impact the demand forecast.  And sincethe RMSmaximizes revenue overall, review overrides not just on the day that you're questioning but also on surrounding dates, for example, on theBusiness Analysis Dashboard.
Removing these overrides might adjust the demand to a value closer to your expectation.
Notes:
- Select a pricingora demand override, not both. Override the price when you need to ensure a certain price. Override demand when you know something about that, not when you want to change the price.Watchthis videoon how demand impacts pricing.
Select a pricingora demand override, not both. Override the price when you need to ensure a certain price. Override demand when you know something about that, not when you want to change the price.Watchthis videoon how demand impacts pricing.
- After removing overrides,  wait for the next processing before reviewing the forecast. That ensures that forecast and decisions are based on the most recent  data.
After removing overrides,  wait for the next processing before reviewing the forecast. That ensures that forecast and decisions are based on the most recent  data.
YourPricing Configurationcontrols howthe RMSuses the pricing setup without constraining the system. For example, define a price range from whichthe RMSpicks an appropriate price.
The RMSconsiders theimpact of publicly available prices of your competitors on your demand(if enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.).
For example, you might question why the system decreased the remaining demand forecast for a certain date, even though you expect higher demand. Before you override the demand, check if competitors lowered their prices, which can reduce the amount of business that you can attract. The system will still optimize pricing and demand to ensure that you capture the maximum revenue, but only from that reduced demand.
Rate Shopping setupcontrols howthe RMSuses competitive rate information.
Rooms configuration tellsthe RMShow to manage your room types. Check for any restrictions on theRoom TypeandUpgrade Pathsetup, because they impact the system's ability to accept demand, even when the demand is not above capacity.
If you disagree with the demand because you expect unusual transient demand, add aSpecial Event. If it is a repeating event,the RMSuses  the previous instances to forecast and price optimally. If it's a one-time event, ensure you agree with the remaining demand.
Override demand at the appropriate level of detail, based on the level of your demand information, the size of the demand change, and the override period.
Note: Do you want to override the demand because you disagree with theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).? If so, consider that, in the case of demand in excess of the propertyâs capacity, the system decides during the optimization which demand to accept, see theDemand and Wash Definitionsvideo for details.
An Occupancy Date demand override at the Forecast Group level is the most frequent type. You enter the amount of demand increase or decrease. Thenthe RMSdistributes the demand to the different lengths of stay and to the different Room Classes, based on its calculation of expected demand at those levels and the observed patterns for this Forecast Group.
Less frequently, when you know something about the demand by length of stay (LOS) 1 to 8, use theArrival by LOSdemand override. For example, you know that a tactical weekend promotion will impact demand only for Friday arrival, 2-night LOS. You donât want the system to distribute the increase to all LOS, so you use the Arrival By LOS override type.
Before you select this type, keep in mind thatthe RMSforecasts demand by LOS. For example, you need to increase  demand staying 4 nights, while your average property LOS is 2 nights. However the system might already forecast higher demand for LOS 4 for the impacted Forecast Group.Therefore, use an Occupancy Date demand override instead and letthe RMSdistribute the demand  accordingly.
The same applies to demand for stays longer than LOS8.Unless you haveExtended Stay Forecasting, you can't override such demand, butthe RMSforecasts it and distributes an Occupancy Type override to longer lengths of stay as well.
In rare cases, you might have specific knowledge about demand at the Room Class level. In that case, apply an Occupancy DateorArrival by LOSdemand override at the Room Class level.
If you need to override the demand for more than just one day at a time, you can apply Multiday Demand Overrides byOccupancy DateorArrival by LOS.
An incorrect multiday demand override has a large negative impact, so only use them after reviewing the following questions:
- Are you certain about the type and quantity of demand that you expect?
Are you certain about the type and quantity of demand that you expect?
- Have you investigated the demand forecast? If you have, weigh the possible negative impact against delaying the override and monitoring the situation until the system learns the changes on its own.
Have you investigated the demand forecast? If you have, weigh the possible negative impact against delaying the override and monitoring the situation until the system learns the changes on its own.
- Have you consideredother factors, see step 1)?
Have you consideredother factors, see step 1)?
- Determine if the selected Forecast Group contains other business where the demand does not need to be overridden. If it does contain other business, you need to assess what the overall impact on the Forecast Group is, considering that it includes other business that does not need to be overridden.
Determine if the selected Forecast Group contains other business where the demand does not need to be overridden. If it does contain other business, you need to assess what the overall impact on the Forecast Group is, considering that it includes other business that does not need to be overridden.
- If you are uncertain about the size of the impact, use theData Detailsin the Business Analysis Dashboard to view all business included in the Forecast Group and how big each of them is.Notes: The system calculates remaining demand only at the Forecast Group, not at more detailed levels, so estimate the share by using the Occupancy Forecast for the override period.
If you are uncertain about the size of the impact, use theData Detailsin the Business Analysis Dashboard to view all business included in the Forecast Group and how big each of them is.Notes: The system calculates remaining demand only at the Forecast Group, not at more detailed levels, so estimate the share by using the Occupancy Forecast for the override period.
- Review the systemâs forecast of remaining demand (RD) for the selected Forecast Group on thecalendar. Based on your expectation of demand and the share percentage considerations from step 2, what % of increase or decrease do you need to apply?
Review the systemâs forecast of remaining demand (RD) for the selected Forecast Group on thecalendar. Based on your expectation of demand and the share percentage considerations from step 2, what % of increase or decrease do you need to apply?
- Is more than one Forecast Group impacted, for example, because business is moving from one Forecast Group to another? In that case, consider the first bullet and ensure that a Multiday Demand Override is the right solution for all impacted Forecast Groups before you override.
Is more than one Forecast Group impacted, for example, because business is moving from one Forecast Group to another? In that case, consider the first bullet and ensure that a Multiday Demand Override is the right solution for all impacted Forecast Groups before you override.
- If you are certain that a Multiday Demand Override is necessary, the next step is to decide which Forecast Group to override. SeeMultiday Demand Overrides by Occupancy Datefor how to select the matching Forecast Group.
If you are certain that a Multiday Demand Override is necessary, the next step is to decide which Forecast Group to override. SeeMultiday Demand Overrides by Occupancy Datefor how to select the matching Forecast Group.
- If the remaining demand forecast is very low, the percentage increase might have to be very high to achieve an intended amount. For example, if the remaining demand forecast is only for 1 room on average, and you are expecting 10 rooms, then you would need to apply a 1000% increase to achieve that.Note: the only way to enter a specific value instead of a % change is to enter an Override by Occupancy Date. And if your override is for a Forecast Group with a zero forecast of remaining demand, a value override by day and Room Class is your only option, since a % increase of zero does not achieve your goal.
If the remaining demand forecast is very low, the percentage increase might have to be very high to achieve an intended amount. For example, if the remaining demand forecast is only for 1 room on average, and you are expecting 10 rooms, then you would need to apply a 1000% increase to achieve that.
Note: the only way to enter a specific value instead of a % change is to enter an Override by Occupancy Date. And if your override is for a Forecast Group with a zero forecast of remaining demand, a value override by day and Room Class is your only option, since a % increase of zero does not achieve your goal.
The RMSlearns and adjusts to changes in demand once it sees proof of it in the booking data. For example, it's early April and you know that extra demand from a new corporate account will not start booking until May. If the booking window for that type of business is 2 to 4 weeks, you might want to override the demand only for May and possibly June, because by June the system will have seen the impact of the new bookings and adjusted the forecast for July and onwards accordingly.
Does the change of demand apply to the entire period? Or are different days of that period affected differently, like peak days versus shoulder days?
Note: the override period is limited to the two months that are visible on the calendar.
For shorter periods, or when the % demand change varies often within the period, use the Demand by Occupancy Date override for a single day. Then use the previous day and next day arrows to move to a different day. The advantage of applying the override day-by-day versus for multiple days is that you can see the demand details for each day and each Forecast Group before deciding for which Forecast group and how much, if at all, to override demand.
Monitoring your demand overrides  to ensure that they remain accurate is important, but it can be time consuming. Therefore,the RMSmonitors them for you. The system adjusts your demand override if it becomes unrealistic compared to what is actually getting booked.
The RMSdoesnotadjust an unconstrained demand override of zero for the Non-Block Forecast Groups, regardless of booking activity.
For example, two months ago you added an override for tomorrow, setting the remaining demand forecast to 100 rooms. After that, you never removed or modified the override. In this case, you would not wantthe RMSto still forecast 100 rooms in remaining demand for arrival tomorrow, since almost all of that 100-room demand should have booked by now. Rather than making you adjust and modify your override as the arrival date gets closer,the RMSdoes the monitoring and adjusting for you.
How the system adjusts your overrides differs by the type of Forecast Group that you applied it to, either Non-Block or Block:
The RMSadjusts the override, if above zero, based on remaining time to arrival and based on booking pace.
For example, 60 days ago the system forecasted zero remaining demand for today. You disagreed and  applied a remaining demand override of 100 rooms. If between 60 days ago and today, no new reservations booked for the non-block type Forecast Group,the RMSwould slowly have adjusted your override down to almost zero today.
The RMSmakes this adjustment based on the observed booking pace patterns. The system knows that the remaining demand should have booked in the 60 days, and it would consider any rooms that booked in that time as well, based on the expected booking pace.
The 100 rooms of remaining demand are also subject to optimization, meaning that if the system forecasts demand in excess of capacity, it might use LRV to close out the demand.
An unconstrained demand override value of zero prevents the system from adjusting the user remaining demand over time.The RMSdoesn't forecast any additional demand and considers the On Books as the Occupancy Forecast.
Whenthe RMSadjusts a non-block demand override, you see the adjusted and your original override values in theBusiness Details and Overrideswindow.
In the example below, the original remaining demand override shows in the Unconstrained Demand Override column on the right side. The user entered the override as a percentage at the Forecast Group level.The RMSdistributed the percentage as a value to each of the Room Classes, based on its calculation of expected demand by Room Class: 66.27 for Standard, 4.98 for Deluxe, and 2.19 for Suite.
The User Remaining Demand column in the middle displays the system's adjusted values: 53.57 for Standard, 4,13 for Deluxe, and 1.85 for Suite.
The system's forecast of remaining demand (28.78, 2.67, and 0.60) is lower than the adjusted user overrides. Whilethe RMSadjusts the override based on booking pace, it maintains the original user intention of higher demand.
The RMSassumes that when you override demand for Block Forecast Groups, you are certain that the demand will materialize. Therefore, it adjusts the override only based on booking pace and On Books at the time of the override, but not on remaining time to arrival. The system also considers your override as constrained demand and does not subject it to optimization in case of demand in excess of capacity. Let's look at a few examples. All are for arrival today and for a Forecast Group that contains group business.
- 60 days ago, on books was zero. You  overrode remaining demand to 100. Today, on books is still zero. Aside from wash,the RMSdoesn't adjust your override and still expects 100 rooms of remaining demand for today.
- 60 days ago, on books was zero. You  overrode remaining demand to 100. A new group books after the override, and on books today is 50.The RMSapplies the new group booking to your override and forecasts only 50 rooms of remaining demand for today.
- 60 days ago, on books was 100, and you overrode remaining demand to zero. A group of 50 cancels after your override, and today on books is 50.The RMSstill expects 50 rooms of remaining demand for today because it honors your override combined with the on books number at the time of the override. In other words, when you override remaining demand, you also tellthe RMSto expect existing on books business, even if that business could cancel.
These examples show that it's important that you regularly review and, if applicable, remove your demand overrides for block-type Forecast Groups to ensure that the system knows the truth.
You can see your original demand override and the system's expectation in theBusiness Details and Overrideswindow.
In the illustration below, you entered an override for a Forecast Group with 25 rooms On Books, shown on the left side. You expect 50 rooms of remaining demand, and that override value is displayed in the User Remaining Demand column in the middle. The 25 On Books at the time of the override, plus the 50 remaining demand are saved as the Constrained Demand Override of 75 rooms, displayed on the right.The RMSexpects those 75 rooms even if On Books change after the override:
- If a group of 50 books a day after the override, on books is 75.The RMSadjusts the User Remaining Demand to zero. The Constrained Demand Override remains at 75.
- If a group of 25 cancels, On Books becomes zero.The RMSadjusts the User Remaining Demand to 75, still expecting your Constrained Demand Override of 75.
Regardless of the adjustments thatthe RMSmade to demand overrides, you still need to review them regularly. You should determine if the conditions that caused you to apply them changed and monitor howthe RMSis adjusting them. After the system can see evidence of the changes in demand, we suggest that you remove the overrides and let the system take over the forecasting completely.
When 
 you add, remove, or review and keep an override, add a note 
 that helps you understand at the next step why the override is in place 
 and what conditions led you to place it or keep it.
