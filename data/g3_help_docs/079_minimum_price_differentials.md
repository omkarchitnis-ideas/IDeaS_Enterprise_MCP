# Minimum Price Differentials

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rooms/Rooms-Minimum-Price-Differential.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rooms/Rooms-Minimum-Price-Differential.htm`
- **Ingestion Date:** `2026-09-11 22:13:00`

---

# Minimum Price Differentials

Minimum Price Differential is an optional setup that enforces a minimum price difference between Room Classes.The recommended default values are zero to ensure the system can optimize the price difference between Room Classes based on their remaining demand.SeeRoom Class Pricingfor details.
Adding Minimum Price Differentials might lead to suboptimal results, see thisscenario. You might need to set up Minimum Price Differentials due to your property's business practices. For example, if your Deluxe Room Class always needs to achieve $20 more in room revenue than Standard, set up a Minimum Price Differential of $20 between them. For more information, viewbest practices for Minimum Price Differential Configuration.

## Setup Steps

### Setting Up for All Days and Seasons

- ClickNextafter you complete Price Ranking and Upgrade Path setup. The Minimum Price Differential step displays.G3 RMSdisplays Room Classes as you ordered them in Price Ranking and Upgrade Path.
- Enter a default value in theMinimum Price Differentialfield.This value can be a positive integer or zero.
- ClickApply. The value becomes the default difference between all Room Classes with a ranking relationship.
- Change the value between Room Classes, as needed.
- If you need to control the Minimum Price Differential at the day of week or seasonal level, click theAdvanced Settingslink. See Minimum Price Differential by Day of Week and Season below.
- ClickNext. Continue to complete all the steps in Rooms Setup.

### Setting Up by Day of Week and Season

If needed, you can vary the differentials by day of week and season.
- Click, thenInventory, and thenRooms Configuration.
- ClickNextafter you complete Price Ranking and Upgrade Path setup. The Minimum Price Differential step displays.G3 RMSdisplays Room Classes as you ordered them in Price Ranking and Upgrade Path.
- Enter a default value in theMinimum Price Differentialfield. This value can be zero or a positive integer.
- ClickApply. The value becomes the default difference between all connected Room Classes.
- Change the default value between Room Classes, as needed.
- Click theAdvanced Settingslink if you need to set up price differentials by day of week and season.
- For the necessary Room Class pairs and days of week, change the minimum price difference that must be in place between the two Room Classes. Each row displays connected Room Classes: theFrom Room Classcolumn represents the lower ordered Room Class, and theTo Room Classcolumn represents the higher ordered Room Class.
- Click Addfollowing a room type if you need to add a season. The Add Season window opens.
- Click theStart DateorEnd Datecalendars to add the seasonal date range. The date range must be in the future.
- Enter theMinimum Price Differentialfor each day of week in the season.
- ClickApply.
- Continue to add seasons following the steps above to set up all required seasons.
- To make changes, click Edit. To delete a season, click Delete.
- ClickNext. Continue to complete all the steps in Rooms Setup.
If you add seasons that lead to overlapping dates,G3 RMSfollows these rules:
- If you add a new season in the middle of an existing season,G3 RMSsplits the existing season into two seasons, one before the new season and one after the new season. These two have the values of the original season. The new season has the new values.
- If you add a new season that partially overlaps (later start date, same end date as existing season), two seasons result. The new season and its values apply to the overlapping dates.
- If you add a new season that includes all the dates of an existing season, the new season takes over and its values replace those  of the existing season.
