# Group Price Ranking and Upgrade Path

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Rooms-Group-Price-Ranking.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Rooms-Group-Price-Ranking.htm`
- **Ingestion Date:** `2026-09-11 22:12:59`

---

# Group Price Ranking and Upgrade Path

This tab displays the price ranking for Group Pricingand Function Spaceevaluations. If you set up one linear path in the previous step,Price Ranking and Upgrade Path,G3 RMSuses that same linear setup for group evaluations. If your property usesAdvanced Settings, you can change the ranking of Room Classes for group evaluations.
All properties use this tab to exclude Room Classes from Run-of-House evaluations, seeimpact details. Examples might be a Room Class with large specialty suites or with vacation rentals.

### How Group Price Ranking and Upgrade Path Impacts Group Evaluations

#### Run-of-House

When you run a Run-of-House group evaluation,G3 RMSconsiders which of the available room types to use to maximize the available capacity to sell. It starts from the lowest-ranked Room Class that is marked asInclude in ROH Evaluation. If a group request is larger than the capacity of the lowest-ranked Room Class,G3 RMSalso uses the second-ranked included Room Class. If a request exceeds the bottom two Room Classes combined,G3 RMSalso uses the third-ranked Room Class, and so on.
If upgrades are not allowed from the lowest Room Class to a higher Room Class, the system assumes that the property turns away any excess remaining demand for this Room Class, even if there is capacity in the higher Room Classes. Thus, not setting Up an Upgrade Path might result in a high recommended rate for a group because it can't be accommodated without turning away business.

#### Room Class

When you run a Room Class group evaluation, the Group Price Ranking and Upgrade Path helps the system select the Recommended Rate for room types of different Room Classes. The system tries to maintain your ranking setup by using the average Recommended Rate per Room Class.
For both Room Class and Run-of-House group evaluations,G3 RMScalculates displacement of the forecasted transient demand based on your main Upgrade Path.

## Setup Steps

- Clickand
	thenRooms Configuration.
- ClickNextafter you completePrice Ranking and Upgrade Pathsetup. The Group Price Rank and Upgrade Path step displays. The default Room Class order is by ADR.
- Click the upor down arrowfor any Room Class to adjust its price ranking position, with the lowest priced Room Class in the bottom position as Room Class "1." Your changes save automatically.
- By default,G3 RMSincludesall Room Class in a Run-of-House (ROH) evaluation. Click the icon to excludea Room Class.
- ClickNext. Continue to complete all the steps in Rooms Setup.
