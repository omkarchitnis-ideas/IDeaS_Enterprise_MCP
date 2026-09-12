# Best Practices for Linked Products

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Linked-Products/BP-Linked-Products.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Linked-Products/BP-Linked-Products.htm`
- **Ingestion Date:** `2026-09-11 22:14:16`

---

# Best Practices for Linked Products

You can manage linked products in yourselling system, but there are benefits when you use linked products instead.

#### Flexible and Dynamic Pricing Made Easy

The RMScanoptimizethe pricing of linked products for you, based on the demand for each product. Instead of fixed or ruled-based pricing, the system selects the optimal price from an adjustment range that you define. And it does that for each linked product and in each processing.

#### Ease of Use

You can set up pricing of linked products  easily and with more details, like discounts by days to arrival or by season. You can also view and manage the prices of your  products in one place.

#### Better Optimization

Linked products givethe RMSmore information about the value of your products. For example,the RMSknows that a market segment with a Qualified Linked attribute includes rate codes whose pricing is based onthe primary priced product, but not if that means 5%, 10%, or 20% off the price. It estimates the pricing based on historical data.
For linked products, you define their pricing. And knowing the value of the products helpsthe RMSbetter optimizeLast Room Value (LRV)andpricing.
You can choose to control the pricing for your products or you can letthe RMSoptimizepricing from a range of adjustments that you define. In both cases the system's process looks like the below.SeePricing Scenariosfor examples.
When you add a new optimized product with no or limited history, you want to link it to a similar rate code with a lot of history. Then,the RMScan use the history to understand how the price behaves.
For example, you replace an advance purchase promotion, rate code ADVP, with a new promotion that is changeable for a fee, rate code CHANGE. In  the product Definition of the new promotion, you add both CHANGE and ADVP as Rate Codes in theDefinitionsof the product.
If linking another rate code isn't possible, we recommend that you use a small range for the adjustment values. Without historical data,the RMSlikely prices the product close to the median value of the adjustment range (after considering the hierarchy), until it has enough data to more accurately determine the weight for the product.
This best practice applies to adding any product if your property has limited history, like in a Synthetic Data build.

## Pricing Scenarios

Values in the Product Adjustment column might be set up by you or optimized bythe RMS. The values only illustrate the calculation.
Note:
- Example row 1: the calculated value of 85 is adjusted up to 90 due to the Floor value.
- Example row 2: the rounding rule requires rates end in 5.00, so the calculated value is adjusted up from 152.60 to 155.00.
- Example row 3: the  rounding to 9.00 would result in a value of 99. But 99 is below the Floor Value of 100, therefore the Final Price is 100. Note that rounding rules apply only to theFloor TypeAdjustment to Primary Product Floor, but not to this Fixed type of 100. For Fixed Floor Type, ensure your Floor values match your rounding rules, in this example 99 or 109.
- If the product's floor conflicts with its adjustments, the floor wins. For example, a product's adjustment is between 10% and 40% offthe primary priced product. The price ceiling is 500 and floor is 100. The available range for the product is therefore from 450 (500 - 10%) and 60 (100 - 40%). If you set a product floor of 455, it's higher than the range allowed by the adjustments.G3 RMSpicks the floor value of 455.
- If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter all values in Linked Products setup inclusive of tax.  ViewEntering and Display of Taxes inthe RMSfor more information.
