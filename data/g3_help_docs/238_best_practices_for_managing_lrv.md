# Best Practices for Managing LRV

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/BP-Managing-LRV.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/BP-Managing-LRV.htm`
- **Ingestion Date:** `2026-09-11 22:14:47`

---

# Best Practices for Managing LRV

## Reviewing LRV

Complete the following to investigate the LRV. Or review itspurpose and frequently asked questions.
- Clickand thenInvestigator.
- Select the date to review.
- Scroll down to Pricing Details and click the Price for the Room Class to review.
- Check the last bullet point under Additional Details whether there is enough demand to fill the Room Class.
- ClickSee more details.
- Compare Remaining Demand - Total against theAvailable Capacity to SellPhysical Capacity plus Overbooking minus On Books and minus Out of Order. This value is the number of rooms that the RMS can sell before the property or room type is sold out.for the selected Room Class.
If the demand value is larger than the capacity, then there is enough demand to fill the Room Class andG3 RMSuses LRV to restrict demand. If you need to analyze the business mix, view the remaining demand by Forecast Group.
Are you wondering why LRV is well above zero even though Total Demand is well below Authorized Capacity? If you have more than one Room Class, this is likely due to the Upgrade Path.
In Investigator, review the Pricing Details for the date in question. In this example, LRV for Standard, Deluxe and Premium is in the 100 to 200 range:
But when you select the Room Class and scroll down to review the Price Ranking Chart, you can see that, on Sept. 15, the combination of On Books and Remaining Demand (=Total Demand) for Deluxe and Premium doesnât reach the Effective Capacity line. That means demand is well below capacity for both, so why the high LRV?
There are three factors that explain this:
- The solid blue arrows indicate that theUpgrade Pathis enabled between Room Classes: from Standard to Deluxe and to Premium.
- Demand for the Standard Room Class exceeds capacity (above the gray line) and the excess demand is enough to fill Deluxe and Premium with upgrades or upsells.
- To maximize revenues,G3 RMSbalances the LRV across Room Classes so that a higher-ranked Room Class (with the Price Rank and Upgrade arrow) always has a higher LRV than a lower-ranked Room Class. Without this balancing, LRV might be 500 for Standard and close to zero for Deluxe and Premium. That would mean that a guest could book a low-priced rate code around 100 for the higher Deluxe and Premium Room Classes, but not for Standard. Not a revenue-optimal or logical situation. With balancing, the LRV for all three Room Classes is well above 100 and the low-priced rate code can't be booked.
Use the Pricing Details table in Investigator to review LRV for neighboring days. While the system calculates LRV for each occupancy date, it finds an optimal mix of demand that results in the maximum revenue for a whole set of days rather than for each individual night. The system might be very restrictive for a peak night that has more demand than capacity to direct demand to shoulder nights that do not have enough demand to sell out, which you can see in the week below.

## Setting Up theselling systemfor LRV

To apply the LRV in aselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.,G3 RMSadjusts the value to changes occurring in between optimizations. The adjusted value is called a Hurdle.
You must enable and set up Hurdles in your selling system. Your selling system uses Hurdle values to handle reservation requests.
Use these best practices to ensure they function correctly. Some  features might not be supported by your selling system. For specific setup help, , contact your IDeaS representative. Or reviewhowG3 RMSapplies the LRV in theselling system.
For yielding purposes, theselling systemuses the value from the Rate Detail within the Rate Code setup, loaded for each room type.
If you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration.,G3 RMSadds thetax amountto the LRV. That allows for correct restrictions of your tax-inclusive rate codes. Discuss your setup with your IDeaS representative prior to decision upload.
You may have set up package elements in yourselling systemfor accounting purposes (for example, a package element to inform theselling systemthat the setup of the Bed and Breakfast package rate of $120 includes $20 breakfast revenue and $100 room revenue). Theselling systemignores that package element for yielding purposes and compares $120 against theHurdle valueunless you deduct the $20 as a cost to lower the yieldable value.

#### Yieldable

Theselling systemcompares the setup value of a Yieldable rate code against theHurdle valueto decide it's available or not. In other words, the availability of the rate code is at the full discretion of the property.

#### Non-Yieldable

Some rate contractsor the top level of a hotel loyalty programmay require a Non-Yieldable status. That means theselling systemchecks the rate against any inventory restrictions but doesn't compare it against theHurdle value. Except for contractual obligations, use of Non-Yieldable status for a rate code should be rare.

#### Yield As

Last Room Availability (LRA)rate contracts mean that a rate must be available as long as the contracted room type is available forBARBest Available Rate. The lowest non-restricted product with flexible cancellation policy that anyone can book. The RMS optimizes the pricing of the BAR product. Other products, like Advanced Purchase or packages, can be linked to the BAR price.. IDeaS recommends that you set these rate codes to Yield As the highest BAR rate (for BAR by LOS) or the Daily BAR rate plan (for BAR by Day) to ensure that LRA rates are restricted when BAR rates are restricted.
Having an LRV doesn't replace your selling strategy. For example, if you have a very low employee rate that is not meant for general sale, you must still set up the rate accordingly in theselling system. Otherwise, a zero LRV in low demand periods opens such a rate for sale.
After you enable Hurdles in your selling system, remove all manual restrictions except those that are related to the strategic availability of rates. An example of a strategic availability is a rate with a two night minimum stay requirement. Such a rate needs to be set up or restricted to only allow reservations with a minimum length of stay of 2 nights. The same applies to advanced purchase rates: the minimum days to arrival restriction should still form part of the rate set up. For example, an advanced purchase rate that should only be sold 21 days prior to the arrival date should have 21 applied in the Minimum Advance Booking Window set up within the rate code.
