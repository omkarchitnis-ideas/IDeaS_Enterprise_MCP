# Glossary

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Glossary.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Glossary.htm`
- **Ingestion Date:** `2026-09-11 22:12:08`

---

# Glossary

- ActualThe occupancy, revenue or ADR that the property achieved, once the day is in the past. Actual occupancy is also called Final Rooms Sold.
- ADRAverage Daily Rate. Room revenue divided by the number of rooms of occupancy.
- AlertAn Alert in the G3 RMS Information Manager warns you about critical data and configuration issues. Action Alerts quickly because they mean that the system can't work optimally, or sometimes not at all.
- AncillaryRevenue generated from sources other than room bookings. Examples include restaurant, spa, golf, entertainment, and gaming revenue.

In Group Pricing, ancillary revenue excludes conference and banquet revenue. You can configure ancillary revenue categories separately for group and transient market segments.
- ARRAverage Room Rate. The same as ADR (Average Daily Rate).
- Arrival DateThe date on which the guest arrives.
- Arrival DemandIn G3 RMS, the remaining price-able unconstrained demand that will arrive on a date in the future. It is limited to market segments that are impacted by pricing changes (all unqualified and all linked qualified market segments) and only applies to a selected length of stay and room class.
- Authorized CapacityThe Effective Capacity (physical capacity minus Out of Order rooms) plus Overbooking.
- Available Capacity to SellPhysical Capacity plus Overbooking minus On Books and minus Out of Order. This value is the number of rooms that the RMS can sell before the property or room type is sold out.
- BARBest Available Rate. The lowest non-restricted product with flexible cancellation policy that anyone can book. The RMS optimizes the pricing of the BAR product. Other products, like Advanced Purchase or packages, can be linked to the BAR price.
- Base ProductThe rate code that is the starting point for the price of linked products. The linked products are child products of the Base Product. The RMS calculates the price for the Base Product, then determines the price for its children by adjusting the Base Product price.
- Base Room TypeThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.
- BetaA "Beta" label displays to identify new features that are not yet generally available. You will see this label if your property is using the feature as part of a pilot agreement with IDeaS.
- Block TypeBusiness that is booked as a group of rooms instead of individual reservations. It mostly refers to group business, but also includes transient wholesale (or allotment) business that has contracted a number of blocked rooms per day.
- Booking PaceMeasures how the occupancy changes as the arrival date approaches. It shows the speed at which reservations are booked.
- Break Even RateIn Group Pricing, the lowest rate to charge the group to at least generate the same profit as the profit the group will displace.
- Business Day End (BDE)Also known as Nightly Processing. The standard daily system update that runs during overnight hours after the end of the business day.
- Business TypeA data level for reporting, like Transient or Group, right below total property level.
- CeilingThe maximum, or highest, price that your property is willing to sell.
- Component PartsThe physical room types that form the parts of a Component Room Type.
- Component Room TypesA room type code that is formed by combining multiple physical room types. For example, room type CR1 is formed by combining one PR1 and one PR2 physical room type.
- Component RoomsAn individual room number that is formed by combining multiple physical room numbers. For example, room number 200 is formed from room numbers 101 and 102.
- ConcessionsIn a Group Pricing Evaluation, concessions are discounted and/or complimentary group rooms that are negotiated with a group.
- Conference & BanquetIn Group Pricing, revenue sources not related to guest rooms, such as meeting room rental, audio/visual equipment, banquet food and beverage, etc.
- Constrained DemandThe number of rooms that you can sell considering your property's capacity and restrictions on bookings.
- Cost of WalkCost of Walk happens if your property is unable to provide the confirmed room to a guest and has to relocate, or walk, the guest to another hotel. In that situation, costs might include the hotel room at the other hotel, a taxi, etc. 
Cost of Walk influences the overbooking level: the RMS weighs the risks of overbooking, represented by Cost of Walk, against its benefits, which are the additional revenues from selling another room. The higher the Cost of Walk, the lower the RMS tends to overbook.
- CRSCentralized Reservation System. A centralized reservation system that is used to take reservations for one or multiple hotels.
- Cutoff DateUntil this date, a property holds a block of rooms at a certain price for a group. After this date, the property can release any unsold rooms from the  block for general sale.
- Data Capture ModeA early status when IDeaS builds the RMS for a new property. During this setup step, the RMS has received the property's data, but the data is not yet saved in the RMSdatabase. The System Date is today.
- Data ExtractsFiles with new and changed booking data that the RMS receives from the reservation system. It includes reservations, group blocks, and inventory summary data. Also called Snapshots or Daily Extracts.
- Data Mapping ModeA early status when IDeaS builds the RMS for a new property. During this set-up step, the RMS is processing historical data extracts in consecutive order and is saving these data extracts to the the RMS database. The System Date is a past date.
- Data Population ModeAn early status when IDeaS builds the RMS for a new property. During this set-up step, the RMS is processing the daily the RMS data extracts on a daily basis. The System Date is today.
- Decision CreationA one-way status when the RMS receives data from the reservation system, creates forecasts and outputs (like pricing), but does not send outputs to the selling system.
- Decision DeliveryA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system.
- Differential DecisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case.
- DisplacementIn a Group Pricing evaluation, displacement refers to the rooms, revenue or profit that you lose from other bookings when you accept a group.
- DOWDays of the week.
- DTADays to Arrival. The difference between the System Date and the Occupancy or Arrival Date that you are viewing.
- Effective CapacityThe property's physical capacity minus the out of order rooms.
- Final PriceThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing.
- FloorThe minimum, or lowest, price that your property is willing to sell.
- Forecast GroupSimilar market segments combined by the RMS: You characterize market segments by adding attributes. the RMS combines similar market segments into Forecast Groups to ensure sufficient booking data. Forecast Groups with similar characteristics and enough data improve forecasting and optimization performance.
- Forecast WindowThe Forecast window defines the number of days for which the RMS forecasts unconstrained demand. It also defines the window for which you can run Group Pricing evaluations. The default Forecast Window is 365 days, but it can be set to a maximum of 730 days. The Forecast Window usually matches the length of the Optimization Window.
- Full Pattern Length of Stay (FPLOS)Restrictions that determine if a rate is open for an arrival date and length of stay. See the scenarios in the Restriction Configuration topic for examples.
- Group BlockThe number of rooms allocated to a group in the reservation system that provides the RMS with data.
- Group WashThe difference between the number of rooms blocked at its peak and the final number of rooms actually occupied.
- HTNGHospitality Technology Next Generation is an association that creates standards to enable better  integration between systems. Examples of reservation systems that use the HTNG standard are: 
Protel i/o, Suite8, NEC, Spectra, WebRezPro, Vail LMS, Infor HMS, Newbook, RMS PMS.
- Inbound SystemA system that sends data to the RMS. A PMS or CRS are examples of Inbound Systems. Some PMS and CRS are also Outbound Systems, which means they receive decisions from the RMS.
- Incremental RoomsIn Group Pricing, the net gain (or loss) in number of rooms that results from accepting a group. This value equals the Total Rooms for the group minus Displaced Rooms.
- Intraday Processing (IDP)Abbreviated IDP, it's a system update that occurs between nightly updates. For details search for the Processing topic. Also known as Current Day Processing (CDP).
- Length of Stay (LOS)The number of days a guest is staying at the hotel. This value is also the difference between the departure date and the arrival date.
- LRVA control that blocks lower-valued yieldable business when the RMS thinks that your property might sell out. It ensures that you accept only the most valuable demand. For example, a $150 LRV means that guests can book a Flexible Rate product at $160, but not a discounted PrePay&Save product at $140. The RMS optimizes LRV by Room Class.
- Market DataBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.
- Market SegmentA grouping of rate codes with similar attributes that describe their behavior. The RMS groups similar Market Segments together into Forecast Groups, which it uses to forecast unconstrained demand.
- Master ClassThe Room Class for which a value displays if there is only space in the RMS to show one, for example, when you see only one price on a page.
- MaterializationThe status of a group booking, for example tentative or definite.
- Minimum Acceptable Rate (MAR)In Group Pricing, the lowest price that you are willing to charge a group. Used in Group Pricing Configuration with the Upper Limit to provide the RMS with a range of group rates for Group Pricing Evaluations.
- Minimum Length of Stay (MLOS)Restrictions that prevent the guest from booking a stay shorter than the number of days selected. See the scenarios in the Restriction Configuration topic for examples.
- Nightly ProcessingAlso known as Business Day End or BDE. The standard daily system update that runs during overnight hours after the end of the business day.
- Non-Yieldable RatesAn attribute in G3 RMS Market Segment configuration to define rate codes that are available for any length of stay regardless of the inventory controls set by your property. it refers to a configuration setting in the property's reservation system that does not allow the LRV to control the availability of a rate code.
- Occupancy DemandThe remaining price-able unconstrained demand that will stay over an occupancy date in the future. It is limited to market segments that are impacted by pricing changes (all unqualified and all linked qualified market segments) and only applies to the selected Room Class or Room Type.
- Occupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).
- OptimizationThe step in the RMS Processing when the system uses the demand forecast (volume and value), the available capacity to sell, your configuration, and your interactions (like events, overrides) to calculate the outputs that maximize your revenues or profits. Outputs include pricing for the primary priced product, LRV, and overbooking. An Optimization also updates the constrained Occupancy Forecast.
- Optimization WindowThe number of days for which the RMS produces outputs (like pricing) and a constrained occupancy forecast. You can view the optimized outputs and occupancy forecast for the Optimization Window, but the system only sends outputs for the Upload Window. The Optimization Window usually matches and can't be longer than the Forecast Window.
- Out of Order (OOO)Refers to rooms that you physically can't sell, for example, because they need repair. 
OOO rooms reduce the Available Capacity to Sell, thus OOO changes affect the system's forecasts and outputs like pricing. Don't use OOO status to hold reservations, see Business Practices Help text for more information.
- Outbound SystemA system that receives data from the RMS, for example a selling system. Some outbound systems support a two-way transfer of information. That means they act as an outbound system receiving data and as an inbound system sending data to the RMS.
- OverbookingThe practice of selling more rooms than are physically present in your hotel to make up for wash (cancellations, no-shows etc.). The goal of overbooking is to maximize revenue by achieving as close to 100% occupancy as possible on any given day.
- OverrideWhen you change a value that the RMS%] generated, for example, an override of the remaining demand or wash forecast.
- Per Room Servicing CostIn Group Pricing, the average direct cost to your hotel of an occupied room, which may include costs such as housekeeping and guest amenities. Typically, this cost is not high, as it represents the difference in cost between a vacant, clean room and an occupied room. In other words, it is the additional costs that occur when a guest is in the room. These figures should be available from the Housekeeping Manager or Finance team.
- PermissionsTogether, Role and User management define the Permissions (under Configure). 
- Roles define the access to the RMS functionality, like a role that can add pricing overrides but can only view the pricing configuration. 
- And each user is assigned a role with the appropriate access.
- Physical CapacityThe total number of guest rooms at a property, including out of order rooms.
- Pickup (referring to Groups)For Groups, for example in Group Wash by Group, the number of rooms for which there are reservations against the group block in the property's reservation system (the system that provides the data to the RMS).
- Pickup (referring to On Books growth)The change in a performance metric between two dates. For example, the Occupancy On Books pickup since yesterday.
- Post-StayIn Group Pricing, the days following a group departure date.
- Pre-StayIn Group Pricing, the days prior to a group arrival date.
- Price ExcludedA Base Room Type setup option that means that the RMS doesn't optimize pricing for the room types of such a Room Class and instead sends the fixed price, plus any offsets, to the selling system.
- Primary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.
- ProPAROnly available if you enabled Profit or Channel Optimization. Profit per available room. ProPAR equals the profit divided by capacity (based on property's selection, either Physical Capacity or Effective Capacity, and is comparable to RevPAR.
- ProPOROnly available if you enabled Profit or Channel Optimization. Profit per occupied room. ProPOR equals the profit divided by the number of occupied rooms and is comparable to ADR.
- Push ChannelChannels that automatically receive inventory availability and pricing from the PMS or CRS. Restrictions translate Last Room Value (LRV) into controls that these channels can understand.
- QualifiedAn attribute in G3 RMS Market Segment configuration to define rate codes that you can only book if you sign in as a member or if you enter a code, for example, a corporate rate code.  The opposite attribute, unqualified, is for public rate codes that anyone can book.
- Recommended RateIn a Group Pricing evaluation, the optimal group price. When calculating the price, the RMS considers both maximizing profits and the probability of a group accepting a specific price.
- Remaining DemandThe remaining unconstrained demand for a date in the future. This value is either generated by the RMS or, in case of an active user demand override, the user override value plus or minus a possible system adjustment. The RMS adjusts a demand override according to the booking pace, so the override remains accurate after its implementation.
- Reservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.
- RestrictionsAn inventory or pricing control function to ensure that some dates are not sold below a certain rate or length of stay, for example, a three-night minimum length of stay restriction.
- Revenue OptimizationRevenue Optimization is a business discipline and culture that focuses on balancing supply and demand in a rational and disciplined systematic way to maximize revenue and profit while managing risk under current and anticipated market conditions.
- RevPARRevenue Per Available Room. The total room revenue divided by the total number of rooms (capacity).
See the Property Information topic for the capacity definition.
- RMSRevenue Management System. A reference to G3 RMS, used throughout this Help text.
- Same Time 2 Years Ago (ST2Y)The equivalent day or period two years ago. ST2Y is adjusted by day of week so the past data is compared to the same days of the week as this year.
- Same Time Last Year (STLY)The equivalent day or period last year. STLY is adjusted by day of week so last year's data is compared to the same days of the week as this year.
- Selling SystemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.
- Semi-Yieldable RatesAn attribute in G3 RMS Market Segment configuration to define rate codes that can be closed but only when the same room type or length of stay is closed for your the primary priced product; for example, Last Room Available (LRA) accounts.
- Shoulder DateA date that is adjacent to a busy date.
- Smith Travel Research (STR)STR is a global provider of competitive benchmarking, information services and research to the hotel industry. STR reports provide property performance data compared to its competitive aggregate and general market, allowing you to follow trends in occupancy, average daily rate (ADR), revenue per available room (RevPAR).
- Special EventA  period when the transient patterns (occupancy, revenue, ADR, pace) differ from normal patterns. This can be a holiday, a sporting event, a convention, etc. Adding such events in the RMS helps improve its forecasts and outputs (like pricing).
- SystemA reference to the RMS, used throughout this Help text.
- System CEOThe IDeaS name for a system administrator role. Users with this role configure a property's permissions: creating other Roles, then assigning them to Users. They ensure that the right users have the appropriate access in the system.
- System DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.
- System Dormant ModeA status when the RMS is receiving extracts, but IDeaS temporarily paused the processing of these extracts as it is carrying out a scheduled support activity. The System Date is when the last extract was processed.
- System ModeA status defined by how the RMS  is receiving, populating, and sending data. To see your System Mode in G3 RMS, click the Important Information icon in the top right corner of any page (next to your initials).
- System Paused ModeA status when the RMS is no longer receiving daily data extracts and has not processed since the last extract was received. The System Date is when the last extract was received.
- System Remaining DemandG3 RMS generated remaining unconstrained demand for a date in the future.
- System Total DemandOn Books plus the remaining unconstrained demand.
- Tax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration.
- Total DemandThe combination of the rooms on books and the remaining unconstrained demand.
- Total Demand - GroupGroup On-Books+Group Remaining Demand
- Total Demand - TransientTransient On-Books+Transient Remaining Demand
- TransientGuests who book individually rather than with a group.
- Unconstrained DemandUnconstrained, or true demand refers to how much you could sell if there were no constraints such as the hotelâs capacity or restrictions on bookings. This demand forecast shows you the potential demand, not just the limited demand that you accept.
See the Demand and Wash (Overview) topic for how the system calculates unconstrained demand.
- UnqualifiedAn attribute in G3 RMS Market Segment configuration to define public rate codes that anyone can book. The opposite attribute, qualified, is if you need to sign in as a member or enter a code to book the rate code.
- Upload WindowThe Upload Window is the number of days for which the RMS sends controls including pricing, overbooking and LRV, to your selling systems. It also defines the period for which you can upload changed controls. The Upload Window is limited by the inventory window of your reservation system, so it is the number of days for which your PMS or CRS can accept reservations and controls. Typically, that limit is 365 days, but some reservation systems allow up to 396 days. The window also depends on your IDeaS subscription and can't be longer than the Optimization Window. Contact your IDeaS representative to change your Upload Window.
- Upper LimitIn Group Pricing configuration, the maximum price that you would charge a group in a high demand period. Used with the Default MAR to provide G3 RMS with a range of group rates for Group Pricing Evaluations.
- User Constrained DemandThe user generated remaining constrained demand for a date in the future. This value is used for Forecast Groups with a booking type attribute of âblock,â so typically for groups. G3 RMS may still apply wash to the override value but otherwise accepts the value as the new forecast.
- User Remaining DemandThe user generated remaining unconstrained demand for a date in the future. This value is the user override plus or minus a possible system generated adjustment. G3 RMS adjusts the userâs demand override according to the booking pace so that the override remains accurate after its implementation.
- Virtual SuiteAnother name for a Component Room Type.
- WashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization.
- YieldableAn attribute in G3 RMS Market Segment configuration that refers to a configuration setting in the property's reservation system that allows the LRV to control the availability of a rate code.
