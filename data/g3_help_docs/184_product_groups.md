# Product Groups

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Linked-Products/Linked-Products-Product-Groups.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Linked-Products/Linked-Products-Product-Groups.htm`
- **Ingestion Date:** `2026-09-11 22:14:12`

---

# Product Groups

Use a Product Group if you require thatG3 RMSprices different optimized linked products with the same adjustment on the same occupancy date. For example, you offer two or more loyalty rates, and you want all to have the same adjustment. See the detailedscenariobelow.
Note:
- A Product Group can only include linked products that are not a Base Product of another product.  In the scenario below, you can't add Advance Purchase to a Product Group since it's the base product for another rate, Loyalty Advance Purchase.
- You can use a Product Group only for optimized products. For other linked products, you set the adjustment values yourself.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click Advanced Settings.
- ClickProduct Groups. You can create only one Product Group.
- Enter aNamethat describes the Product Group.
- ClickProductsand select the checkbox for linked products that belong to this group.
- ClickSave.

## Scenarios

### Using a Product Group to Manage Loyalty Rates

Loyalty rates are discounted products for  members of a loyalty program that must be booked directly with the property. In the below example, a property has an Advance Purchase product with a non-refundable deposit. It is an optimized product, priced 5 to 20% offBARBest Available Rate. The lowest non-restricted product with flexible cancellation policy that anyone can book. The RMS optimizes the pricing of the BAR product. Other products, like Advanced Purchase or packages, can be linked to the BAR price.. Both products have loyalty versions, Loyalty BAR and Loyalty Advance Purchase. Each is set up with an adjustment range of between 1 and 5% off the non-loyalty version. The property wants the adjustment for the two loyalty products to be the same on any given occupancy date.
Therefore, they add a Loyalty Product Group that includes Loyalty BAR and Loyalty Advance Purchase. WhenG3 RMSselects the optimal adjustment for the two Loyalty rates for a specific date, it considers that they must be the same percentage.
Note that the adjustment range for the products in the Product Group don't have to match. In this example, Loyalty BAR could be -1 to -10% and Loyalty Advance Purchase could be at -1 to -5%. In that case,G3 RMSkeeps the adjustment at the shared range of -1 to -5%.
