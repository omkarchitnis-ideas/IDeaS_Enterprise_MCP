# Rate Protect

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Market-Segments/Market-Segment-Rate-Protect.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Market-Segments/Market-Segment-Rate-Protect.htm`
- **Ingestion Date:** `2026-09-11 22:12:30`

---

# Rate Protect

Use the Rate Protect tab to define rate codes that vary between fixed price and a discount off BAR, (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.). A fixed price when the price of BAR is above that fixed price. And a discount off BAR when BAR is below the fixed price. For example, CORP1 is a negotiated corporate rate with a fixed price of 200. But when your BAR is equal to or lower than 200, CORP1 is priced at 10% off BAR. When BAR is above 200, CORP1 behaves like business that isattributed as non-Linked; below 200 like Linked to Base Product - BAR.
G3 RMSneeds to know about such rate codes because it considers all demand that is Linked to Base Product - BAR when it determines pricing (seeprice calculationfor details). And if your property has high-volume accounts with such pricing,G3 RMSmight sometimes not lower the BAR price below the fixed value. Using the CORP1 example, when BAR is at or below 200, CORP1 drops from the fixed value of 200 to 180 (200 - 10%, or 20, = 180). So if you have 100 CORP1 reservations each night, then you have 20,000 revenue from that account when BAR is 201 or above. Below a BAR of 201,G3 RMSneeds to consider that the CORP1 revenue drops to 18,000 or lower. So the system only drops BAR below 201 if the gains from other segments outweigh the loss in CORP1 revenue.
Therefore, afterassigning the attributes, define the exact pricing of the rate code in the Rate Protect tab.
Note: if BAR goes below the fixed price (201 in this example), you seeon thePricingpage.

## Setup Steps

You can set up Rate Protect after you assign   attributes in the Market Segments tab. The Rate Protect setup doesn't impact the next two steps: loading of data and Create and Commit Forecast Groups.
If you make changes to your Rate Protect setup, you don't need to Create and Commit Forecast Groups again.
- Click, thenForecasts, and thenMarket Segments.
- Click theRate Protecttab.
- Existing Rate Protect products display. Select an action:Click  to adda new product.Click   to changean existing product.Click tocopy a product. You must assign rate codes to the copied product on theDefinitiontab, because each rate code can be associated only with one product. Defaults, Seasons, and other details on the Definitions tab are copied.Click todelete a product.Rate Protect setup consists of three steps:Definitionof the product (name, rounding, etc.),Defaultpricing, and, if needed, different pricing forSeasons.
- Click  to adda new product.
- Click   to changean existing product.
- Click tocopy a product. You must assign rate codes to the copied product on theDefinitiontab, because each rate code can be associated only with one product. Defaults, Seasons, and other details on the Definitions tab are copied.
- Click todelete a product.
- Enter theProduct Name. This can be the same as the rate code name or, if you create one product for multiple rate codes with the same pricing, a different name.
- Enter an optionalDescriptionto provide more information about the product.
- Select theBase Productthat the rate code is priced off when it's not fixed.In most cases that's the BAR price.
- If needed, select the optionalSeasonal Product Onlycheckbox, for example, for a winter promotion. When you select this option, theDefaultstab is not available for the product. Seasonal products use the default pricing of their parent product.
- If the contract for the rate code includes aRounding Rule, select it here. Otherwise, selectNone.
- Enter aFloor, either as a fixed  value or as a percentage adjustment to the floor of yourPrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.. If the price that is adjusted offthe Base Productis below the Floor value,G3 RMSreplaces that price with the Floor value.The Floor value isnotrounded. Therefore, ensure that a fixed Floor value reflects your rounding rules.If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter the fixed value inclusive of tax.
- The Floor value isnotrounded. Therefore, ensure that a fixed Floor value reflects your rounding rules.
- If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter the fixed value inclusive of tax.
- Select theRate Codes.Select one or more rate codes and click>to add them to the product. Click>>to add all rate codes to the product.You can link each rate code to only one product. Rate codes that you already associated with another product don't display.If you use linked products and select a rate code in theDefinitiontab, you can't select the same rate code in Rate Protect.
- Select one or more rate codes and click>to add them to the product. Click>>to add all rate codes to the product.
- You can link each rate code to only one product. Rate codes that you already associated with another product don't display.
- If you use linked products and select a rate code in theDefinitiontab, you can't select the same rate code in Rate Protect.
- Select theRoom Typesthat you sell for this product. Select one or more room types and click>to add them to the product. Click>>to add all room types to the product.
- ClickNextto set up the Default pricing.
In Defaults you define the fixed Price and the adjustment off the Base Product.
- Select theDay of Weekcheckbox if the product's  adjustment varies by the arrival day of week. For example, guests are offered a different discount if they arrive on weekdays rather than weekends. If you select Day of Week adjustments, you are not required to set up a value for all days of the week, but you must set up at least one.
- Select theRoom Classcheckbox if you want to vary the adjustment by Room Class. The displayed Room Classes depend on the Room Types that you selected for the product on the Definition tab. Set up  values for every Room Class.
- Enter the fixedPrice.G3 RMSassumes the product is priced at this value unless the Base Product price is equal or lower than the value. If needed, complete by Day of Week and Room Class.
- Enter theAdjustment (%)that the product is priced off the Base Product's price. Must be a negative number between 100 and zero.
- ClickNextto set up any required Seasons. The Defaults save automatically.
Use Seasons for two purposes:
- To set up the pricing for products that are only available for specific periods in the year. For these products, you selectedSeasonal Product Onlyon theDefinitiontab, and you must have at least one season set up. For example, you offer a promotion only during the winter months.
- To define dates when the pricing for a year-round product differs from its pricing on theDefaultstab. For example, you price a corporate rate 10% lower over the winter months.
Seasonal products apply to arrival, not booking date. For example, you can't use them for a campaign for the summer with a promotional rate code that can only be booked from May 1 to May 15.
- Click to adda new season. Or click editto change an existing season.
- Enter aSeason Name.
- Select theStart Dateand theEnd Dateof the season.
- If needed, select theDay of Weekcheckbox.
- If needed, select theRoom Classcheckbox.
- Enter the fixedPricefor this season.
- Enter theAdjustment (%)that the product is priced off the Base Product's price. The value must be a negative number between 100 and zero.
- Click to savethe changes.
- ClickDoneto return to the start page.
- Your new product displays. Check theActivebox andG3 RMSoptimizes based on the product's Rate Protect setup.
