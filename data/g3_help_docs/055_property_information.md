# Property Information

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Property/Property-Information.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Property/Property-Information.htm`
- **Ingestion Date:** `2026-09-11 22:12:44`

---

# Property Information

## Property Name

Use the Property Information tab to change the property 
 name that displays inG3 RMSwherever the full property title is used. The name should reflect the legal name of the property, because IDeaS also uses this name in support and billing documents.

### Editing the Property Name

- Click, thenProperty, and thenProperty Specific.
- Enter a newProperty Name.
- ClickSave.

### Capacity Used to Calculate Occupancy %, ADR, and RevPAR

Displays ifG3 RMSusesPhysicalThe total number of guest rooms at a property, including out of order rooms.orEffective CapacityThe property's physical capacity minus the out of order rooms.when it calculates occupancy-based metrics like Occupancy on books %, ADR, or RevPAR. If your property is part of a larger company, the value defaults to the value selected by your company.  If you are the authorized person for the company, contact IDeaS to change the setting.

### Exclude Market Segments

In some reports (Data Extract, Booking Pace) and dashboards (At a Glance, Business Analysis) you can exclude the data from bookings with specific market segments, for example, those with zero room revenue. Use the arrow>to tellG3 RMSwhich market segments to exclude.

## Room Revenue Tax

If you are in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration., use the Property Information tab to add the room tax percentage during the initial setup of your property.G3 RMSdeducts the tax percentage from your tax-inclusive pricing values so that it can use net values for optimization.
Should your room tax percentage change, use this tab to change the tax value. When you change the room tax percentage, the changes take effect for all future pricing decisions after the next processing. A change to the tax value does not impact historical data.
If your property uses the OXI integration, contact your IDeaS representative. IDeaS Teams need to apply tax changes for OXI properties.

### Entering and Display of Tax inG3 RMS

#### How to enter taxes

With tax-inclusive pricing, you enter most setup and override values including tax:

#### HowG3 RMSdisplays taxes

With tax-inclusive pricing,  the system displays some values inclusive and others exclusive of tax, depending on the purpose of the value:

### Enabling Room Revenue Tax

- Click, thenProperty, and thenProperty Specific.
- If you selected tax-inclusive pricing for property creation,Yesis selected for the Default Room Revenue Tax setting. Your room tax value displays as a percentage.
- Edit the percentage value as needed.
- ClickSave.

### Seasonal Tax

In rare cases, countries change the room tax for a limited time, for example to stimulate travel during a demand disruption. If that applies to your property, you can use the seasonal tax functionality. See ourDemand Disruption topicon how to manage a temporary tax change inG3 RMS.
- UnderSeasons, type a name for the season.
- Select theStartandEnd Datefor the season. The dates refer to the arrival dates when the different tax applies.
- Enter the roomTaxpercentage.
- Click add.
- ClickSave.
- If needed, make changes, for example to extend the end date.
