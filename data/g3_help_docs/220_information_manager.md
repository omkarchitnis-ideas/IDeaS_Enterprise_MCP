# Information Manager

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Information-Manager/Information-Manager.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Information-Manager/Information-Manager.htm`
- **Ingestion Date:** `2026-09-11 22:14:35`

---

# Information Manager

Use the Information Manager every day to ensure that you know what the system knows, the system knows what you know, and the system knows the truth. The Information Manager displays specific tasks for you that are prioritized withscoringand that suggest the steps how to resolve them.G3 RMScategorizes tasks intoAlerts,Exceptions,andNotifications.

### What Help Do You Need With the Information Manager?

- I need to learn how tofilterAlerts, Exceptions,and Notifications.
I need to learn how tofilterAlerts, Exceptions,and Notifications.
- I need to understand how to prioritize my tasks based on theScoring.
I need to understand how to prioritize my tasks based on theScoring.
- I need to understandwhich category of tasks I should resolve first.
I need to understandwhich category of tasks I should resolve first.
- I want to learn more about eachAlert,Exception,andNotification.
I want to learn more about eachAlert,Exception,andNotification.

### Counts

Clickand next toInformation Manageryou seethat shows the total number of Alerts, Exceptions,or Notifications that you have not reviewed.G3 RMSdisplays the same number in the top right of the page. Within Information Manager, each sub-tab displays the individual count in parenthesisto specify the total Alerts, Exceptions,or Notifications.
These counts apply to your view: either a single property or, if you are a multi-property user and are viewing a Property Group, all properties within that group.
If your permissions setup gives you Corporate Access, you can also see theShow All Countsbutton. Click it to view the number of Alerts, Exceptions,and Notifications that you have not reviewed for all properties assigned to you, regardless of your defined view. SeeProperty 
 Group Viewsfor more information about viewing multiple properties.

## Filters

Click the filter iconto locate the Alerts, Exceptions,or Notifications that you want to see. The filter options described below change depending on the tab on which you are working.
ClickApplyin the filter window to display a list that matches your criteria and save your criteria. ClickResetto restore the default filters.
If  you are working in aProperty Group View, use the Property filter to locate the items for your selected properties.
Enter partial property titles in the search field to find properties that include those consecutive characters. The default view is all properties.
Unless an Exception orNotification is suspended,G3 RMSchecks the condition that caused it during the next optimization. Status refers to whetherG3 RMSstill found the condition in its optimization. If the condition still exists,G3 RMSkeeps an Active status for aException orNotification.
For example, your property gets a Notification that the occupancy forecast increased by more than the threshold of 20%, and you do not take any action on the Notification. The Notification status is Active. In the next optimization, the occupancy forecast for the same date changes by less than the threshold of 20%. The Notification status changes to Inactive. If the change is outside the threshold again the next day, the Notification becomes Active again.
The default view includes all Active items.
State indicates the actions users have taken for the Alert, Exception,or Notification. The default view is all New, Viewed, Actioned, and Investigated items.
Filter for a specificExceptionorNotification. The default view includes allExceptions orNotifications with a status of Active.
The date filter is Available forExceptions andNotifications. This selection filters for the occupancy dates for which the item applies. The default view includes all Occupancy Dates with Active items.
Use this to filter Alerts, Exceptions, and Notifications by the date when they were first triggered.
Use this filter to view Notifications only for the selected days of week.

## Scoring

Information Manager prioritizes your tasks by assigning a score that represents the urgency. Color coding indicates the severity of the issue.

### Understand Which Task Should Be Resolved First

In general, Alerts score higher thanExceptions andNotifications because their possible negative impact can be higher. Resolve tasks by the severity of the issue, starting with the Alerts that have a score of 200+ first.
WhenG3 RMSfirst creates the task, it assigns a score to it.G3 RMSscores Alerts higher thanExceptions, which it scores higher thanNotifications. Alerts score higher because they are more directly related to potential higher revenue loss, and Notifications score lower because they only inform you of change that the system has made.
Within each area, scoring varies. Scoring 
	 depends on a few factors:
- The age of the information.
- The frequency 
 of occurrence. For example, the score increases if the same Alert remains unresolved two 
 days in a row.
- The impact of the Alert on the system. For example, a processing Alert has a higher base score than a setup Alert.
- The distance 
 of the condition from the threshold that is set up. For example, a Notification for an ADR change that 
 is four times larger than the threshold gets a higher score 
 than one that is only twice as large.
The system records when you 
 view the Alert or take an action, either by clicking on a link to resolve it or selecting a checkbox to indicate that you completed a task outside ofG3 RMS. Taking an action does not immediately change the score.G3 RMSchecks again during its next nightly processing (or intraday processing, only for the Unassigned Market Segment and Unassigned Room Type Alerts). If the condition that triggered 
 the Alert is gone,G3 RMSsets the score to zero and considers 
 the Alert resolved.
If 
 the condition reoccurs, the Alert remains active.G3 RMSincrements 
 the score for each day that the issue is not resolved, just as the possible 
 negative impact increases with each day the Alert is not resolved.  For example, if the starting score for an Alert is 200,G3 RMSincrements that score by 20 for each day that the issue remains 
 unresolved.
The 
 system records your action on the Exception and sets the score to zero, either when you select one of the links or checkboxes in theHow do I action the Exceptionsection.
G3 RMSchecks the situation again during its next nightly optimization. 
If the condition that triggered the Exception reoccurs,G3 RMScreates the Exception again with the same starting score.
If 
 you don't take action, the possible negative revenue impact of the Exception 
 might increase.G3 RMSincrements the score for each 
 day that the condition continues to exist. If you take no action, but the condition 
 does not reoccur,G3 RMSdecreases the score each day, and the Exception 
  disappears once the score drops below one.
If the date of an Exception passed before you could review it,G3 RMSkeeps the Exception 
 active to make sure you have a chance to review it. However, it decreases 
 the score for each passing day to show the decreasing importance.
Starting 
 scores also depend on the distance of the condition from the threshold that is set up. For example, an ADR forecast change that is four times larger than the 
 threshold gets a higher score than one that is only twice as large.
If 
 you choose any of the options to action the Notification,G3 RMSrecords the step and sets 
 the score to zero. With all of the action steps  except suspending the Notification,G3 RMSchecks the situation again during the next nightly optimization. If the condition that triggered the 
	 Notification reoccurs,G3 RMScreates a new Notification with the same 
	 starting score.
If you do not take any action, one of the following occurs:
- G3 RMSincrements the score for each day that the condition continues to 
	 exist.
- If the 
	 condition does not reoccur,G3 RMSdecreases the score each day. The Notification disappears once the score drops below one.
For 
 example, assume the defined threshold for a Forecast Change is more than 
 10% up or down, and yesterday a forecast change of 11% triggered a Notification 
 with a starting score of 100 for an occupancy date. If you took no action 
 yesterday, and today you see another change in forecast of more than 10% 
 up or down, the score increases. However, if the forecast change today 
 was below 10%, the score decreases.
If you are viewing Information Manager for in a multi-property view,G3 RMSsets priorities by the individual Alert. Information Manager 
	 shows information across your entire portfolio so that you can identify 
	 the property that needs the most attention.
