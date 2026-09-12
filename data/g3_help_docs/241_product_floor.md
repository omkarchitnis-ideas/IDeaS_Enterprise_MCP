# Product Floor

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Product-Floor.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Product-Floor.htm`
- **Ingestion Date:** `2026-09-11 22:14:49`

---

# Product Floor

Use this feature to control howG3 RMSapplies the selectedFloor Typeand value  to room types in your Linked products. If negative product Adjustments or negative Offsets for non-Base Room Types result in a conflict with the Product Floor, you can select howG3 RMSapplies the floor. Select one of the following options based on your preferred outcome:
- All Room Types in a Room Class(Default):Ensures that all room types in a Room Class stay above the defined floor. If negative product adjustments or negative Offsets conflict with the Product Floor,G3 RMSmight adjust non-Base Room Type prices and not apply the configured Offset. See thescenario.
All Room Types in a Room Class(Default):Ensures that all room types in a Room Class stay above the defined floor. If negative product adjustments or negative Offsets conflict with the Product Floor,G3 RMSmight adjust non-Base Room Type prices and not apply the configured Offset. See thescenario.
- Only the Base Room Type:G3 RMSapplies the floor only to the Base Room Type and always uses your defined Offsets for the non-Base Room Types. In case of conflicts, this option prioritizes the Offsets and might mean the prices for non-Base Room Types fall below the floor.
Only the Base Room Type:G3 RMSapplies the floor only to the Base Room Type and always uses your defined Offsets for the non-Base Room Types. In case of conflicts, this option prioritizes the Offsets and might mean the prices for non-Base Room Types fall below the floor.
This setting applies at the property level and affects all linked products (optimized, non-optimized, and group products). Before changing it, review the impact on  all  products for your property.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click Advanced Settings.
- ClickProduct Floor.
- Select one of the two options, then clickSave.
Select one of the two options, then clickSave.
- Verify the selected option on the Definition tab of the Linked Product, next toProduct Floor - Value.
Verify the selected option on the Definition tab of the Linked Product, next toProduct Floor - Value.

## Scenario

The Primary Priced Product has a Ceiling of 300 and a Floor of 100. The Standard Room Class contains:
- STD1 (Base Room Type)
STD1 (Base Room Type)
- STD2 with a fixed offset of +10
STD2 with a fixed offset of +10
The Linked Product is defined with:
- An adjustment of -25%
An adjustment of -25%
- A % Floor Type of -10% of the Base Product Floor (90)
A % Floor Type of -10% of the Base Product Floor (90)
For a specific date, the Base Room Type price is 100. Therefore, for the Primary Priced Product:
- STD1 = 100
STD1 = 100
- STD2 = 110
STD2 = 110
With either Product Floor option,G3 RMSprices STD1 for the Linked Product at 90. It uses the floor price of 90 instead of the -25% adjustment, which would result in a price of 75.
- With theAll Room Typesoption,G3 RMSapplies the floor to all room types. It prices both STD1 and STD2  at 90 and ignores the Offsets.
With theAll Room Typesoption,G3 RMSapplies the floor to all room types. It prices both STD1 and STD2  at 90 and ignores the Offsets.
- With theOnly the Base Room Typeoption, the system applies the floor only to the Base Room Type and keeps the Offset. STD1 is priced at 90 and STD2 at 99.
With theOnly the Base Room Typeoption, the system applies the floor only to the Base Room Type and keeps the Offset. STD1 is priced at 90 and STD2 at 99.
If the Offset for STD2 is -10 instead of +10, theOnly to Base Room Typeoption  prices STD2 at 81. BecauseG3 RMSpreserves the Offset for non-Base Room Types, the resulting price is  below the floor.
