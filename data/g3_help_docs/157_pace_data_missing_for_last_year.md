# Pace Data Missing for Last Year

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/BAD/Missing-Pace-Data.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/BAD/Missing-Pace-Data.htm`
- **Ingestion Date:** `2026-09-11 22:13:53`

---

# Pace Data Missing for Last Year

This information only applies if your property'sReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.is Opera with OXI interface, or if it is based onHTNGHospitality Technology Next Generation is an association that creates standards to enable better  integration between systems. Examples of reservation systems that use the HTNG standard are: 
Protel i/o, Suite8, NEC, Spectra, WebRezPro, Vail LMS, Infor HMS, Newbook, RMS PMS.standards.

## Group Pace Initialization Period

If your property'sReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.is Opera with OXI interface, or if it is based onHTNGHospitality Technology Next Generation is an association that creates standards to enable better  integration between systems. Examples of reservation systems that use the HTNG standard are: 
Protel i/o, Suite8, NEC, Spectra, WebRezPro, Vail LMS, Infor HMS, Newbook, RMS PMS.standards,  your reservation systems aren't sendingG3 RMSthe date on which a group block is booked.  Since these reservation systems don't send booked dates for group business, STLY data for group is incorrect.G3 RMScan't show only transient STLY data and hide group STLY data. Therefore, it doesn't display any STLY data until it captures one year of data.
In this case,G3 RMSuses a Group Pace Initialization Period to  understand group booking patterns for your property.
With other reservation systems,G3 RMSuses the booking dates of past group blocks to understand group booking patterns, specificallyBooking PaceMeasures how the occupancy changes as the arrival date approaches. It shows the speed at which reservations are booked.andWashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization.. In other words, group block booking dates impact the system's forecasts of  group remaining demand and group wash.
Without booking dates for past groups,G3 RMSuses a 90-day Group Pace Initialization Period. During this time,G3 RMStemporarily uses the data from future groups to understand group booking patterns. The system doesn't receive the booking date for future groups either, but it knows the date on which the block was first created and uses that as the booking date. During this temporary phase,G3 RMScollects daily pace information, which provides a much more detailed picture of group booking patterns. After it learns from 90 days of daily pace,G3 RMSupdates the booking pace patterns that it uses to forecast group remaining demand and wash. After this period,G3 RMScontinues to learn and improve booking patterns.
The 90 days required for the Group Pace Initialization Period might need to be extended for properties with very long booking windows

## Improving the Forecast during this Period

How is the Group Demand Forecast Impacted by Missing Group Booking Dates? The missing dates apply mostly to the timing of remaining demand. For example,G3 RMSexpects a total of 100 rooms to be booked by group guests. The group booking pace indicates that 75% of those guests book prior to 28 days. In this example, the remaining demand forecast shows that 25 rooms of remaining demand for groups exists 28 days out.
You can use different methods to improve your group forecast during this period. How you do so depends on when you completed the Create and Commit Forecast Groups process. If you are unsure about your timing, speak with your primary IDeaS contact. Regardless,G3 RMSdoes not display STLY data until one year of data capture.

#### During the 90-Day Group Pace Initialization Period

G3 RMSis still using booking patterns based only on future groups. You likely know more about group demand and wash thanG3 RMS. Review forecasts and decisions closely before you move intoDecision DeliveryA two-way status when the RMS receives data from the reservation system, produces forecasts and ouputs (like pricing), and sends outputs to the selling system..
- Review the remaining group forecast and, if necessary,override remaining demand and its washby Forecast Group.
- Review the wash of existing groups on books and, if necessary,override wash by Individual Group.
- WhenG3 RMScollects 91 days of pace, it optimizes using the updated booking patterns. After the first optimization, you might seechanges in forecasts and decisions. Review them closely.

#### After the 90-Day Group Pace Initialization Period

When you commit Forecast Groups after the 90-day period,G3 RMSuses booking patterns based on the 90-day period to forecast group demand and wash. Continue to review your forecasts and decisions, sinceG3 RMScontinues to learn and update the booking patterns.

## Forecasting without STLY Data

Because you can't see STLY data inG3 RMS, you might be concerned about the system's forecasting performance. AlthoughG3 RMScan't display any STLY data because group STLY is incorrect, it does have booking pace data available for forecasting. Transient booking pace data is available for both historical and future bookings. For group booking pace, the system uses data from future groups and constantly improves booking patterns based on daily pace data.
Furthermore, while STLY data is a critical factor in manual forecasting, it is only one of many data points thatG3 RMSuses for forecasting. AndG3 RMSuses a much more granular approach, with a separate forecast for each Forecast Group and Room Class combination. For more details, seeHowG3 RMSCalculates Unconstrained Demand Forecasts.
Therefore,G3 RMScan produce robust group demand and wash forecasts even when the system starts out without STLY data for historical group blocks.

## Overriding Wash During this Period

Since group booking pace impacts the demand forecasts, it can affect Last Room Value (LRV), which in turn can affect pricing decisions.  However, overbooking is most directly impacted. The group booking patterns used during the 90-day period tend to have lower wash and therefore lower overbooking. On the other hand, if the data from future group blocks indicates a large amount of group cancellations,G3 RMSincreases overbooking accordingly. Therefore, sharing withG3 RMSwhat you know about group wash is particularly important during the Group Pace Initialization Period.
After the end of the Group Pace Initialization Period, you might see changes to forecast and decisions, particularly to overbooking. You might notice that overbooking values increase after the Group Pace Initialization Period ends.
