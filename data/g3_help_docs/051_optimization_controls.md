# Optimization Controls

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Optimization/Optimization-Controls.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Optimization/Optimization-Controls.htm`
- **Ingestion Date:** `2026-09-11 22:12:41`

---

# Optimization Controls

Consider using the following optional settings:
- Cancel/Re-Book Percentage: allowsG3 RMSto consider revenue losses from a price reduction, when guests cancel their reservations and re-book at a lower rate.
Cancel/Re-Book Percentage: allowsG3 RMSto consider revenue losses from a price reduction, when guests cancel their reservations and re-book at a lower rate.
- Price Drop Restrictions: controls price drops close to the arrival date if you prefer avoiding price drops over maximizing revenues.
Price Drop Restrictions: controls price drops close to the arrival date if you prefer avoiding price drops over maximizing revenues.
- Optimization Method 2:  applies if you wantG3 RMSnot only to inform you of arrival dates with LRA impact but also to close temporarily BAR availability for those dates.
Optimization Method 2:  applies if you wantG3 RMSnot only to inform you of arrival dates with LRA impact but also to close temporarily BAR availability for those dates.
To see the history of changes, such as who updated the settings and when, click export.

## Cancel/Re-book Percentage

Enable the Cancel/re-book percentage option if you wantG3 RMSto consider revenue losses from a price reduction, when guests cancel their reservations and re-book at a lower rate.
By default,whenG3 RMSdetermines pricing, it doesn't expect that guests cancel and re-book if the price drops. The system drops the price if that brings  more revenue overall. When you enter a cancel/re-book percentage value,G3 RMScompares the rewards against the risks of lowering prices:
- Reward: based on the expected remaining demand for each price point, how much more revenue you gain from a price drop.
- Risk: based on the cancel/re-book percentage, how much revenue you lose from existing On Books business.
G3 RMSconsiders those factors in its optimization and selects the optimal price. It only drops the price if the rewards outweigh the risks.

### Setup  Steps

- Click, thenProperty, and thenProperty Specific.
- Click theOptimization Controlstab.
- Enter a percentage value in theCancel/re-book percentagefield.
- ClickSave.

### Best Practices

#### Enable the functionality if:

- You are concerned that you lose revenue because your guests cancel and re-book after price reductions.
- You don't think you lose revenue, but you are concerned that pricing gets lower as the arrival date gets closer. For example, someclientsset a strategic high percentage to avoid "educating" consumers that the longer they wait to book the reservation, the lower the price.

#### Determine the optimal value

G3 RMSdoesn't collect any personal information from reservations. Therefore, it can't track which or how many guests cancel and re-book. You could track such information by comparing cancellations against new reservations for a given booking date.Or you might have this information available from a frequent guest program.
The value is meant to be an estimate.We recommend that you start with a low value, for example 5% or 10%. Or, if available, base the value on actual cancel and re-book data.Then observe the impact on the number of pricing reductions for a period. Compare that to what you observed before the change. If price reductions don't decrease enough, increase the amount by 5% and observe again. Continue until you find an acceptable level.
Note:
- When the Cancel/Re-book feature is enabled, the system considers revenue losses only for some market segments, those that you attributed as "Unqualified" or "Linked to BAR."
- Early in the booking curve, this feature has little impact on price reductions. That's because, with little or no business on books, there is no business that can cancel.

## Price Drop Restrictions

Use this optional functionality to control price drops close to the arrival date. You define conditions, for example a minimum revenue gain. The conditions need to be met beforeG3 RMScan lower a pricing decision. If you use this functionality, you tell the system that, for the defined conditions, you prefer avoiding price drops over maximizing revenues. This might be the case because you have business rules to prevent price drops close to arrival.
Note:
- The price drop restrictions apply to thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.and, if used, toIndependent Products.
The price drop restrictions apply to thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.and, if used, toIndependent Products.
- If price drop restrictions conflict withCompetitive Market Constraints,G3 RMSignores the constraints.
If price drop restrictions conflict withCompetitive Market Constraints,G3 RMSignores the constraints.

### Setup  Steps

- Click, thenProperty, and thenProperty Specific.
Click, thenProperty, and thenProperty Specific.
- Click theOptimization Controlstab.
Click theOptimization Controlstab.
- SelectEnable Price Drop Restrictions.
SelectEnable Price Drop Restrictions.
- All days of week are checked. Clear any day  for which you don't want to apply the price drop restriction.
All days of week are checked. Clear any day  for which you don't want to apply the price drop restriction.
- Enter the number ofDays to Arrivalin theValuefield to apply it to each day of the week.
Enter the number ofDays to Arrivalin theValuefield to apply it to each day of the week.
- Press theTabkey to go to each day of the week and to change values, if needed.
Press theTabkey to go to each day of the week and to change values, if needed.
- Enter the values for theRevenue Threshold For Price. Select afixed value or apercentage.
Enter the values for theRevenue Threshold For Price. Select afixed value or apercentage.
- Enter the values for theMaximum Price Drop. Select a fixed valueor a percentage.
Enter the values for theMaximum Price Drop. Select a fixed valueor a percentage.
- ClickSave.
ClickSave.
- If needed, click to addSeasons when the values differ from the Defaults.
If needed, click to addSeasons when the values differ from the Defaults.

### Data Details

### Best Practices

#### Match business rules

Someclientsdon't allow price drops close to arrival. Use the functionality to enforce such strict rules.

#### Manage impact of upgrading

Someclientsbalance room types prior to the arrival date by upgrading reservations. If such upgrading results in higher-priced room types becoming sold out and lower-priced room types becoming available, thenG3 RMSmight reduce pricing. Let's say that your property balances inventory two days prior to arrival and wants to avoid any resulting price drops. In that case, enable the restrictions, set theDays to Arrivalto 2 and theMaximum Price Dropto zero.

#### Manage impact of group wash

Another scenario might be that you want to avoid price drops due to group wash, for example on cut off day. Before setting up Price Drop Restrictions, make sure that you follow aconsistent processfor loading groups. If you load group consistently, wash forecasts improve. That means thatG3 RMScan better predict when and how much groups wash and will drop price less often.

#### Set restrictions only close to arrival

Each time your defined restrictions prevent a price drop, you accept a possible revenue loss, up to the amount of yourRevenue Threshold For Price. The higher you set theDays to Arrivalvalue, the larger the possible losses.

## Optimization Method 2

This alternative optimization method is not beneficial for mostclientsand the module is not visible by default. IDeaS contacts clients that may benefit from this feature to discuss the considerations. Optimization Method 2 only applies if you wantG3 RMSnot only to inform you of arrival dates with LRA impact but also to close temporarily BAR availability for those dates.
For more information on LRA impact and the available LRA options, seeLast Room Availability (LRA).

### Setup  Steps

- Click.
- In thePropertysection, clickProperty Specific.
- ClickOptimization Controls.
- SelectEnablefor Optimization Method 2.
- ClickSave.

### Best Practices

- Compared to the default optimization, Optimization Method 2 is better at considering when different types of future remaining demand book. Thus, with regards to LRA,G3 RMScan better react to dates when it forecasts that the remaining demand for low-value LRA business will book earlier than high-value BAR business and will potentially displace that high-value BAR business. In the case, this method should lead to better decisions and higher revenues.
- Optimization Method 2 leads to less stable decisions, meaning that the systemâs decisions change much more frequently in between optimizations. These changes are partly due to the increased complexity from considering when different types of remaining demand book, but also because this model explicitly plans to implement different pricing approaches over the booking period for each arrival date. More frequent decision changes may make monitoringG3 RMSmore time consuming.
- When Optimization Method 2 is enabled, remaining demand values may no longer be aligned with the occupancy forecast. Due to the differences in how remaining demand and expected occupancy are calculated in Method 2, on-books plus remaining demand can sometimes be less than the occupancy forecast.
- Consider when your LRA business typically books versus when your BAR business books. If both have similar booking windows, then the ability of Optimization Method 2 to better react to dates with LRA impact may be outweighed by its disadvantages. Consider this method if LRA business usually books earlier than BAR business.
