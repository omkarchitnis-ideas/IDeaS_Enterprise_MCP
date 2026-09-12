# Best Practices for Supplements

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BP-Supplements.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BP-Supplements.htm`
- **Ingestion Date:** `2026-09-11 22:14:21`

---

# Best Practices for Supplements

## Set up Supplements Only Where Needed

You are not required to set up supplements for all room types. For any room type, occupancy type or day of week that does not include supplements, keep the default supplement value as 0.00. You also have the option of adding in a supplement cost just for a specific season.
The price for rooms only, without the added cost of supplements, displays as Rooms Only BAR inPricing.

## Include Taxes

If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter Supplements inclusive of tax. This applies to all pricing setup  values. ViewEntering and Display of Taxes inthe RMSfor more information. The tax for Supplements is only broken out by your PMS, but not bythe RMS.

## Include Supplements in Pricing Values

When you set upCeiling/Floor, enter the values inclusive of the single occupancy supplement. You also enter Specific pricing overrides as the final price, including the cost of the single occupancy supplement.The RMSsends your price override to yourSelling SystemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data..

## Exclude Supplements from Offsetsand Minimum Price Differentials

Exclude the cost of supplements when you enterOffsets.Also exclude supplements if you need to set upMinimum Price Differentials.

## Know the Impact of Changing Supplement Values

If you change the supplement values,the RMSignores theMinimum Change Valueand updates and sends any pricing decisions that changed as a result of the new pricing setup .

## Scenarios for Pricing Calculations

Supplements are set up for each room type, occupancy type, and day of week. To determine the pricing decision,the RMSadds supplement andOffsetvalues to the Optimal Price. Unlike offsets, supplement values for each occupancy type are added individually, not cumulative on top of the single occupancy value. Rounding the pricing decision also applies if you set upRounding Rules.
See thePricing Overviewfor details on howthe RMScalculates Final Price, considering rounding rules, offsets, supplements, and minimum change.
In the example below, the hotel charges the same price for single and double occupancy for all room types. They also add a charge for each extra adult and an extra breakfast charge per adult, but a child breakfast is free. For simplicity, extra child does not display in the example below, but it works the same as extra adult.
