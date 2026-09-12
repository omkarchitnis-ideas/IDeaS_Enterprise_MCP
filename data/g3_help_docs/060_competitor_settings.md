# Competitor Settings

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping-Competitor.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping-Competitor.htm`
- **Ingestion Date:** `2026-09-11 22:12:48`

---

# Competitor Settings

Use the Competitor Settings tab to tellG3 RMShow to display your competitors' publicly available pricing data and,if enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section., how to use the data.
For an overview, reviewall steps and the benefits of Rate Shopping setup.

### What Help Do You Need with Setting up the Competitors?

- I need to set up how mycompetitors displaythroughoutG3 RMS.
I need to set up how mycompetitors displaythroughoutG3 RMS.
- I need to configure howG3 RMSuses the competitor rate shopping data.
I need to configure howG3 RMSuses the competitor rate shopping data.
- I want to temporarilyIgnore Competitor Datawhile a competitor is pricing much higher or lower than me.
I want to temporarilyIgnore Competitor Datawhile a competitor is pricing much higher or lower than me.
- A competitor's prices include costs like breakfast or taxes, but our prices don't. I need to use aRate Adjustmentto make the values comparable.
A competitor's prices include costs like breakfast or taxes, but our prices don't. I need to use aRate Adjustmentto make the values comparable.
- I want to review thebest practicesfor setting up my competitors.
I want to review thebest practicesfor setting up my competitors.
- I need to set up aCompetitive Market Position Constraintto maintain a specific pricing position in my competitive set.
I need to set up aCompetitive Market Position Constraintto maintain a specific pricing position in my competitive set.

## Setup Steps

- Click, thenExternal Data, and thenRate Shopping.
- Click theCompetitor Settingstab.
G3 RMSselectsMedian PriceforShow competitor by, either automatically or after you clickSuggestin theRoom Class Mapping tab. Use these steps to review and, if needed, change the setup.
- Select the competitor to display on pages where you see only one, like on the daily details card of the At a Glance dashboard. Use one of two options:SelectShow competitor byand select a 
	 price level if you want the displayed competitor to meet your price level criteria.G3 RMSpicks the matching one from all competitors checked for Use Rate Shopping Data, excluding your own property.Highest Price: displays the competitor with the highest price for each date.Lowest Price: displays the competitor with the lowest price for each date.Median Price: displays the median competitor, or the competitor with the price in the middle when you sort competitors by pricing for each date.SelectSelect a specific 
competitorand choose a property name from the list, if you always want to display the same competitor, regardless of price. The same property and its daily rates display in pricing data.
- SelectShow competitor byand select a 
	 price level if you want the displayed competitor to meet your price level criteria.G3 RMSpicks the matching one from all competitors checked for Use Rate Shopping Data, excluding your own property.Highest Price: displays the competitor with the highest price for each date.Lowest Price: displays the competitor with the lowest price for each date.Median Price: displays the median competitor, or the competitor with the price in the middle when you sort competitors by pricing for each date.
- Highest Price: displays the competitor with the highest price for each date.
- Lowest Price: displays the competitor with the lowest price for each date.
- Median Price: displays the median competitor, or the competitor with the price in the middle when you sort competitors by pricing for each date.
- SelectSelect a specific 
competitorand choose a property name from the list, if you always want to display the same competitor, regardless of price. The same property and its daily rates display in pricing data.
- ClickSave.
- Click Export to Excelto download your settings. The export includes sheets for each rate shopping tab.
G3 RMSselectsUse Rate Shopping Datafor all competitors, either automatically orafter you clickSuggestin theRoom Class Mapping tab.
- If available, select theProductfor which you make selections.
- Make the appropriate selections and changes for how to display or use rate shopping data, seeData Detailsfor descriptions.
- ClickSave
- If you useindependent products, you can define the ignore settings byProduct. Linked products use their Base Product's selection.
- Select theIgnore Competitor Datacheckbox.
- Click to adda competitor that you want to be ignored.
- Clickand use the calendar menus to define theStart DateandEnd Datefor when to ignore the competitor's data.
- Select theCompetitor Name.
- Select anyRoom Class. Only Room Classes that you have selected inRoom Class Mappingare available.
- If needed, change for which Day of Week (DOW) the data is ignored.
- Select theChannel Name. You can select multiple channels.
- Click the note iconto add aNoteand enter an explanation for why you decided to ignore the data.
- If needed, repeat the previous steps to add other competitors.Note: If you use a competitive constraint,G3 RMSwarns you if ignoring competitors means that it can't apply the constraint, seeconstraint definitions.
- The table displays present and future ignored periods. Use the Action column to:Click the note icon  
	 to see notes that have been added. A note iconindicates that no note has been added. A note icon with a check markindicates that a note is present.Click to editor deletethe ignored period.
- Click the note icon  
	 to see notes that have been added. A note iconindicates that no note has been added. A note icon with a check markindicates that a note is present.
- Click to editor deletethe ignored period.
If your property usestax inclusive pricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration.,G3 RMSsets up a tax Rate Adjustment, either automatically or after you clickedSuggestin theRoom Class Mapping tab. In that case, review and, if needed, change the setup.
- Select theRate Adjustmentcheckbox.If you shop for multiple products,Applies to Property level onlymeans that the setup applies to all products.
- In theSelect anyfield, decide how to apply the adjustment:SelectDefaultto apply the adjustments to all properties, including your own.For example, if you use tax inclusive pricing.Select a specific competitor if the adjustment applies only to some competitors and not your own property. For example, only one competitor's prices include breakfast.If you use both, the  Default adjustment applies to all competitorsexceptthe specific ones.
- SelectDefaultto apply the adjustments to all properties, including your own.For example, if you use tax inclusive pricing.
- Select a specific competitor if the adjustment applies only to some competitors and not your own property. For example, only one competitor's prices include breakfast.
- If you use both, the  Default adjustment applies to all competitorsexceptthe specific ones.
- Set the values forTax (Deduction)orOther (Deduction):SelectPercentageorValuefor the amount to deduct from rate shopping values.In the last field, type the percentage or value to deduct from  rate shopping values.
- SelectPercentageorValuefor the amount to deduct from rate shopping values.
- In the last field, type the percentage or value to deduct from  rate shopping values.
- Click add. If you're done, continue to the last step to save your changes. Otherwise repeat the previous steps to:Define exceptions from the Default. For example, you deduct tax from all competitors, but  you also deduct breakfast for one competitor that offers breakfast.Define adjustments for other competitors.
- Define exceptions from the Default. For example, you deduct tax from all competitors, but  you also deduct breakfast for one competitor that offers breakfast.
- Define adjustments for other competitors.
- If needed, addSeasonswhen the default values differ, for example if a competitor includes breakfast only during part of the year:Enter aNamefor the season.Select Default or a specific property for which the season applies.Select theStartandEnd Dateof the season.Select theTaxandOtherdeductions, following the same steps as for the Defaults.Click add.
- Enter aNamefor the season.
- Select Default or a specific property for which the season applies.
- Select theStartandEnd Dateof the season.
- Select theTaxandOtherdeductions, following the same steps as for the Defaults.
- Click add.
- ClickSave.
If needed, clickto delete a Rate Adjustment.

## Data Details

### Competitor Configuration
