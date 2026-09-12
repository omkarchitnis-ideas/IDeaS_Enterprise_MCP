# Hot Start - Synthetic Data

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/LDB/Limited-Data-Build.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/LDB/Limited-Data-Build.htm`
- **Ingestion Date:** `2026-09-11 22:13:06`

---

# Hot Start - Synthetic Data

Hot Start - Synthetic Data enables properties with less than 365 days or no historical data to benefit fromG3 RMSoutputs like pricing without a long wait. Here are some common examples:
- A property has not yet opened. It might take reservations or start taking them soon.
- A property opened recently and has very limited historical data.
- A property switched brands and lost its previous historical information.
- An open property has made large changes to its market segmentation and can't use the historical information anymore.
The missing historical data is replaced by two other data sources. You select another data source forBooking Patterns, for example a generic property. You provideProjectionsfor the expected demand by market segment. AndG3 RMSCreates Synthetic History, then uses all these data sources in its next processing.
View the  video in Resources on the right for a summary a Synthetic Data build.

### Synthetic Data Stages

Below is an overview of the Synthetic Data stages. For detailed descriptions of each step, see theWork Flowbelow.
Note: If your property usesComponent Rooms, you have to set those up before step 3).

## Work Flow

Complete the steps in the following order:
- Add Room Types:G3 RMSneeds to know your property's room types and their capacity. If you are inData Capture ModeA early status when IDeaS builds the RMS for a new property. During this setup step, the RMS has received the property's data, but the data is not yet saved in the RMSdatabase. The System Date is today.or later, yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.provides this data. Otherwise, add it in theRoom Typetab.
- Add Market Segments:G3 RMSneeds to know your property's market segments.  If you are in Data Capture Mode or later, yourreservation systemprovides this data.  Otherwise, add it in theMarket Segmenttab.
- Complete Rooms Setup:   includes mapping your room types to Room Classes, defining your Cost of Walk and othersteps.If your property usesComponent Rooms, it also includes their setup.
- Set up Market Segments: Assign attributes to all your market segments. Review allMarket Segment Setupsteps. Some steps need to wait until after you Create Synthetic History.
- Complete Your Projections: In the Projections tab, complete the following:Select dates for the projections:The first arrival date for which system forecasts demand, often called the opening date.When business patterns are normal and the system can use Actuals to forecast demand.See how toselect the correct dates for your projections.Complete the projected rooms sold and revenue.Normally, when historical data is available,G3 RMSuses all demand history to calculate unconstrained demand. With Synthetic Data, your projections by market segment replace the demand history. Therefore, your projections aren't an exact forecast of the next year. Instead, they reflect the current typical business. SeeBest Practicesfor more detail. If you have usable history, you can provide projections for fewer than 365 days. The maximum is for 730 days.
- Select dates for the projections:The first arrival date for which system forecasts demand, often called the opening date.When business patterns are normal and the system can use Actuals to forecast demand.See how toselect the correct dates for your projections.
- The first arrival date for which system forecasts demand, often called the opening date.
The first arrival date for which system forecasts demand, often called the opening date.
- When business patterns are normal and the system can use Actuals to forecast demand.See how toselect the correct dates for your projections.
When business patterns are normal and the system can use Actuals to forecast demand.See how toselect the correct dates for your projections.
- Complete the projected rooms sold and revenue.Normally, when historical data is available,G3 RMSuses all demand history to calculate unconstrained demand. With Synthetic Data, your projections by market segment replace the demand history. Therefore, your projections aren't an exact forecast of the next year. Instead, they reflect the current typical business. SeeBest Practicesfor more detail. If you have usable history, you can provide projections for fewer than 365 days. The maximum is for 730 days.
- Select Booking Patterns:This step helpsG3 RMSunderstand theBooking PaceMeasures how the occupancy changes as the arrival date approaches. It shows the speed at which reservations are booked.andWashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization.of each market segment. In other words, booking patterns show how your business picks up and cancels across the booking window. Since the system can't derive booking patterns from historical data, you select another source. For example, you can choose a generic property with similar booking and cancellation patterns. When your property has enough usable actual data, you switch to using your own data. Use theBooking Patterntab for your selection.
- Complete Remaining Setup: For details, seePricingandRate Shoppingsetup.
- After you complete the setup, contact IDeaS to run the Synthetic Data build.
- Synthetic Data build:In the process,G3 RMSuses your projections to simulate the missingMaster ClassThe Room Class for which a value displays if there is only space in the RMS to show one, for example, when you see only one price on a page.data for the past year, by market segment. If you have more than one Room Class, the system distributes projections to them primarily according to their capacities. For distributing the revenue projections, your pricing structure andPrice Rankingalso matter.G3 RMSthen  uses the simulated historical data, the booking patterns, and on books data to create forecasts and decisions.After the process completes, the Projections and Booking Pattern tabs are unavailable. IDeaS tells you when you can continue with the next step.
- In the process,G3 RMSuses your projections to simulate the missingMaster ClassThe Room Class for which a value displays if there is only space in the RMS to show one, for example, when you see only one price on a page.data for the past year, by market segment. If you have more than one Room Class, the system distributes projections to them primarily according to their capacities. For distributing the revenue projections, your pricing structure andPrice Rankingalso matter.G3 RMSthen  uses the simulated historical data, the booking patterns, and on books data to create forecasts and decisions.
- After the process completes, the Projections and Booking Pattern tabs are unavailable. IDeaS tells you when you can continue with the next step.
- Create and Commit Forecast Groups. SeeForecast Groups Setup.
- Forecast Review: Regularly review your projections to ensure that they stay accurate compared to actual pick-up, seereview the projectionsfor details. To change your projections, contact IDeaS to unlock that pageand to request running a new Synthetic Data build.  To see when the last processing ran, click Important Informationin the top right.
- ManageG3 RMSin Synthetic Data:After you switch toDecision Delivery ModeA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system., you are fully using the system in your day-to-day operation. If needed, manage changes that require re-running the process.After a full year of normal business, most clients contact IDeaS to end the Synthetic Data phase. See Manage the Move from a Synthetic Data to a Standard build.Note: you can use Synthetic Data for longer, for example, if you expect very different business volume after the first year. For more details, see Synthetic Data After the First Year.
- After you switch toDecision Delivery ModeA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system., you are fully using the system in your day-to-day operation. If needed, manage changes that require re-running the process.
- After a full year of normal business, most clients contact IDeaS to end the Synthetic Data phase. See Manage the Move from a Synthetic Data to a Standard build.Note: you can use Synthetic Data for longer, for example, if you expect very different business volume after the first year. For more details, see Synthetic Data After the First Year.

## Best Practices

### Inform IDeaS of Milestones and Changes

The steps in the work flow rely on a specific order. You are responsible for most of them, but some must be completed by IDeaS. Therefore, when you complete Steps 1 to 6, contact us so that we can run the Synthetic Data build.
After the process completes, you can't change any of the Synthetic Data setup. To make a change to your data, contact IDeaS to unlock the tabs. After you complete your changes, contact IDeaS to request another Synthetic Data build. This reprocessing ensures thatG3 RMSconsiders the changes in its forecasts and decisions.
If you upload a new Projected Rooms Sold and Revenue file, it overwrites the previous data. Ensure that the new workbook is accurate to prevent the loss of data.
When you are ready to switch to a Standard build, contact IDeaS Support.

### Manage Synthetic Data After the First Year

Most clients use Synthetic Data only for a full year of normal business. But sometimes, new properties expect big changes in business in the second year. For example, business might change due to a better market presence or new corporate clients. In that case, forecasts might be too low when they reach into the second year because they are based on low actual production of the first year. In that case, continue using the Synthetic Data and update your projections, if needed.

### Manage Changes that Require Running a New Synthetic Data Build

Following are examples of changes that require you tocontact IDeaS to request a new Synthetic Data build:

#### Changes in the Opening Date or the Normalization Date

For details seeSelecting the Correct Dates for Your Projections.

#### Your Actual Business Is Very Different Than Your Projections

For details seeReviewing your Projections.
Changes to yourRoom Classsetup after the Synthetic Data build impact the outputs like pricing. That includes creating a new room type, moving a room type between Room Classes, and creating a new Room Class.
When market segments change afterthe Synthetic Data build, they impact yourBooking Patternselections.G3 RMSshows you the below warning messages:

##### Business Type Changes

When the business type of a market segment changes, for example from Group to Transient,G3 RMSwarns you. A red icondisplays after the market segment name in the Booking Pattern tab. It means that the selected pattern for that market segment has been removed. This removal applies if you selected patterns from either agenericor aspecific similarproperty.
Select a different pattern and verify that yourProjected Rooms Sold & Revenuevalues are still appropriate. If you need to make changes, contact IDeaS to unlock the tabsand to request a new Synthetic Data build.

##### New Market Segment

A new market segment triggers a yellow warning icon. It displays after the market segment name in the Booking Pattern tab. The warning means that you must assign attributes to the market segment inMarket Segment Setup.
After you assign attributes, contact IDeaS support to unlock the setup tabs so that you can set the Booking Pattern and update your Projections. Once complete,request a new Synthetic Data build from IDeaS.

### Manage the Move from a Synthetic Data to a Standard Build

After a year of normal business, a property can switch from a Synthetic Data to a Standard build. Here is a list of what to expect and do. Note that if your property belongs to a larger enterprise, a corporate office might complete some of the steps for you.
- When you are ready to switch, contact your IDeaS representative.
- After IDeaS advises you that the property is ready, assign attributes to your market segments at a more granular level. This helpsG3 RMSproduce better outputs like pricing.
- Review your setup and, if needed, make changes to reflect what you have learned in the first year. For example, if you used Synthetic Data for opening a new property, you might not have known who your appropriate competitors are. Ensure that you reviewPricing,Competitor Settings,Room Type,Price Ranking and Upgrade Path,andCost of Walk.
- IDeaS switches your property from a Synthetic Data to a Standard build.
- Use thereview processto check the forecast and outputs like pricing closely, because they likely changed significantly. That's due to the configuration changes and the change in howG3 RMSforecasts:During the Synthetic Data period, the system uses your projections and recent past trends to forecast.With a Standard build,G3 RMSuses recent seasonal performance and all the historical data that it collected during the Synthetic Data period. Seehow transient forecasts vary by days to arrival.Note: the system does not use all historical data if you placed rooms out of order during your Synthetic Data period and resolved the relatedAlertwith option C)Don't use the data to forecast. In that case,G3 RMSignores the out of order period.
- During the Synthetic Data period, the system uses your projections and recent past trends to forecast.
- With a Standard build,G3 RMSuses recent seasonal performance and all the historical data that it collected during the Synthetic Data period. Seehow transient forecasts vary by days to arrival.Note: the system does not use all historical data if you placed rooms out of order during your Synthetic Data period and resolved the relatedAlertwith option C)Don't use the data to forecast. In that case,G3 RMSignores the out of order period.
- If after your review you disagree with the forecast in general or for long periods of time, open acasefor a Forecast Review by Revenue Optimization Analysts. It illustrates the factors contributing to the forecast.
If after your review you disagree with the forecast in general or for long periods of time, open acasefor a Forecast Review by Revenue Optimization Analysts. It illustrates the factors contributing to the forecast.
- If you want to understand the past booking behavior which is the basis forG3 RMSforecasts, ask your IDeaS representative for a Market Segment-to-Forecast Group Analysis.
If you want to understand the past booking behavior which is the basis forG3 RMSforecasts, ask your IDeaS representative for a Market Segment-to-Forecast Group Analysis.
- If forecasts donât meet your expectations after steps 6. and 7., contact your IDeaS representative.
If forecasts donât meet your expectations after steps 6. and 7., contact your IDeaS representative.
- After the initial review continue to monitor outputs like forecasts and pricing regularly. Lessen the frequency and level of detail as you gain confidence.Notes:Group forecasts  improve over time. After the switchG3 RMSforecasts group demand based on the historical data and future definite groups. As more and more groups turn definite, the system learns to improve its forecasts.IfG3 RMSfinds large performance changes in the first three months after the switch from Synthetic Data, they have a larger impact on the forecast than similar periods in the past. For example, bookings increase greatly one month after your switch to a Standard build compared to similar periods during the Synthetic Data period. The system then uses the stronger booking levels of the recent past to forecast demand.
- Group forecasts  improve over time. After the switchG3 RMSforecasts group demand based on the historical data and future definite groups. As more and more groups turn definite, the system learns to improve its forecasts.
- IfG3 RMSfinds large performance changes in the first three months after the switch from Synthetic Data, they have a larger impact on the forecast than similar periods in the past. For example, bookings increase greatly one month after your switch to a Standard build compared to similar periods during the Synthetic Data period. The system then uses the stronger booking levels of the recent past to forecast demand.
- Three to six months after switching to a Standard build, you get an alert about switching tobooked data.The switch helpsG3 RMSimprove the distribution of demand by Room Class. Seebooked vs. stayedfor details.
