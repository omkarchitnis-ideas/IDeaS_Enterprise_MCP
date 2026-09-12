# Best Practices for Managing Special Events

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Special-Events/BP-Managing-Special-Events.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Special-Events/BP-Managing-Special-Events.htm`
- **Ingestion Date:** `2026-09-11 22:14:50`

---

# Best Practices for Managing Special Events

## Understanding Special Events inthe RMS

The RMSuses some or all of the following criteria to differentiate Special Events from normal periods. Use this criteria when you consider whether to enter days as Special Events:
- Booking Pace: Bookings for Special Events are made much earlier or much later than normal.
- Business Mix: Special Events change the business mix, as one Forecast Group may have much higher or much lower volume than its normal booking patterns.
- Occupancy: Occupancy may be impacted, as the occupancy for a Special Event date may be much higher or much lower than normal.
- Room Revenue: Special Events typically impact room revenue.
Note:The RMSdoes not consider unusual periods of group activity that are not matched by unusual transient patterns as Special Events because it already considers each group individually.
Special Events should be "special," not the norm. We recommend that a maximum of 20% of days in a year be marked as Special Events, including pre- and post-event dates. This helps the system achieve the best possible  forecasts.
There's no impact on the system from Special Events marked as Informational Use Only, but too many informational events may create clutter on dashboards and reports that makes it difficult to review the system-relevant Special Events.
Always enter a Special Event when you know that the transient patterns differ from normal patterns. Althoughthe RMSlooks for outliers and may detect an obvious outlier (like the snow storm in the example above), real outliers are rarely obvious in statistical terms and are not easy for the system to detect. We recommend that you work as a team: you enter Special Events when you expect unusual transient demand patterns, andthe RMSanalyzes and decides how to handle them.
Special Events helpthe RMSimprove forecasts in two ways:
- The RMSremoves the Special Events from the data it uses to forecast "normal" transient demand. For example, a bad storm on one Saturday means that day's transient patterns and occupancy are very different from normal Saturdays. When the system looks for day-of-week patterns to forecast normal transient demand for upcoming Saturdays, it ignores the data from the Special Event Saturday that is the outlier. It continues to forecast future Saturdays using normal transient business patterns.
- For repeat events,the RMSuses the past to forecast the future. For example, you add a Special Event with past and future instances for an annual convention that impacts transient demand. In that case, the system uses an average of the transient demand of all past instances of the convention to forecast its future instances.
The RMSlooks for Special Events on its own and reviews the ones that you entered. The system analyzes the demand patterns for those Special Events and determines if the transient patterns are statistically different from normal ones. If they are different, the system removes the dates from the data that it uses to forecast normal transient demand. In most cases,the RMSdoes not have enough information to identify a Special Event until it has passed.
Whenthe RMSreviews a Special Event that you entered, it may find that there is no or little variation from normal transient patterns during those dates. For example, the system may decide that the dates display normal patterns, except there is a 20% increase over normal demand. In that case,the RMSremoves the 20% increase and continues to use the Special Event data to forecast normal transient demand.
When you add or remove past instances of a Special Event,the RMSchecks all its demand models to ensure they are current. That might cause large changes in demand forecasts and decisions that seem disproportionate. For example, you add a single Special Event. After the next optimization, you notice large changes in the demand forecast. The changes apply to the entire forecast window.
If that is the case,the RMSlikely found other changes in patterns of its demand models that are not related to the Special Event change. For example, an increase in business volume in a Forecast Group. Without the Special Event change,the RMSwould have found that increase in its next regular check of demand models. SeeSelf-Learningfor more details.

## Managing Special Event Data

Pre- and post-event dates helpthe RMSunderstand the impact of the Special Event on surrounding days and are distinct from the actual event days.G3 RMSremoves these dates from the data it uses to forecast "normal" transient demand.
For example, a city-wide conference from Monday to Friday may have the Sunday as a pre-event date because some guests arrive early for preparation and set up. The same event may have Friday and Saturday as post-event dates that impact transient business because many guests stay longer for shopping and sightseeing.
To forecast future instances of repeat events,the RMSchooses the best fit from over 100 demand models. Depending on the patterns, it may use a different demand model for pre- and post-events days, or it may use the same model.
If Special Events occur on a definite date or follow a monthly recurring day of the week pattern, select theRecurrencecheckbox when you set up the event. Define a repeat event's date pattern, andthe RMScreates multiple instances based on the date or monthly recurring day on which the Special Event occurs.
For recurring events  without a consistent date or day pattern, define each past and future instance of the Special Event individually. However, always include past instances, even if they donât follow a pattern.
The transient demand, the booking pace, and the wash are all based on all available past instances. Thus, ensure that the all the instances are  good references, seeDelete Unusual Instances.
Data retentionlimits the past instances to a maximum of three years.
All instances of a repeat event with similar demand should have the same number of days, which providethe RMSoptimal reference points when forecasting future events. This includes pre-event, main event, and post-event days.

#### Scenario When Dates Do Not Match

There may be valid scenarios where the event dates with similar demand don't match exactly. When these differences exist, the forecasting logic may provide unexpected results. We recommend you review the forecast for the impacted dates after the next optimization to ensure the results meet your expectations.
For example, below is howthe RMShandles an event where the number of days in the event do not match.
The illustration below shows howthe RMSaligns the event dates of the past and future instance for forecasting purposes. Orange dates are pre-event and post-event days. Green dates are event days.
What if the dates were reversed, so the past instance had three peak nights (4, 5 and 6 July) and the future instance had four peak nights (3, 4, 5 and 6 July)? In that case, 6 July would be forecasted based on an average of the past instanceâs three peak nights, since there is no direct match.
Special Events inthe RMScan overlap. However, if two Special Events always overlap, create one Special Event instead. For example, if a repeating city-wide convention always falls on a public holiday that is also set up as a Special Event, the convention and public holiday should be set up as a single Special Event. However, if the city-wide convention occurs only once and that instance falls on a repeat holiday, create two separate Special Events.
If one instance of a repeat Special Event had very different transient demand and wash patterns than in previous years, remove the instance from the Special Event. For example, a concert that impacts transient business always occurs on one weekend in July. However, if the  attendance last year was unusually low, remove that instance from the Special Event. This allowsthe RMSto use only the data from the two previous years when forecasting future instances of the concert.
Then decide if last yearâs instance of the concert should be a separate Special Event. If its patterns are different from normal transient patterns, create a separate Special Event just for last year. If the attendance was so low that there was no difference to normal patterns, delete the instance, andthe RMSuses the data to forecast normal demand.
Note: Adding or removing past instances impacts the forecast, seeUnderstand the Forecast Impact.
An atypical event is a recurring event that impacts demand differently depending on the specific instance. For example, a sporting event where your hotel team's games against its arch rival may draw more interest than normal home game.  Deleting one instance of the Special Event may not be enough to account for these demand differences.
For the best possiblethe RMSforecasts, create separate recurring Special Events for each demand level. In this example, you create one event for "home games â high demand" and one for "home games â medium demand." If the patterns for "home games â low demand" are similar to normal demand days, no Special Event is necessary.
Such Special Events need to be grouped together  by demand and their duration. For example, if you have many conventions in your market that impact your transient demand, you could create three Special Events for high, medium and low impact for two-day conventions, three Special Events for high, medium and low impact for three-day conventions, and so on, instead of listing each convention separately.
If you know the date of a one-time Special Event that occurs outside of the optimization window, add the Special Event inthe RMSand load your restrictions into theselling systemprior to when the date opens for sale. After the date is added tothe RMS, review the system's forecast. If needed, use overrides. Then you can remove the restrictions in yourselling systemand monitor the Special Event and overrides inthe RMS.
If a future event has no historical instance within the booking data window, you may have insights thatthe RMSdoesn't. For example, a convention that changes locations each year is scheduled in your city six months from now.  You expect strong transient demand for the event. However, if no reservations are on books,the RMSmay not  recognize it as a Special Event yet. As a result, the system may not have raised the forecast and implemented more restrictive controls.
Even if your booking pace is already stronger than normal,  the system knows that, in most cases, a strong early pace is not a reliable indicator for higher remaining demand.The RMSwill not forecast it as a Special Event and may simply add the forecasted remaining demand to the higher on books.
Thus, whenthe RMSdoesn't have any historical instance to help it forecast a future Special Event, monitor it closely. If needed, use demand overrides on the remaining demand to match your expectations.

## Setting Up Future Special Events

For properties with Synthetic Data, don't enter your high or low demand expectations for Special Events in the projections. SeeManage Special Events with Demand Overridesfor more details.
For full and partial seasonal closures, including closures on only some days of the week, enter a Special Event that repeats annually. For example, if a property closes from Sunday through Thursday during four weeks of low demand and opens only on Fridays and Saturdays. Enter a Special Event with multiple instances, each should cover the SundayâThursday closure period when hotel inventory is set to out of order.
SeePeriods of Restricted Inventoryfor information about managing these periods and understand howthe RMSreacts to the impact of restricted inventory.
When you create a Special Event, you can flag it asInformational Use Only.The RMStreats these events as normal days.  This helps remind you of these events on the Special Event Management page.
For example, you should not consider unusual periods of group activity that are not matched by transient activity to be Special Events. However, you can use Informational Use Only events to remind you of unusual group business, like when a group books all rooms for a one-night stay.

## Reviewing Your Special Events

As part of your regular tasks, review and update your  Special Events for both future and historical dates. Ensure that the most recent past instance is the correct one to forecast the next, the dates are correct, and review the past events, and delete those with little impact. A day that seemed like a Special Event six months ago may not look like one after the day has passed. If that is the case, delete the Special Event.
