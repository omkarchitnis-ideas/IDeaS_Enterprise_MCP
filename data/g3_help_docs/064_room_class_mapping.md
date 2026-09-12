# Room Class Mapping

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping-Room-Class.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping-Room-Class.htm`
- **Ingestion Date:** `2026-09-11 22:12:50`

---

# Room Class Mapping

Room Class mapping ensures thatG3 RMScompares similar room types when using  publicly available competitor pricing data  (ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.). For example, comparing the competitors' Standard room types to your Standard Room Class and not competitors' Suites to your Standard Room Class. You achieve that by mapping competitors' room types to your equivalent Room Classes.
If your property hasRate Data Advantage, useSmart Mappinginstead.
During the initial setup,G3 RMSmaps each competitor room type to the Room Class with the closest ADR. The system does that either automatically or after you clickSuggest. Review the suggestions to ensure they meet your business needs. The Suggest option also selects a defaultDisplay Channel, selects allCompetitors, and defines aRate Adjustmentfor properties withtax inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration.. After the initial setup, anAlertinforms you of a new competitor room type.
For an overview, reviewall steps and the benefits of Rate Shopping setup.

## Setup Steps

Until you finish mapping all your room types, a warning messagedisplays at the top of the page. This message disappears after you save this setup.
- Click, thenExternal Data, and thenRate Shopping.The Room Class Mapping tab displays.
- IfG3 RMShasn't already completed the mapping, clickSuggest.Note:The Suggest button is not available for properties using Synthetic Data.IfG3 RMSsuggests the mapping but leaves some Competitive Room Types unmapped, it means that the competitor prices the room type on average more than 30% above or below your highest or lowest priced Room Class. We recommend that you don't use competitors with such different pricing than your own, seebest practices for selecting competitors.
Note:
- The Suggest button is not available for properties using Synthetic Data.
- IfG3 RMSsuggests the mapping but leaves some Competitive Room Types unmapped, it means that the competitor prices the room type on average more than 30% above or below your highest or lowest priced Room Class. We recommend that you don't use competitors with such different pricing than your own, seebest practices for selecting competitors.
- Review and, if needed, change or complete the setup in the columns. See Data Details below for information about the columns.
- ClickSave.
- Click Export to Excelto download your settings. The export includes sheets for each rate shopping tab.

## Data Details

## Best Practices

### Know how to React when You See the Default Standard Room Class

Sometimes you see a Competitive Room Type calledStandard Room Class. The warning messageat the top of the page means that the room type is unmapped. This happens in two scenarios:

#### Single competitive room type

Many rate shopping vendors can't provide data by room type. In this case, "Standard Room Class" displays as the only name in the Competitive Room Type column. This is regardless of how many room types your competitors use. We recommend that you map the one room type to your Master Class or the lowest priced Room Class with the largest inventory. In most cases, the rate shopping data of your competitors is for their equivalent Master Class as well. Therefore, it is the correct product to which the system should compare.

#### Rate shopping error

The RMSchecks rate shopping feeds to ensure the data is complete. If the system notices that the room type field is empty, it adds the unmapped "Standard Room Classâ to the existing mapped Competitive Room Types. Standard Room Class contains the rate shopping data of any missing room type field. How you handle the unmapped room type depends on the volume and value of the missing data:
- Map it to the appropriate Room Class if the missing room type data is for a large date range or for most competitors and it is forappropriate competitors.
- Leave it unmapped if the missing room type data is for a small date range or for few competitors and it isnotfor appropriate competitors.
