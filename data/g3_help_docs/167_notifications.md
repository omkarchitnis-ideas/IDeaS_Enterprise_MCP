# Notifications

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Information-Manager/Notifications.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Information-Manager/Notifications.htm`
- **Ingestion Date:** `2026-09-11 22:14:00`

---

# Notifications

Notifications inform you when key system values change or reach a specific value. For example, when pricing changes by a large amount or when the Occupancy Forecast reaches 90%. You define Notifications to ensure that 
 you know what the system knows.

### What Help Do You Need With Notifications?

- I want to see theBest Practicesfor setting up and monitoring Notifications.
- I want to watch avideoor see thestepsto setup Notifications.
- I need to learn about thetwo categories, business change and specific value.
- I want to see thedetailsfor each Notification that I can set up.
- I need to understand thescoringfor Notifications.

### Two Categories of When You Get Notified

#### When the Business Changes

G3 RMSmeasures the change between the current and the previous results and triggers a Notification if the change meets your defined threshold.For example, that the Occupancy Forecast increased  by more than 5% or that Overbooking at the Master Class level increased by more than 5 rooms. You have two options for when the system measures the change:
- Change From Last Optimization: The 
		 system compares the optimization results from the last processing to the results from the previous processing.  These changes can be between anytype of processing.
- Change From Last Nightly Optimization: The 
		 system compares the optimization results from last night's processingto the results from the previous nightly processing.Even if the property subscribes to optional intraday processing, this Notification is only sent if a change meets your threshold after the nightly processing.

#### When Data Reaches a Specific Value

G3 RMSchecks if a property value meets your defined condition. For example, that a competitor's price is at or below $200 or that property overbooking is at or above 15 rooms. You have two options for when the system checks values:
- Value as of Last Optimization: The property value met your defined condition after the optimization results from the last processing. The change values can occur between anytype of processing.
- Value as of Last Nightly Optimization: The property value met your defined condition after the optimization results from the last nightly processing.Even if the property subscribes to optional intraday processing, this Notification is only sent if a change meets your threshold after the nightly processing.

## Setup Steps

Your browser does not support the video tag.
- Clickand thenInformation Manager.
- ClickNotifications.
- Click the configuration icon. The Notification Configuration window opens.
- Click the add iconto start the 
	 setup wizard.
- In the Property step, selectProperties(if the Notifications are 
	 for individual properties) orProperty Groups(if the Notifications are for groups of properties that you set up).Note: When you set up a Notification for aProperty Group, the Notification is applied to all properties associated with that Group, even if the property is added to it later.
- Locate the Properties or Property Group in the left pane:Enter a full or partial name in the search field to filter for names that contain those characters.Click a Property or Property Group to select it.PressCtrlorShift+ click to select multiple properties.
- Enter a full or partial name in the search field to filter for names that contain those characters.
- Click a Property or Property Group to select it.
- PressCtrlorShift+ click to select multiple properties.
- Click>to add the selected properties or Property Groups to the Selected for Notification pane, or click>>to add all the properties or groups. The properties that you
	 add will receive the Notifications that you 
	 select in the next steps in the wizard.
- ClickNext.
- In the Notification Details step, select theTypeof Notification.See the short summary of these types in theOverview, or seeData Detailsfor descriptions of each Notification.
- Select the desired options forSub-Type,Notification Level, andNotification Sub-Level. The options vary by the selected Type.
- ClickNext.
- In the Condition step, select the conditions under whichG3 RMSwill send a Notification. Your options vary, depending on your selections in Notification Details:Select if the amount of change or specific valueIncreased by _ or more,Decreased by _ or more, orIncreased or decreased by _ or morethan the threshold that you set up.Enter the threshold value in the open field.Select if the change or specific value applies to the number ofRooms, aPercent, aPrice Pointor aCurrencyvalue.
- Select if the amount of change or specific valueIncreased by _ or more,Decreased by _ or more, orIncreased or decreased by _ or morethan the threshold that you set up.
- Enter the threshold value in the open field.
- Select if the change or specific value applies to the number ofRooms, aPercent, aPrice Pointor aCurrencyvalue.
- ClickNext.
- In the Monitoring Window step, select the desiredStart DateandEnd Datefor the 
	 period in whichG3 RMSwill monitor these changes, within the forecast window:Click the default date.Complete one of the following options:Enter a date in theSelectionfield.SelectSpecific Datefrom the menu. Click the arrows icons to navigate between months or years. Click the appropriate date in the calendar.SelectRolling Datefrom the menu. SelectTodayor choose to offset today by a defined number of days by selectingToday +. Enter the number of offset days in the selection field.ClickApply.
- Click the default date.
- Complete one of the following options:Enter a date in theSelectionfield.SelectSpecific Datefrom the menu. Click the arrows icons to navigate between months or years. Click the appropriate date in the calendar.SelectRolling Datefrom the menu. SelectTodayor choose to offset today by a defined number of days by selectingToday +. Enter the number of offset days in the selection field.
- Enter a date in theSelectionfield.
- SelectSpecific Datefrom the menu. Click the arrows icons to navigate between months or years. Click the appropriate date in the calendar.
- SelectRolling Datefrom the menu. SelectTodayor choose to offset today by a defined number of days by selectingToday +. Enter the number of offset days in the selection field.
- ClickApply.
- ClickFinish. 
	 The Notification Type that you created displays in the Notification Configuration window, 
	 with the change parameters that you set up for it.
G3 RMSseparates the steps to resolve 
 Notifications 
 into "Investigation" and "Action" options.G3 RMSchanges the score only if you take an action, even if the action is to make no change.
- If needed, click the filter iconto locate the Notifications to resolve.  SeeFiltersfor a description of options and results displayed when using filters.
- Filter 
 the results further by typing partial titles in theSearch for Notifications ...field. 
 For example, type "Overbooking" to find Notifications with "Overbooking" in the title.  Click the refresh iconto clear the filter.
- Select the Notifications to resolve:Select a Notification.Select the checkboxes in the right column if you want to action multiple Notifications together. For example, multiple Forecast Change Notifications for one date but different Room Classes all have the same cause. Selecting multiple Notifications limits the available actions that you can take.
- Select a Notification.
- Select the checkboxes in the right column if you want to action multiple Notifications together. For example, multiple Forecast Change Notifications for one date but different Room Classes all have the same cause. Selecting multiple Notifications limits the available actions that you can take.
- Investigate and take action, using the details in the right pane and the instructions that display belowHow do I investigate the NotificationorHow 
	 do I action the Notification.Click the blue linked text.G3 RMSopens a new 
	 tab or window and goes to the appropriate page where you take the necessary steps to investigate or resolve the issue. This option is not available if you selected multiple Notifications.Select the checkbox toMake no changes to the systemif you choose to continue monitoring  the occupancy date.Select the checkbox toSuspend the notification on this dateif you no longer wantG3 RMSto monitor the same condition for this occupancy date. For example, an arrival date outside of the main booking window may experience many changes to its forecast, so you may not want to monitor this date at this time. In this case, select the checkbox to suspend the Notification. As the date approaches, you can clear the checkbox, andG3 RMSwill monitor the occupancy date for you again.For the Booking Pace Notification, you can also selectSuspend and monitor, resume if the difference to the threshold increases. For details, review itsDescription.
- Click the blue linked text.G3 RMSopens a new 
	 tab or window and goes to the appropriate page where you take the necessary steps to investigate or resolve the issue. This option is not available if you selected multiple Notifications.
- Select the checkbox toMake no changes to the systemif you choose to continue monitoring  the occupancy date.
- Select the checkbox toSuspend the notification on this dateif you no longer wantG3 RMSto monitor the same condition for this occupancy date. For example, an arrival date outside of the main booking window may experience many changes to its forecast, so you may not want to monitor this date at this time. In this case, select the checkbox to suspend the Notification. As the date approaches, you can clear the checkbox, andG3 RMSwill monitor the occupancy date for you again.
- For the Booking Pace Notification, you can also selectSuspend and monitor, resume if the difference to the threshold increases. For details, review itsDescription.
- After you investigate or resolve the issue, return to 
	the Notifications page.G3 RMSrecords your actions in Notification History.
- Add a note regarding the resolution by clicking the 
	 note iconin the right pane.
When you create and save a Notification, it is enabled. You 
 can temporarily disable a Notification and re-enable it to use another 
 time instead of recreating it.
- Click the configuration icon. The Notification Configuration window opens.
- Locate the Notification to be disabled. If needed, click the filter iconto filter for a property or Notification type.
- Select theDisablecheckbox for the Notification to be disabled. A confirmation window displays.
- ClickYesto disable the Notification and delete all active instances of it.
To re-enable a Notification, clear theDisablecheckbox.
- Click the configuration icon. The Notification Configuration window opens.
- Locate the Notification to be edited. If needed, click the filter iconto filter for a property or Notification type
- Select the Notification to edit. A Notification Details pane opens with details about the Notification.
- ClickEditon the bottom right corner of the window. The Notification Details become available for editing.
- Change theNotification Details, theConditionthat defines whenG3 RMSwill trigger the Notification, or theMonitoring Window.
- ClickSave.
- Click the configuration icon. The Notification Configuration window opens.
- Locate the Notification to be deleted. If needed, click the filter iconto filter for a property or Notification type
- Select the Notification to delete. A Notification Details pane opens with details about the Notification.
- Click the delete icon.
- ClickYesto confirm the deletion.

## Notification Details

The table below provides details about each Notification that you can set up:

## Best Practices

The number of 
	 Notifications that you receive is dependent on how you set them up and the amount 
	 of volatility in your booking data. If you consistently receive too few or too many Notifications, review your Notification setup.
G3 RMSregularlyupdates the demand modelsthat it uses to calculate demand. This can trigger changes to forecasts and decision and, therefore, new Notifications. These updates of the demand models also happen after some changes thattrigger a Sync. For example, when you change pastSpecial Eventsorchange market segment attributes.
When the system receives rate shopping data for an arrival date for the first time (andif market data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.), it might change its forecast and decisions for that date,  triggering Notifications.
Uncertainty and decisions may change as an arrival date approaches. When you enter your main booking window,G3 RMSreceives more booking data, which reduces its forecasting uncertainty and may cause more changes to the forecast, potentially triggering more Notifications.
You don't need to act on Notifications becauseG3 RMSalready acted. For example, if the Occupancy Forecast change meets or exceeds the threshold that you set up, you don't need to change pricing. The system already optimized the remaining unconstrained demand and decided if decisions need to change. You can review Notifications daily, but they  are for your information only and, therefore, are less important than Alerts and Exceptions.
Notifications help the system know what you know. Notifications may point you to a situation where you need to share your knowledge with the system. For example, investigating a change in the overbooking decision may lead you to realize that you need to override a group's wash.
Often, just viewing the Notification details may provide you with enough information to know what the system knows, and no further investigation may be necessary. When you aren't sure if you need to share something with the system or when you question a new Occupancy Forecast or decision, click one of the links to investigate the Notification in the Notification details. Theninvestigate forecastand decisions.
If 
	 youinvestigated forecastand decisions yesterday, and you interacted 
	 withG3 RMSby, for example, placingDemand and Washoverrides, you 
	 should feel comfortable that Notifications are due to your changes
	 and spend little time investigating.
