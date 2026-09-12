# Last Room Value (LRV)

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/LRV.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/LRV.htm`
- **Ingestion Date:** `2026-09-11 22:12:54`

---

The purpose of Last Room Value

# Last Room Value (LRV)

G3 RMSuses the Last Room Value (LRV) to help you accept only the most valuable demand. LRV helps you block lower-valued yieldable business whenG3 RMSthinks that your property might sell out.
For example, an LRV of $150 means that guests can book a Flexible Rate product at $160, but not a discounted PrePay&Save product at $140.G3 RMSoptimizes LRV by Room Class.See an overview video in the Resources on the right.
If your property uses Profit Optimization, the LRV is based on profit. Review the differencesin this topic.
Let's use an example to illustrate the LRV. Imagine a five-room hotel that is so popular that ten guests want to book it. The guests differ in how much they are willing to pay. Five want to pay $200-$300, and the other five want to pay less than $200. Based on the hotelâs demand and forecast, we want to allow only the five highest paying guests to book. To do that,G3 RMSsets the Last Room Value at $200.  Like a bouncer at a nightclub,  the LRV enables you to prevent everybody wanting to pay less than $200 from  booking a room at your hotel.
Of course, real life is more complex than a five-room hotel with exactly 10 rooms of demand. That's whyG3 RMScan send other values to yourselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.. They ensure that the LRV remains current between optimizations, while reservations are being booked and canceled.The selling system uses the LRV and these other values fromG3 RMSto calculate a Hurdle value. The Hurdle value helps the system decide if a rate code is available or not when a guest inquires. Learn more aboutHurdle valuesandbest practicesfor setting up yourselling system.

### What Help Do You Need With LRV?

- I want to review thebest practices and examplesfor LRV.
- I need to learn howG3 RMScalculates LRV.
- I want to understand ifG3 RMSwants me tosell a $10 Rate if the LRV is only $10.
- I need toinfluence the LRV.
- I want to know what happens ifLRV is higher than the highest price.
- I need to learn abouthowG3 RMSadjusts the LRV for theselling systemandhow I can set that up.

## Frequently Asked Questions

G3 RMScalculates LRV for each occupancy date,  for each Room Class and length of stay. The below factors impact LRV. To investigate LRV, review theBest Practices.
- The volume of demand, or how many rooms are on books, how many are still expected, and how much of that demand will wash. Review the demand and wash forecast fromDemand and WashManagement, or learn more abouthowG3 RMSforecasts unconstrained demand.
- The value of demand. Calculation varies by type of demand. For example, the value of the Equal to BAR Unqualified demand is based on the Ceiling/Floor values that are set up, while non-linked qualified demand is based on historical and On-Books ADR.
- The uncertainty of the demand to come. For example, far into the future uncertainty is high andthe RMSmight price lower.You can see uncertainty in theActual versus Expected On Booksdata in the Investigator.Another example is the impact on LRV. A 0.00 LRV day has the same impact on restrictions as a 0.01 LRV day, but the uncertainty might be very different: for the 0.00 day,the RMSis certain that demand is not enough to fill the property. But with 0.01 LRV, there is still some uncertainty about the volume of demand. There might be a chance that demand reaches or surpasses capacity as the arrival date approaches and asthe RMSreceives more data.
- Available Capacity to SellPhysical Capacity plus Overbooking minus On Books and minus Out of Order. This value is the number of rooms that the RMS can sell before the property or room type is sold out.. Setup settings likeRoom Typeor theUpgrade Pathcan affect that capacity, so they also impact the LRV.
- The Booking Pace, or when different types of business book.
- Maximizing revenue overall, not just for a single day, single length of stay, or a single Room Class.In theInvestigate the Impact of Neighboring Daysexample, a very high LRV on the peak night versus very low ones on the shoulder nights helps smoothing out demand patterns.TheWhy DoesG3 RMSselect a Price below LRV?scenario shows how LRV supports stay-through demand.TheInvestigate LRV across Room Classesscenario shows why the LRV might be high for a low-demand Room Class.
- In theInvestigate the Impact of Neighboring Daysexample, a very high LRV on the peak night versus very low ones on the shoulder nights helps smoothing out demand patterns.
- TheWhy DoesG3 RMSselect a Price below LRV?scenario shows how LRV supports stay-through demand.
- TheInvestigate LRV across Room Classesscenario shows why the LRV might be high for a low-demand Room Class.
- Maximizing revenue while optimizing Pricing, Last Room Value and Overbooking together. For an example of how overriding one decision impacts the other two, seeBest Practices for Overbooking.
The LRV is a value andnota price or rate.  Last Room Value is the maximum room revenue that you can expect to make from the last room available for sale. Thus, if your demand is less than your capacity, the LRV will be zero because the last room available for sale will remain unsold. With an LRV of zero,G3 RMSisnotselling a zero dollar price but is accepting rate codes that are above that zero value. You can set upG3 RMSto send the LRV  as a control to thedesignated reservation system (typically your PMS or CRS), where it acts like a nightclub bouncer to accept all rates.
You can't override LRV, but you're still in control because you can influence it. Unlike pricing, LRV is not a familiar concept for which you  have set  the value before. The complex calculations of the LRV data inputs are impossible for anyone to replicate at the required granularity. However, like pricing, you can directly influence LRV through the inputs into optimization. Unconstrained Demand is one of the inputs into LRV. If you know something about the remaining demand that the system does not, share that information through aDemand Override. The change in demand will have a direct impact on LRV and other outputs.
LRV is calculated by arrival day, Room Class, and for each length of stay. If the LRV is higher than your highest value ofthe primary priced product, your guests might no longer be able to book that Room Class for that day and length of stay, since the LRV closes all lowerYieldablerates.
G3 RMSmarks these days with a LRV Greater Than Price iconinPricing.
For example, if your property has Standard and Suite Room Classes, and the Standard LRV is larger than your highest Standard rate for a one-night stay, the icon displays for the Standard Room Class. The icon indicates that your guests might no longer be able to book any Standard Room for a one-night stay, since the LRV closes all lower yieldable rates, includingthe primary priced product. At the same time, the Suite LRV might be lower than your highest Suite rate, so Suites will remain open.
G3 RMSmight expect that you need to accept some lower value business to maximize revenues. For example, if your overbooking is high due to high wash expectationsor due to your upgrade path, then Available Capacity to Sell might exceed Remaining Demand and the LRV will tend to be low. If you do not agree with the Remaining Demand, share what you know withG3 RMS.
What if LRV is near or at zero even though your property is already sold at or above the property overbooking level and Remaining Demand is very low? This might occur because the system considers that if On Books business cancels more than expected, it will be difficult to fill the open rooms due to the low remaining demand. So if cancellations cause rooms to become available, a low LRV ensures that the property accepts all possible remaining business.
Are you far out from the day of arrival in the booking curve? Uncertainty is higher for dates further in the future when On Books is low. Therefore, LRV might be low.G3 RMSwill likely raise the LRV as business materializes and the uncertainty decreases. Use thebest practices to review the LRV.

#### When the Restricted Price Is Not the Highest Available Price

If your property usesBAR by Day pricing, the price might be restricted by the LRV on a day when the selected price is not the highest available price point, as a result of stay-through demand.
With this type of pricing, the pricing decision for each day is used by both one-night stays and guests staying through that night.G3 RMSmight select a price below LRV for a single day, even though a higher price is available. That is because it wants to encourage more stay-through demand.G3 RMSmarks these days with an LRV Greater Than Price icon.
This scenario does not apply to BAR by LOS pricing, becauseG3 RMSprices each LOS independently.
The following example shows a three-night stay: Tuesday-Thursday. The pricing decision for Wednesday is the highest available price. An LRV Greater Than Price icondisplays on Tuesday, because BAR 2/190 is below the LRV of 200:
In this example, the system keeps the pricing decision lower on Tuesday to maximize revenue across all lengths of stay, as indicated by the LRV Greater Than Price icon. The restriction could be related to the three-night length of stay or demand from any longer stay.
For a BAR by LOS property, BAR is not restricted for Tuesday because the price for a three-night length of stay is above the LRV of 400.

#### When a Room Class BAR Is Lower Than LRV

In some instances,G3 RMSmight set the pricing decision for a Room Class below LRV, even though a BAR level priced above LRV is available. This instance is similar to the condition that triggers thePricing Override is Below the Last Room Value (LRV) Exception. The decision appears to be a suboptimal, so why would the system choose it? The answer is thatG3 RMSchooses the optimal decisions to maximize revenues across all Room Classes, which might mean that the decision for a single Room Class appears suboptimal.
Occurrences of this condition often result from setup issues, specifically restrictive overbooking and upgrade paths. For example, a property has Standard and Deluxe Room Classes. Standard still has a lot of demand at around $200, but it is already sold out and overbooking is set up at none. The higher Deluxe Room Class still has a lot of inventory, but not enough demand to fill it, so the LRV for Standard might be $200 and Deluxe is close to zero.
Even with Upgrade Path enabled, you cannot sell any more Standard rooms due to the lack of overbooking, regardless of the price. So the only way to maximize revenues is to price Deluxe similar to the $200 Standard demand. However, the highest possible price for Standard is $250, and the Room Class order prevents the system from selling Deluxe below Standard. Thus, the only way to price Deluxe at around $200 is to push the Standard decision below that, like $180. Since the pricing decision for Standard is irrelevant because you cannot sell any more Standard rooms anyway, the system sets a suboptimal Standard price in order to sell Deluxe and maximize revenues. If the property disagrees, they can override the pricing decision.
To apply the LRV in aselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.,G3 RMSadjusts the value to changes occurring in between optimizations. The adjusted value is called a Hurdle. For example, a selling system gets 10 new reservations for a date right after getting a new LRV fromG3 RMS. To account for these changes,G3 RMSadjusts the LRV with values like the LRV Delta, which it adds to the LRV for each new reservation. For details, seehow the Hurdle is calculatedorreview the best practices for setting up your selling system for the Hurdle.
When a selling system receives an inquiry for an arrival date and length of stay, it compares the Hurdle value against the setup value of a product (a rate code and room type combination) to decide whether that product is available or not.
For example, a reservations agent gets a call for a specific rate and runs a rate query in your selling system. For the requested date and length of stay, the price of that rate code for the standard room is $100. If the Hurdle for Standard Room Class is $90, the rate code shows available for standard. If the Hurdle is $110, the agent doesn't see the rate code. The same applies to availability searches on your web booking engine.
Note that the Hurdle can impact room types differently. In the previous example, the Standard Room Class LRV of $110 is delivered to the selling system for the ST and SK room types. The price for ST forthe primary priced productis $100, and for SK it's $120. In that case the price for ST is closed, while the price for SK is open.
Note: If your selling system doesn't support or yourG3 RMSsubscription doesn't include Hurdle values,G3 RMScan translate the LRV into another, less flexible, format, like Min LOS, for sending decisions. SeeRestriction Setupfor more information.

### HowG3 RMSCalculates the Hurdle

For each reservation inquiry the selling system  checks if a yieldable rate is available. To come up with the Hurdle, it starts with the Last Room Value, then adds theLRV Deltamultiplied by the smaller of:
- Number ofIncremental Rooms Soldsince the last optimization.
Number ofIncremental Rooms Soldsince the last optimization.
- Rooms Sold Ceiling.
Rooms Sold Ceiling.
Review what those three components mean or look at an example:
The Delta ensures that  the LRV adjusts between optimizations, based on new reservations or cancellations. A new reservation for a day increases the LRV by the Delta, a cancellation decreases it by the Delta, same for reservation changes.
In each optimization,G3 RMSrecalculates the Delta by Room Class and occupancy date, based on how much it expects On Books and LRV to change until the next optimization. Very simplified, if it expects both the LRV and the On Books to go up by 10, then the Delta is 1, meaning that 10 Deltas at 1 each increase the LRV by the expected amount of 10. If you have questions about specific Delta values,open a case.
Some selling systems might not support LRV Delta values, or they might not support this control at the Room Class level. If this control is not supported at the Room Class level,G3 RMSprovides Deltas at the property level.
The Rooms Sold Ceiling is  the maximum number of rooms to which the selling system applies the LRV Delta. The control is used to avoid that Deltas increase the LRV by too much in cases when many new reservations are made in between optimizations. For each booking, cancellation or change the selling system updates the number of transient Incremental Rooms Sold since the last optimization (and resets that number to zero after each successful upload of decisions fromG3 RMS). When the number of Incremental Rooms Sold exceeds the Rooms Sold Ceiling, the system stops adding Deltas and instead keeps the Hurdle value at the value of the Rooms Sold Ceiling.
The MaxSold value considers a property'sEffective CapacityThe property's physical capacity minus the out of order rooms., Overbooking, and Rooms Sold. When the number of Incremental Rooms Sold reaches MaxSold, the selling system stops accepting any more transient bookings.
That means that if new reservations reach the MaxSold level, your selling systems show you as not available for that date, Room Class and, if applicable, length of stay. But until the next optimization you still show available rooms inG3 RMS, because the new reservations are not reflected.
If you have questions about the MaxSold on specific dates,open a case.
In the below example the LRV for a given Room Class at the last optimization was $90. The Delta is calculated at $1 and the Rooms Sold Ceiling is 3. For the first room booked after the optimization (left side) the system uses the Hurdle value of $90. For each new room booked the Hurdle value increases by the Delta of $1, so for the fourth room it's $93. With the fourth room the Rooms Sold Ceiling of 3 is reached, since three Deltas have been added. That means that the Hurdle value now stays at this level, meaning if there is fifth (or more) booking the Hurdle remains at $93.

### Adjusting the Yieldable Value

To check availability, the selling system compares a rate's value  to the Hurdle. But what if the setup value isn't representative, for example, because it's a package containing theater tickets that bring you no profit. Then you want to adjust the yieldable value of the package to the value of the room revenue. The adjustment types vary by selling system, some examples are Stay Cost/Value, Fixed Cost/Value, Per Person Cost/Value, or Yield As.
- In the case of the package, deduct the costs of the package portion to lower the yieldable value. If the theater package is set up at $300, it may be the highest priced rate code that you offer, but it includes $200 in ticket costs that bring little or no profit for you. Subtract the $200 ticket cost to lower the yieldable value to $100. Such package adjustments might be per room per day, or per person per stay, or other combinations.
- Add value to increase the yieldable value of rates that deliver an add-on value to your property. 
For example, a resort or casino might offer a discounted $100 rate to guests who spend a lot of money in other areas, like gambling, spa or golf. The overall value of these customers to the hotel is much higher than the guest room rate. Thus, the hotel can add $200 of average expected spend in those other areas to increase the yieldable value to $300.
- Yield Asenables a rate code to have the same yield controls as another rate code. 
This option is often used for corporate rates that have Last Room Availability (LRA) status and can only be yielded the same asthe primary priced product. For example, if you set the corporate LRA rate code LRA1 to "Yield As" BAR (either the designated daily BAR rate code or the highest value BAR rate code), then the Rate Code LRA1 will be yielded at the value of the current BAR decision and not to the LRA1 value that is set up.
When the selling system evaluates a reservation inquiry against the Hurdle value, it calculates the Rate Value as follows:
Rate Yieldable Value = configured Room Rate value â negative Rate Adjustment Values and/ or + positive Rate Adjustment Values
