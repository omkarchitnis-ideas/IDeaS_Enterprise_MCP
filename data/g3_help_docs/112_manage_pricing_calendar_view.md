# Manage Pricing - Calendar View

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Pricing-Calendar-View.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Pricing-Calendar-View.htm`
- **Ingestion Date:** `2026-09-11 22:13:23`

---

# Manage Pricing - Calendar View

Use the Calendar Viewto view and manage pricing by product or customize the data that displays, like adding Authorized Capacity or Competitors. If you want to quickly override multiple dates with different prices or view your pricing next to the publicly available prices of competitors, use theTabular View.

### What Help Do You Need With Pricing?

- I want toview the datathat is relevant to Pricing in Calendar View.
- I need toinvestigatethe factors that led to a price.
- Pricing overrides can have unintended consequences. I need to review thebest practicesbefore I override.
- I need to view  thestepsto override pricing.
- I want to apply the same override to a longer date range withMultiday Overrides.
- I want to test the impact of overrides before saving them by runningWhat If.
- I need to share my price strategy withG3 RMSinPricing Configuration.
- I want to understand howG3 RMSdetermines pricing.
- I want to understand howG3 RMSpricesLinked ProductsorGroup Products.

## Steps to Manage Pricing

- Clickand thenPricing.If you visit this page often, clicknext to the name to add it to the Quick Access menu.
Clickand thenPricing.If you visit this page often, clicknext to the name to add it to the Quick Access menu.
- Calendar View displays if it's set up as the default inPreferences. Otherwise click.
Calendar View displays if it's set up as the default inPreferences. Otherwise click.
G3 RMSdisplays the price for the Base Room Type of all Room Classes, next to relatedpricing data, like Occupancy Forecast, andiconsthat indicate relevant conditions. Use the following options to change the information displayed:
- If your property useslinked products,group products, orindependent products,  select to view more than one Product.
If your property useslinked products,group products, orindependent products,  select to view more than one Product.
- To change the period from the default 14 days, clickFromandToand select your desired dates.
To change the period from the default 14 days, clickFromandToand select your desired dates.
- If you set upInventory Groups,  select one to limit the displayed Room Classes.
- Select a specificRoom Classto view other Room Types.
- Click thefilterto change the view, for example, to display only dates with pricing changes.
Note: if no prices display for a linked product, it can be because the product has anadvance bookingrequirement. For example, with a 15-day advance booking minimum, no prices display for the 14 days that follow theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert., because the product can't be booked.
- Click the filterto change the information displayed in the Calendar View.
- Select up to fiveProductsthat you want to view.
- Limit the displayed dates  with any of the below selections:UnderDates With, select a certain condition. For example, dates with a price change or when the price is above or below a certain amount.Select aDay of Weekto view pricing data only for selected days.Select an override checkbox to show dates with activeOverrides. SeeIconsfor details about override types.Select one or moreRestrictions, for example, when LRV is greater than price. SeeIconsbelow for more information.
- UnderDates With, select a certain condition. For example, dates with a price change or when the price is above or below a certain amount.
- Select aDay of Weekto view pricing data only for selected days.
- Select an override checkbox to show dates with activeOverrides. SeeIconsfor details about override types.
- Select one or moreRestrictions, for example, when LRV is greater than price. SeeIconsbelow for more information.
- Select up to four pieces ofAdditional Information, for example On Books or pricing of the default competitor. SeeAdditional Informationfor details.
- SelectSave as defaultto display the selections each time you open the Calendar View for this property.
- ClickApplyto save the filters. ClickResetto return to the default view.
The following options  vary based on the Product you select:
- ClickCompetitorsto view theCompetitor Detailsand how your pricing compares to your market.
- ClickSummaryto view some of the factors that led to the system's price. The Summary window displays, where you can also click to view theOverride Historytab.
- For a deeper understanding of the price, clickto go to theInvestigator.
- For information about the underlying concepts, reviewHowG3 RMSDetermines Price.
- See howG3 RMSpricesLinked ProductsorGroup Products
If you have an Independent Product with a Blended Price, usethese stepsto override.
All pricing overrides can have unintended consequences. Be sure you are familiar with theBest Practices for Overriding Pricing.
Your browser does not support the video tag.
- If needed,change your dataselections, for example the dates or Room Class.With the default Room Class selectionAll, you can override theFinal Priceonly for theBase Room TypesThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.. To override non-Base Room Types, select a specific Room Class.
If needed,change your dataselections, for example the dates or Room Class.
With the default Room Class selectionAll, you can override theFinal Priceonly for theBase Room TypesThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.. To override non-Base Room Types, select a specific Room Class.
- If you uselinked productsorgroup products, and have many Room Classes that you want to apply the same adjustment to, selectLinked Products: Adjust All Room Classes.
If you uselinked productsorgroup products, and have many Room Classes that you want to apply the same adjustment to, selectLinked Products: Adjust All Room Classes.
- Click theFinal Pricevalue for the date, product, and room type that you want to override.The Override window opens. IfG3 RMSfinds a data condition that it considers  meaningful for its price, it points that out with a light bulb iconand a short explanation.
Click theFinal Pricevalue for the date, product, and room type that you want to override.The Override window opens. IfG3 RMSfinds a data condition that it considers  meaningful for its price, it points that out with a light bulb iconand a short explanation.
- Review theOverride Detailsdata to help you understand the product pricing.
Review theOverride Detailsdata to help you understand the product pricing.
- How you add an overridevaries based on the product type and the definedOverride Type:BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.)or Independently Priced Products: enter the value of the Final Price for the appropriate type of override.Include room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..If you override at the Base Room Typelevel,the RMSadds the overrides to all room types in the same Room Class, including any applicableOffsets.If you override a non-Base Room Type,the RMSdoesnotcheck the price against   other Room Classes, surrounding dates, or Offsets. Seeselecting the best override typefor details.Linked Optimized Productsor Group Products: enter new percentage values for the adjustment range. The left value equals the Floor and the right value the Ceiling of the adjustment range.User-Defined Linked Products: enter the adjustment value for the override. Based on the product'sDefinition, the value is for aFixedorPercentageadjustment.
How you add an overridevaries based on the product type and the definedOverride Type:
- BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.)or Independently Priced Products: enter the value of the Final Price for the appropriate type of override.Include room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..If you override at the Base Room Typelevel,the RMSadds the overrides to all room types in the same Room Class, including any applicableOffsets.If you override a non-Base Room Type,the RMSdoesnotcheck the price against   other Room Classes, surrounding dates, or Offsets. Seeselecting the best override typefor details.
BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.)or Independently Priced Products: enter the value of the Final Price for the appropriate type of override.Include room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..
- If you override at the Base Room Typelevel,the RMSadds the overrides to all room types in the same Room Class, including any applicableOffsets.
If you override at the Base Room Typelevel,the RMSadds the overrides to all room types in the same Room Class, including any applicableOffsets.
- If you override a non-Base Room Type,the RMSdoesnotcheck the price against   other Room Classes, surrounding dates, or Offsets. Seeselecting the best override typefor details.
If you override a non-Base Room Type,the RMSdoesnotcheck the price against   other Room Classes, surrounding dates, or Offsets. Seeselecting the best override typefor details.
- Linked Optimized Productsor Group Products: enter new percentage values for the adjustment range. The left value equals the Floor and the right value the Ceiling of the adjustment range.
Linked Optimized Productsor Group Products: enter new percentage values for the adjustment range. The left value equals the Floor and the right value the Ceiling of the adjustment range.
- User-Defined Linked Products: enter the adjustment value for the override. Based on the product'sDefinition, the value is for aFixedorPercentageadjustment.
User-Defined Linked Products: enter the adjustment value for the override. Based on the product'sDefinition, the value is for aFixedorPercentageadjustment.
- Click the notes iconand enter an explanation for the override. That helps you decide later if you still need overrides. A saved note displays with a check mark.
- ClickApplyto continue. The Unsaved Changes icondisplays. To revert the change, click the icon.
ClickApplyto continue. The Unsaved Changes icondisplays. To revert the change, click the icon.
- If available, clickWhat 
	 Ifto see the results of your override before saving. For more information, seeWhat If.
If available, clickWhat 
	 Ifto see the results of your override before saving. For more information, seeWhat If.
- ClickSaveto save your changes. The Unsaved Changes icon is removed, and the override icon displays.
ClickSaveto save your changes. The Unsaved Changes icon is removed, and the override icon displays.
- Before you can send new pricing overrides to yourselling system, click the flagand then clickSync Allto start aSync. If available, clickSync All and UploadorUploadto send the new values to yourselling system.
Before you can send new pricing overrides to yourselling system, click the flagand then clickSync Allto start aSync. If available, clickSync All and UploadorUploadto send the new values to yourselling system.
- If needed,change your dataselections, for example the dates or Room Class.
- Click theFinal Pricevalue of the date, product, and room type for which you want to remove the override.The Override window opens. IfG3 RMSfinds a data condition that it considers  meaningful for its price, it points that out with a light bulb iconand a short explanation.
- Review theOverride Detailsdata to help you understand the product pricing.
- Click delete.
- ClickApplyto continue. The Unsaved Changes icondisplays. To revert the change, click the icon.
- ClickWhat 
	 Ifto see the results of your override before saving. For more information, seeWhat If.
- ClickSaveto save your changes. The Unsaved Changes icon is removed.The price is unchanged,G3 RMSreviews the price in the next processing.
G3 RMSdisplays the price for the Base Room Type of all Room Classes, next to relatedpricing data, like Occupancy Forecast, andiconsthat indicate relevant conditions.
- Select the product to view. You can only view products with matching seasons.
Select the product to view. You can only view products with matching seasons.
- Select a specificRoom Classto view other Room Types.
Select a specificRoom Classto view other Room Types.
To add an override for an individual date, useTabular View.
With the default Room Class selectionAll, you can override the Final Price only for theBase Room TypesThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.. Select a specific Room Class to override non-Base Room types.
- Click theFinal Pricevalue for the date range and room type that you want to override.
Click theFinal Pricevalue for the date range and room type that you want to override.
- Enter the override value for the Final Price. The Unsaved Changes icondisplays. To revert the change, click the icon.At the Base Room Typelevel, the override applies to all room types in the Room Class. IfOffsetsexist for other room types,G3 RMSadds them to the override.
Enter the override value for the Final Price. The Unsaved Changes icondisplays. To revert the change, click the icon.
At the Base Room Typelevel, the override applies to all room types in the Room Class. IfOffsetsexist for other room types,G3 RMSadds them to the override.
- ClickSaveto save your changes. The Unsaved Changes icon is removed, and the override icon displays.
ClickSaveto save your changes. The Unsaved Changes icon is removed, and the override icon displays.
- Before you can send new pricing overrides to yourselling system, click the flagand then clickSync Allto start aSync. If available, clickSync All and Uploadto send the new values to yourselling system.
Before you can send new pricing overrides to yourselling system, click the flagand then clickSync Allto start aSync. If available, clickSync All and Uploadto send the new values to yourselling system.
- If needed, change your data selections, for example the Product or Room Class.
If needed, change your data selections, for example the Product or Room Class.
- Click delete.G3 RMSremoves all overrides for the select date range, product, and room type.
- ClickApplyto continue. The Unsaved Changes icondisplays. To revert the change, click the icon.
- ClickSaveto save your changes. The Unsaved Changes icon is removed.The price is unchanged,G3 RMSreviews the price in the next processing.

## Data Details

The following data display on the Pricing page by default.

#### Additional Information

Click the filterto display the followingAdditional Information:

#### Primary Priced ProductDetails

#### Linked, Group, and Independent Product  Details
