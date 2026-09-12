# System Health

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Information-Manager/System-Health.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Information-Manager/System-Health.htm`
- **Ingestion Date:** `2026-09-11 22:14:54`

---

# System Health

If enabled,System Health checks the quality of the data thatG3 RMSreceives 
 each day from theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.and from rate shops. System Health can find issues that prevent the best possible  forecast and decisions.Color-coded results based on a total score provide immediate feedback on the System Health status.

## Steps to Review

- Clickand thenInformation Manager.
- ClickSystem Health. 
	 The system displays each property's Data Quality score 
	 represented by three traffic light colors. Hover 
	 over the icon to see the current data quality score.
Red: A score below 5 warns you that the property has failed numerous checkpoints, or many dates have failed a checkpoint. A red flag can indicate that the property has failed one checkpoint repeatedly.
Yellow: A score from 5 to below 7.5 means that the property has failed a small number of checkpoints, and the 
 number of dates that these checkpoints have failed are limited.
Green: A score between 7.5 and 10
 indicates that the data is acceptable.
- Click a property to view the details in the Data Quality Check Points window on the right. Each of the checkpoints is assigned a certain weight depending on how much it can impact the quality of the systemâs forecast and decisions. Based on each checkpointâs data quality and weighting, the total score and color of the property is calculated. The order of the checkpoints is based on importance, with the most urgent failures displayed on top.

## Data Details

When you select a property, the following information 
	 displays in the right pane:

### Data Quality Checkpoints

The table below defines each data quality checkpoint that is assessed 
 byG3 RMS, describes how the data quality affects system forecasting and 
 decisions, and outlines a most likely resolution step.
