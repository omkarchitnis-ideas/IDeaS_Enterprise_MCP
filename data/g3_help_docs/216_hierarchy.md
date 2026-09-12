# Hierarchy

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Linked-Products/Linked-Products-Hierarchy.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Linked-Products/Linked-Products-Hierarchy.htm`
- **Ingestion Date:** `2026-09-11 22:14:33`

---

# Hierarchy

Use this feature to ensure thatG3 RMSmaintains a pricing hierarchy between products.
You have two linked optimized products that require a deposit and are derived off the fully flexible, unrestricted, public rate code, usuallyBARBest Available Rate. The lowest non-restricted product with flexible cancellation policy that anyone can book. The RMS optimizes the pricing of the BAR product. Other products, like Advanced Purchase or packages, can be linked to the BAR price.. One, Advance Purchase, is non-refundable and can't be changed. The other, Semi-Flexible, can be changed for a fee. Since Advance Purchase has stricter conditions, you set up a Hierarchy for this linked product so that it's always priced below or equal to the Semi-Flexible product.
You can also use Hierarchies for independent products. For example to ensure that the extended stay product for stays of 30 days or longer is always priced equal or below the product for stays of 7 - 30 days.
To learn how to avoid theInvalid Hierarchywarning during the setup,  viewbest practicesfor Hierarchy setup.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click Advanced Settings.
- ClickHierarchy.
- UnderProduct, select the product that needs to be priced less than or equal to another product.
- UnderRelates To, select the higher priced product for this rule.
- If needed, define aMinimum Differencebetween the two products.G3 RMSmaintains the difference between theFinal PricesThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing.of the two products.
- Click to addthe hierarchy rule.
- Repeat steps 4 to 6 to add other  hierarchy rules.
- ClickSave.
