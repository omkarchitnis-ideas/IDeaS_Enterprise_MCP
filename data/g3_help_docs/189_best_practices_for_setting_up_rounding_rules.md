# Best Practices for Setting Up Rounding Rules

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BP-Rounding-Rules.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BP-Rounding-Rules.htm`
- **Ingestion Date:** `2026-09-11 22:14:15`

---

# Best Practices for Setting Up Rounding Rules

Review the following best practices for setting up Rounding Rules or view example in thescenarios.

### Understand whenG3 RMSApplies Rounding Rules

The RMSapplies price rounding rules to produce theFinal PriceThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing.value.
- For the Base Room Type,the RMSapplies rounding rules to the Optimal Price to determine Final Price.
- To price the other room types in the Room Class, the system appliesOffsetsto the Optimal Price of the Base Room Type. Then it applies rounding rules to determine Final Price.
SeeFinal Price Calculationfor an overview of howthe RMSconsiders rounding rules, offsets, supplements, and minimum change values.

### Align Your Floor and Ceiling Values with Your Rounding Warnings

A warning displays if yourFloor and Ceilingvalues in Pricing setup do not meet your rounding requirements. For example, your rounding rule requires all prices to end with 9.00, but you try to save a Ceiling value of 500. If you continue and save the 500, the systemâs Final Price will never be more than 499.
A warning also displays in Pricing if your override values do not comply with your rounding rules. Using the above example, you would not be able to set a pricing override of 500.

### Understand How Rounding Works with Offsets

Be aware of how the addition of both offsets and rounding to non-base room types can result in unexpected prices, especially if you use Percentage offsets. For example, the system's pricing decision for the Base Room Type is 97.33. Rounding the 1's place value to the nearest 9 brings this price to 99.00. A different room type has a 5% offset and, therefore, has a price of 102.20. The same rounding rule applied to this price brings it back down to 99.00.
In this case, you might not have expected that the two room types have the same price. In other cases, you might be surprised by an unexpectedly large gap between the room types.  For more details, viewFinal Price Calculation.

### Consider that Changes Trigger Decision Uploads

If you change the Rounding Rules,the RMSignores theMinimum Change Valueand sends any pricing decisions that changed as a result of the new pricing setup .  For example,  if decisions must now end in .99,the RMSupdates and sends any future decisions that changed as a result (it does not send decisions that already ended in .99).

## Scenarios

Review these examples to understand how rounding rules behave. The  place values that are not noted in these examples use the ALL selection.
