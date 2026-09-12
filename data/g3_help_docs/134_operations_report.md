# Operations Report

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Operations-Report.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Operations-Report.htm`
- **Ingestion Date:** `2026-09-11 22:13:38`

---

# Operations Report

Generate orschedulethe Operations Report to help you with scheduling of front desk, restaurant, and other hotel operations. You can view on books and a forecast of arrivals and departures to get an understanding of the breakdown between arrivals, departures, and stay-thrus at a property, as well as the additional business to expect for an arrival date.

### How the Operations Forecast Differs from the Occupancy Forecast

The forecasted occupancy in the Operations report might differ from theOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details).in other reports and dashboards. Here's why:
- G3 RMSdetermines the Occupancy Forecast through a complex optimization process. It completes the Operations Forecasts after the optimization process, not as part of it, and includes data inputs calculated during the optimization process, like expected demand to come.
- To calculate arrival and departure forecasts,G3 RMSuses both on-books counts and the Occupancy Forecast in conjunction with length of stay patterns. This estimation does not guarantee that these values reconcile with the Occupancy Forecast in all cases.
- When the forecast occupancy for a future arrival date is below the on-books count for that arrival date,G3 RMSuses the on books values as the forecast for arrivals and departures.
- The Operations Forecast doesn't consider unusual patterns due to Special Events (outside of On Books) or group blocks that have not recorded all pickup on blocks.

## Reporting Steps

There are no filter criteria for the Operations Report. The report always displays information for theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.to the System Date + 21 days.
- Click, thenReports, and thenOperations.
- ClickGenerate.
- Click the export iconif you want to export the data to a spreadsheet.
SeeExporting and Printing Reportsfor more information about managing report downloads 
		in your browser.

## Data Details

The Operations Report provides the following data:
