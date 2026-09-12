# Channel Settings

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping-Channel.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping-Channel.htm`
- **Ingestion Date:** `2026-09-11 22:12:47`

---

# Channel Settings

If the use of publicly available competitor pricing datais enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.,G3 RMSuses all channels to measure your competitors' impact on your demand and your pricing, for example, from Expedia or the Global Distribution System (GDS). Use the Channel Settings tab to manage how channels display, how they're used for Competitive Market Position Constraints, and, if needed, to ignore a channel.
For an overview, reviewall steps and the benefits of Rate Shopping setup.

### Default Channel Settings

Default Channel Settings serve two purposes:
- For all properties the default controls the channel whose rate shopping data displays on calendars and in reports 
	 where only a single competitive rate can be displayed.
- If you are usingCompetitive Market Position Constraints,G3 RMSonly considers competitive rate information 
	 from the channel that you select here.
If needed, vary the default channel by day 
	 of the week. For example, some competitors might sell via Expedia only on the weekends. In that case, you might select the GDS for weekdays and Expedia for weekends.If you have rate shopping data for products other than the primary priced, you can vary the default channel by product.
Click theAdd Seasonlink if you want to override the default channel for a few exceptional days in the year. For example, the default channel might not provide reliable rate shopping data during a season because some competitors limit inventory to only one channel over a high demand period. The link changes toUpdate Seasonafter you create seasons.

## Setup Steps

During the initial setup and for most properties,G3 RMSautomatically selects all channels and sets the first channel in the rate shopping files as the default channel. If needed, change the selections.

### Setting Up Channel Display Settings

- Click, thenExternal Data, and thenRate Shopping.
- Click theChannel Settingstab.
- Complete or review the setup, like the Display Name. See Data Details for more information.
- ClickSave.
- If needed, selectIgnore Channel, to ignore competitor pricing data from a specific channel. For example, when your shopping data includes a channel with prices that are not in parity with other channels.The following options to ignore display:Click to adda channel.Select theChannel Name. You can ignore any channel except the Default Channel.If needed, change for which Day of Week (DOW) the system ignores the data.Click the note iconto add aNoteand enter an explanation for why you ignored the data.Click to savethe Ignore Channel changes.
- Click to adda channel.
- Select theChannel Name. You can ignore any channel except the Default Channel.
- If needed, change for which Day of Week (DOW) the system ignores the data.
- Click the note iconto add aNoteand enter an explanation for why you ignored the data.
- Click to savethe Ignore Channel changes.
- Click Export to Excelto download your settings. The export includes sheets for each rate shopping tab.

### Setting Up Default Channels

If you clickSuggestin theRoom Class Mapping tab,G3 RMSselects the first channel from the shopping data as the default Display Channel. Use these steps to review and, if needed, change the setup.
- Click, thenExternal Data, and thenRate Shopping.
- Click theChannel Settingstab.
- If available, select theProductfor which you define the default channel.
- Under Default Channel Settings, review or select a channel for eachDay of Week.
- ClickSave.

### Setting Up Default Channels by Season

- After setting the default channel by day of week, clickAdd Season.
- Enter a descriptive label for the period in theNamefield.
- Select aStart DateandEnd Datefor the period. The date ranges for seasons cannot overlap.
- Select a default channel for eachDay of Weekduring the period.
- Click the add icon. The season is added to the table.
- Repeat the steps, as needed, to add additional seasons.
- ClickSave.

## Data Details

This information is available in the table of seasons:
