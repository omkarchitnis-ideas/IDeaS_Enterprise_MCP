# Independent Products

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Independent-Products.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Independent-Products.htm`
- **Ingestion Date:** `2026-09-11 22:12:34`

---

# Independent Products

For allclients,G3 RMSoptimizes pricing for thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..With a  subscription,G3 RMScan optimize pricing for other products whose demand is completely independent from the Primary Priced Product or from Linked Products.
An extended-stay hotel has a product for stays of 15 days or longer, called LOS15, for which there is consistent demand throughout the year. For two days in a month, the demand (green bars) and price (blue line) ofthe primary priced productis very high, due to a citywide event. If the LOS15 rate is set up as a Linked Product,G3 RMSconsiders its demand as related tothe primary priced productand might price the LOS15 product too high (red line) to capture demand.
But if the LOS15 product is set up as an Independent Product,G3 RMScreates a separate Forecast Group for it and can better understand its demand and therefore price it optimally.

## Setup and Management Steps

With Independent Products, there are some differences in setup and in how you manage demand and pricing:

### Market Segments Configuration

By assigning theEqual toand Base Product attribute  to a rate code or market segment you define the business thatG3 RMSuses to price theprimary productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.. For each independent product, you also need to define the business that the system uses to price it. To do that you can change theEqual to Base Productattribute to apply to the independent product instead of BAR. The same applies to theLinked toattribute.
When you select a new Independent Product as the Base Product,G3 RMSforces you to name the product using the same name as in yourselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data..

### Pricing Configuration

The setup for an independent product includes the steps for the primary product:Definition,Ceiling/Floor,Offsets, and, if needed,Supplements. The Base Room Types are the same ones as for the primary product.  If needed, you can:
- Create separateRounding Rulesfor each independent product.
- Define aBlended Pricewhen you want the price of an independent product to stay the same.
- Set a minimum difference between independent products inHierarchy.

### Rate Shopping Configuration

For each Independent Product, you can set a different default channel, use the data of differentcompetitors, and, if needed, create different Competitive Market Position Constraints.

### Permissions

Use Role Management inPermissionsTogether, Role and User management define the Permissions (under Configure). 
- Roles define the access to the RMS functionality, like a role that can add pricing overrides but can only view the pricing configuration. 
- And each user is assigned a role with the appropriate access.to control access to Independent Products.

### Demand and Wash Management

View and, if needed, override the demand for independent products.
Note: Demand overrides  byArrival by LOSare not available with independent products. Instead,  override demand byOccupancy Date, and select the product that matches the length of stay that you want to override.For example, if you know something about the demand for monthly stays, select the extended stay product that you defined for that length of stay.

### Pricing

You can view and, if needed, overridepricingof independent products. If you subscribe to publicly available competitor data for independent products, you can view that data too.

### Monitoring

#### At a Glance

When you select a date on theCalendar, the daily details display the pricing for the primary product and for all independent products.

#### Business Analysis

In theSummarytab a filter allows you to view pricing related data for any of your Independent products instead of the primary product.
Forecast Groups for extended stay properties are based on the split market segment level by length of stay (LOS) data. This allowsG3 RMSto identify and link demand to the appropriate extended stay rate level.For example, an 8-night LOS discount booking displays as DISC_ES1, and a 20-night LOS corporate booking displays as CORP_ES2.Learn more about theBusiness Analysis Data Details.

#### Reports

In theData Extraction,Decision Pace,Output Override,Pricing Override History, andPricingreports, you can select to view the data for independent products.

#### Notifications

You can set upNotificationsfor independent products, for example, when pricing changes by a certain threshold.

#### Data Feed

With a subscription, theData Feedincludes data of independent products, for example, pricing overrides or configuration.
