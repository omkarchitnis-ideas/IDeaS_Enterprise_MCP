# Competitive Market Position Constraints

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping-Constraints.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping-Constraints.htm`
- **Ingestion Date:** `2026-09-11 22:12:48`

---

# Competitive Market Position Constraints

Use these constraints to enforce a certain pricing position based on the publicly available competitive pricing data (ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.). Examples:
- UseNot Lowto constrain pricing above the lowest-priced competitors.
UseNot Lowto constrain pricing above the lowest-priced competitors.
- Limit your prices to the lower half of your competitors until you have 50% occupancy on books.
Limit your prices to the lower half of your competitors until you have 50% occupancy on books.
By default, constraints are turned off. Seebest practicesandscenariosto learn when to use them.

### What Help Do You Need With Constraints?

- To understand how constraints work, I want to see avideo and examples.
To understand how constraints work, I want to see avideo and examples.
- I need to understand  thedefinitions of the constraintsand whenG3 RMSignores them.
I need to understand  thedefinitions of the constraintsand whenG3 RMSignores them.
- I need to know thestepsto set up either a Standard or an Occupancy-Based constraint.
I need to know thestepsto set up either a Standard or an Occupancy-Based constraint.
- I want to seescenariosfor when to use a constraint.
I want to seescenariosfor when to use a constraint.

## Setup Steps

- Click, thenExternal Data, and thenRate Shopping.
Click, thenExternal Data, and thenRate Shopping.
- Click theCompetitor Settingstab.
Click theCompetitor Settingstab.
- Select theProductto define different constraints for eachindependent product. Linked products use their Base Product's selection.
Select theProductto define different constraints for eachindependent product. Linked products use their Base Product's selection.
- Click theEnable Competitive Market Position Constraintslink. The Competitive Market Position Constraints window opens.
Click theEnable Competitive Market Position Constraintslink. The Competitive Market Position Constraints window opens.
Note: If you use both Standard and Occupancy-Based Constraints,G3 RMSfirst looks for Occupancy-Based, then for Standard constraints. For both types, it first looks for a season, then the default.
- Click theStandardtab.
Click theStandardtab.
- Next toDefault, clickto add a constraint.
Next toDefault, clickto add a constraint.
- Select aRoom Class. The list includes all mapped Room Classes but notUnassignedones.
Select aRoom Class. The list includes all mapped Room Classes but notUnassignedones.
- Select a constraint for each day 
	 of the week. For details, view theirdefinitions.
Select a constraint for each day 
	 of the week. For details, view theirdefinitions.
- Clickto save the constraint. If needed, add constraints for other Room Classes.Note:G3 RMSwarns you if not enough competitors are configured to apply this constraint, seeIgnore Constraints.
Clickto save the constraint. If needed, add constraints for other Room Classes.Note:G3 RMSwarns you if not enough competitors are configured to apply this constraint, seeIgnore Constraints.
- If needed, clicknext toSeasonsto add constraints that differ from the default setup for a specific period.
If needed, clicknext toSeasonsto add constraints that differ from the default setup for a specific period.
- Review and, if needed, editor deleteyour constraints. Add optional Occupancy-Based constraints, or if you're done, clickxto close the window.
Review and, if needed, editor deleteyour constraints. Add optional Occupancy-Based constraints, or if you're done, clickxto close the window.
Use this type when you want to constrain pricing at orbelowa number of competitors and vary that constraint based on the amount of On-Books. Reviewa scenarioor seean example.
- Click theOccupancy-Basedtab.
Click theOccupancy-Basedtab.
- Next toDefaultorSeasons, clickto add a constraint.Note: you can set up only a seasonal constraint, leaving the default empty, or a default with or without seasonal exceptions.
Next toDefaultorSeasons, clickto add a constraint.Note: you can set up only a seasonal constraint, leaving the default empty, or a default with or without seasonal exceptions.
- Select aRoom Class.
Select aRoom Class.
- Select theThresholdsfor each day of the week:Maximum On Books %: enter a percentage up to whichG3 RMSapplies the pricing rule defined in the next row.Note: The On Books values applies to theEffective CapacityThe property's physical capacity minus the out of order rooms.at the property, not the Room Class level.Maximum Market Percentile: enter a number for the percentile of competitor prices that you want the system to price below. For example, for a certain day your competitors' prices are 100, 125, 150, 175, and 200. If you enter 25 as Maximum Market Percentile, the system tries to price at or below 125. With 0 as the percentile, at or below 100. Percentile 100  means no price constraint.
Select theThresholdsfor each day of the week:
- Maximum On Books %: enter a percentage up to whichG3 RMSapplies the pricing rule defined in the next row.Note: The On Books values applies to theEffective CapacityThe property's physical capacity minus the out of order rooms.at the property, not the Room Class level.
Maximum On Books %: enter a percentage up to whichG3 RMSapplies the pricing rule defined in the next row.Note: The On Books values applies to theEffective CapacityThe property's physical capacity minus the out of order rooms.at the property, not the Room Class level.
- Maximum Market Percentile: enter a number for the percentile of competitor prices that you want the system to price below. For example, for a certain day your competitors' prices are 100, 125, 150, 175, and 200. If you enter 25 as Maximum Market Percentile, the system tries to price at or below 125. With 0 as the percentile, at or below 100. Percentile 100  means no price constraint.
Maximum Market Percentile: enter a number for the percentile of competitor prices that you want the system to price below. For example, for a certain day your competitors' prices are 100, 125, 150, 175, and 200. If you enter 25 as Maximum Market Percentile, the system tries to price at or below 125. With 0 as the percentile, at or below 100. Percentile 100  means no price constraint.
- Clickto save the constraint. If needed, add other constraints. For example, adding one for 20% and one for 40% meansG3 RMSapplies the first constraint up to 20% On Books and the second one between 20% and 40% On Books.Note:G3 RMSwarns you if not enough competitors are configured to apply this constraint, seeIgnore Constraintsfor details and all conditions that keep the system from applying a constraint.
Clickto save the constraint. If needed, add other constraints. For example, adding one for 20% and one for 40% meansG3 RMSapplies the first constraint up to 20% On Books and the second one between 20% and 40% On Books.Note:G3 RMSwarns you if not enough competitors are configured to apply this constraint, seeIgnore Constraintsfor details and all conditions that keep the system from applying a constraint.
- If you set up aDefaultand have seasonal exceptions, clicknext toSeasonsto add constraints that differ from the default.
If you set up aDefaultand have seasonal exceptions, clicknext toSeasonsto add constraints that differ from the default.
- Review and, if needed, editor deleteyour constraints. Once you're done, clickxto close the window.
Review and, if needed, editor deleteyour constraints. Once you're done, clickxto close the window.
- After you close the constraints window, you see a newUse in Competitive Market Position Constraintscolumn with all competitors selected. Clear the checkbox for competitors you don't want the system to use. This selection  might differ from the one forUse Rate Shopping Data. For example, you wantG3 RMSto use a competitor's data to influence the demand forecast, but you don't want their aggressive pricing to impact your pricing in theAbove All Competitorsconstraint. In that case, clear that competitor forUse in Competitive Market Position Constraints.
After you close the constraints window, you see a newUse in Competitive Market Position Constraintscolumn with all competitors selected. Clear the checkbox for competitors you don't want the system to use. This selection  might differ from the one forUse Rate Shopping Data. For example, you wantG3 RMSto use a competitor's data to influence the demand forecast, but you don't want their aggressive pricing to impact your pricing in theAbove All Competitorsconstraint. In that case, clear that competitor forUse in Competitive Market Position Constraints.
- ClickSave.
ClickSave.

## Data Details

Following are definitions of the Standard and Occupancy-Based constraints and whenG3 RMSignores them. Note that the system ignores any constraint:
- If the rate shop contains no open rates. Closed rates are not considered in the constraints.
- If the constraint results in pricing options that are below the LRV.
- If the constraint results in pricing options that cause violations of Price Ranking between Room Classes.
- If constraints and pricing setup or overrides conflict. For example, yourCeilingdoesn't allow to price Above All competitors.
If your setup causesG3 RMSto ignore any constraint, you see a warning.If you ignore the warning and continue with the setup, you seean exceptionon the next day.
