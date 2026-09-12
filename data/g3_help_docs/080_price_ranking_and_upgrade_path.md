# Price Ranking and Upgrade Path

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Rooms-Price-Ranking.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Rooms-Price-Ranking.htm`
- **Ingestion Date:** `2026-09-11 22:13:01`

---

# Price Ranking and Upgrade Path

Price Ranking and Upgrade Path ensure thatG3 RMSconsiders your pricing hierarchy to price optimally and maximize revenue opportunities. These two separate setups are the fourth step in the Rooms setup. For a summary of all the steps in Rooms setup, seeRooms Configuration Overview.

### Price Ranking

G3 RMSoptimizes pricing for each Room Class, but it does not optimize them independently.Instead,G3 RMSconsiders your pricing hierarchy and respects the Room Class ranking that you set up. You set up price ranking to ensure thatG3 RMSmaintains your pricing hierarchy while pricing optimally. SeeBest Practicesto learn more.
IfG3 RMSoptimized all Room Classes independently, under certain demand and price sensitivity data conditions, the system might price a Suite Room Class lower than a Standard Room Class. This data-driven optimization approach does not work for most properties because it does not consider room type positioning integrity or operational issues.
For Standard and Suite Room Classes, for example, you might rank Standard as 1, below Suite, which is 2, to tellG3 RMShow to price those Room Classes relative to each other. In the optimization,G3 RMSensures that the lowest priced room type of the Standard Room Class is never priced higher than the lowest priced room type of the higher ranked Suite Room Class.
If you are concerned about how this approach works with your business processes, contactyour IDeaS representative.
Note: If you add a Specific pricing override, the override doesn't adjust to fit your price ranking setup. Learn more inbest practices for overriding Pricing.

### Upgrade Paths

#### With Room Type Overbooking Option

In an ideal world, the capacity of your Room Classes matches their demand. Often, however, capacity and demand do not match. You might have more demand than you can accommodate for your Standard Room Class, and perhaps little demand for your Suites. In this case, if you want to maximize your revenue opportunities, you might decide to overbook your Standard rooms more than you would normally allow, and upgrade or upsell that demand to achieve a sellout. An upgrade path helps you do this. SeeBest PracticesandScenariosto learn more.
When you enable the upgrade path between two Room Classes, the  higher ranked Room Class (such as Suites) accepts upgrades from the lower ranked Room Class (such as Standard), butonlyon days when the Suite Room Class has less forecasted demand than capacity, and Standard has more demand than capacity. In other words, the excess Suite inventory can be added to the overbooking of the Standard Room Class, but only on days with that particular demand distribution.
For example,G3 RMSforecasts more demand for your Standard rooms than their capacity. It also forecasts no demand for your Suite rooms. If you allow upgrades from the Standard Room Class to the Suite Room Class,G3 RMScan overbook your Standard rooms by the full capacity of the Suite rooms. This overbooking is in addition to the normal overbooking that the system calculates for Standard rooms based on expected wash.
An upgrade path is necessary if you want to maximize revenue in every situation. Without it, you might be turning away demand when one Room Class has more demand than capacity, and another has less demand than capacity.

##### Upgrade Path and Pricing Ranking Together

The upgrade path always follows the price ranking order to ensure thatG3 RMSdoes not plan upgrades to rooms that could potentially be priced lower. If you choose to exclude a Room Class from the upgrade path, it is still included in the price ranking. When you include a Room Class in the upgrade path, you share all rooms of all room types included in the Room Class.

#### With Run of House Overbooking Option

If you useRun of House Overbooking, you can't change the upgrade path page. All higher ordered Room Classes must accept upgrades from lower ordered Room Classes and Advanced Settings are not available.

## Setup Steps

- ClickNextafter you completeRoom Typesetup.
- By defaultG3 RMSsorts your Room Classes by historical ADR, with the lowest priced Room Class in the bottom position as Room Class "1." If needed, click to move a Room Class upor downin the price ranking
- ClickNext. The upgrade path page displays.G3 RMSuses price ranking as the order for the upgrade path.A solid arrowindicates the path is both Price Rank and Upgrade. When this arrow displays, a higher ranked Room Class (such as Suites) accepts upgrades from a lower ranked Room Class (such as Standard).  In other words, the excess Suite inventory can be added to the overbooking of the Standard Room Class. But only on days when the Suite Room Class has less forecasted demand than capacity, and Standard has more demand than capacity.An outlined arrowindicates Price Rank Only. When this arrow displays, the higher Room Class is skipped in the upgrade path. The upgrade path continues at the next higher Room Class that is above a solid arrow. However, any rooms that have no demand in the skipped Room Class remain unsold.
- A solid arrowindicates the path is both Price Rank and Upgrade. When this arrow displays, a higher ranked Room Class (such as Suites) accepts upgrades from a lower ranked Room Class (such as Standard).  In other words, the excess Suite inventory can be added to the overbooking of the Standard Room Class. But only on days when the Suite Room Class has less forecasted demand than capacity, and Standard has more demand than capacity.
- An outlined arrowindicates Price Rank Only. When this arrow displays, the higher Room Class is skipped in the upgrade path. The upgrade path continues at the next higher Room Class that is above a solid arrow. However, any rooms that have no demand in the skipped Room Class remain unsold.
- Click a solid arrowto change it to a Price Rank Only outlined arrow, to remove the Room Class above it from the upgrade path. Click the arrow again to restore it to a solid arrow and include the Room Class in the upgrade path. This arrowmeans you can't change the settings, seeRun of House overbooking.
- ClickNext. Continue to complete all the steps in Rooms setup.
