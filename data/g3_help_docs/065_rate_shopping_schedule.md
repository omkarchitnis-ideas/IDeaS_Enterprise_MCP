# Rate Shopping Schedule

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping-Schedule.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping-Schedule.htm`
- **Ingestion Date:** `2026-09-11 22:12:51`

---

# Rate Shopping Schedule

Use Rate Shopping Schedule to ensure thatG3 RMSuses only the current pricing of your competitors to improve  its outputs like pricing  (ifmarket data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.). Define the number of days thatG3 RMSuses the publicly available competitor data and when the system should ignore the data.
If the data does not arrive as per the schedule, you get anAlert. For an overview, reviewall steps and the benefits of Rate Shopping setup.
WithRate Data AdvantageG3 RMSgets rate shopping data at many more levels than with the Standard subscription and only considers the data as stale if it didn't receive competitor prices foranylevel for the selected arrival date ranges. If   the system received data for some but not all levels and stopped using the old data only for the missing levels, you see aData Qualitywarning.

## Setup Steps

Complete the steps for each rate shopping window:
- Click, thenExternal Data, and thenRate Shopping.
- Click theRate Shopping Scheduletab.
- Complete the following options:
- Click the add iconto add a row to the table with the Rate Shopping Window, Frequency of Delivery, and days after which rate shopping data is stale and not used.
- Continue to add rows until all rate shopping windows are recorded.
- ClickSave.
- Click Export to Excelto download your settings. The export includes sheets for each rate shopping tab.
Click the delete iconto remove any instance of the Rate Shopping Schedule. If you need to change an existing schedule, first delete it, then create a new one.

## Best Practices

### Set up the Schedule 
for Each Rate Shopping Window

In the below example, you set up two rate shops. The first, daily rate shop sends rate shopping data for 
 the next 90 days. For this immediate business, you want to stop 
 using the data three days after the last file was received. For the next 180 days, it is seven days after the last file. See the next best practice for a scenario.

### Verify Your Setup in Competitor Details

You can verify if youâre receiving data according to your schedule configuration  on theCompetitor Detailsscreen. Let's say that today is January 9, and you are looking at the rate shopping data for June 1, which means the setup for the 180 day window applies. The Updated On column shows  January 1. That means that the expected update on January 8 was missed, and in the last nightly optimization the system/the RMSno longer used the old data of the rate shop because it was older than 7 days.

### Be Aware of the Default Window

If you do not define rate shopping windows in the Rate Shopping Schedule, 
 the number of days after which data is no longer used falls back to the default 
 value of 30 days.
