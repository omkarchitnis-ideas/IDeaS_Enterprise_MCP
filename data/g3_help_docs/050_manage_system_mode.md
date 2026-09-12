# Manage System Mode

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Optimization/Decision-Configuration-Manage-System-Mode.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Optimization/Decision-Configuration-Manage-System-Mode.htm`
- **Ingestion Date:** `2026-09-11 22:12:41`

---

# Manage System Mode

Use the Manage System Mode tab in Decision Configuration during  a property'sG3 RMSimplementation to switch fromDecision CreationA one-way status when the RMS receives data from the reservation system, creates forecasts and outputs (like pricing), but does not send outputs to the selling system.toDecision DeliveryA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system.. This means that your property goes from  a one-way communication between yourselling systemandG3 RMSto a two-way communication.
You can also view the length of yourForecastThe Forecast window defines the number of days for which the RMS forecasts unconstrained demand. It also defines the window for which you can run Group Pricing evaluations. The default Forecast Window is 365 days, but it can be set to a maximum of 730 days. The Forecast Window usually matches the length of the Optimization Window.,OptimizationThe number of days for which the RMS produces outputs (like pricing) and a constrained occupancy forecast. You can view the optimized outputs and occupancy forecast for the Optimization Window, but the system only sends outputs for the Upload Window. The Optimization Window usually matches and can't be longer than the Forecast Window., and Upload Windows, seeData Detailsfor more information.  SeeRequest Full Uploadfor the other tab in Decision Configuration.
The Manage System Mode tab is enabled only for large enterprises to manage   switching from Decision Creation to Decision Delivery duringG3 RMSroll-out. Contact your IDeaS representative if your company is interested in using it.

## Steps to Manage the System Mode

- Click, thenDecisions, and thenDecision 
	 Configuration.
Click, thenDecisions, and thenDecision 
	 Configuration.
- Click theManage System Modetab, if not already open.
Click theManage System Modetab, if not already open.
Not all of the following steps might apply to your property.
- Select the System Mode that you want to switch to. The current mode shows asActive:Decision Delivery:Select this option if your property is in the initialG3 RMSimplementation or if you temporarily switched it back to Decision Creation. Decision Delivery  means that you want the system to start sending decisions to yourselling system. Review the Selling System Information table on the right side for the details of which decision type theselling systemreceives.Steps to complete before you select Decision Delivery.Investigateyour forecast and decisions to ensure they match your expectations.The first upload includes all decisions for 
		 the number of days specified in theUpload WindowThe Upload Window is the number of days for which the RMS sends controls including pricing, overbooking and LRV, to your selling systems. It also defines the period for which you can upload changed controls. The Upload Window is limited by the inventory window of your reservation system, so it is the number of days for which your PMS or CRS can accept reservations and controls. Typically, that limit is 365 days, but some reservation systems allow up to 396 days. The window also depends on your IDeaS subscription and can't be longer than the Optimization Window. Contact your IDeaS representative to change your Upload Window.. After that,G3 RMSsends onlydifferential decisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case..Ensure that 
				 yourselling systemis ready to accept decisions fromG3 RMS.If you have any manual restrictions in yourselling system, you must remove them after the first nightly processing following the switch to Decision Delivery mode. That avoids conflicts with theG3 RMSdecisions.
Select the System Mode that you want to switch to. The current mode shows asActive:
- Decision Delivery:Select this option if your property is in the initialG3 RMSimplementation or if you temporarily switched it back to Decision Creation. Decision Delivery  means that you want the system to start sending decisions to yourselling system. Review the Selling System Information table on the right side for the details of which decision type theselling systemreceives.Steps to complete before you select Decision Delivery.Investigateyour forecast and decisions to ensure they match your expectations.The first upload includes all decisions for 
		 the number of days specified in theUpload WindowThe Upload Window is the number of days for which the RMS sends controls including pricing, overbooking and LRV, to your selling systems. It also defines the period for which you can upload changed controls. The Upload Window is limited by the inventory window of your reservation system, so it is the number of days for which your PMS or CRS can accept reservations and controls. Typically, that limit is 365 days, but some reservation systems allow up to 396 days. The window also depends on your IDeaS subscription and can't be longer than the Optimization Window. Contact your IDeaS representative to change your Upload Window.. After that,G3 RMSsends onlydifferential decisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case..Ensure that 
				 yourselling systemis ready to accept decisions fromG3 RMS.If you have any manual restrictions in yourselling system, you must remove them after the first nightly processing following the switch to Decision Delivery mode. That avoids conflicts with theG3 RMSdecisions.
Decision Delivery:Select this option if your property is in the initialG3 RMSimplementation or if you temporarily switched it back to Decision Creation. Decision Delivery  means that you want the system to start sending decisions to yourselling system. Review the Selling System Information table on the right side for the details of which decision type theselling systemreceives.
- Investigateyour forecast and decisions to ensure they match your expectations.The first upload includes all decisions for 
		 the number of days specified in theUpload WindowThe Upload Window is the number of days for which the RMS sends controls including pricing, overbooking and LRV, to your selling systems. It also defines the period for which you can upload changed controls. The Upload Window is limited by the inventory window of your reservation system, so it is the number of days for which your PMS or CRS can accept reservations and controls. Typically, that limit is 365 days, but some reservation systems allow up to 396 days. The window also depends on your IDeaS subscription and can't be longer than the Optimization Window. Contact your IDeaS representative to change your Upload Window.. After that,G3 RMSsends onlydifferential decisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case..
Investigateyour forecast and decisions to ensure they match your expectations.
The first upload includes all decisions for 
		 the number of days specified in theUpload WindowThe Upload Window is the number of days for which the RMS sends controls including pricing, overbooking and LRV, to your selling systems. It also defines the period for which you can upload changed controls. The Upload Window is limited by the inventory window of your reservation system, so it is the number of days for which your PMS or CRS can accept reservations and controls. Typically, that limit is 365 days, but some reservation systems allow up to 396 days. The window also depends on your IDeaS subscription and can't be longer than the Optimization Window. Contact your IDeaS representative to change your Upload Window.. After that,G3 RMSsends onlydifferential decisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case..
- Ensure that 
				 yourselling systemis ready to accept decisions fromG3 RMS.If you have any manual restrictions in yourselling system, you must remove them after the first nightly processing following the switch to Decision Delivery mode. That avoids conflicts with theG3 RMSdecisions.
Ensure that 
				 yourselling systemis ready to accept decisions fromG3 RMS.
If you have any manual restrictions in yourselling system, you must remove them after the first nightly processing following the switch to Decision Delivery mode. That avoids conflicts with theG3 RMSdecisions.
- Decision Creationin the rare scenario that your property is in Decision Delivery and you need to  stop all decision uploads.A switch to Decision Creation does not reverse previously uploaded decisions. You must now manually update all the decisions in yourselling systemto keep them current.
Decision Creationin the rare scenario that your property is in Decision Delivery and you need to  stop all decision uploads.
A switch to Decision Creation does not reverse previously uploaded decisions. You must now manually update all the decisions in yourselling systemto keep them current.
- Switch to the new mode using one of two options:Click toSwitch Now. The status changes to Pending.For  Decision Delivery only, click toSchedule for later. Select a date and time for the switch.At that timeG3 RMSswitches modes  and sends an Alert, System Mode Changed to Decision Delivery.Until then you can change the time of when Decision Delivery begins.
Switch to the new mode using one of two options:
- Click toSwitch Now. The status changes to Pending.
Click toSwitch Now. The status changes to Pending.
- For  Decision Delivery only, click toSchedule for later. Select a date and time for the switch.At that timeG3 RMSswitches modes  and sends an Alert, System Mode Changed to Decision Delivery.Until then you can change the time of when Decision Delivery begins.
For  Decision Delivery only, click toSchedule for later. Select a date and time for the switch.
- At that timeG3 RMSswitches modes  and sends an Alert, System Mode Changed to Decision Delivery.
At that timeG3 RMSswitches modes  and sends an Alert, System Mode Changed to Decision Delivery.
- Until then you can change the time of when Decision Delivery begins.
Until then you can change the time of when Decision Delivery begins.
- You must enterNotesbefore you can save the change. This helps when you review previous System Mode changes.
You must enterNotesbefore you can save the change. This helps when you review previous System Mode changes.
- UnderSettings, review the Forecast, Optimization, and Upload Window for your property. Of these three  you can only change theUpload Windowwhich represents the maximum number of days for whichG3 RMSsends decisions. SeeData Detailsfor more information.
UnderSettings, review the Forecast, Optimization, and Upload Window for your property. Of these three  you can only change theUpload Windowwhich represents the maximum number of days for whichG3 RMSsends decisions. SeeData Detailsfor more information.
- ClickSave.The System Mode Change - Important Information window opens.
ClickSave.The System Mode Change - Important Information window opens.
- Review and, if you haven't already, complete the required steps. Then, clickAccept.Decision Configuration 
 changes go into effect with the next nightly processing.If you switched to Decision Delivery,  go into yourselling systemto verify that the  decisions have been applied as expected.
Review and, if you haven't already, complete the required steps. Then, clickAccept.
- Decision Configuration 
 changes go into effect with the next nightly processing.
Decision Configuration 
 changes go into effect with the next nightly processing.
- If you switched to Decision Delivery,  go into yourselling systemto verify that the  decisions have been applied as expected.
If you switched to Decision Delivery,  go into yourselling systemto verify that the  decisions have been applied as expected.
- Clickin the top right of the page.The History of Changes window opens.
Clickin the top right of the page.The History of Changes window opens.
- Review the previous changes, like the name of the property, who made the change and the Notes they entered.
Review the previous changes, like the name of the property, who made the change and the Notes they entered.
- ClickXorCloseto return to the Manage System Mode tab.
ClickXorCloseto return to the Manage System Mode tab.

## Data Details

### System Mode

### Selling System Information

The table shows to which selling systemsG3 RMSsends decisions and the type of decision. The selling systems and decision types differ for each client, following are the main decision types and some examples.
