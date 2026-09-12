# Per Person Pricing

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Per-Person-Pricing.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Per-Person-Pricing.htm`
- **Ingestion Date:** `2026-09-11 22:12:36`

---

# Per Person Pricing

G3 RMSuses Per Person Pricing to forecast and optimize by the number of occupants, instead of by room. This allows the system to restrict by occupancy type when the demand exceeds capacity.
In this graph, you see the unconstrained demand forecast for a Forecast Group and Room Class. With Per Person Pricing,G3 RMSalso forecasts demand by occupancy for each day. For example, for Tuesday the demand for two adults and two children (in blue) is enough to fill this Room Class, so the system raises the LRV above the price for the three lower-occupancies, restricting their availability.
Note: you can't see the unconstrained demand by occupancy in the system. The system displays demand for each Forecast Group and Room Class; adding the data for each occupancy becomes too granular.
With this pricing option, the system's optimized price is typically for a two-adult occupancy, and it uses Offsets to price single occupancy,  additional adults, and children. If needed, you can also price children by age group withOccupant Grouping. This is often used by all-inclusive resorts and properties where most room types accommodate more than three adults.
G3 RMScan also optimize the total package revenue, not just room revenue. This option, called Total Rate optimization, is helpful for all-inclusive resorts where the price combines the room with other revenues, like food and beverage. This means that the system considers the total revenue of a rate code as its value of demand. For example, a price of 500  includes 200 room revenue and 300 for food and beverage and entertainment. The Room Revenue optimization considers only the 200 room revenue value, but the Total Rate optimization considers the full 500 value.
See how the value of demand impacts the calculation ofpricingandLRV.
If you're interested, contact your IDeaS representative to see if your reservation andsellingAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.systems support these options.

## Steps to Setup and Monitor

When you use  Per Person Pricing and with Total Rate optimization, there are some differences in setup and monitoring:

#### Rooms Configuration

- Define theMaximum Occupancyby room type, for example, three persons in the Standard King and four in the Superior King. This allows you to set up the optimal pricing for each room type.
Define theMaximum Occupancyby room type, for example, three persons in the Standard King and four in the Superior King. This allows you to set up the optimal pricing for each room type.
- Per Person Pricing properties often have many and very different room types. Use theUpgrade Pathto reflect your setup. For example, your setup can't upgrade from a Room Class with a maximum occupancy of five to one with a maximum of four.
Per Person Pricing properties often have many and very different room types. Use theUpgrade Pathto reflect your setup. For example, your setup can't upgrade from a Room Class with a maximum occupancy of five to one with a maximum of four.

#### Pricing Configuration

- Define theOccupant Groupings, like the age groups for pricing children, and at what occupancy you price by extra adults versus a fixed price.
Define theOccupant Groupings, like the age groups for pricing children, and at what occupancy you price by extra adults versus a fixed price.
- Enter the Offsets per person, following thesebest practices. To understand how Offsets impact the prices, review thescenarios.
Enter the Offsets per person, following thesebest practices. To understand how Offsets impact the prices, review thescenarios.

#### Monitoring - Operations Report

Use theOperations reportto see the On Books and forecasted number of adults and children.

#### Monitoring -  Revenue Values inG3 RMS

G3 RMSuses the total rate code value for all revenue metrics, like ADR and RevPAR. For example, on all pages where you seeADRAverage Daily Rate. Room revenue divided by the number of rooms of occupancy., Help says that it's based on room revenue. If you have  Total Rate optimization, ADR is instead based on all revenues included in your all-inclusive price.

#### Monitoring - Business Insights Dashboard

The Business Analysis dashboard displays theAll-Inclusive Rate. Its value  is the basis for all revenue metrics like ADR and RevPAR. It's also the value of the reservation thatG3 RMSconsiders in the optimization.
