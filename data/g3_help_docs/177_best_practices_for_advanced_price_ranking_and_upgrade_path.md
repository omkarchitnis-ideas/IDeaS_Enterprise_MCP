# Best Practices for Advanced Price Ranking and Upgrade Path

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/BP-Rooms-Price-Ranking-Advanced.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/BP-Rooms-Price-Ranking-Advanced.htm`
- **Ingestion Date:** `2026-09-11 22:14:07`

---

# Best Practices for Advanced Price Ranking and Upgrade Path

Review these best practices andscenarioswhen setting up Advanced Price Ranking and Upgrade Path

## Best Practices

### Use the Correct Arrows to Define Relationships

Vertical arrows within a tower always point up. In other words, price ranking and upgrade path always go from the lowest priced Room Class at the bottom up to the  higher priced Room Classes.
Horizontal arrows indicate relationships for price ranking or both price ranking and upgrade between towers. They can point in either direction between towers.
Price ranking is represented only by the arrows. There is not a numbered price rank displayed for each Room Class. This is because, with more than one tower, there are almost always Room Classes without direct price ranking relationship. SeeScenario 2below.

### Be Careful With Towers Without An Upgrade Relationship

You can have independent towers that have no upgrade or no price rank and upgrade relationship with the other towers. However, keep in mind that any such independent tower, like an independent Room Class, cannot accept excess demand. In the case of zero demand for the independent tower or Room Class and more demand than capacity for the other tower,the RMSconsiders all the excess demand of the other tower as lost, and the independent tower or Room Class remains empty. SeeScenario 2below.

### Understand the Impact on Price Ranking

When you set up an Advanced Price Ranking and Upgrade Path,the RMSno longer checks if your pricing inPricing Configurationis aligned with the Room Class hierarchy. As an extreme example,the RMSwould not warn you if you set up pricing for your highest-ranked Suites lower than for your Standard rooms.
Therefore, we recommend that you only enable the Advanced Settings if you truly require them. See the scenarios below for hotel setup when Advanced Settings are needed.
If you do not require Advanced Settings, clickExist Advanced Settingsto restore a linear path.

## Scenarios

### Scenario 1: Two Physical Towers

In the example below, the property has two physical towers, the Resort View Tower and the Ocean View Tower. Each has Standard, Deluxe, and Suites. The setup below indicates the following:
- Each of the two towers has a straight price ranking and upgrade path, from Standard to Deluxe to Suites.
- Price ranking and upgrades go from the Resort View to the Ocean View Tower at each level. For example, the Resort View  Deluxe can upgrade to either the Resort View Suite or to the Ocean View Deluxe.
- Resort View Deluxe and Ocean View Standard both have to be priced below Ocean View Deluxe and above Resort View Standard. Otherwise, they are priced independently from each other because they are in separate towers. Based on their pricing setup, that could mean that Ocean View Standard is sometimes priced above Resort View Deluxe and sometimes below.

### Scenario 2: Two Inventories That Don't Share Demand

In the example below, the hotel has six Room Classes separated into two inventories. The setup below indicates the following:
- The Regular Hotel Rooms in the left tower and the Residences on the right have a straight upgrade path and price ranking within themselves.
- There are no upgrade path relationships between the two inventories. If there is excess demand in either of the towers and not enough demand in the other tower,the RMSconsiders the excess demand as lost.
- Residences  â  1 Bedroom have to be priced below Specialty Suites, but there is no other price ranking relationship between Residences and Regular Hotel Rooms. If the pricing setup allows it, Residences  â 1 Bedroom and Residences â Studio could be priced below Suites, Deluxe and Standard, if that was the output of the optimization.

### Scenario 3: Two Inventories with Linear Price Ranking

In the example below, the hotel has six Room Classes separated into two inventories. The setup below indicates the following:
- Both towers have a straight upgrade path and price ranking within themselves.
- Standard View cannot upgrade to Junior Suite, because, even though the Junior Suite is larger than the Standard View, guests insist on the view. However, the Price Rank Only arrow between them means that Standard View must be priced below Junior Suite.
- Despite the Price Rank Only arrow (between Standard View and Junior Suite), each Room Class still has an uninterrupted upgrade path to the highest Room Class. Any excess demand is always accommodated if there is not enough demand for higher ranked Room Classes.
- Pass Throughs are necessary to ensure the desired relationships, for example, that Standard View is ranked above Standard and below Junior Suite and that, at the same time, Standard View has upgrade paths with Standard and Junior Suite View.
- This example is rare because a linear price ranking applies to all Room Classes: Standard is ranked 1, Standard View ranked 2, Junior Suite  ranked 3, Junior Suite View ranked  4, One Bedroom Suites  ranked 5, and so on.

### Scenario 4: Two Inventories with Price Ranking and Upgrades

In this example, the hotel has five Room Classes separated into two inventories. The setup below indicates the following:
- Both towers have a straight upgrade path and price ranking within themselves.
- Standard 2 Doubles cannot upgrade to Junior Suite, because the Junior Suite can't accommodate more than 2 guests and most demand for the Standard 2 Doubles is for 3 or more guests.
- Standard King can only accommodate two guests, Standard 2 Doubles four guests. Demand often can't be moved between the two types.  Therefore, the two Standard room types are in separate Room Classes even though their ADR is similar.
- Standard King has to be priced lower than Junior Suites, but Standard 2 Doubles can be priced the same or higher than Junior Suites. This might occur when there is excess demand for triple or quadruple occupancy room types and not enough to fill the single or double occupancy room types.
