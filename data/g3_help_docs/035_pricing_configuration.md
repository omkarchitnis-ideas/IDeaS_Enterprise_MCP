# Pricing Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Pricing-Configuration-Overview.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Pricing-Configuration-Overview.htm`
- **Ingestion Date:** `2026-09-11 22:12:31`

---

# Pricing Configuration

Use Pricing Configuration to share your price strategy withG3 RMSand to ensure the system picks an appropriate price. For example, define the price range from whichG3 RMSchooses the price for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..
Based on your  subscription, you also define the pricing strategy for other products, likelinked,group, orindependent products.

### What Help Do You Need with Setting Up Pricing?

- I want anoverview of the steps to set up pricingand how to share my pricing strategy withG3 RMS.
- I want to understandhowG3 RMSuses my pricing setup when it calculates the Final Price.
- I need to complete or review pricing setup:
- I need todefine the Base Room Typesfor whichG3 RMSoptimizes pricing for each Room Class.
- I have a Room Class with a fixed price. I need toensure thatG3 RMSdoesn't price that Room Class.
- I need to ensure that the system follows our rules about how pricing values end. SeeRounding Rules.
- I need to define the price range from which the system picks the price ofthe primary priced product. SeeCeiling/Floor.
- I need to define howG3 RMSprices non-base room types and other occupancy types, like extra adult. SeeOffsets.
- I need toset upproducts that are linked tothe primary priced product(or to other products). Seelinked products.
- I need toset upproducts that automate pricing for groups that don't require profit and displacement evaluations. Seegroup products.
- I need toset upproducts that are priced independently from the primary priced product. Seeindependent products.
- I'm in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration.and enter all pricing values  inclusive of tax. Give me an overview ofentering and display of tax.
- Our pricing includes non-room supplements, like breakfast. I need to define thesesupplements.
- I want to understand why a lower ranked room type is priced higher
than a higher ranked room type. SeePrice Ranking.

### How to Share Your Pricing Strategy withG3 RMS

View this video or review the description of the process below.
Your browser does not support the video tag.

#### 1)Follow this process to share your pricing strategy

Note that the order in the setup process differs from the order in whichG3 RMScalculates the Final Price.
The key step that defines your pricing strategy is setting the Ceiling and Floor values. These values  define the price range thatG3 RMSuses to choose the Optimal Price. But the Optimal Price is a ârawâ price, not ready for guests, so use other setup, like rounding rules, to produce the Final Price that your guests see.
AfterG3 RMSproduces decisions, you can check your pricing strategy. Review the Highest and Lowest prices on the Summary tab of theBusiness Analysis Dashboard. Or, export to Excelto review pricing and Offsets on a spreadsheet. This is useful if you have many Room Classes and seasons.

#### 2) If needed, share your pricing strategy for linked, group, and independent products

With a subscription,G3 RMScan manage the pricing oflinked products, like Advance Purchase,group products, like third party group bookings, andindependent products, likelong-stay pricing.

## Setup Steps

- Click, thenDecisions, and thenPricing.
- Click Advanced Settingsto review or set upBase Room TypesandRounding Rules.
- Clickto review or set up theCeiling/Floor,Offsetsand, if needed,Supplementsof the Primary Priced product.
- Clickto addLinked Products,Group Products, orIndependent Products.
- If needed, define the Advanced Settings. For example,Package Elementsfor linked products or aBlended Pricefor independent products.
- For independent products, clickto set up theCeiling/Floor,Offsetsand, if needed,Supplements.
- Click to edit, copy, or deleteproducts.For more details, review all the setup steps forlinked productsorgroup products.If a product is centrally managed by your company, you can only viewit.
- If needed, use the arrowsto change the display order of your products.

## Data Details

The details vary based onyour subscription, for example, if you have linked products.

## Final Price Calculations

View the work flows below to understand howG3 RMSuses your pricing setup to calculate the Final Price based on the Optimal Price.
Note:
- The Optimal Price also considers anyMinimum Price Differentialthat you set up as part of your Rooms setup. To learn about Optimal Price calculation, reviewHowG3 RMSDetermines Pricing.
- For properties withSupplements,G3 RMSremoves the supplement value from Ceiling/Floor values before it calculates Optimal Price.

#### Base Room Type (Single Occupancy)

#### Double Occupancy

#### Room Type 2, same Room Class (Single Occupancy)

#### Double Occupancy

#### Extra Adult

#### Base Room Type (2 Adult Occupancy)

#### 1 Adult Occupancy

#### 3 Adult Occupancy

#### Room Type 2, same Room Class (2 Adult Occupancy)

#### 1 Adult Occupancy

#### Extra Adult
