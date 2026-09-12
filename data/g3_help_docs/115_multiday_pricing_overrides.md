# Multiday Pricing Overrides

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Pricing-Override-Multiday-CP.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Pricing-Override-Multiday-CP.htm`
- **Ingestion Date:** `2026-09-11 22:13:25`

---

# Multiday Pricing Overrides

Use multiday overrides to change the pricing for more than one day at a time.
Use multiday overrides carefully. The impact of multiday pricing overrides is much larger than an override for a single day.

### What Help Do You Need With Multiday Pricing Overrides?

- I need to view thestepsto override pricing for a longer date range.
I need to view thestepsto override pricing for a longer date range.
- Overriding pricing can have unintended consequences. I need to review thebest practicesbefore I override.
Overriding pricing can have unintended consequences. I need to review thebest practicesbefore I override.
- Multiday overrides have a large impact so I want to test their impact before saving them by running aWhat If.
Multiday overrides have a large impact so I want to test their impact before saving them by running aWhat If.
- Instead of a longer Multiday Override, I want to add a season inCeiling/Floor.
Instead of a longer Multiday Override, I want to add a season inCeiling/Floor.

## Override Steps

- Clickand thenPricing.Based on yourPreferences, Calendar or Tabular View displays the pricing decisions.
- If needed, change the displayed data, for example, the Room Class, date range, or Product for which you want to add or remove overrides.Learn how to change pricing data inCalendarorTabularview.
- If you uselinked productsorgroup products, and have many Room Classes that you want to apply the same adjustment to, selectLinked Products: Adjust All Room Classes.
- ClickMultiday Overrides.The Multiday Overrides window displays.
- Update theStart Date,End Date,Product, andRoom Classthat the override applies to. Note that your options are limited to the selections on the Pricing page.
- Select theDay of Weekcheckboxes if you want to add or remove overrides only for certain days of the week.  If you do not select any days, the override applies to all days.
- If you selected only one Room Class, you can select theRoom Typeto which the overrides will apply. Note that only for the Base Room Typeyou can:Add or remove Ceiling and Floor overrides. For other room types,G3 RMScalculates the pricing decision usingOffsetsfrom the Base Room Type.Add or remove a Specific override for all room types within a Room Class at once.
- Add or remove Ceiling and Floor overrides. For other room types,G3 RMScalculates the pricing decision usingOffsetsfrom the Base Room Type.
- Add or remove a Specific override for all room types within a Room Class at once.
- How toAdd Overridevaries on the type of product:BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) or Independently Priced Products: enter the value of the Final Price for the appropriate type of override., including room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..If you view all Room Classes, an override applies to the  Base Room Type. IfOffsetsexist for other room types,G3 RMSadds them to the override. If you want to apply an override to a non-Base Room Type, you must first select the Room Class in step 2 then you can enter the Specific pricing override in the Multiday Override screen.When you add a Specific override,G3 RMSapplies and displays it as a   Floor and Ceilingoverride, same  as if you apply it in the Tabular View. For example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.Linked Optimized Productsor Group Products: enter a new percentage value for the adjustment. To add a specific adjustment, enter the same value inFloorandCeiling.User-Defined Products: enter the adjustment value for the override. Based on the product'sDefinition, the value is for aFixedorPercentageadjustment.Note: if a product can be overridden depends on the definedOverride Type.
- BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) or Independently Priced Products: enter the value of the Final Price for the appropriate type of override., including room tax if you usetax-inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration..If you view all Room Classes, an override applies to the  Base Room Type. IfOffsetsexist for other room types,G3 RMSadds them to the override. If you want to apply an override to a non-Base Room Type, you must first select the Room Class in step 2 then you can enter the Specific pricing override in the Multiday Override screen.When you add a Specific override,G3 RMSapplies and displays it as a   Floor and Ceilingoverride, same  as if you apply it in the Tabular View. For example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.
- If you view all Room Classes, an override applies to the  Base Room Type. IfOffsetsexist for other room types,G3 RMSadds them to the override. If you want to apply an override to a non-Base Room Type, you must first select the Room Class in step 2 then you can enter the Specific pricing override in the Multiday Override screen.
- When you add a Specific override,G3 RMSapplies and displays it as a   Floor and Ceilingoverride, same  as if you apply it in the Tabular View. For example, if you override the price  to 100,the RMSapplies that as a Ceiling override of 100 and a Floor override of 100.
- Linked Optimized Productsor Group Products: enter a new percentage value for the adjustment. To add a specific adjustment, enter the same value inFloorandCeiling.
- User-Defined Products: enter the adjustment value for the override. Based on the product'sDefinition, the value is for aFixedorPercentageadjustment.
Note: if a product can be overridden depends on the definedOverride Type.
- Clickto add a note explaining the override. That helps you monitor overrides, to decide if you keep or remove them. After you save a note, the notes icon displays with a check markfor all days of the override.
- ClickApply. This  iconmeans that you have unsaved changes. To revert the change, click the icon.
- ClickWhat Ifto see the results of your changes before saving. For more information, seeWhat If.
- ClickSave. The unsaved changes icons are removed and the override icons display.
- To send new pricing overrides to theselling systemimmediately, clickUpload.Note: The same applies to linked and group products when you override theBase ProductThe rate code that is the starting point for the price of linked products. The linked products are child products of the Base Product. The RMS calculates the price for the Base Product, then determines the price for its children by adjusting the Base Product price.. To see the new Final Price for linked and group products immediately, click the flagand start a Sync.
The Multiday Overrides window displays your selections. SeeAccessing Multiday Overridesto learn how to change your display.
- In theRemove Overridecolumn, select the checkbox for the appropriate override type.
- ClickApply. The unsaved changes iconindicates the dates where you want to remove overrides.
- ClickWhat Ifto test the impact of removing the override. SeeWhat Iffor details.
- ClickSaveto finalize the override removal. The icons are removed.The price is unchanged,G3 RMSreviews the price in the next processing.
