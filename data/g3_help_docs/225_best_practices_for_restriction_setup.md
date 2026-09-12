# Best Practices for Restriction Setup

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/BP-Restriction-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/BP-Restriction-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:14:39`

---

# Best Practices for Restriction Setup

## Determine If You Need to Set up Restrictions

You know all the selling systems and channels that you work with. IDeaS knows how to integrate them withthe RMS. Therefore, as part of the sales and implementation process, we ask you for a list of your selling systems. Based on that list, your IDeaS contact tells you what setup you need to complete inthe RMSand your selling system.
If you do not complete the setup for a selling system, or if you add or change a selling system without informing IDeaS, that selling system cannot receive controls fromthe RMS. Its pricing and availability of yieldable rates might be out of parity with your other channels. If you are unsure about how controls fromthe RMSare implemented in one of your selling systems, please contact your distribution partner.

## Set up Yieldable Rate Code Values Correctly

Some selling systems allow you to add yieldable costs and values (also referred to asHurdle Rate Adjustments) to rates for adjusting the value at which the rate  is yielded. For example, a $200 package may include $100 of costs for non-hotel items like tickets or limo, so for yielding purposes, you might want the rate value to be only $100, not $200.
Yieldable costs and values allow you to achieve this in a reservation system, like your PMS or CRS. However, many reservation systems don't provide this information tothe RMS. Therefore, set up the yieldable rate code values so that they represent the value that you want LRV to control.

### Examples

- Refer to the above example of the package that includes $100 in tickets. If the total value is fixed at $200, then set up the rate only at the value of the pure room revenue or the value at which you wish to yield the rate, so $100 in this case.
- If you have a corporate rate that is 15% off BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) that must remain available as long as BAR is available due to anLRA (Last Room Availability)commitment, set up it with a 0% offset.
- In a resort or casino property, you might offer a discounted rate to those guests that spend the most on other revenues like gambling, spa or golf. Load the rate as derived off BAR with a value that represents the additional value that those guests spend above the average guest that paysthe primary priced product.
- Review theLOS1 BAR Bed and Breakfast RateandLOS1 Tax Includedexamplesbelow. .

## Only Set up Rates Unique to Channels That Can't Accept LRV

Only set up rates that are unique to those channels that can't accept LRV. For example, you have an Advanced Purchase rate that you sell both on your direct channels and on OTA channels. Your direct channels accept LRV, but the OTA channels don't. In this case, we recommend that you create two separate rates, one for direct and one for OTA channels.
This is because the selling system for your direct channels checks for restrictions like MinLOS and FPLOS before it checks for LRV. And  if MinLOS or FPLOS prevent the sale of the rate, the LRV is never checked. But you want selling systems to check for LRV because it is the better, more  flexible restriction. And if you have two separate Advanced Purchase rates, the direct channel continues to use the more flexible LRV restriction. Only the OTA channels use the MinLOS or FPLOS restrictions, since this is all they can accept.

## Only Set up the Necessary Room Types

You might have rates that you sell only for some room types but not for others. For example, you have a derived corporate rate for which you do not sell your Suite room types. In this case, leave the Suite room type fields blank, andthe RMSwill not produce any restrictions for the room type.

## Manage Rate Fences in Your Selling System

For example, you have a promotional rate that requires a minimum length of stay (MinLOS) of three nights. If the LRV is zero or below the value of the rate,the RMSdoesn't create a restriction for this rate. To ensure that the rate isn't available for a one-night stay, set up the MinLOS fence in your selling systems. The set up varies by system, it can be either in the setup of the rate itself (for example in the Rate Header) or as a restriction on the rate code level (the RMSapplies its restrictions at the rate code by room type level).

## Use the Restriction Report to Manually Control Rate Availability

The RMScan include theFPLOSRestrictions that determine if a rate is open for an arrival date and length of stay. See the scenarios in the Restriction Configuration topic for examples.orMinLOSRestrictions that prevent the guest from booking a stay shorter than the number of days selected. See the scenarios in the Restriction Configuration topic for examples.restrictions in the decision uploads, if your selling systems support that. Otherwise, use the Restriction Report to implement the restrictions manually.See theRestriction Reportto view the MinLOS or FPLOS restrictions thatthe RMSgenerates.

## Contact IDeaS for Questions

Managing the distribution of your rates and availability in all your selling systems is complex. Some systems can accept and translate LRV, which enables them to distribute to other selling systems that don't accept LRV directly. In such a casethe RMSdoesn't need to deliver restrictions in addition to the LRV. In other cases, MinLOS or FPLOS need to replace LRV entirely. Contact your IDeaS representative if you have questions about howthe RMSdelivers controls. Consult with your IDeaS and selling system contacts regarding distribution requirements.

## Set the Values for Linked Products in Pricing Setup

Use theRestrictionstab in linked products setup to define the rate codes for whichthe RMSshould use the value from Pricing instead of from Restriction setup. This avoids defining the value of linked products twice, in Restriction and Pricing setup. After you select rate codes in the Restrictions tab of Pricing setup for linked products, you define their value in Pricing setup for linked products, not in Restrictions setup. The selected rate codes display in Restrictions setup in a new tab, Product Restrictions. You can use the tab to:
- View the rate codes that you selected in the Restrictions tab of linked products setup.
- Select theDo Not Generate Restrictionsbox if you don't wantthe RMSto send restrictions for a rate code.
- Click the product name to open linked product setup.

# Scenarios for Calculations

The calculation for converting LRV to restrictions varies by product type and whether you selected MinLOS or FPLOS restrictions, but the process is the same.The RMScompares the LRV against the value of the yieldable rate (as defined  in Restriction setup), by room type, day of week and, if applicable, by season. If the LRV is larger, it produces a restriction that indicates that the rate or rate category is not available for a given arrival and stay pattern and room type.
Note:The RMSdoesn't translate LRV into more restrictive controls like Closed to Arrival (CTA) or Closed (for all stay-throughs).
In all the following examples, BAR refers to yourprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..

## MinLOS Restrictions

For all examples, the values in the table are for an arrival on Thursday, April 1 for a Standard King room type. 
The first and second example are for a rate query for a 1-night stay and for a U.S. property, meaning it sells rooms excluding tax. Therefore, the examples do not consider tax deductions â all revenue is attributed to room revenue.

### LOS1 â Simple Example

### LOS 1 BAR Bed and Breakfast Rate

In this example, we only use the 10% off BAR derived version of the above example. The main difference is that  both the BAR price point and the corporate rate include breakfast, which is valued at $20.
Remember that for yielding purposesthe RMScompares only the room revenue value against the LRV. The room revenue for a derived rate  is calculated based on the BAR decision, which in turn uses the set up BAR values that exclude breakfast (and, if applicable, taxes).

### LOS1 Tax Included

The next example is a 1-night stay when your property uses tax-inclusive pricing. In this example, the tax is 20%, and BAR and CORPL20 do not include breakfast. Instead of a percentage, the corporate rate is a fixed $20 off BAR.

### LOS - BAR by LOS

If you book a multiple night stay, there are slight differences by BAR type. In both examples, we use a 3-night stay for arriving on Thursday, and the property sells exclusive of tax. Both examples also illustrate restriction calculation for a derived rate with different fixed discounts by day of week.

### LOS3 - BAR by Day or Continuous Pricing

## FPLOS Restrictions

For this example, we look at LOS1 to LOS7 for the same Thursday, April 1 arrival. CORPGOV is a fixed rate: $100 for Monday through Friday and $125 for Saturday and Sunday.
For each LOS, we add the total LRV and compare it to the total rate value for the same LOS. For example, the total LRV for a 2-night stay is Thursdayâs $90 + Fridayâs $120 = $210. That total is higher than the total CORPGOV value of $200 ($100 for Thursday and Friday each). Therefore, LOS2 has a X for Closed (O is for Open).
Delete this text and replace it with your own content.
