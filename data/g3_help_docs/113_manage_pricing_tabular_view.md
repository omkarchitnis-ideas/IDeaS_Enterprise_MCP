# Manage Pricing - Tabular View

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Pricing-Tabular-View.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Pricing-Tabular-View.htm`
- **Ingestion Date:** `2026-09-11 22:13:24`

---

When Should I Use Pricing Overrides?
Understand the Process to Decide if a Pricing Override is Best

# Manage Pricing - Tabular View

Use the Tabular Viewto view your pricing next to the publicly available prices of multiple competitors or quickly override multiple dates with different prices. If you want to view pricing by product or customize the displayed data (like LRV, Forecast, or Capacity), useCalendar View.

### What Help Do You Need With Pricing?

- I want to view therelevant datato Pricing in Tabular View.
- I need toinvestigatethe factors that led to a pricing decision.
- I need to review thebest practicesfor the unintended consequences of  overrides.
- I need to view thestepsto override pricing.
- I want to apply the same override to a longer date range withMultiday Overrides.
- I want to test the impact of overrides before saving them by runningWhat If.
- I need to share my price strategy withG3 RMSinPricing Configuration.
- I want to understand howG3 RMSdetermines pricing.
- I want to understand howG3 RMSpricesLinked ProductsorGroup Products.

## Steps to Manage Pricing

- Clickand thenPricing.
Clickand thenPricing.
- Tabular View displays if it's set up as the default inPreferences. Otherwise click.
Tabular View displays if it's set up as the default inPreferences. Otherwise click.
- If your property useslinked products,group products, orindependent products, select to view more than one Product.
If your property useslinked products,group products, orindependent products, select to view more than one Product.
- To change the period from the default 14 days, clickFromandToand select your desired dates.
To change the period from the default 14 days, clickFromandToand select your desired dates.
- If you set upInventory Groups,  select one to limit the displayed Room Classes.
- Select a specificRoom Classto view other Room Types.
- Click thefilterto change the view, for example, to display only dates with pricing changes.
Note: if no prices display for a linked product, it can be because the product has aadvance bookingrequirement. For example, with a 15-day advance booking minimum, no prices display for the 14 days that follow theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert., because the product can't be booked.
- Click the filterto change the information displayed in the Tabular View.
- Select up to fiveProductsthat you want to view.
- Select if you want to display linked products byPriceorAdjustment.
- Select specificCompetitorsto display next to your prices.
- Limit the dates thatG3 RMSdisplays with any of the below selections:UnderDates With, select a condition, for example, dates with a price change.Select aDay of Weekto view pricing data only for selected days.Select an override checkbox to show dates with activeOverrides. SeeIconsfor details about override types.Select one or moreRestrictions, for example, when LRV is greater than price. SeeIconsfor more information.
- UnderDates With, select a condition, for example, dates with a price change.
- Select aDay of Weekto view pricing data only for selected days.
- Select an override checkbox to show dates with activeOverrides. SeeIconsfor details about override types.
- Select one or moreRestrictions, for example, when LRV is greater than price. SeeIconsfor more information.
- Select whatAdditional Informationyou want to see, for example, On Books or pricing of the default competitor. SeeAdditional Informationfor details.
- SelectSave as defaultto display this selection each time you open the Tabular View for this property.
- ClickApplyto save the filters. ClickResetto return to the default view.
The following options  vary based on the Product you select:
- ClickSummaryto view some of the factors that led to the system's pricing decision. The Summary window opens, where you can also click to view theOverride Historytab.
- For a deeper understanding of the price, clickfrom the Summary window to go to theInvestigator.
- For information about the underlying concepts, reviewHowG3 RMSDetermines Price.
- See howG3 RMSpricesLinked ProductsorGroup Products
All pricing overrides can have unintended consequences. Be sure you are familiar with theBest Practices for Overriding Pricing.
- If needed,change your dataselections, for example the dates or Room Class.With the default Room Class selectionAll, you can override the Final Price only for theBase Room TypesThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.. Select a specific Room Class to override non-Base Room types.
If needed,change your dataselections, for example the dates or Room Class.
With the default Room Class selectionAll, you can override the Final Price only for theBase Room TypesThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.. Select a specific Room Class to override non-Base Room types.
- If you uselinked productsorgroup products, and  you want to apply the same adjustment to all Room Classes, selectLinked Products: Adjust All Room Classes.
If you uselinked productsorgroup products, and  you want to apply the same adjustment to all Room Classes, selectLinked Products: Adjust All Room Classes.
- In the table, click the cell for the date, product, and room type that you want to override.
In the table, click the cell for the date, product, and room type that you want to override.
- Enter the value of the override:For BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.)or Independently Priced Products:  the value of the Final Price.Include room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..For user defined linked products:  the adjustment value off its Base Product.For linked optimized productsor group products: the percentage values for the adjustment range. The left value equals the Floor and the right value the Ceiling of the adjustment range. This overrides the adjustment values that are set up in the product'sDefaultsorSeasons.
Enter the value of the override:
- For BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.)or Independently Priced Products:  the value of the Final Price.Include room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..
For BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.)or Independently Priced Products:  the value of the Final Price.Include room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..
- For user defined linked products:  the adjustment value off its Base Product.
For user defined linked products:  the adjustment value off its Base Product.
- For linked optimized productsor group products: the percentage values for the adjustment range. The left value equals the Floor and the right value the Ceiling of the adjustment range. This overrides the adjustment values that are set up in the product'sDefaultsorSeasons.
For linked optimized productsor group products: the percentage values for the adjustment range. The left value equals the Floor and the right value the Ceiling of the adjustment range. This overrides the adjustment values that are set up in the product'sDefaultsorSeasons.
- Press the Tab key to navigate to other room types and to the next day. Unsaved changes are highlighted in yellow.
Press the Tab key to navigate to other room types and to the next day. Unsaved changes are highlighted in yellow.
- Click theicon to revert a change. ClickCancelto revert all changes.
Click theicon to revert a change. ClickCancelto revert all changes.
- ClickWhat 
	 Ifto see the results of your override before saving. For more information, seeWhat If.
ClickWhat 
	 Ifto see the results of your override before saving. For more information, seeWhat If.
- ClickSave.The dates with overrides are highlighted in pinkand display the Floorand Ceilingoverride icons. For example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.
ClickSave.The dates with overrides are highlighted in pinkand display the Floorand Ceilingoverride icons. For example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.
- Before you can send new pricing overrides to yourselling system, click the flagand then clickSync Allto start aSync. If available, clickSync All and UploadorUploadto send the new values to yourselling system.
Before you can send new pricing overrides to yourselling system, click the flagand then clickSync Allto start aSync. If available, clickSync All and UploadorUploadto send the new values to yourselling system.
- If needed,change your dataselections, for example the dates or Room Class.
If needed,change your dataselections, for example the dates or Room Class.
- In the table, click deletefor the date, product, and room type for which you want to remove the override.
- Click theicon to revert a change. ClickCancelto revert all changes.
- ClickWhat 
	 Ifto see the results of your override before saving. For more information, seeWhat If.
- ClickSave. The Unsaved Changes icon is removed.The price is unchanged,G3 RMSreviews the price in the next processing.

## Data Details

The following data display on the Pricing page, by default.

#### Additional Information

Click the filterto display the followingAdditional Information:
