# Best Practices for Setting Up Competitors

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/BP-Rate-Shopping-Competitor.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/BP-Rate-Shopping-Competitor.htm`
- **Ingestion Date:** `2026-09-11 22:14:25`

---

# Best Practices for Setting Up Competitors

You must selectUse Rate Shopping Datafor at least one competitor.The RMSalso  uses your property's rate shopping data for comparison with your competitors and you can't change the setup or remove your property from this setup.
Select the Use in Rate Shopping checkbox for all appropriate competitors, sothe RMScan calculate how much their pricing impacts your demand.If you have multiple products, you might vary the selections. For example, if a competitor doesn't sell or isn't an appropriate competitor for one of the products, don't select them for that product.
Including only appropriate competitors is more important when you have a large number of competitors in your rate shopping data. When you have only three competitors,the RMScan easily differentiate each of their impacts on your demand. When you have ten competitors, that task may be very difficult.
Do not select the Use in Rate Shopping checkbox for those competitors that do not directly impact your rate strategy and are only included in your competitive set for informational purposes. Whilethe RMScan measure competitorsâ impact, it still relies on you to provide it with meaningful data. If you include properties that price very differently than you and your appropriate competitors, you may givethe RMSa false impression of competitorsâ rates, which could lead to a suboptimal forecast and pricing.
If you can include vacation rentals in your rate shopping data, ensure they are appropriate competitors, since there is no standard rating system:
- Is the product comparable? Are the services, facilities, and their quality the same? Does it attract the same type of traveler?
- How near is the listing to your property? The closer it is, the more it might be an appropriate  competitor.
- Is the vacation rental priced similarly to matching room types at your property?
If you include vacation rentals, ensure that they are mapped to a matching room type, seeRoom Class Mapping.
You might have a competitor that prices at a very high or low rate until the typical booking window begins, for example, 90 days to arrival. This property remains an appropriate competitor within 90 days, but you don't want their extreme pricing to impact your forecast and decisions outside of 90 days. Use this feature to ignore the competitor's rate shopping data until the defined booking window arrives.
A competitor might price very differently than you only during a limited period, for example, when it undergoes a renovation. Such a property remains an appropriate competitor before and after the renovation, but you don't want their abnormal pricing during the renovation to negatively impact your forecast and decisions. Use Ignore Competitor Data to define a period when you wantthe RMSto ignore rate shopping data for that competitor.
A competitor's business practices 
 might also differ from yours only on specific days of the week during that period. For example, the competitor offers extremely high rates on 
 three weekends in October due to a large group that is booked on those 
 days. Use Ignore Competitor Data to select specific days of the week 
 within a period on which to ignore the competitor's rates.
When using this optional setup, be sure to enter a note explaining 
 the reason why you decided to ignore the data for the period.
We recommend that you keep the past two years of periods that you set up to ignore competitors' data.the RMSuses up to two years of historical rate shopping data to understand demand and Reference Price. Keeping the Ignore Competitor Data periods ensures thatthe RMScontinues to exclude historical rate shopping data that should not influence your pricing.
Use Rate Adjustment setup for deductions from rate shopping values. For example, the rate shopping data of your competitors includes breakfast and the your pricing values don't include it. In that case, rate shopping data is inflated by the breakfast value and doesn't offer a true comparison to your unqualified pricing. To avoid that, enter the  breakfast value as a Rate Adjustment.The RMSremoves the value from the rate shopping data and uses the adjusted values in its optimization. The system doesnotremove the value from the displayed competitor prices, for example, those inCompetitor Details.
Another example is if your property is in a country where booked prices have to include taxes (like VAT or GST). During optimization,the RMScompares revenue data (for example ADR) from yourreservation systemto competitor rate shopping data. For a true comparison, both values must have the same tax status, either including or excluding tax.
For mostclients, thereservation systemsends revenue data exclusive of tax. And rate shopping data usually includes tax. If thatâs the case at your property, add the tax value as an adjustment so thatthe RMShas comparable values, both exclusive of tax. Ifthe RMSreceives revenue and rate shopping data exclusive of tax, donât add any adjustment. If you are unsure whether your system sends data with or without tax, contactyour IDeaS representative.
What if a new competitor has opened in your market, and you know it has an immediate impact on your demand?The RMScan detect such overall one-time shifts in demand very quickly. However, unless your rate shopping data vendor can provide historical data,the RMSwaits 30 days after receipt of the first data file before it considers the impact of price changes of a new competitor. Therefore, to react to a price change for a specific arrival date, you may need to use demand overrides untilthe RMScompletes its learning.
