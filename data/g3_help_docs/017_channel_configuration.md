# Channel Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Channel-Costs/Channel-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Channel-Costs/Channel-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:12:18`

---

# Channel Configuration

Use the Export and Import buttons on Channel Configuration  to informG3 RMSabout your acquisition costs. For example, you might pay a fixed fee of 5 for all bookings from your CRS. And for a reservation from an Online Travel Agency (OTA), like Booking.com, you pay an additional fee of 20% of the value of the reservation.

### What Are the Benefits of Setting up Channel Costs?

Channel Costs don't impact the forecast and decisions (unless you useProfit Optimization). But they display in theChannel ForecastandBusiness Insightsdashboards. Those dashboards help you understand the costs and, therefore, better manage channels. For example, use the dashboards to:
- Understand how channel costs impact Net Revenue, Net ADR, and NetRevPARRevenue Per Available Room. The total room revenue divided by the total number of rooms (capacity).
See the Property Information topic for the capacity definition.of every reservation and compare that to last year.
- Perform a true, cost-adjusted revenue comparison between channels, like a commissionable versus a merchant-model OTA.
- View a forecast of business by channel and the expected channel costs.
Use an Excel template to import your initial values or to export existing setup. You also use the export option to review and change your costs. Review thebest practices for defining channel costs.

## Setting Up Channel Configuration

### Export/Import Channel Costs

- Click, thenExternal Data, and thenChannel.
- Click theExport/Importtab.
- Select the template type:To set up Channel Costs for the first time, selectBlank.To update existing costs, selectCurrent Settings.Note: Importing the worksheet deletes existing costs without keeping a record of the old values. Always review your new costs before you import.
- To set up Channel Costs for the first time, selectBlank.
- To update existing costs, selectCurrent Settings.Note: Importing the worksheet deletes existing costs without keeping a record of the old values. Always review your new costs before you import.
- ClickExport.
- Add costs or change existing values as needed.Click an empty field (Channel, Source, etc.) and select from the options thatG3 RMSfound in your reservations data. Don't enter new values.When you enter the cost for Monday, it copies to all days. If needed, edit by day of week.Enter the cost in the same currency that your  property sells at, which is the same asRMS currencylisted in Important Information.SeeDatafor definitions and view theBest PracticesandScenarios.
- Click an empty field (Channel, Source, etc.) and select from the options thatG3 RMSfound in your reservations data. Don't enter new values.
- When you enter the cost for Monday, it copies to all days. If needed, edit by day of week.
- Enter the cost in the same currency that your  property sells at, which is the same asRMS currencylisted in Important Information.
Enter the cost in the same currency that your  property sells at, which is the same asRMS currencylisted in Important Information.
- SeeDatafor definitions and view theBest PracticesandScenarios.
- Save the modified workbook in an XLSX format.
- Click theChoose Filebutton.
- Navigate to and select the saved workbook.
- ClickImport.
- G3 RMSvalidates the workbook to check for data and formatting errors. If the system finds no errors, it confirms the upload with a message. If it finds errors, it cancels the import and tells you which rows have errors. Click the Excel iconto export the error list. Correct the errors, then import the workbook again. SeeFix the issues that cause import failures.

## Data in Channel Costs

If you exported a Blank worksheet, you can select from the Sources, Channels, market segments, rate codes, and room types thatG3 RMSfound in reservations data. If you are updating existing Channel Costs, you select the options from your last import.

## Best Practices

Follow the below recommendations to simplify the task of defining the channel costs forG3 RMS. See thescenariofor setup examples.

### Understand HowG3 RMSCalculates Channel Costs

G3 RMSlooks at five fields in each booking to determine the costs: the Channel, Source, Market Segment, Rate Code, and Room Type. In the Excel template, you define the costs for those fields. You use either Universal or Specific costs.
If more than one cost applies to a booking,G3 RMSadds them up. There can be up to 5 Universal costs per booking, one for each field. But there can only be one Specific cost per booking.

### Use Universal and Specific Costs for Faster Setup

- Use Universal to define costs that apply every time that a booking includes one of those five fields. For example, every booking with the SourceOur Websitehas a fixed cost of 5. Define Universal costs for only one of the five fields and set all other levels toAll.
- Use Specific to define costs that have exceptions. For example, all bookings with theLCAmarket segment have a 10% commission cost. But if the market segment isLCAand the rate code isLCA1, the commission is zero.
- You can define Specific Costs for a combination of fields. If more than one Specific cost applies to a booking,G3 RMSuses the one with the higher number of defined fields (meaning, not set to All). In the aboveLCAexample, the 10% commission cost is only defined at the market segment level (LCA), the other four fields are set to All. The 0% commission cost is defined for the market segment (LCA)andthe rate code (LCA1), so for two fields. In that case, the more specific definition for the rate code (with two fields) "wins," andG3 RMSassigns 0% commission.

### Use Universal Costs if You Are Concerned about Input Errors

You might be concerned thatG3 RMSassigns no costs to input errors (for example, a market segment isn't updated when the rate code changes) and bookings for new rate codes. See theExpedia examplesin the scenario for how to avoid this.
To avoid incorrect costs for new rate codes, you can also use Rate Code Patterns. They are useful if you have rate codes that have the same cost and a similar naming convention. For example, you have three rate codes that have the same fixed cost, EXP20, EXP25, and EXP30. Enter EXP* andG3 RMSapplies the cost to all rate codes that begin with EXP.

### Fix the Issues that Cause Import Failures

If the worksheet has data or format issues, the import fails. To  avoid failures, ensure the following:
- Don't create unclear cost definitions. This occurs when multiple specific costs with the same number of defined fields (meaning, not set to All) apply to a booking. See theScenariossection for an example.
- Don't add, delete, move, or rename columns.
- Don't change the name of the Channel Costs tab.
- File type remains .xlsx.
- Don't create any  overlapping periods. If you leave days undefined,G3 RMSassumes there are no costs for this period.
- Don't leave the Fixed and Percentage Cost fields blank, enter zero, if needed.

### Understand How to Use Source versus Channel

G3 RMSconsiders a Channel as the parent of Sources. For example, Global Distribution System (GDS) is the channel that includes multiple sources, like Sabre, Amadeus, etc. However there isn't one industry standard, and your hierarchy might be the opposite, with GDS as the Source and Sabre as the Channel. If that's the case, followG3 RMS's understanding of hierarchy  when you enter channel costs to ensure that the system understands your setup.
Your use of Channels and Sources might also depend on what data is available from your reservation system. Many systems define the booking sourceandthe channel for a reservation, others only support one or the other. If you use only Sources and thus define costs only at that level, select All for Channel for all cost definitions.

## Scenarios

Below you see the Channel Costs setup for a property. Below the table, you can see what costsG3 RMSassumes for some example bookings, based on this setup. For simplicity, the scenarios:
- Assume that every booking has a channel and a source.
- Show only some of the available columns, for example, no Room Type level.
- Show the default costs instead of by day of the week.
- Show only a few cost definitions, for example, only two sources.

### Two Universal Costs Apply

G3 RMSreceives a booking with ChannelCRS, SourceCall Center, Market SegmentBAR, and Rate CodeBAR. The system determines a total cost of 17 by adding the costs of the two rows that match:
- Row 1 for the Channel (fixed cost of 5)
- Row 3 for the Source (fixed cost of 12).

### One Universal and One Specific Cost Apply

#### Booking: GDS/Amadeus/BAR/BAR

The system assumes a fixed cost of 10 (row 2) and a percentage cost of 10 (row 4). If this is a two-night stay,G3 RMSassumes a fixed cost of 10 (once per booking) and a percentage cost of 20 (10 per day).

### Multiple Specific Costs Match a Booking

#### Booking: GDS/Amadeus/LCA/LCA1

Total costs are 10 fixed and 5% commission:
- Row 2 for the GDS Channel, 10 fixed.
- Rows 4 (Source), 5 (Market Segment) and 6 (Rate Code) all apply to the booking.G3 RMSuses only line 6 (5%) since it has the most fields defined.

### Expedia bookings

Expedia bookings at this property  come via CRS and differ by rate code and market segment.
- Bookings at the commissionable model have a Percentage Cost and are in market segment COM.
- For Merchant model bookings, in market segment MER, the normal Percentage Cost is 25 for rate code EXP25. For Promotions, the property sometimes agrees to higher Percentage Costs, 30%, EXP30.

#### CRS/Expedia/COM/EXPCOM20

The total costs are 5 fixed and 20% commission:
- Row 1 for the CRS Channel, 5 fixed.
- Row 7 for the EXPCOM20 Rate Code, 20% commission.

#### CRS/Expedia/COM/EXPCOM25:

Total costs are 5 fixed. Only the CRS Channel costs of row 1 applies to this booking.
This shows the problem of defining costs for specific rate codes. EXPCOM25 is a new commissionable Expedia rate code that the property forgot to add to the channel costs. To avoid this, define costs at the market segment level with exceptions at the rate code level. See the next example.

#### CRS/Expedia/MER/EXP30:

Total costs are 5 fixed and 30% commission:
- Row 1 for the CRS channel, 5 fixed
- Row 8 (25%) and Row 9 (5%) apply and are added together, for a total 30% commission.
Setting a Universal cost at the Market Segment level for MER avoids the issue of the previous example.
And the Universal cost for EXP30 helps avoid missing channel costs for input errors. For example, if an EXP30 booking is manually added but has the wrong Channel, Source, and Market Segment,G3 RMSstill assigns some cost. However, if a manually entered booking has the EXP25 rate code but an incorrect Channel and Market Segment,G3 RMSdoesn't find any matching costs and assumes it's zero.

### Costs Vary at Rate Code Level

What if a rate code involves a commission payment in some cases only? For example, you pay 10% commission for a booking atthe primary priced productfrom your GDS channel  when a travel agency is attached and zero % commission otherwise. In that case define the cost for the more frequent scenario.

### Unclear Setup

If a booking contains GDS/Sabre/CP,G3 RMScan't know which of these two costs apply. That's because they both match and they both have two fields defined. An import with such an unclear setup causes an import failure.
However the below setup is valid, even though a GDS/Sabre/CP booking matches both definitions. That is because, if two specific cost definitions match a booking,G3 RMSchooses the more specific one. In this case the system uses the second definition and applies the 15 percentage cost.
