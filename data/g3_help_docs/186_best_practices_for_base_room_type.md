# Best Practices   for Base Room Type

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/BP-Base-Room-Type.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/BP-Base-Room-Type.htm`
- **Ingestion Date:** `2026-09-11 22:14:13`

---

# Best Practices   for Base Room Type

## Select the Largest Capacity Room Type

Ifthe RMSassigns the Base Room Types, it selects the Base Room Type that has the highest number of past bookings with theEqual to BAR Product attribute. Follow a similar best practice if you assign the Base Room Types yourself and select the room type with the largest capacity. This room type usually has the most reservations and the most data to use as a basis for the Room Class decisions.
The Base Room Type iconidentifies these room types throughoutthe RMS.

## Decide if Your Property Needs Minimum Change Values

Set a Minimum Change Value if a large number of pricing changes have a negative impact on your selling systems. For example, by causing slower performance or increased costs.  Or, use the functionality to avoid negative guest perception in a high priced market. For example, without a Minimum Change Value, a pricing decision could change four times by $1, from $495 to $499, in as many optimizations. With a $5 Minimum Change Value,the RMSwould not send a new pricing decision, because the amount of change, $1, is below the threshold.
Note the impact ofRounding Rules. In the above $499 example, and with rounding rules that enforce prices ending in $5 or $9, no Minimum Change Value is needed. That is because all prices between $495 to $499 would be rounded up or down. The price would only change once, from $495 to $499.
If you are not concerned about selling systems or guest perception, select a small or no Minimum Change Value. This way,the RMScan optimize revenues without constraints.

## Include Taxes in Minimum Change Value

If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., enter the Minimum Change Value inclusive of tax. This applies to all pricing setup  values. ViewEntering and Display of Taxes inthe RMSfor more information. For example, if you require a Minimum Change Value of 10 inclusive of tax, enter 10. If your tax is 20%, then the Minimum Change value of 10 includes a tax of 2.

## Understand Howthe RMSResolves Conflicts with Minimum Change Values

### Price Ranking Hierarchy Beats Minimum Change Setup

If a Minimum Change Value leads to prices that break theprice ranking hierarchy,the RMSignores the Minimum Change setup. See the RC4 row in the table for an example.

### Minimum Change Setup Beats Minimum Price Differentials

The RMSignores the Minimum Price Differential if a Minimum Change Value prevents the suggested price. See the RC2 row in the following example.

### Pricing Setup Changes Beat Minimum Change Setup

If you change the setup inRounding Rules,OffsetsorSupplements,the RMSupdates and sends any pricing decisions that changed as a result of the new pricing setup . For example,  if decisions must now end in .99 due to a new Rounding Rule,the RMSupdates and sends any future decisions that changed as a result, but does not send decisions that already ended in .99. After changes to pricing setup,the RMSignores the Minimum Change Value until the next nightly processing completes.

## Redo the Base Room Type Setup if Room Classes
           Change

If you make changes to yourRoom Class setup(for example, moving a room type from one Room Class to another),you are prompted to set up your Base Room Types.

## Redo the Pricing and Offsets Setup if the Base Room Type Changes

If you change the Base Room Type for a Room Class,the RMSremoves the Ceiling and Floor values, Offsets, and future overrides for its Room Class. You must then again set up these values for the Room Class.
