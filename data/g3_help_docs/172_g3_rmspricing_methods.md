# G3 RMSPricing Methods

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/About/PricingMethods.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/About/PricingMethods.htm`
- **Ingestion Date:** `2026-09-11 22:14:04`

---

# G3 RMSPricing Methods

During the initial implementation for your property, you select one of the following pricing types:Continuous Pricing,BAR by LOS, orBAR by Day. In each pricing method,G3 RMSoptimizes the price for each Room Class. The differences are whether pricing is by occupancy date or by arrival date by length of stay, and how you set up and maintain prices.
Some pricing methods might not be supported by your selling systems, distribution systems, and connected channels. Seeselecting a pricing methodfor details.

### Daily Continuous Pricing

G3 RMScreates a price for each night of stay, based on the demand and price sensitivity of each night. For each Room Class you define the price range thatG3 RMScan select from.G3 RMSsends a price by arrival date for each room type.
Daily Continuous Pricing includes two options:

#### Per Room

By default,G3 RMSproduces a price for each arrival date and room type, based on a single occupancy. The system optimizes for room revenue. This type of pricing is commonly used by hotels, which price by roomand, if needed, add supplements for extra services, like breakfast.

#### Per Person

Properties where most room types accommodate more than 3 or 4 adults or all-inclusive resorts often use Per Person Pricing. In this option,G3 RMSoptimizes not by room, but by number of occupants. And the system prices for a two adult occupancy and uses Offsets to price single occupancy,  additional adults. and children. You can also price children by age group withOccupant Grouping.
And for properties like all-inclusive resorts, where the price includes lodging, food and beverage, entertainment, etc.,G3 RMScan also optimize for total revenue, not just room revenue.  For all options and the steps, see thisoverview of Per Person Pricing.
If you're interested, contact your IDeaS representative. We need to test to ensure that your reservation andsellingAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.systems support these options.

### Daily Continuous Pricing Examples

G3 RMScan select any price between the ceiling and floor values, as long as the price meets the minimum rules.

#### Pricing Setup

#### Rules

- Minimum change for standard = 3.00
- Minimum change for deluxe = 5.00
- All prices must end in XX9.99

#### Continuous Pricing Decisions

- Standard room pricing for arrival on 1 January for three nights: 429.99+219.99+329.99=979.97
- Deluxe room pricing for arrival on 1 January for three nights: 549.99+409.99+629.99=1589.97

### BAR by Day (also called Daily BAR or Daily Pricing)

G3 RMSproduces a different price for each night of stay, based on the demand and price sensitivity of each night. With this approach, you set up pricing as a set of price levels with values assigned by room type and by season.G3 RMSsets a price for each arrival date, which incorporates all the demand that stays through that night.G3 RMSdeploys a value by arrival date for each room type.

### BAR by LOS (also called Arrival Date by Length of Stay, or Length of Stay Pricing)

G3 RMSproduces a price based on the arrival date and the guestâs length of stay, offering a separate price for each LOS 1-8+. This option considers the demand and price sensitivity for each arrival date based on the selected length of stay. Like the BAR by Day approach, you set up pricing as a set of price levels with values assigned by room type and by season.G3 RMSsends rates for each rate code to each arrival date, length of stay and, where possible, room type combination.

### BAR by Day or BAR by LOS Examples

The following examples show price setup  and output for BAR by Day and BAR by LOS. For these pricing options,G3 RMScan select only the price points set up in Rate Plan setup as the daily BAR decision.

#### Rate Plan Setup

#### BAR by Day Decisions

- Standard room pricing for arrival on 1 January for three nights: 500+450+400=1350
- Deluxe room pricing for arrival on 1 January for three nights: 750+750+800=2300

#### BAR by LOS Decisions

##### Standard Room Class

##### Deluxe Room Class

- Standard room pricing for arrival on 1 January for three nights: 500+500+500=1500
- Deluxe room pricing for arrival on 1 January for three nights: 800+800+800=2400

### Selecting a Pricing Method

The primary difference between Daily BAR and Daily Continuous Pricing is the constraint on the pricing decision due to the different setup. Thus, this section groups the two together when looking at business considerations.
Use these key business considerations to select a pricing methodology:

#### Guest Pricing Presentation

How is your market accustomed to being presented with a price?
Some markets or guests prefer to be presented with a single price that applies to each night of their stay, regardless of how long they stay (BAR by LOS). Others are amenable to having a different price for each night (BAR by Day). In some markets, guests prefer to see a total price for their stay, avoiding any challenges with different rates applying to different nights of the stay.

#### Price Strategy and Business Need

What strategy is required to capture optimal revenues based on the business mix?
The pricing model that is most appropriate depends on your business model and the average length of stay. You need to ensure that you can capture the most appropriate demand by arrival date and LOS.
For example, a luxury property often has higher average lengths of stay and can gain additional value by charging the optimal price based on the selected stay pattern (BAR by LOS). However, if the average LOS is one night, the additional value from pricing by arrival date and LOS is likely lower (BAR by Day).

#### Deployment of Price Strategy

Investigate if yourSelling SystemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.and connected channels support the distribution of your pricing selection.
For example, will BAR by LOS pricing be distributed to key Online Travel Agent (OTA) channels?
Consider the following:
- If some OTA channels cannot accept pricing by LOS, how much of your production comes from these channels?
- If most of your production comes from OTA channels that can accept this pricing approach (like Expedia and Booking.com), are they sufficient?
If you also require price parity, consider if it can be achieved with your selected pricing method and deployment systems.

### Pros and Cons of Each Pricing Approach

The following tables list reasons for and against each pricing method:

#### Continuous Pricing

#### BAR by Day

#### BAR by LOS
