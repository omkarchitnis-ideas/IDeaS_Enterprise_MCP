# Best Practices for Minimum Price Differential

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/BP-Rooms-Minimum-Price-Differential.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/BP-Rooms-Minimum-Price-Differential.htm`
- **Ingestion Date:** `2026-09-11 22:14:44`

---

# Best Practices for Minimum Price Differential

## Align Minimum Price Differentials with Your Past Pricing

For example, if you priced Deluxe 10 above Standard in the past, don't use a Minimum Price Differential of 30. Otherwise, price ranking forcesthe RMSto push up the prices of higher ranked Room Classes as well. That might lead to uncompetitive pricing for those higher ranked Room Classes.

## Align Minimum Price Differentials with Pricing Setup

Set a Minimum Price Differential that is smaller than the difference between the Floors (and Ceilings) of two Room Classes. For example, for Standard Room Class the Floor and Ceiling are 100 and 150, for Deluxe 140 and 190. The system wants to select the lowest price for Standard and Deluxe. But if you set a Minimum Price Differential of 50, then the system can't select the Floor values (100 for Standard, 140 for Deluxe), because they are only 40 apart.

## Understand Howthe RMSApplies Minimum Price Differentials

As part ofPrice Ranking,the RMSapplies the Minimum Price Differentials  to the Optimal Price decision, before applyingRounding RulesandSupplements. SeeHowthe RMSDetermines Pricing. SeeHowthe RMSDetermines Pricing.
Notes:
- Other setup, for example, setting appropriate Ceiling and Floor values for each Room Class, Price Ranking, and Rounding Rules might already ensure differentials.
Other setup, for example, setting appropriate Ceiling and Floor values for each Room Class, Price Ranking, and Rounding Rules might already ensure differentials.
- The RMSdoesn't apply the differentials to Room Class Group Evaluations.
The RMSdoesn't apply the differentials to Room Class Group Evaluations.

## Use Minimum Price Differential if Past Pricing Isn't Representative

Use a Minimum Price Differential if the historical ADR difference between two Room Classes is no longer representative. For example, in the past the ADR difference between your Standard and Deluxe Room Classes was very small. That's because they were very similar or because the Front Desk regularly upgraded guests for free. Now you expect a higher ADR difference because of a renovation or because of a change in the upgrade policy. In that case, you might need to set a temporary Minimum Price Differential. Oncethe RMSlearns the new differential from the historical data, you can remove it.

## Include Tax

If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter Minimum Price Differentials inclusive of tax. For example, if you require a minimum price difference of 10 between the Standard and the Deluxe Room Class, enter 10. If your tax is 20%, the Minimum Price Differential of 10 includes a tax of 2. ViewEntering and Display of Taxes inthe RMSfor more information.

## Exclude Supplements

If your property set up non-roomSupplements, the differential values should not include the cost of non-room supplements. For example, you require a minimum difference of 30 between the Standard and the next higher Deluxe Room Class. But out of the difference of 30, 20 is breakfast and set up as a supplement. In that case, enter 10 as your Minimum Price Differential.The RMSadds 20 when it calculates the Final Price decisions.

## Monitor Your Overrides

If you enter a Specific pricing override, your override does not adjust to fit your Minimum Price Differential rules. Seebest practices for overriding pricingfor more information.

# Scenarios

## Minimum Price Differentials Might Restrict Optimal Pricing

Before you set up any differential, remember thatthe RMSalso considers yourPricingSetup and Price Ranking when it prices Room Classes.  Adding a Minimum Price Differential might restrict the system's ability to find the optimal pricing decision. Here is a simplified example:
The Standard Room Class is ranked lowest as number 1, and its pricing decision is $199. For the Deluxe Room Class, the next higher ranked one, you set up pricing from a Floor of $150 to a Ceiling of $250. You also require rounding to rates ending in $9 for both prices. Based on very low Deluxe demand and the observed price sensitivity,the RMScalculates optimal results if Deluxe is priced only slightly above Standard. With a $0 minimum differential,the RMScan price at $209 and maximize revenue.
However, if you set a $30 minimum differential between Standard and Deluxe, the lowest possible pricing decision thatthe RMScan select is $229. In this scenario, though, there might be no demand for Deluxe at $229. Therefore, if you enable upgrades between Standard and Deluxe,the RMSmight forecast to overbook Standard up to the amount of the unused Deluxe capacity. You will sell only rooms at $199 and upgrade many to Deluxe, instead of selling at least some Deluxe at $209.

## The RMSCan Ignore Minimum Price Differentials due to Minimum Change Values

See this scenario inMinimum Change Value.
