# G3 RMSRelease Notes

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/About/Whats-New.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/About/Whats-New.htm`
- **Ingestion Date:** `2026-09-11 22:12:11`

---

# G3 RMSRelease Notes

Use the Release Notes to preview the  improvements coming toG3 RMSin the upcoming release, or to view recently introduced ones. You automatically receive the latestG3 RMSversion, click Announcementsin the top right to see the date and time of your release. If you don't see an icon, your role lacks the permissions, if needed, contact yourSystem CEOThe IDeaS name for a system administrator role. Users with this role configure a property's permissions: creating other Roles, then assigning them to Users. They ensure that the right users have the appropriate access in the system..
Your property's System CEO  has Read/Write access to all newG3 RMSfeatures, unless the feature requires a license. And the System CEO manages the permissions for all users, so contact them if you don't have the expected access to new functionality. This might be your supervisor or corporate revenue management representative.

## Release 10.5.2 - September 15 and 16, 2026

The following items are turned on in the 10.5.2 release. Preview the 10.5.3 release on Tuesday, September 22, 2026.
When you review pricing decisions in Price Investigator, you now see:
- Clearer messages that explain whyG3 RMSrecommends a price. This helps you quickly understand why the price differs from historical pricing.
Clearer messages that explain whyG3 RMSrecommends a price. This helps you quickly understand why the price differs from historical pricing.
- New charts that highlight the size and direction of the impact on price from specific factors like demand, competitor pricing, or neighboring days.These charts replace the currentgauge charts.As the typically largest factor, demand always appears in the chart. If another factor is the main reason for the difference from Historical ADR, the chart also shows that factor.All remaining factors appear as Other.
New charts that highlight the size and direction of the impact on price from specific factors like demand, competitor pricing, or neighboring days.
- These charts replace the currentgauge charts.
These charts replace the currentgauge charts.
- As the typically largest factor, demand always appears in the chart. If another factor is the main reason for the difference from Historical ADR, the chart also shows that factor.
As the typically largest factor, demand always appears in the chart. If another factor is the main reason for the difference from Historical ADR, the chart also shows that factor.
- All remaining factors appear as Other.
All remaining factors appear as Other.
- The messages and the chart also display on the Manage Pricing  Summarytab.
The messages and the chart also display on the Manage Pricing  Summarytab.
We enable this change for clients in phases, finishing on Monday, September 21, 2026. Contact your IDeaS representative to learn when it's enabled for you.
You can now use theRequest Full Uploadtab on the Decision Configuration page to resend decisions to one or more selling systems without contacting IDeaS Support. This saves you time and gives you more control.
If you have the required permission, you can:
- Select the selling systems and decision types to include.
Select the selling systems and decision types to include.
- Request the upload now or schedule it for the next BDE.
Request the upload now or schedule it for the next BDE.
- Review previous and scheduled upload requests and their status.
Review previous and scheduled upload requests and their status.
For details, reviewHelp. We enable this on Thursday, September 17, 2026, 8:00 CST.
If your property usesHot Start - Synthetic Data, you can now run a Synthetic Data Build directly inG3 RMS. Previously, you had to contact IDeaS to run this step, so this change saves you time and gives you more control.
After you complete the Synthetic Data setup, use the newCreate Synthetic Historytab to start the process.G3 RMScreates synthetic history using your projections and booking patterns and then uses that history, together with current on-books data and other configurations, such as Pricing, to generate forecasts and pricing recommendations during the next processing cycle.

#### Key benefits:

- Create both initial and future Synthetic Data Builds.
Create both initial and future Synthetic Data Builds.
- Identify and resolve configuration issues before starting the build.
Identify and resolve configuration issues before starting the build.
- Receive immediate feedback and links to the relevant configuration areas when issues exist.
Receive immediate feedback and links to the relevant configuration areas when issues exist.
- Resolve critical issues and review the RMS recommendations that support best practices.
Resolve critical issues and review the RMS recommendations that support best practices.
- View the build progress.
View the build progress.

#### Additional information:

- IDeaS support for issues remains available to assist you.
IDeaS support for issues remains available to assist you.
- Component room support is coming in a future release.
Component room support is coming in a future release.
- Your System CEO must grant Read/Write access to run Synthetic Data Builds.
Your System CEO must grant Read/Write access to run Synthetic Data Builds.
- We enable this on Thursday, September 17, 2026, 8:00 CST.
We enable this on Thursday, September 17, 2026, 8:00 CST.
Asannounced in 10.4.4, we complete the roll-out of these changes with the 10.5.2 deployment, contact your IDeaS representative to learn when they are enabled for your property.
These changes do not apply toPrice ExcludedA Base Room Type setup option that means that the RMS doesn't optimize pricing for the room types of such a Room Class and instead sends the fixed price, plus any offsets, to the selling system.Room Classes. Overrides to such Room Classes continue to work as before.
If you useRate Data Advantage, you can now view the last mapped date directly on the Smart Mapping page. Point toReview Suggestionsto confirm the date whenG3 RMSlast mapped even when there no new suggestions exist.
You can soon run group evaluations for multiple properties on the new Group Pricing page. Aside from the more modern workflow, the new version also improves on the old Group Pricing evaluations by letting you include up to 30 properties in one evaluation instead of five. This helps revenue and sales teams evaluate larger opportunities with fewer manual workarounds.
Evaluations for up to five properties will continue to return results in real time. Evaluations with six or more properties will process in the background. When the results are ready, you will receive an email with a direct link so you can continue working during processing.
We plan to enable the redesigned Multi-Property Group Pricing experience after the 10.5.3 deployment, watch future announcements for the confirmed date.

### Other Fixes and Performance Improvements

## Release 10.5.1 - August 24 and 25, 2026

The following items were turned on in the 10.5.1 release.
Weâve improved and renamed theOccupancy Changenotifications. The changes better differentiate On Books changes from Forecast changes and allow you to monitor On Books changes for metrics other than the current occupancy, like revenue and, if enabled, profit.

#### Name change

These name changes affect all Notification pages in the Information Manager: Setup, List view, and Details view.
With a Data Feed subscription, new files will use the new On Books Change name.

#### New On Books Metrics

You can now monitor the On Books Change for the following metrics:
- Occupancy On Books, Revenue On Books, ADR On Books and RevPAR On Books.
Occupancy On Books, Revenue On Books, ADR On Books and RevPAR On Books.
- If you use Profit Optimization, you can also monitor Profit On Books, ProPAR On Books, and ProPOR On Books
If you use Profit Optimization, you can also monitor Profit On Books, ProPAR On Books, and ProPOR On Books

#### Profit Metrics in Forecast Change Notifications

If you useProfit Optimization, the Forecast Change Notifications now support the following metrics:
- Profit
Profit
- ProPOR
ProPOR
- ProPAR
ProPAR
Based on your feedback inIDeaShare, you can now set your default views directly from the Channel Forecast dashboard, saving you time. To access  clickin the top right on the dashboard to open the settings, like viewing by Channel, Source, or Source by Channel.
We removed the Forecast Settings tab under Channel configuration.
You can now also select the following:
- Default View Type (Chart or Table).
Default View Type (Chart or Table).
- More channels, sources, or channel-by-source combinations (10 instead of the previous limit of 5, allowing for a more comprehensive forecasting analysis).
More channels, sources, or channel-by-source combinations (10 instead of the previous limit of 5, allowing for a more comprehensive forecasting analysis).
Based on your feedback in IDeaShare, you now have a clearer, more consistent way to apply a floor of a Linked Pricing product across the room types of your Room Classes.
If negative Product Adjustments or negative Offsets for non-Base room types result in a conflict between the Offsets and the Product Floor, you can choose howG3 RMSapplies the floor. Select your option based on your preferred outcome:
- All Room Types in a Room ClassThis is the default option and might mean that the pricing of non-Base Room Types does not follow your Offsets.
All Room Types in a Room ClassThis is the default option and might mean that the pricing of non-Base Room Types does not follow your Offsets.
- Only the Base Room TypeApply the floor only to the Base Room Type and allow other room types to be priced below the floor.
Only the Base Room TypeApply the floor only to the Base Room Type and allow other room types to be priced below the floor.
Select the options in the newProduct Floormenu, under Pricing Configuration >> Advanced Settings.
The Primary Priced Product has a Ceiling of 300 and a Floor of 100. The Standard Room Class contains:
- STD1 (Base Room Type)
STD1 (Base Room Type)
- STD2 with a fixed offset of +10
STD2 with a fixed offset of +10
The Linked Product is defined with:
- An adjustment of -25%
An adjustment of -25%
- A % Floor Type of -10% of the Base Product Floor (90)
A % Floor Type of -10% of the Base Product Floor (90)
For a specific date, the Base Room Type price is 100. Therefore, for the Primary Priced Product:
- STD1 = 100
STD1 = 100
- STD2 = 110
STD2 = 110
With either Product Floor option,G3 RMSprices STD1 for the Linked Product at 90. It uses the floor price of 90 instead of the -25% adjustment, which would result in a price of 75.
- With theAll Room Typesoption,G3 RMSapplies the floor to all room types. It prices both STD1 and STD2  at 90 and ignores the Offsets.
With theAll Room Typesoption,G3 RMSapplies the floor to all room types. It prices both STD1 and STD2  at 90 and ignores the Offsets.
- With theOnly the Base Room Typeoption,G3 RMSapplies the floor only to the Base Room Type and keeps the Offset. STD1 is priced at 90 and STD2 at 99.
With theOnly the Base Room Typeoption,G3 RMSapplies the floor only to the Base Room Type and keeps the Offset. STD1 is priced at 90 and STD2 at 99.
If the Offset for STD2 is -10 instead of +10, theOnly to Base Room Typeoption  prices STD2 at 81. BecauseG3 RMSpreserves the Offset for non-Base Room Types, the resulting price is  below the floor.
If you manage Permissions, you can now manage the access to each Advanced Setting separately (for Pricing Configuration).
Previously, you could only set the permission for all Advanced Settings together. For example, now you can allow one role Read/Write access to Base Room Type but Read Only for Rounding Rules. This change gives you greater flexibility to manage permissions, reducing the risk of unintended configurations.
This change doesnotimpact your existing permissions. After the change, any role has the same permissions for each Advanced Setting that it previously had at the total Advanced Settings level.

#### New Exception When a Blended Price Nears Its End Date

If you use the Blended Price setup for Independent Products, you now will get an Exception when the defined End Date is nearing. This helps you avoid that a Blended Price expires and thatG3 RMSswitches to daily pricing.
The Exception:
- Triggers when the Blended Priceâs End Date is less than 30 days beyond the Upload Window.
Triggers when the Blended Priceâs End Date is less than 30 days beyond the Upload Window.
- Can be suspended for a specific duration, like two weeks, and for a specific product.
Can be suspended for a specific duration, like two weeks, and for a specific product.
- Automatically resolves when you extend the Blended Priceâs End Date beyond the Upload Window plus 30 days.
Automatically resolves when you extend the Blended Priceâs End Date beyond the Upload Window plus 30 days.

#### New Weekly Frequency Available for Blended Price Setup

Based on your feedback, you can now create a Blended Price using a weekly Frequency in addition to the existing monthly option. When you set up a weekly frequency, you can:
- Define the day of the week when your week begins.
Define the day of the week when your week begins.
- Create a Blended Price with or without an end date, like the monthly option.
Create a Blended Price with or without an end date, like the monthly option.
In your Personal Details (click your initials in the top-right, then Preferences, and Change Personal Settings) you can now also select Chinese as yourPreferred language.
We enable this feature for all clients on Monday, August 24, 2026.
Soon, when you click to configureProperty Attributesan updated page opens in a new tab and in the sameUniversal Adminlocation where you already manage Permissions:
- If you have set up attributes, they are automatically transferred to the new page, you donât have to do anything.
If you have set up attributes, they are automatically transferred to the new page, you donât have to do anything.
- The functionality is the same, but some steps differ slightly, for help click the familiar ? icon in the top right of the page.
The functionality is the same, but some steps differ slightly, for help click the familiar ? icon in the top right of the page.
- The Attribute Help topic will be separate from the remainingG3 RMScontent. To view a Help topic other than Permissions, open Help from the browser tab withG3 RMS.
The Attribute Help topic will be separate from the remainingG3 RMScontent. To view a Help topic other than Permissions, open Help from the browser tab withG3 RMS.
- We plan to release this change with the 10.5.2 deployment, look for future release notes for the final confirmation.
We plan to release this change with the 10.5.2 deployment, look for future release notes for the final confirmation.

### Other Fixes and Performance Improvements

## Release 10.4.4 - August 3 and 4, 2026

The following items were turned on in the 10.4.4 release.

### Pricing - Improved Pricing Overrides for Consistency and Clarity

The following improvements make pricing overrides easier to understand when you review your prices:
- When you override at the Base Room Type level, you see the override icon only on the Base Room Type, even thoughG3 RMSmight change the prices of Non-Base Room Types based on Offsets. This gives you a clearer view with fewer icons and clarifies at what level you applied the override.
When you override at the Base Room Type level, you see the override icon only on the Base Room Type, even thoughG3 RMSmight change the prices of Non-Base Room Types based on Offsets. This gives you a clearer view with fewer icons and clarifies at what level you applied the override.
- When you change overrides at the Base Room Type level,G3 RMSnow automatically makes the changes for non-Base Room Types and you no longer must select theApply/Delete overrides to all room typesoption, saving you time.
When you change overrides at the Base Room Type level,G3 RMSnow automatically makes the changes for non-Base Room Types and you no longer must select theApply/Delete overrides to all room typesoption, saving you time.
- When you use a Specific override at the Base Room Type level, it triggers a Sync flag andG3 RMSconsiders the impact on demand and all outputs like Last Room Value in its optimization. Previously, the system did not optimize around a Specific Override in the Calendar view.
When you use a Specific override at the Base Room Type level, it triggers a Sync flag andG3 RMSconsiders the impact on demand and all outputs like Last Room Value in its optimization. Previously, the system did not optimize around a Specific Override in the Calendar view.

#### Recommended Actions

During the deploymentG3 RMSremoves the specific override icons from non-base room types if you added an override to the Base Room Type and clickedApply to All Room Types. The overrides itself and the icon on the Base Room Type remain.
If you applied a specific override directly on a non-base room type, the icon and the override remain in place. Thus, we recommend that you:
- Print an Output Override report before your deployment date and use it to:
Print an Output Override report before your deployment date and use it to:
- Prior to deployment, review all overrides, and remove any that are no longer needed.
Prior to deployment, review all overrides, and remove any that are no longer needed.
- After the deployment, review if you need any non-base room type overrides to display the override icon. Remember, this change only removes the icon for non-base room types, not the override itself.If you changed your Offsets since you applied an override, used Apply to All Room Types, and the Base Room Type override still existed at the time of the deployment,G3 RMSwill change the prices of those overrides for non-base room types, applying the new Offset values.
After the deployment, review if you need any non-base room type overrides to display the override icon. Remember, this change only removes the icon for non-base room types, not the override itself.
If you changed your Offsets since you applied an override, used Apply to All Room Types, and the Base Room Type override still existed at the time of the deployment,G3 RMSwill change the prices of those overrides for non-base room types, applying the new Offset values.
If you have questions or notice anything unexpected, reach out to your IDeaS representative or submit a case. To see the changes in the mobileG3 RMSapp, download the newest version in the Play Store (Android devices) or the App Store (iOS, iPhone or iPad).
We enable this change in phases starting on Thursday, August 6, and completing it after the release of 10.5.2, September 16,  2026. Contact your IDeaS representative to learn when it's enabled for you.

### Demand and Wash Multiday Override â New Fixed Value Option

Based on your suggestions inIDeaShare, when you apply Multiday Overrides on the Demand and Wash page, you now have the option to enter a fixed value for the remaining demand. Previously you had to enter a percentage change to the forecasted demand.
- This applies only to the Override by Occupancy Date, not the Arrival by LOS type.
This applies only to the Override by Occupancy Date, not the Arrival by LOS type.
- We  deploy this change by Wednesday, August 26, 2026.
We  deploy this change by Wednesday, August 26, 2026.

### Group Wash by Group - Displays Tentative Block Information

If your reservation system sendsTENTATIVE-Non Adjustgroup data, you can now also review theTentative Blockdata for Group and Transient Block market segments.

### At a Glance Dashboard - New Extended Stay Data Available

If you useExtended Stay Forecasting and Optimization, you now see the following new data on the At a Glance dashboard:
Below the Calendar, the new summary shows:
- Average Length of Stay (ALOS)
Average Length of Stay (ALOS)
- Short Stay Occupancy %
Short Stay Occupancy %
- Extended Stay Occupancy % (ESOCC)
Extended Stay Occupancy % (ESOCC)
SeeHelpfor details on this data. Comparing your mix of short-stay and extended-stay demand to prior-year results can help you identify what is driving or lagging performance, and assess your strategy against overall results.
The Extended Stay Summary is available for single-property, not multi-property views.
When you click a single date on the Calendar, you'll now see ALOS and ESOCC On Books values for the selected date and compare them to last year (Actual).

### Manage Independent Products with Blended Pricing on the Pricing Calendar View

If you use Independent Products that haveBlended Pricingset up, you can now use the Calendar View on the Pricing page to manage them better. Select a single product with the appropriate setup and you see the prices by the configured Blended Pricing season date ranges. Previously, you could only view pricing by individual occupancy date.Review all steps in Pricing.

### Group Pricing - Updated ROH Rate When Adjusting Room Class Prices

In a Room Class Evaluation, when you change theRecommended Pricefor one or more Room Classes,G3 RMSnow updates theROH Recommended Priceto match your changes.
G3 RMSrecalculates the ROH Recommended Price using a weighted average of your updated Room Class prices. This helps you see the full pricing impact of your adjustments.

### Coming Soon - Run Synthetic Data Build inG3 RMS

If your property usesHot Start - Synthetic Data, you can now run a Synthetic Data Build directly inG3 RMS. Previously, you had to contact IDeaS to run this step, so this change saves you time and gives you more control.
After you complete the Synthetic Data setup, use the newCreate Synthetic Historytab to start the process.G3 RMScreates synthetic history using your projections and booking patterns and then uses that history, together with current on-books data and other configurations, such as Pricing, to generate forecasts and pricing recommendations during the next processing cycle.

#### Key benefits:

- Create both initial and future Synthetic Data Builds.
Create both initial and future Synthetic Data Builds.
- Identify and resolve configuration issues before starting the build.
Identify and resolve configuration issues before starting the build.
- Receive immediate feedback and links to the relevant configuration areas when issues exist.
Receive immediate feedback and links to the relevant configuration areas when issues exist.
- Resolve critical issues and review the RMS recommendations that support best practices.
Resolve critical issues and review the RMS recommendations that support best practices.
- View the build progress.
View the build progress.

#### Additional information:

- IDeaS support for issues remains available to assist you.
IDeaS support for issues remains available to assist you.
- Component room support is coming in a future release.
Component room support is coming in a future release.
- Your System CEO must grant Read/Write access to run Synthetic Data Builds.
Your System CEO must grant Read/Write access to run Synthetic Data Builds.

### Coming Soon - Information Manager â Improved Occupancy Change Notification

Weâve improved and renamed theOccupancy ChangeNotifications. The changes differentiate On Books changes from Forecast changes and allow you to monitor On Books changes for metrics other than the current occupancy, like revenue and, if enabled, profit.

#### Name change

These name changes affect all Notification pages in the Information Manager: Setup, List view, and Details view.
With a Data Feed subscription, new files also use the new On Books Change name, not the previous Occupancy Change names.

#### New On Books Metrics

You can now monitor the On Books Change for the following metrics:
- Occupancy On Books, Revenue On Books, ADR On Books and RevPAR On Books.
Occupancy On Books, Revenue On Books, ADR On Books and RevPAR On Books.
- If you use Profit Optimization, you can also monitor Profit On Books, ProPAR On Books, and ProPOR On Books.
If you use Profit Optimization, you can also monitor Profit On Books, ProPAR On Books, and ProPOR On Books.
We plan to release this with the upcoming 10.5.1 iteration. See future announcements for the final confirmation.

### Coming Soon - Pricing Configuration â Simplified Floor Setup for Linked Pricing Products

Based on your feedback inIDeaShare, you now have a clearer, more consistent way to apply a floor of a Linked Pricing product across the room types of your Room Classes.
When negative Product Adjustments or negative Offsets for non-Base room types result in a conflict between the Offsets and the Product Floor, you can now select howG3 RMSapplies the floor:
- All Room Types in a Room ClassThis is the default option and might mean that the pricing of non-Base Room Types does not follow your Offsets.
All Room Types in a Room ClassThis is the default option and might mean that the pricing of non-Base Room Types does not follow your Offsets.
- Only the Base Room TypeApply the floor only to the Base Room Type and allow other room types to be priced below the floor.
Only the Base Room TypeApply the floor only to the Base Room Type and allow other room types to be priced below the floor.
Select the options in the newProduct Floormenu, under Pricing Configuration, Advanced Settings.

### Other Fixes and Performance Improvements

## Release 10.4.3 - July 13 and 14, 2026

### Group Pricing Improvements

#### More Details Page Displays Better on Smaller Screens

You can now view the Evaluation Results More Details page without horizontal scrolling on smaller screens (below 1920 x 1080 resolution).

#### Improved Adjust Results Slider

We improved the Adjust Results slider to give you better control and prevent large, unintended price changes. A full adjustment now caps at 2Ã the original price.
You can still:
- Adjust the slider multiple times to increase the price further.
Adjust the slider multiple times to increase the price further.
- Enter a specific override value with no limit.
Enter a specific override value with no limit.

### Coming Soon - Group Wash by Group Displays Tentative Block Information

If your reservation system sendsTENTATIVE-Non Adjustgroup data, you can now also review theTentative Blockdata for Group and Transient Block market segments.

### OtherFixes and Performance Improvements

## Release 10.4.2 - June 22 and 23, 2026

The following items were turned on in the 10.4.2 release.

#### Day of Week Added on the Evaluation Results Page

When you viewMore Detailson the Group Pricing Evaluation Results page, you can now see the day of week next to the Date of Stay column. This makes it easier to review patterns without viewing a calendar or going to the Guest Rooms tab.

#### Evaluation â Use the Tab Key to Move Between Fields

Based on yourIDeaSharerequests, you can now tab between evaluation input fields using the keyboard, saving you time when entering the group information.

#### Evaluation Results Color Updates

Based on your IDeaShare requests, the colors that indicate the profitability status of an evaluation are now easier to distinguish. Previously the colorindicating that the Recommended Price is constrained by Average MAR was easy to confuse with the colorfor not profitable results. The new colorfor constrained results  is easier to tell apart.

### Group Wash by Group - Improved Wash Override When Group Market Segment Change

When the market segment of a group with a Wash override changes,G3 RMSnow correctly updates the override based on the change.

### Configure Permissions â Ability to Search Roles

On the Roles page, you can now search by name to quickly find what you need.

### Help Content - Best Practices Move to Standalone Topics

To prepare Help content for future improvements, most Best Practices sections inG3 RMSHelp are now in standalone Best Practices topics. This change is now complete as of June 8, 2026. What this means for you:

#### Update any saved or shared links.

Revise bookmarks, documentation, or shared links for Best Practices to direct to the new pages.
There are no changes to the content. Only the location of Best Practices content has changed.

### Other Fixes and Performance Improvements

## Release 10.4.1 - June 1 and 2, 2026

The following items were turned on in the 10.4.1 release.

### New Group Pricing Evaluation Page

#### Add Notes in Evaluations

We announced this for 10.3.3 but then postponed the release. You will now see the change one week after the 10.4.1 release dates, with deployment for all clients completed by Thursday, June 11, 2026.
Based on your suggestions inIDeaShare, you can now add notes when you run an evaluation on the Group Pricing Evaluation page. You can save more than one note, and each note shows who added it and when. If you use the Approval process, you can now access both the evaluation and approval notes with the same Notes icon.

#### Smaller File Size When You Download a Results PDF

When you download a PDF of an Evaluation Result, the file is now significantly smaller, making it easier for you to share and send the file via email.

### Configure Permissions - Option to Export the Authorization Groups

On the Authorization Groups page, you can now download a list of all groups, including their name, description, and rules.

### Faster Intraday Processing (IDP)

This was initially announced for the 10.3.1 release. We will now  enable these changes for all pricing products in 10.4.1.
The Intraday Processing Window now finishes faster after you save an override and if you had no other changes. Previously, the processing after an override used the full forecasting window, normally 365 days. Now, it uses the shorter IDP optimization window. If an override falls outside that window,G3 RMSextends the window to the override date plus 14 days.
For Independent Products,G3 RMSuses the last override date + twice the product's definedMaximum DaysforLength of Stay.

### Rate Shopping - Expanded View of Competitive Market Position Constraints

Based on your feedback in IDeaShare, you can now view more than three rows of your Competitive Market Position Constraints configuration on theCompetitor Settingstab. This makes it easier to review multiple constraints at once.

### User Activity Log Report - Improved for Function Space Properties

When you run a User Activity Log report, you now also see all Function Space activity in the Group Pricing Evaluation section.

### Other Fixes and Performance Improvements

## 10.3 Releases

The following items were turned on in the 10.3.4 release.

### Business Analysis Dashboard - Highlight When Ceiling or Floor Constrain the Price

Based on your suggestions inIDeaShare, you now see highlighting on the Floor and Ceiling rows in the Summary tab of the Business Analysis dashboard. This helps you quickly spot dates where your Pricing setup might constrain the RMS price, so you can decide whether to update your Floor or Ceiling.

### New Group Pricing Evaluation Results â Improved Display of Large Currency Values

On the Group Pricing Evaluation Results page, large currency values are now easier to read.

### Occupancy Forecast - Improved Estimate at the Market Segment Level

We announced this for 10.3.3 but then postponed its release. You will now see the change in 10.3.4.
The Occupancy Forecast includes not only the Forecast Group level, but also an estimate for the market segment level, seethe Note in this definition. Those market segment estimates include expected upgrades between Room Classes based on theUpgrade Path setup.
Based on your feedback, we have improved howG3 RMSestimates the upgrades of on the books business. After this change, you might see improvements in the Occupancy Forecast values at the market segment and room type level if the following are true:
- A Forecast Group contains multiple market segments.
A Forecast Group contains multiple market segments.
- The Forecast Group has business on the books.
The Forecast Group has business on the books.
- The system expects to upgrade at least some of that on the books business.
The system expects to upgrade at least some of that on the books business.
This change doesnotaffect:
- The Occupancy Forecast at the Forecast Group and Room Class level.
The Occupancy Forecast at the Forecast Group and Room Class level.
- The unconstrained demand forecast.
The unconstrained demand forecast.
- Any system outputs like pricing.
Any system outputs like pricing.

### Configure Permissions - Option to Export the Authorization Groups

On the Authorization Groups page you can now  download a list of all groups, including their name, description and rules.

### Coming Soon - Improved Pricing Overrides for Consistency and Clarity

The following improvements will make pricing overrides easier to understand when you review your prices :
- When you override at the Base Room Type level, you see the override icon only on the Base Room Type, even thoughG3 RMSmight change the prices of Non-Base Room Types based on Offsets. This gives you a clearer view with fewer icons and clarifies at what level you applied the override.
When you override at the Base Room Type level, you see the override icon only on the Base Room Type, even thoughG3 RMSmight change the prices of Non-Base Room Types based on Offsets. This gives you a clearer view with fewer icons and clarifies at what level you applied the override.
- When you change overrides at the Base Room Type level,G3 RMSnow automatically makes the changes for non-Base Room Types and you no longer must select the Apply/Delete overrides to all room types option, saving you time.
When you change overrides at the Base Room Type level,G3 RMSnow automatically makes the changes for non-Base Room Types and you no longer must select the Apply/Delete overrides to all room types option, saving you time.
- When you use a Specific override at the Base Room Type level, it triggers a Sync flag andG3 RMSconsiders the impact on demand and all outputs like Last Room Value in its optimization. Previously, the system did not optimize around a Specific Override in the Calendar view.
When you use a Specific override at the Base Room Type level, it triggers a Sync flag andG3 RMSconsiders the impact on demand and all outputs like Last Room Value in its optimization. Previously, the system did not optimize around a Specific Override in the Calendar view.

### Other Fixes and Performance Improvements

The following items were turned on in the 10.3.3 release.

### Configure Permissions â Option to Export Users

On the Users page you can now download a list of all users, including their Role, the creation date, and their last login date.

### Changes in the New Group Pricing Evaluation

#### Add Notes to Evaluations

POSTPONEDThe Evaluation Notes in Group Pricing will be released at a later date, view future release notes for updates.
Based on your suggestions in IDeaShare, you can now add notes for evaluations in Group Pricing. The note displays the name of the user and the date and time that the note was added. This allows you to record and review any information about the group.

#### User Activity Log Report Captures All Group Pricing Activity

You now see user actions from the redesigned Group Pricing pages in the User Activity Log report. This gives you a complete audit trail of Group Pricing evaluations, making it easier to track changes, support reviews, and meet reporting needs inG3 RMS.

#### Evaluation Results Page - Demand360 Uses RMS Currency

If you are using Demand360 and if that data arrives in a different currency, you now get more reliable comparisons when you review group evaluation results.G3 RMSnow converts the data to your RMS currency before using it in evaluations. This helps ensure ADR  comparisons are meaningful and aligned with how you manage pricing.
We will roll out this change in phases:
- On Thursday, April 23, 2026, we enable it for properties that have existing currency mismatches, updating the values for all past and current dates.
On Thursday, April 23, 2026, we enable it for properties that have existing currency mismatches, updating the values for all past and current dates.
- After that we enable it for all other properties to avoid future mismatches.The rollout finishes by Wednesday, May 6, 2026.
After that we enable it for all other properties to avoid future mismatches.The rollout finishes by Wednesday, May 6, 2026.

#### Evaluation Results Page - Updated Market Data Label

If your property has an integration forSmith Travel Research (STR)STR is a global provider of competitive benchmarking, information services and research to the hotel industry. STR reports provide property performance data compared to its competitive aggregate and general market, allowing you to follow trends in occupancy, average daily rate (ADR), revenue per available room (RevPAR)., we've replaced LY Market withLY Comp Seton the Evaluation Results ADR row for STR. This aligns with the other market data labels and doesnotaffect the displayed values.

### Occupancy Forecast - Improved Estimate at the Market Segment Level

POSTPONEDThe Occupancy Forecast - Improved Estimate at the Market Segment Level will be released at a later date, view the future release notes for the updates.
The Occupancy Forecast includes not only the Forecast Group level, but also an estimate for the market segment level, seethe Note in this definition. Those market segment estimates include expected upgrades between Room Classes based on theUpgrade Path setup.
Based on your feedback, we have improved howG3 RMSestimates the upgrades of on the books business. After this change, you might see improvements in the Occupancy Forecast values at the market segment and room type level if the following are true:
- A Forecast Group contains multiple market segments.
A Forecast Group contains multiple market segments.
- The Forecast Group has business on the books.
The Forecast Group has business on the books.
- The system expects to upgrade at least some of that on the books business.
The system expects to upgrade at least some of that on the books business.
This change doesnotaffect:
- The Occupancy Forecast at the Forecast Group and Room Class level.
The Occupancy Forecast at the Forecast Group and Room Class level.
- The unconstrained demand forecast.
The unconstrained demand forecast.
- Any system outputs like pricing.
Any system outputs like pricing.

### Other Fixes and Performance Improvements

The following items were turned on in the 10.3.2 release.

### Data Extraction Report â Add the Ceiling/Floor Values

In the Data Extraction report you can now include the configured Floor and Ceiling values. The report will show you the values:
- For theBase Room TypeThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.of theMaster ClassThe Room Class for which a value displays if there is only space in the RMS to show one, for example, when you see only one price on a page..
For theBase Room TypeThe one room type in each Room Class on which the RMS bases its pricing for the other room types in the Room Class.of theMaster ClassThe Room Class for which a value displays if there is only space in the RMS to show one, for example, when you see only one price on a page..
- By Occupancy Date.
By Occupancy Date.
- Only for thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..
Only for thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..

### Information Manager - Filter Labels for Exceptions Match the Exception Names

Based on your suggestions inIDeaShare, the filter labels will align with the actual Exception names. This makes it easier to pick the right Exception in the filter and avoids confusion when names are similar.

### Independent Products - Renaming Price Change Range to Blended Price

If you useIndependent Products, you now see a new name for thePrice Change Rangeconfiguration:Blended Price. The name change clarifies what this option does and aligns with how our clients commonly refer to it.
You see the new name in the Pricing configuration in the Advanced Settings menu, the page name, and in the existing warning message. As an example, the message now says: This product is configured for Blended Price with frequency of None and Monthly.

### Group Pricing Configuration - Best Practices on the Sales and Catering Status Codes Page

On the Sales and Catering Status Codes page in Group Pricing configuration, you now see a short best practice note. It explains how to define statuses on this page. Use it as a quick checklist while you set up or review your mapping.

### Group Pricing Evaluation Informs You When Group Pricing Configuration is Incomplete

In the new Group Pricing module,G3 RMSnow displays a message at the top of the Evaluation List page telling you when the Group Pricing configuration is incomplete for Ceiling and Floor, Servicing Cost, or Base Room Type. When this message displays, theNew Evaluationbutton is disabled. You can review the results of a saved evaluation, but you can't re-evaluate a group until the configuration is complete.

### Function Space Configuration -G3 RMSAutomatically Maps Market Segments

G3 RMSwill auto-assign new or unmapped Sales and CateringMarket Segmentsto the group segment with the highest volume. This prevents processing failures and speeds up setup. You still get an Alert in the Information Manager so you can review and update the mapping anytime  in the Function Space configuration in Market Segments.

### Data Feed - Function Space Configuration and Saved Evaluation Files (2 of 2)

You now get a second set of Function Space related files for enabled properties. The included files show current configuration and help you monitor the configuration for your properties.
We activate this on Wednesday, April 1, 2026.
With a subscription to the Configuration files, the following files are sent once per month for properties that use Function Space inG3 RMS.

##### FunctionSpaceDayParts

- Reports the Day Parts periods defined by the property - name, start time, and duration.
Reports the Day Parts periods defined by the property - name, start time, and duration.
- Specifications:FunctionSpaceDayParts_Spec.xlsx
Specifications:FunctionSpaceDayParts_Spec.xlsx
- File Sample:FunctionSpaceDayParts_20260301_0221_20171011_Monthly.psv
File Sample:FunctionSpaceDayParts_20260301_0221_20171011_Monthly.psv

##### FunctionSpaceForecastLevels

- Defines what the hotel considers as low, medium, and high forecast levels for the Demand Calendar heat map.
Defines what the hotel considers as low, medium, and high forecast levels for the Demand Calendar heat map.
- Specifications:FunctionSpaceForecastLevels_Spec File.xlsx
Specifications:FunctionSpaceForecastLevels_Spec File.xlsx
- File Sample:FunctionSpaceForecastLevels_20260301_0221_20171011_Monthly.psv
File Sample:FunctionSpaceForecastLevels_20260301_0221_20171011_Monthly.psv

##### FunctionSpaceIndivisibleFunctionRooms

- Lists the details for all indivisible function rooms that are set up in Function Room configuration.
Lists the details for all indivisible function rooms that are set up in Function Room configuration.
- Specifications:FunctionSpaceIndivisibleFunctionRooms_Spec.xlsx
Specifications:FunctionSpaceIndivisibleFunctionRooms_Spec.xlsx
- File Sample:FunctionSpaceIndivisibleFunctionRooms_20260301_0221_20171011_Monthly.psv
File Sample:FunctionSpaceIndivisibleFunctionRooms_20260301_0221_20171011_Monthly.psv

##### FunctionSpacePackageElementsConfiguration

- Lists the details of all Function Space Package Elements.
Lists the details of all Function Space Package Elements.
- Specifications:FunctionSpacePackageElements_Spec.xlsx
Specifications:FunctionSpacePackageElements_Spec.xlsx
- File Sample:CPGP02_FunctionSpacePackageElementsConfiguration_20260301_0221_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpacePackageElementsConfiguration_20260301_0221_20171011_Monthly.psv

##### FunctionSpacePackageConfiguration

- Lists the details of all Function Space Packages, for example, the included Package Elements.
Lists the details of all Function Space Packages, for example, the included Package Elements.
- Specifications:FunctionSpacePackageConfiguration_Spec.xlsx
Specifications:FunctionSpacePackageConfiguration_Spec.xlsx
- File Sample:FunctionSpacePackageConfiguration_20260301_0221_20171011_Monthly.psv
File Sample:FunctionSpacePackageConfiguration_20260301_0221_20171011_Monthly.psv

### Other Fixes and Performance Improvements

The following items were turned on in the 10.3.1 release.

### Well Wishes and Managing Your RMS in Disrupted Periods

In recent weeks, some hotels across the globe have experienced unexpected shifts in demand driven by a mix of factors, including severe weather and localized social or geopolitical disruptions. While the specific causes and impacts vary by region, we recognize that these events can create uncertainty for our clients, their teams, and the guests they serve.
At IDeaS, the safety and well‑being of our clients, partners, and their communities remain foremost in our thoughts. We hope each of youâand your teamsâremain safe during these periods of disruption.
As a gentle reminder, our RMS Help Center includes guidance on how to manage your system when demand patterns become irregular. You can find step‑by‑step support here:Demand Disruptions.
These resources outline best practices for adjusting forecasts, understanding the effects of extraordinary events, and ensuring your system continues to support sound, data‑driven decisions during turbulent periods.

### Group Pricing Evaluation - Export the List to Excel

On the new Group Pricing landing page you can export a list of your saved evaluations to Excel. The export includes evaluation details and the date range defined on the page.

### Business Insights Dashboard - Label Changes

The following changes on theBusiness Insightsdashboard clarify rate code and revenue labels and align them across the different optimization types. They apply to both the This Year and Last Year views.
- Rate Value changes to:Rate Code Value
Rate Value changes to:Rate Code Value
- Rate Value Last Year changes to:Rate Code Value Last Year
Rate Value Last Year changes to:Rate Code Value Last Year
- All Inclusive Rate changes to:Rate Code Value â All Inclusive
All Inclusive Rate changes to:Rate Code Value â All Inclusive
- All Inclusive Rate Last Year changes to:Rate Code Value Last Year â All Inclusive
All Inclusive Rate Last Year changes to:Rate Code Value Last Year â All Inclusive
- Total Revenue changes to:Total Folio Revenue
Total Revenue changes to:Total Folio Revenue

### Pricing â Faster Processing After an Override

Like the improved Sync (see 9.8.4 release), theIntraday ProcessingAbbreviated IDP, it's a system update that occurs between nightly updates. For details search for the Processing topic. Also known as Current Day Processing (CDP).now finishes faster after you save an override and if you made no other changes. Previously, the processing after an override used the full forecasting window, normally 365 days. Now, it uses the shorter IDP optimization window. If an override falls outside that window,G3 RMSextends the window to the override date plus 14 days.
For Independent Products,G3 RMSuses the last override date + twice the productâs definedMaximum DaysforLength of Stay.
These changes significantly shorten the duration of the IDP.
The earlier Sync improvements now also apply to Independent Products:
After an override for an Independent Product, clickingandSync AllorSync All and Uploadnow triggers a shorter process. Instead of using the full optimization window,G3 RMSonly syncs the period from today until the last override date + twice the productâs definedMaximum DaysforLength of Stay, but never beyond yourOptimization WindowThe number of days for which the RMS produces outputs (like pricing) and a constrained occupancy forecast. You can view the optimized outputs and occupancy forecast for the Optimization Window, but the system only sends outputs for the Upload Window. The Optimization Window usually matches and can't be longer than the Forecast Window..

### Pricing Configuration - Improved Mapping of Rate Codes when Defining Your Priced Products

In the Definition tab of Pricing configuration, when you map products like Linked and Independent to rate codes you will notice the following improvement that ensures the best possible setup.
These changes do not affect your existing products. They apply only when you make configuration changes in the future.
If a rate code belongs to market segments attributed asEqual to BAR(Equal to Base Product if you use Independent products) and as Forecast TypeDemand and Wash, it no longer displays as a mapping option on the left under Rate Codes. This applies to attribution at both the Market Segment and Rate Code level.
You can still view and map rate codes that are attributed asLinked to BAR(or Linked to Base Product).
If a rate code belongs to market segments attributed asEqual to BAR(or Equal to Base Product) and as Forecast TypeDemand and Wash, you can map only an Independent Product to the rate code.
In market segment configuration, either at the rate code or the market segment level, when you change an attribute that affects the mapped rate codes for a Linked or Independent product, a message now shows you all the rate codes to be unmapped and for which product they are unmapped. This helps you understand how your attribute change affects the configuration of your priced products.

### New Alert - Unassigned Sales and Catering Status Code

Properties with anintegration to AmadeusSales & Event Management (ASEM) now receive an Alert in the Information Manager whenG3 RMSis ready to use tentative group forecasting.
To enable it, click the link under How do I action the Alert? and assign at least one Sales and Catering Status Codes as Tentative.
The Alert doesnotapply to properties using Opera PMS Cloud or Opera Sales Event Management Cloud (OSEM).

### Use of Physical or Effective Capacity in KPIs â View Your Setting inG3 RMS

WhenG3 RMScalculates metrics such as Forecast %, On Books %, or RevPAR, it can usePhysicalThe total number of guest rooms at a property, including out of order rooms.orEffective CapacityThe property's physical capacity minus the out of order rooms.. You can now see which applies to your property on the Property Information tab in Property Specific configuration. Unchanged is that  the authorized person at a company has to  contact IDeaS to update the setting.

### Data Feed - Function Space Configuration and Saved Evaluation Files (1 of 2)

For enabled properties you now getFunction Spaceinformation in the Data Feed. The new files show the current configuration and the saved evaluations from the past 7 days. These files help you monitor the configuration and the evaluations of your properties.
We activate this on Wednesday, March 11, 2026. See the Coming Soon announcement for additional files.
For properties that use Function Space inG3 RMS:
- The Configuration files are sent monthly on the designated day if you have a Configuration  subscription.
The Configuration files are sent monthly on the designated day if you have a Configuration  subscription.
- The FunctionSpaceEvaluation file is sent weekly and includes all evaluations from the last 7 days. This file is provided with the core Data Feed.
The FunctionSpaceEvaluation file is sent weekly and includes all evaluations from the last 7 days. This file is provided with the core Data Feed.

##### FunctionSpaceServicingCost

Shows the per room servicing cost by Room Class and your preferred unit of measurement.
- Specifications:FunctionSpaceServicingCost_Spec.xlsx
Specifications:FunctionSpaceServicingCost_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceServicingCost_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceServicingCost_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceConferenceandBanquet

- Shows the conference and banquet revenue streams and their profit percentage.
Shows the conference and banquet revenue streams and their profit percentage.
- Specifications:FunctionSpaceConferenceandBanquet_Spec.xlsx
Specifications:FunctionSpaceConferenceandBanquet_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceConferenceandBanquet_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceConferenceandBanquet_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceAncillary

- Shows the ancillary revenue and profit percentage defined for each revenue stream by market segment.
Shows the ancillary revenue and profit percentage defined for each revenue stream by market segment.
- Specifications:FunctionSpaceAncillary_Spec.xlsx
Specifications:FunctionSpaceAncillary_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceAncillary_20260224_0648_20170910_Monthly.psv
File Sample:CPGP02_FunctionSpaceAncillary_20260224_0648_20170910_Monthly.psv

##### FunctionSpaceStatusCodes

- Shows the block statuses defined for each sales and catering Group status code when the systems are integrated.
Shows the block statuses defined for each sales and catering Group status code when the systems are integrated.
- Specifications:FunctionSpaceStatusCodes_Spec.xlsx
Specifications:FunctionSpaceStatusCodes_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceStatusCodes_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceStatusCodes_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceSCMarketSegmentMapping

- Shows how market segment codes used in the sales and catering system are assigned to the RMS market segment codes when the systems are integrated.
Shows how market segment codes used in the sales and catering system are assigned to the RMS market segment codes when the systems are integrated.
- Specifications:FunctionSpaceSCMarketSegmentMapping_Spec.xlsx
Specifications:FunctionSpaceSCMarketSegmentMapping_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceSCMarketSegmentMapping_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceSCMarketSegmentMapping_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceSCGuestRTMapping

- Shows how guest room types used in the sales and catering system are assigned to the RMS room types when the system are integrated.
Shows how guest room types used in the sales and catering system are assigned to the RMS room types when the system are integrated.
- Specifications:FunctionSpaceSCRoomTypeMapping_Spec.xlsx
Specifications:FunctionSpaceSCRoomTypeMapping_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceSCGuestRTMapping_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceSCGuestRTMapping_20260224_0648_20171011_Monthly.psv

##### FunctionSpacePreferredRoomType

- Shows which room types are permitted to be used in evaluations.
Shows which room types are permitted to be used in evaluations.
- Specifications:FunctionSpacePreferredRoomType_Spec.xlsx
Specifications:FunctionSpacePreferredRoomType_Spec.xlsx
- File Sample:CPGP02_FunctionSpacePreferredRoomType_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpacePreferredRoomType_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceEventTypes

- Defines which function space event types are used for out of order.
Defines which function space event types are used for out of order.
- Specifications:FunctionSpaceEventTypes_Spec.xlsx
Specifications:FunctionSpaceEventTypes_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceEventTypes_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceEventTypes_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceMinProfit

- Shows the minimum profit rules defined by the property.
Shows the minimum profit rules defined by the property.
- Specifications:FunctionSpaceMinProfit_Spec.xlsx
Specifications:FunctionSpaceMinProfit_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceMinProfit_20260224_0648_20171011_Monthly.psv
File Sample:CPGP02_FunctionSpaceMinProfit_20260224_0648_20171011_Monthly.psv

##### FunctionSpaceCeilingFloor

- Shows the default and seasonal Ceiling and Floor threshold defined by the property for group pricing.
Shows the default and seasonal Ceiling and Floor threshold defined by the property for group pricing.
- Specifications:FunctionSpaceCeilingFloor_Spec.xlsx
Specifications:FunctionSpaceCeilingFloor_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceCeilingFloor_20260224_0648_20170910_Monthly.psv
File Sample:CPGP02_FunctionSpaceCeilingFloor_20260224_0648_20170910_Monthly.psv

##### FunctionSpaceEvaluation

- Shows the evaluations that were run and saved in the last 7 days.
Shows the evaluations that were run and saved in the last 7 days.
- Specifications:FunctionSpaceEvaluation_Spec.xlsx
Specifications:FunctionSpaceEvaluation_Spec.xlsx
- File Sample:CPGP02_FunctionSpaceSavedEvaluation_20260224_0648_20171004_Weekly.psv
File Sample:CPGP02_FunctionSpaceSavedEvaluation_20260224_0648_20171004_Weekly.psv

### Coming Soon - Data Feed - Function Space Configuration and Saved Evaluation Files (2 of 2)

For enabled properties you will soon get a second set of Function Space files. The included files show current configuration and help you monitor the configuration for your properties.
We plan to activate this on  Wednesday, April 1, 2026. Watch the upcoming release announcements for the confirmed date.
For properties that use Function Space inG3 RMSthe following files are sent once per month:

##### FunctionSpaceDayParts

- Reports the Day Parts periods defined by the property - name, start time, and duration.
Reports the Day Parts periods defined by the property - name, start time, and duration.
- Specifications:FunctionSpaceDayParts_Spec file.xlsx
Specifications:FunctionSpaceDayParts_Spec file.xlsx
- File Sample:view sample files in a future release announcement.
File Sample:view sample files in a future release announcement.

##### FunctionSapceForecastLevels

- Defines what the hotel considers as low, medium, and high forecast levels for the Demand Calendar heatmap.
Defines what the hotel considers as low, medium, and high forecast levels for the Demand Calendar heatmap.
- Specifications:FunctionSapceForecastLevels_Spec File.xlsx
Specifications:FunctionSapceForecastLevels_Spec File.xlsx
- File Sample:
File Sample:

##### FunctionSpaceIndivisibleFunctionRooms

- Lists the details for all indivisible function rooms that are set up in Function Rooms configuration.
Lists the details for all indivisible function rooms that are set up in Function Rooms configuration.
- Specifications:FunctionSpaceIndivisibleFunctionRooms_Spec.xlsx
Specifications:FunctionSpaceIndivisibleFunctionRooms_Spec.xlsx
- File Sample:
File Sample:

##### FunctionSpacePackageElementsConfiguration

- Lists the details of all Function Space Package Elements.
Lists the details of all Function Space Package Elements.
- Specifications:FunctionSpacePackageElements_Spec.xlsx
Specifications:FunctionSpacePackageElements_Spec.xlsx
- File Sample:
File Sample:

##### FunctionSpacePackageConfiguration

- Lists the details of all Function Space Packages, for example, the included Package Elements.
Lists the details of all Function Space Packages, for example, the included Package Elements.
- Specifications:FunctionSpacePackageConfiguration_Spec.xlsx
Specifications:FunctionSpacePackageConfiguration_Spec.xlsx
- File Sample:
File Sample:

### Other Fixes and Performance Improvements

## 10.2 Releases

The following items were turned on in the 10.2.4 release.

### Well Wishes and Managing Your RMS in Disrupted Periods

In recent weeks, some hotels across the globe have experienced unexpected shifts in demand driven by a mix of factors, including severe weather and localized social or geopolitical disruptions. While the specific causes and impacts vary by region, we recognize that these events can create uncertainty for our clients, their teams, and the guests they serve.
At IDeaS, the safety and well‑being of our clients, partners, and their communities remain foremost in our thoughts. We hope each of youâand your teamsâremain safe during these periods of disruption.
As a gentle reminder, our RMS Help Center includes guidance on how to manage your system when demand patterns become irregular. You can find step‑by‑step support here:Demand Disruptions.
These resources outline best practices for adjusting forecasts, understanding the effects of extraordinary events, and ensuring your system continues to support sound, data‑driven decisions during turbulent periods.

### Optimized Linked Products - Price Ranking between Room Classes Enforced by Final Price

WhenG3 RMSdetermines the adjustments by Room Class for an Optimized Linked Product, it uses Final Price to ensure that a higher-ranked Room Class is priced higher than a lower-ranked one. Previously it applied the Price Ranking to the adjustments themselves.
This improved approach ensures better pricing by Room Class, for example, by enablingG3 RMSto apply a higher adjustment to a higher-ranked Room Class with a low LRV while setting a lower adjustment for a lower-ranked Room Class with a high LRV.
We enable this change for clients in phases, completed  by Tuesday, March 17, 2026. Contact your IDeaS representative to learn when it's enabled for you.

### Channel Forecast Dashboard - New Option to Select the Source

Based on your suggestion in IDeaShare, theChannel Forecast dashboardnow gives you another option to view source-level data.
Currently the option calledSourceallows you to choose up to five sources per channel, but you couldn't view a sourceâs totals across all channels. This option still exists but is renamed toSource by Channel.
The new option is calledSourceand enables you to:
- Select up to five sources for the property, and
Select up to five sources for the property, and
- View each selected sourceâs totals across all the channels that it belongs to.
View each selected sourceâs totals across all the channels that it belongs to.

### Group Floor Overrides - Improved Handling of Group Block Changes

If you enabledGroup Floor Overrides, your settings for individual block days now remain unchanged after minor block adjustments like extending pre- or post-block days.

### Price Drop Restriction Values Become Tax-Inclusive:

If your property is in a country withTax-Inclusive PricingTax-inclusive pricing applies in countries where quoted and booked prices have to include taxes like a Value-Added Tax (VAT) or Goods and Services Tax (GST). If you are not in a country with tax-inclusive pricing, taxes are added to pricing only at the point of payment.

In G3 RMS, tax-inclusive pricing is enabled and configured in Property Specific Configuration.and usesPrice Drop Restrictions,G3 RMSnow considers the configured values forRevenue Threshold for PriceandMaximum Price Dropto be tax-inclusive. Previously you entered these values as tax-exclusive. This change aligns with how you enter other values such as Ceiling/Floor, ensuring consistency across the system.

### Group Pricing Configuration â Renamed the Status Code Tab

If your property has anintegration to a sales and catering system(like Delphi) and you go to configure Group Pricing you see a new tab name,Sales and Catering Status Codes. This name replaces the previous one,Status Codes, to clarify its purpose and to better differentiate it fromGroup Status Codes.

### Coming Soon - Improved Mapping of Rate Codes when Defining Your Priced Products

In the Definition tab of Pricing configuration, when you map products like Linked and Independent to rate codes you will notice the following improvement that ensures the best possible setup.
These changes do not affect your existing products. They apply only when you make configuration changes in the future.
If a rate code belongs to market segments attributed asEqual to BAR(Equal to Base Product if you use Independent products) and as Forecast TypeDemand and Wash, it no longer displays as a mapping option on the left under Rate Codes. This applies to attribution at both the Market Segment and Rate Code level.
You can still view and map rate codes that are attributed asLinked to BAR(or Linked to Base Product).
If a rate code belongs to market segments attributed asEqual to BAR(or Equal to Base Product) and as Forecast TypeDemand and Wash, you can map only an Independent Product to the rate code.
In market segment configuration, either at the rate code or the market segment level, when you change an attribute that affects the mapped rate codes for a Linked or Independent product, a message now shows you all the rate codes to be unmapped and for which product they are unmapped. This helps you understand how your attribute change affects the configuration of your priced products.

### Coming Soon - Data Feed - Function Space Configuration and Saved Evaluation Files

For enabled properties you will soon getFunction Spaceinformation in the Data Feed. The new files show the current configuration and the saved evaluations from the past 7 days. These files help you monitor the configuration and the evaluations of your properties.
Watch upcoming release announcements for the release dates and for additional files.
For properties that use Function Space inG3 RMS:
- The Configuration files are sent monthly on the designated day if you have a Configuration  subscription.
The Configuration files are sent monthly on the designated day if you have a Configuration  subscription.
- The FunctionSpaceEvaluation file is sent weekly and includes all evaluations from the last 7 days. This file is provided with the core Data Feed.
The FunctionSpaceEvaluation file is sent weekly and includes all evaluations from the last 7 days. This file is provided with the core Data Feed.

##### FunctionSpaceServicingCost

Shows the per room servicing cost by Room Class and your preferred unit of measurement.
- Specifications:FunctionSpaceServicingCost_Spec.xlsx
Specifications:FunctionSpaceServicingCost_Spec.xlsx
- File Sample: view sample files in the final release announcement.
File Sample: view sample files in the final release announcement.

##### FunctionSpaceConferenceandBanquet

Shows the conference and banquet revenue streams and their profit percentage.
Specifications:FunctionSpaceConferenceandBanquet_Spec.xlsx
File Sample:

##### FunctionSpaceAncillary

Shows the ancillary revenue and profit percentage defined for each revenue stream by market segment.
Specifications:FunctionSpaceAncillary_Spec.xlsx
File Sample:

##### FunctionSpaceStatusCodes

Shows the block statuses defined for each sales and catering Group status code when the systems are integrated.
Specifications:FunctionSpaceStatusCodes_Spec.xlsx
File Sample:

##### FunctionSpaceSCMarketSegmentMapping

Shows how market segment codes used in the sales and catering system are assigned to the RMS market segment codes when the systems are integrated.
Specifications:FunctionSpaceSCMarketSegmentMapping_Spec.xlsx
File Sample:

##### FunctionSpaceSCGuestRTMapping

Shows how guest room types used in the sales and catering system are assigned to the RMS room types when the system are integrated.
Specifications:FunctionSpaceSCRoomTypeMapping_Spec.xlsx
File Sample:

##### FunctionSpacePreferredRoomType

Shows which room types are permitted to be used in evalatuions.
Specifications:FunctionSpacePreferredRoomType_Spec.xlsx
File Sample:

##### FunctionSpaceEventTypes

Defines which function space event types are used for out of order.
Specifications:FunctionSpaceEventTypes_Spec.xlsx
File Sample:

##### FunctionSpaceMinProfit

Shows the minimum profit rules defined by the property.
Specifications:FunctionSpaceMinProfit_Spec.xlsx
File Sample:

##### FunctionSpaceCeilingFloor

Shows the default and seasonal Ceiling and Floor threshold defined by the property for group pricing.
Specifications:FunctionSpaceCeilingFloor_Spec.xlsx
File Sample:

##### FunctionSpaceEvaluation

Shows the evaluations that were run and saved in the last 7 days.
Specifications:FunctionSpaceEvaluation_Spec.xlsx
File Sample:

### Other Fixes and Performance Improvements

The following items were turned on in the 10.2.3 release.

### Demand and Wash Overrides â Simplified Increase/Decrease Option

You can now  enter a positive value for an increase and a negative value (like -10) for a decrease when you apply a percentage change in an Occupancy Date demand override. Previously you had to select Increase or Decrease when entering the value. This matches the change for the Arrival by LOS demand override released in 10.1.2.

### Business Analysis - Pace Data Dashboard - Improved Visibility of Chart Lines

Based on yourIDeaSharerequest, we darkened the chart lines in the Pace Data dashboard. The new colors, especially the light yellow, allow you to better see the lines against the white background.

### The Alert Rate Shopping Data Did Not Arrive Shows the Shopping Window

The Information Manager Alert, Rate Shopping Data Did Not Arrive, now shows the shopped periods for whichG3 RMSdidnât receive the data at the time defined in the Rate Shopping Schedule tab. You can see the impacted period for whichG3 RMSstopped using the data in the Alert Details, when you click the Alert.
For example, your hotel shops competitor prices daily for the next 90 days and weekly for 180 days. The weekly shop didnât arrive and the RMS stopped using its data . But you did get the daily 90-day file. In that case, the Alert Details tells you thatG3 RMSstopped using the data only for the [91-180] day period.
This is especially helpful if you have multiple shopped windows because it helps you understand exactly which periodsG3 RMSno longer uses for forecasting and pricing recommendations. This change is based on your feedback in IDeaShare.
Check to ensure that your rate shopping schedule is set up. Otherwise, the system uses a default staleness of 30 days, and you do not see the missing window in the Alert Details.

### Group Pricing - Evaluation List Loads Faster

Based on your feedback on the new Group Pricing design, the Evaluation List page now loads faster because, by default, it displays evaluations from the previous 30 instead of the previous 90 days. You can still filterto view more evaluations.

### Other Fixes and Performance Improvements

The following items were turned on in the 10.2.2 release.

### Tentative Booking Data for Improved Group Forecasts Available to More Clients

Tentative Group Forecasts provide you with improved group forecasts by giving the RMS insight into the full life-cycle of a booking, not limited to when the blocks deduct from inventory. With this additional dataG3 RMShas more history to provide the best possible group forecasts, based on historical performance by market segment, day of week, and time to arrival. Seegroup forecastingfor details.
Previously that capability was only available to clients with an Amadeus Delphi sales and catering system. Now itâs also available to clients with an OHIP PMS Integration.

### Delphi Integration Properties - Conference & Banquet Revenue Streams Auto-Completed

For properties with theDelphi Sales & Catering integration,G3 RMSnow completes the revenue streams in the Conference & Banquet tab of Group Pricing Configuration for you, based on your Delphi setup. In future implementations, this saves you setup time. For properties with an existing revenue stream configuration, we merge the setup ofG3 RMSand Delphi using the following process:
- Revenue streams with matching names between the two systems are merged.The names must have an exact match (but not case sensitive).The configuredG3 RMSprofit % remains unchanged.For a merged revenue stream, you can change the profit % but not the name.You canât delete a merged revenue stream.
Revenue streams with matching names between the two systems are merged.
- The names must have an exact match (but not case sensitive).
The names must have an exact match (but not case sensitive).
- The configuredG3 RMSprofit % remains unchanged.
The configuredG3 RMSprofit % remains unchanged.
- For a merged revenue stream, you can change the profit % but not the name.
For a merged revenue stream, you can change the profit % but not the name.
- You canât delete a merged revenue stream.
You canât delete a merged revenue stream.
- Revenue streams inG3 RMSthat donât match a Delphi revenue stream remain unchanged and you can continue to edit them.
Revenue streams inG3 RMSthat donât match a Delphi revenue stream remain unchanged and you can continue to edit them.
- Revenue streams in Delphi that donât match aG3 RMSrevenue stream are added inG3 RMSwith a default profit % of 0.00%. You can change the profit % of such an added revenue stream inG3 RMS, but not the name.
Revenue streams in Delphi that donât match aG3 RMSrevenue stream are added inG3 RMSwith a default profit % of 0.00%. You can change the profit % of such an added revenue stream inG3 RMS, but not the name.
Notes:
- The merging doesnât impact how you run a group pricing evaluation or the recommendations.
The merging doesnât impact how you run a group pricing evaluation or the recommendations.
- We will enable the merging for clients in phases after January 6, 2026. Contact your IDeaS representative to learn when itâs enabled for you.
We will enable the merging for clients in phases after January 6, 2026. Contact your IDeaS representative to learn when itâs enabled for you.

### Automatic Group Floor Override Removal at Cut Off Date

If you enabledGroup Floor Overridesyou can now configure them to exclude group blocks whose contractual cut-off date has passed. This gives you more pricing flexibility after group commitments expire.
We plan to activate this on Wednesday, January 7, 2026.

### The Exception - Specific Override Below LRV - Lists Only the Initial and Latest Records

When thePricing User Specified Override below LRVException  remains unresolved,G3 RMSnow lists only twoLRVA control that blocks lower-valued yieldable business when the RMS thinks that your property might sell out. It ensures that you accept only the most valuable demand. For example, a $150 LRV means that guests can book a Flexible Rate product at $160, but not a discounted PrePay&Save product at $140. The RMS optimizes LRV by Room Class.values in the Details section, the newest and the oldest value. Previously, you saw the LRV value for every date that the Exception remained unresolved, sometimes leading to a long list of exception details. This made the details difficult to read, and for Data Feed clients, caused large data sizes.
Of the following changes, we  activate the first two (the new files) on Wednesday, January 7, 2026, 8:00 AM CST. The third change occurs on your regular release date.

#### New Component Room Configuration File

If you have an active subscription to Configuration files, the new ComponentRoomsConfiguration file enables you to monitor the configuration details for properties withComponent Rooms.
Additional Information:
- File Name: ComponentRoomsConfiguration
File Name: ComponentRoomsConfiguration
- Level: Property
Level: Property
- G3 Data Feed Bucket: Configuration
G3 Data Feed Bucket: Configuration
- Delivery Frequency: Monthly
Delivery Frequency: Monthly
- Delivery Period: Full current configuration
Delivery Period: Full current configuration
- Dependency: Distributed only to properties with an enabled Component Rooms feature.
Dependency: Distributed only to properties with an enabled Component Rooms feature.
- Sample file
Sample file
- Spec file
Spec file

#### New Servicing Cost by LOS Configuration File

If you have an active subscription to Configuration files, the new ServicingCostbyLOSConfiguration file enables you to monitor configuration details for properties with theServicing Cost by LOSfeature.
Additional Information:
- File Name: ServicingCostbyLOSConfiguration
File Name: ServicingCostbyLOSConfiguration
- Level: Property
Level: Property
- G3 Data Feed Bucket: Configuration
G3 Data Feed Bucket: Configuration
- Delivery Frequency: Weekly
Delivery Frequency: Weekly
- Delivery Period: All Available Configuration
Delivery Period: All Available Configuration
- Dependency: Distributed exclusively for properties with this configuration feature enabled
Dependency: Distributed exclusively for properties with this configuration feature enabled
- Sample file
Sample file
- Spec file
Spec file

#### Change in the Reported Period for the ForecastArrivalsDepartures File

The period that is reported in the ForecastArrivalsDepartures Data Feed file changes to System Date through System Date + 21 days (previously  System Date -1 through System Date + 21). This removes the redundant and irrelevant past date.
The following items were turned on in the 10.2.1 release.

### Data Extraction Report - Allow Up to 15 Competitors

Based on many suggestions from you inIDeaShare, the Data Extraction report will allow you to select up to 15 competitors. Previously, you were limited to five and had to run multiple reports to see more competitors. The available competitors in the report are based on the ones you set up in Competitor Settings tab in Rate Shopping.

### Improved Ceiling/Floor Suggestions byG3 RMS

G3 RMSnow recommends more accurate Ceiling/Floor values after you click Suggest in Pricing configuration. Thatâs because the system now better manages competitors with extreme pricing.

### Function Space - Recommended Rental by Function Room and by Occupancy Date

In the results of a Function Space evaluation, the Recommended Rental is a single value for all requested meeting rooms during the group stay. Soon you can view the Recommended Rental at the overall summary level and by Function Room and Occupancy Date. This helps you to easily quote the rental amount at a detailed level to your clients.
To see the details, open the Evaluation Results tab, click View Details, and go to the newFunction Space Recommended Price Detailssection.
Soon you will be able to configureGroup Floor Overridesto exclude group blocks whose contractual cut-off date has passed. This gives you more pricing flexibility after group commitments expire.
We plan to activate this on Wednesday, January 7, 2026. Look for the confirmed date and more details in a future release announcement.
Of the following three changes, we plan to activate the first two (the new files) on Wednesday, January 7, 2026, 8:00 AM CST. Look for their confirmed date in a future release announcement.

#### New Component Room Configuration File

If you have an active subscription to Configuration files, the new ComponentRoomsConfiguration file will enable you to monitor the configuration details for properties withComponent Rooms.
Additional Information:
- File Name: ComponentRoomsConfiguration
File Name: ComponentRoomsConfiguration
- Level: Property
Level: Property
- G3 Data Feed Bucket: Configuration
G3 Data Feed Bucket: Configuration
- Delivery Frequency: Monthly
Delivery Frequency: Monthly
- Delivery Period: Full current configuration
Delivery Period: Full current configuration
- Dependency: Distributed only to properties with an enabled Component Rooms feature.
Dependency: Distributed only to properties with an enabled Component Rooms feature.
- Spec file
Spec file

#### New Servicing Cost by LOS Configuration File

If you have an active subscription to Configuration files, the new ServicingCostbyLOSConfiguration file will enable you to monitor configuration details for properties with theServicing Cost by LOSfeature.
Additional Information:
- File Name: ServicingCostbyLOSConfiguration
File Name: ServicingCostbyLOSConfiguration
- Level: Property
Level: Property
- G3 Data Feed Bucket: Configuration
G3 Data Feed Bucket: Configuration
- Delivery Frequency: Weekly
Delivery Frequency: Weekly
- Delivery Period: All Available Configuration
Delivery Period: All Available Configuration
- Dependency: Distributed exclusively for properties with this configuration feature enabled
Dependency: Distributed exclusively for properties with this configuration feature enabled
- Spec file
Spec file

#### Change in the Reported Period for the ForecastArrivalsDepartures File

The period that is reported in the ForecastArrivalsDepartures Data Feed file will change to System Date through System Date + 21 days (previously  System Date -1 through System Date + 21). This removes the redundant and irrelevant past date.
We will make this change with the 10.2.2 deployment.

### Other Fixes and Performance Improvements

## 10.1 Releases

The following items were turned on in the 10.1.4 release.

### Improved Group Pricing Evaluations

We are excited to announce that we redesigned and updated Group Pricing Evaluations to provide expanded results, actionable insights, and tools tailored for salespeople, to help your sales teams move quickly and negotiate with confidence.
To learn more about the new features of the improved Group Pricing evaluations, view the video below, or click below to see a description with images. When you start using the new design, you can also use Show Me to walk through the new pages in more detail.
Your browser does not support the video tag.
When you click to manage Group Pricing, the page opens in a new browser tab. Help topics exist for both versions. Access Help for the new version  from the new location. For the old version,  click the ? icon on a page of the old group evaluation version.
We enable the updated Group Pricing between Thursday,  December 4 and  Wednesday, December 10,  2025.  Contact your IDeaS representative to learn when it's enabled for you.
- Simplified Evaluation ListProvides a simplified design with clear navigation to evaluate new groups or review saved evaluations.Use the filter to sort the evaluations that display, such as the evaluation date range or the market segment to which the group belongs.Quick Links allow you to quickly access related pages inG3 RMS, like Group Pricing Configuration.
Simplified Evaluation List
- Provides a simplified design with clear navigation to evaluate new groups or review saved evaluations.
Provides a simplified design with clear navigation to evaluate new groups or review saved evaluations.
- Use the filter to sort the evaluations that display, such as the evaluation date range or the market segment to which the group belongs.
Use the filter to sort the evaluations that display, such as the evaluation date range or the market segment to which the group belongs.
- Quick Links allow you to quickly access related pages inG3 RMS, like Group Pricing Configuration.
Quick Links allow you to quickly access related pages inG3 RMS, like Group Pricing Configuration.
- Expanded Evaluation ResultsHighlight key data and options to drill down for more details like displacement and profit analysis.See a range of prices that include the Recommended Price, and a Wish and Walk Price to support pricing negotiations with prospective groups.If your subscription includes STR or Demand360, you can view forecast and performance metrics directly in your evaluation.
Expanded Evaluation Results
- Highlight key data and options to drill down for more details like displacement and profit analysis.
Highlight key data and options to drill down for more details like displacement and profit analysis.
- See a range of prices that include the Recommended Price, and a Wish and Walk Price to support pricing negotiations with prospective groups.
See a range of prices that include the Recommended Price, and a Wish and Walk Price to support pricing negotiations with prospective groups.
- If your subscription includes STR or Demand360, you can view forecast and performance metrics directly in your evaluation.
If your subscription includes STR or Demand360, you can view forecast and performance metrics directly in your evaluation.
- Rules Configuration and Approval ProcessYou can use Rules Configuration to set up approval rules and automate the Group Pricing approval process.The approval rules automatically trigger during the evaluation process.If the group doesn't meet the rule criteria during the evaluation, a red banner displays on the Evaluation Results page, and the approver receives an email with key details and a link to review.Approvers can approve or reject directly from the email or view the full evaluation in Group Pricing. Then the evaluator receives an email of the updated status, and the evaluation automatically updates in Group Pricing.
Rules Configuration and Approval Process
- You can use Rules Configuration to set up approval rules and automate the Group Pricing approval process.
You can use Rules Configuration to set up approval rules and automate the Group Pricing approval process.
- The approval rules automatically trigger during the evaluation process.
The approval rules automatically trigger during the evaluation process.
- If the group doesn't meet the rule criteria during the evaluation, a red banner displays on the Evaluation Results page, and the approver receives an email with key details and a link to review.
If the group doesn't meet the rule criteria during the evaluation, a red banner displays on the Evaluation Results page, and the approver receives an email with key details and a link to review.
- Approvers can approve or reject directly from the email or view the full evaluation in Group Pricing. Then the evaluator receives an email of the updated status, and the evaluation automatically updates in Group Pricing.
Approvers can approve or reject directly from the email or view the full evaluation in Group Pricing. Then the evaluator receives an email of the updated status, and the evaluation automatically updates in Group Pricing.
Notes:
- Users with existing permission to use Group Pricing Evaluations will have  their roles and permissions automatically transfer to the new pages.
Users with existing permission to use Group Pricing Evaluations will have  their roles and permissions automatically transfer to the new pages.
- All the existing saved evaluations automatically transfer to the new Group Pricing module.
All the existing saved evaluations automatically transfer to the new Group Pricing module.
- If needed, click the togglein the top right on the Evaluation List page to temporarily switch back to the old version.
If needed, click the togglein the top right on the Evaluation List page to temporarily switch back to the old version.
- Multi-Property and Function Space evaluations remain unchanged. We plan on announcing an improved functionality in a future release.
Multi-Property and Function Space evaluations remain unchanged. We plan on announcing an improved functionality in a future release.

### Unified Labels for Hot Start and Limited Data Build (LDB)

We are streamlining the names of build types for properties with limited or evolving historical data. The changes clarify and simplify your onboarding experience and make it easier for you to identify the right solution â whether youâre launching a new hotel, transitioning systems, or working with partial data.
The following changes only impact the naming, not how the RMS works.
- The Limited Data Build page will be renamed toSynthetic Data.
The Limited Data Build page will be renamed toSynthetic Data.
- In theImportant Informationwindow and in Data Feed files, you will see the following labels (new ones are bold):Limited Data Build:Hot Start â Synthetic Data.Hot Start:Hot Start â Limited History.Limited Data Build for Inventory Change:Synthetic Data for Inventory Change.
In theImportant Informationwindow and in Data Feed files, you will see the following labels (new ones are bold):
- Limited Data Build:Hot Start â Synthetic Data.
Limited Data Build:Hot Start â Synthetic Data.
- Hot Start:Hot Start â Limited History.
Hot Start:Hot Start â Limited History.
- Limited Data Build for Inventory Change:Synthetic Data for Inventory Change.
Limited Data Build for Inventory Change:Synthetic Data for Inventory Change.
- Alerts and Exceptions in the Information Manager will reflect the updated naming.
Alerts and Exceptions in the Information Manager will reflect the updated naming.
- Case types, online Help, and other learning materials are updated accordingly.
Case types, online Help, and other learning materials are updated accordingly.
We activate this change on Wednesday, December 10, 2025.

### Business Analysis Dashboard - Improvements

#### Save Your Preferred Date Range

You can now to save your default date range that displays when you open the dashboard.
- Click the option toSelect Date.
Click the option toSelect Date.
- SelectRolling Date.
SelectRolling Date.
- Enter your desiredFromandToperiods.
Enter your desiredFromandToperiods.
- Check the box toSave Rolling Date as Default.
Check the box toSave Rolling Date as Default.
To revert to the system default, clear the checkbox. The saved preferences apply only to you and only to the selected property.

#### Settings persevered after switching properties and settings:

- On all tabs, your Inventory Group setting persists when you switch to a property with the same Inventory Group.
On all tabs, your Inventory Group setting persists when you switch to a property with the same Inventory Group.
- On the Summary tab, your filterselections for day of week and occupancy forecast persist when you make any changes, including switching properties.
On the Summary tab, your filterselections for day of week and occupancy forecast persist when you make any changes, including switching properties.
We activate these changes on Wednesday, December 10, 2025.
You can create Projections from similar properties regardless of theirRMS currency, giving you greater flexibility and control. For example, if your Limited Data Build property is the first in a country, you can build it from similar hotels in countries with different currencies.
- For RMS Currency, selectAllinstead of the defaultMy Currency. Then you can still use the ADR Range filter to find the appropriate properties, becauseG3 RMSconverts any different currency to the one used by your property.
For RMS Currency, selectAllinstead of the defaultMy Currency. Then you can still use the ADR Range filter to find the appropriate properties, becauseG3 RMSconverts any different currency to the one used by your property.
- G3 RMSalso converts Revenue and ADR values to your property's RMS currency when it creates the projections.
G3 RMSalso converts Revenue and ADR values to your property's RMS currency when it creates the projections.
We activate this on Wednesday, December 3, 2025.
You can soon useRevPlan's Export to RMSoption to update your Budget and My Forecast inG3 RMSwhen there is a mismatch between theG3 RMSProperty Business Groups and the RevPlan segment names.
The Export to RMS option in RevPlan will be enhanced so you can map your detailed financial segments in RevPlan to the correct Business Group inG3 RMS. After that, you can export as usual.
We  enable this on Tuesday, December 9, 2025.

### Other Fixes and Performance Improvements

The following items were released in the 10.1.3 release.

### Business Analysis Dashboard - Settings Preserved After Switching Properties

If you manage multiple properties and switch properties while on the Business Analysis dashboard,G3 RMSnow maintains the following settings, reducing your number of clicks:
- On all tabs of the dashboard, the date range selected in the buttonor the slider.
On all tabs of the dashboard, the date range selected in the buttonor the slider.
- On the Pace Data tab, your display options, likeShow Expected Booking Pace as oforShow: ADR, remain in effect when you change properties. Additionally, you also keep your filter selection for Business Type.
On the Pace Data tab, your display options, likeShow Expected Booking Pace as oforShow: ADR, remain in effect when you change properties. Additionally, you also keep your filter selection for Business Type.
- POSTPONED - this last item  will be released at a later date, view the future release notes for updates.On the Data Details tab, your row selections, likeExpand by: Forecast Group, persist when you switch the property or change the  filterand Inventory Group selections.
POSTPONED - this last item  will be released at a later date, view the future release notes for updates.On the Data Details tab, your row selections, likeExpand by: Forecast Group, persist when you switch the property or change the  filterand Inventory Group selections.

### Data Feed â New Property Wash % Column in the HotelLevel File

Data Feed users now see theProperty Wash %value by occupancy date in a new column added to theHotelLevelfile. This helps you track property value sizes and changes across their estate.
We  activate this on November 12, 2025.
- Spec file
Spec file
- Sample File
Sample File

### Coming Soon - Unified Labels for Hot Start and Limited Data Build

We are streamlining the names of build types for properties with limited or evolving historical data. The changes simplify your onboarding experience and make it easier for you to identify the right solution â whether youâre launching a new hotel, transitioning systems, or working with partial data.
The following changes only impact the naming, not how the RMS works:
- The Limited Data Build page will be renamedSynthetic Data.
The Limited Data Build page will be renamedSynthetic Data.
- In the Important Information window and in Data Feed files you will see the following labels (new ones are bold):Limited Data Build:Hot Start â Synthetic Data.Hot Start:Hot Start â Limited History.Limited Data Build for Inventory Change:Synthetic Data for Inventory Change.
In the Important Information window and in Data Feed files you will see the following labels (new ones are bold):
- Limited Data Build:Hot Start â Synthetic Data.
Limited Data Build:Hot Start â Synthetic Data.
- Hot Start:Hot Start â Limited History.
Hot Start:Hot Start â Limited History.
- Limited Data Build for Inventory Change:Synthetic Data for Inventory Change.
Limited Data Build for Inventory Change:Synthetic Data for Inventory Change.
- Alerts and Exceptions in the Information Manager will reflect the updated naming.
Alerts and Exceptions in the Information Manager will reflect the updated naming.
- We update case types, online help, and other learning materials accordingly.
We update case types, online help, and other learning materials accordingly.
The rollout is scheduled to begin in early December. Look for the confirmed date in a future release announcement.

### Other Fixes and Performance Improvements

The following items were released in the 10.1.2 release.

### Demand and Wash Overrides â Simplified Increase/Decrease Option

When you apply a percentage change in an Arrival by LOS demand override, you now enter a positive value for an increase and a negative value (like -10) for a decrease. Previously you had to select Increase or Decrease when entering the value. This matches how you enter decreases and increases elsewhere in the system.

### Limited Data Build Changes

Configuring the Booking Pattern tab of a Limited Data Build is now easier, faster, and more accurate. If you selected similar properties to build the projections (see screenshot number 1), check the option toUse Selected Properties for Pattern Configuration(2). Then, go to the Booking Pattern tab (3) and simply review and, if needed, adjust the patterns thatG3 RMSselected for you.
If you select this option:
- On the Booking Pattern tab,G3 RMSselects theA specific similar propertyoption and assigns a similar Property and Market Segment to each of your propertyâs market segments.
On the Booking Pattern tab,G3 RMSselects theA specific similar propertyoption and assigns a similar Property and Market Segment to each of your propertyâs market segments.
- IfG3 RMScanât find a similar property or market segment, they remain unassigned, and you select them.
IfG3 RMScanât find a similar property or market segment, they remain unassigned, and you select them.
- G3 RMScan only auto-select for the option, A specific similar property. You can instead select patterns from A generic property or My property, if you prefer.
G3 RMScan only auto-select for the option, A specific similar property. You can instead select patterns from A generic property or My property, if you prefer.
We enable this change on Wednesday, October 29, 2025.
Based on your suggestions inIDeaShare, in the Projections Builder, when you enter or review the Rooms data, you now see the percentage share by market segment. That helps you validate your entries by segment. For example, if May's total projections are 1,000 rooms and 250 for the Discount segment, you see 25.0 in the % column.
Note: you can edit the number of rooms but not the % value.

### Pricing Configuration - Create Package Elements by Day of Week and Season

Based on your IDeaShare suggestions, you can now customize Package Elements for Linked Products by Day of Week and Season, enabling more tailored package configurations.

### Pricing Configuration - Additional Icons for Price Change Range

If your property uses Independent Products, you see new icons in thePrice Change Rangewindow when ranges are set up without an end dateor when gaps exist in the seasons. This makes it easier to find any issues when you view multiple products.

### Coming Soon - Data Feed â New Property Wash % Column in the HotelLevel File

Data Feed users will soon see theProperty Wash %value by occupancy date in a new column added to theHotelLevelfile. This helps you track property value sizes and changes across their estate.
We plan to activate this on November 12, 2025. Look for the confirmed date in a future release announcement.
- Spec file
Spec file
- Sample File
Sample File

### Other Fixes and Performance Improvements

The following items were released in the 10.1.1 release.

### Pricing Configuration - Edit Seasons During Processing

You can change a season in any Pricing configuration whenG3 RMSis in processingand when the page isnotlocked. Previously you could only edit the Default configurations.

### New Alerts When Wash for Individual Groups Is Disabled or Enabled

The new Alerts inform you afterG3 RMS:
- Turned off Wash forecasts and overrides at the Individual Group level.
Turned off Wash forecasts and overrides at the Individual Group level.
- Turned on that capability if it wasn't available.
Turned on that capability if it wasn't available.
The first Alert is due to poor quality of the group data, for example, caused by using group blocks for some groups and individual bookings for other groups. This causes a mismatch between group block and transactional data and negatively impacts group forecasting. WhenG3 RMSfinds this issue, we first notify you via email, giving you the date when the system switches to use transactional instead of group block data. The next day you see theWash Overrides for Individual Groups are disabledAlert. And on the Individual Groups tab you see a note that Wash overrides arenât available at this level.
The second Alert is for when your property didn't have Group Wash at the Individual Group level and itâs now enabled, for example, because the group data quality improved. In that case you see theWash Overrides for Individual Groups are enabledAlert.
Note: Previously, theSystem CEOThe IDeaS name for a system administrator role. Users with this role configure a property's permissions: creating other Roles, then assigning them to Users. They ensure that the right users have the appropriate access in the system.at the property received an email before disabling this capability and if it was turned back on. Now, they still receive the advance email, then the new Alert after the disabling, and only the Alert, no more email, if it is enabled again.

### Group Floor Overrides - New Icon and Exception for When Override Is Blocked

When the Ceiling value for a date is lower than the group's price,G3 RMScanât apply theGroup Floor Override. This might push the price of thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.below the group price and therefore breach your best price guarantee in your group contract.
Therefore, based on your suggestions in IDeaShare, the system alerts you in two ways whenever this condition occurs, enabling you to correct the situation.
- A warning icon in the Pricing and Group Floor Management pages:You see this iconnext to Final Price. Point to the icon to see the following text with the groupâs price: Ceiling below highest Group Floor price.The icon disappears when the condition no longer applies, for example, after you override the Ceiling.
A warning icon in the Pricing and Group Floor Management pages:You see this iconnext to Final Price. Point to the icon to see the following text with the groupâs price: Ceiling below highest Group Floor price.The icon disappears when the condition no longer applies, for example, after you override the Ceiling.
- New Exception, Ceiling is Below the Highest Group Floor Price, is triggered in the nightly processing in the Information Manager. The Exception:Lists the impacted dates and Room Classes.Provides links to Group Floor Management and Pricing configuration.Allows you to resolve the Exception yourself or auto-resolves after the condition clears.Allows you action multiple Exceptions at once to save you time.
New Exception, Ceiling is Below the Highest Group Floor Price, is triggered in the nightly processing in the Information Manager. The Exception:
- Lists the impacted dates and Room Classes.
Lists the impacted dates and Room Classes.
- Provides links to Group Floor Management and Pricing configuration.
Provides links to Group Floor Management and Pricing configuration.
- Allows you to resolve the Exception yourself or auto-resolves after the condition clears.
Allows you to resolve the Exception yourself or auto-resolves after the condition clears.
- Allows you action multiple Exceptions at once to save you time.
Allows you action multiple Exceptions at once to save you time.
We enable this change between October 1 and 8, 2025.

### Other Fixes and Performance Improvements

## 10.0 Releases

The following items were released in the 10.0.4 release.

### Managing Users â Filtering

Based on many suggestions inIDeaShare, when you go to theIDeaS Admin Userspage, you can again filter the users based on Property, Role, and Authorization Groups.

### Improved Distribution of the Occupancy Forecast to the Market Segment Level

WhenG3 RMSdistributes the Occupancy Forecastfrom the Forecast Group to the market segment level, it now better accounts for seasonal variations. This improves the constrainedOccupancy ForecastThe number of rooms (or percentage of the total number of rooms) that the RMS expects the property to achieve for the period. 
For the calculation, see the Demand and Wash - Overview topic (under Data Details)..
- After this release you willnotsee any changes in the unconstrained demand forecast or decisions, but you might see changes in the Occupancy Forecast at the market segment level.
After this release you willnotsee any changes in the unconstrained demand forecast or decisions, but you might see changes in the Occupancy Forecast at the market segment level.
- We enable this change for clients in phases over three weeks after September 8, 2025. Contact your IDeaS representative to learn when it's enabled for you. For clients with Profit Optimization we enable this in a future release.
We enable this change for clients in phases over three weeks after September 8, 2025. Contact your IDeaS representative to learn when it's enabled for you. For clients with Profit Optimization we enable this in a future release.

### Group Wash by Group â Improved Transient Block Section

If your property uses Transient Blocks, you see two enhancements on the Group Wash by Group page:
- You can now analyze that business in more detail. Previously, the Transient Block section displayed only On Books data. Now, same as for group Block, you can see the Block, Pickup, and Available Block data. This data represents all market segments with theattribute Transient Block.
You can now analyze that business in more detail. Previously, the Transient Block section displayed only On Books data. Now, same as for group Block, you can see the Block, Pickup, and Available Block data. This data represents all market segments with theattribute Transient Block.
- You can applyGroup Occupancy Forecast overridesto Transient Blocks.
You can applyGroup Occupancy Forecast overridesto Transient Blocks.

### Limited Data Build - Suggest Ceiling/Floor Option Available for More Properties

Previously, properties needed to meet the following two criteria before they could useG3 RMSto suggest Ceiling and Floor values in Pricing Configuration. Now you only need to satisfy one  criterion, making the Suggest option available for more properties.
- 90 days of current shopped data or 120 days of historical shopped data.
90 days of current shopped data or 120 days of historical shopped data.
- 120 days (from the Normalization Date) of unmasked historical data.
120 days (from the Normalization Date) of unmasked historical data.

### Rate Shopping Configuration â Use Ignore Competitor for Past Dates

You can nowIgnore Competitorsretroactively. This allowsG3 RMSto ignore the publicly available prices of a competitor for up to 180 days in the past. This is useful if, for example, you realize later that their prices were unreasonable.

### Independent Products with a Price Change Range â Restriction on Multiday Override

If you use the Multiday option to override an Independent Product for a period that exceeds End Date of the productâsPrice Change Range,G3 RMSadjusts the override End Date to the End Date of that configured range.

### Manage Pricing Calendar View â New Filter Option

Based on your suggestions in IDeaShare, when you click theFilter options   on the Pricing page in Calendar view, you now see an Available Capacity to Sell - Room Type Level option in theAdditional Informationsection. Currently you can select to view the Available Capacity to Sell only at the property level.

### Other Fixes and Performance Improvements

The following items were released in the 10.0.3 release.

### Limited Data Build â Redo the Projections from Similar Properties by Editing the Filter

After you clickBuild Projections using Similar Properties, you can now return to the Filter, if youâre not satisfied with the initial results. You can change your previous filter settings, then re-run the projections. When you redo the projections:
- G3 RMSclears the old projections and replaces them with new ones.
G3 RMSclears the old projections and replaces them with new ones.
- You get a warning to confirm or cancel. If you click Cancel, you can return to the original projections.
You get a warning to confirm or cancel. If you click Cancel, you can return to the original projections.
- Your original filter selections remain, so you don't need to re-enter them.
Your original filter selections remain, so you don't need to re-enter them.

### Information Manager - The Alert  Better Detects Formerly Inactivated Room Types

TheInactivated Room Type Alertdetects room types that you previously deactivated using the Replace action (in the Discontinued Room Type Alert). This allows you to reactivate the room type and update the settings so the room type can begin receiving decisions.

### Pricing Independent Products â Create Price Change Range for Current Month

In Pricing Configuration, you can now set up aPrice Change Rangewith a monthly Frequency for the current month. This enables you to enforce a fixed monthly price starting in the current month.
We plan to activate both changes on Thursday, August 28, 2025.
You can now tellG3 RMSto remove theGroup Floor Overrideson or near the groupâs arrival day. This removes constraints on the system's pricing. Use this option if you are allowed to offer public rates lower than the group's price within a certain number of days to arrival, for example, after the group cut-off date.
View the setup steps in the following screenshot of the Group Floor Configuration page:
- SelectStop applying group floor.
SelectStop applying group floor.
- Select when to stop applying the group floor:On the day of arrival.A specific number ofdays to arrival.
Select when to stop applying the group floor:
- On the day of arrival.
On the day of arrival.
- A specific number ofdays to arrival.
A specific number ofdays to arrival.
Notes:
- By default, this optional feature is turned off after rollout and when new properties are added.
By default, this optional feature is turned off after rollout and when new properties are added.
- Updates to this setting apply immediately and trigger aSyncflag.
Updates to this setting apply immediately and trigger aSyncflag.
- If you want to protect a group's price within the defined days to arrival, use aFlooroverride.
If you want to protect a group's price within the defined days to arrival, use aFlooroverride.
You can now add or remove specific dates from consideration forGroup Floor Overrides. This enables you to capture more lower-priced transient demand only on some days, without using a more restrictive pricing override, and while still protecting the prices of groups on other days. In the following screenshot, the 15th is no longer checked andG3 RMSdoesnât consider that date.
And if you want to be more protective of the group rate, you can now add shoulder days thatG3 RMSconsiders for Group Floor overrides.
These changes trigger a Sync flag, so you can sync and send the new pricing decisions to your selling systems or wait until the next scheduled optimization.
In theInformationaldata feed file, we added the following forecast and decision window settings in new columns:
- BDE Forecast Window
BDE Forecast Window
- BDE Decision Window
BDE Decision Window
- IDP Forecast Window
IDP Forecast Window
- IDP Decision Window
IDP Decision Window
- GroupPricingExtendedWindow
GroupPricingExtendedWindow
- Variable Decision Window
Variable Decision Window
These settings determine how many days outG3 RMSforecasts and sends decisions to the propertyâs selling systems. This change helps you with regular audits of these important settings. We plan to activate this change on Wednesday, August 20, 2025,  8:00 AM CST.
Not all clients use the GroupPricingExtendedWindow and Variable Decision Window features. If you don't use these features, the columns are blank.
Spec file
Sample file

### Coming Soon â New Design of the Decision Configuration Page

Currently large enterprises use Decision Configuration to roll outG3 RMSto all their properties, managing the switch from Decision Creation to Decision Delivery. They can also start Full Decision Uploads from Decision Configuration.
The new page is available to all properties and offers more features on two tabs, with a cleaner, easy-to-use design:
- On the Manage System Mode tab, you can:View and, if applicable, change your System Mode and view a history of changes.View the settings for your Forecast, Optimization, and Upload Window.View  what decisionsG3 RMSsends to yourselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data..
On the Manage System Mode tab, you can:
- View and, if applicable, change your System Mode and view a history of changes.
View and, if applicable, change your System Mode and view a history of changes.
- View the settings for your Forecast, Optimization, and Upload Window.
View the settings for your Forecast, Optimization, and Upload Window.
- View  what decisionsG3 RMSsends to yourselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data..
View  what decisionsG3 RMSsends to yourselling systemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data..
- On the Request Full Upload tab, you can:Define the types of decisions and the selling systems you want to upload.Upload full decisions now or at the next processing.Run a report of scheduled or past full decision uploads.
On the Request Full Upload tab, you can:
- Define the types of decisions and the selling systems you want to upload.
Define the types of decisions and the selling systems you want to upload.
- Upload full decisions now or at the next processing.
Upload full decisions now or at the next processing.
- Run a report of scheduled or past full decision uploads.
Run a report of scheduled or past full decision uploads.
Look for the activation date in a future release note.

### Other Fixes and Performance Improvements

The following items were released in the 10.0.2 release.

### Information Manager Changes

#### Information Manager â New Creation Date Column and Filter

Based on a popular suggestion inIDeaShare, we addedCreation Dateto the table and  the filter options in the Information Manager. This allows you to see when Alerts, Exceptions, and Notifications were first triggered and to find these tasks even after they are resolved.

#### New Notification If You Enabled Automated Overbooking Reduction

If you enabled the option toreduce overbooking based on closed competitors, you can now set up a Notification to monitor changes. You can select to be informed when a competitor-related overbooking reduction started or stopped, when an existing reduction changed, and when a reduction to zero occurs.

#### New Alert When the Build Type Changes from Hot Start to Standard

The new Alert,Build Type Changed to Standard From Hot Start, informs you afterG3 RMSswitches from Hot Start to a Standard build. This occurs automatically when your property has enough historical data, seeBuild Typesfor details. The Alert recommends reviewing your forecast and decisions because they likely changed due to this switch.

### Manage Pricing Calendar View â New Filter Option

Based on your suggestions inIDeaShare, you can now see a newOn Books Percentageoption in theAdditional Informationsection when you click the Filteron the Pricing Calendar View page. It displays the Occupancy as a percentage of the capacity at the property level when you select ALL for Room Class. When you select a specific Room Class, the % applies to the selected Room Class.

### Limited Data Build â Property Attributes Option for Creating Projections from Similar Properties

When youcreate Projections from similar propertiesand if your company usesProperty Attributes, you can now:
- See the assigned Property Attributes for the LDB property.
See the assigned Property Attributes for the LDB property.
- Use the auto-filled attributes as the filter settings to find similar properties.
Use the auto-filled attributes as the filter settings to find similar properties.

### Coming Soon â Data Feed Includes Forecast and Decision Window Settings

In theInformationaldata feed file, we added the following forecast and decision window settings in new columns:
- BDE Forecast Window
BDE Forecast Window
- BDE Decision Window
BDE Decision Window
- IDP Forecast Window
IDP Forecast Window
- IDP Decision Window
IDP Decision Window
- GroupPricingExtendedWindow
GroupPricingExtendedWindow
- Variable Decision Window
Variable Decision Window
These settings determine how many days outG3 RMSforecasts and sends decisions to the propertyâs selling systems. This change helps you with regular audits of these important settings.
Notes:
- Not all clients use the GroupPricingExtendedWindow and Variable Decision Window features. If you don't use these features, the columns are blank.
Not all clients use the GroupPricingExtendedWindow and Variable Decision Window features. If you don't use these features, the columns are blank.
- We plan to activate this after the 10.0.3 release, look for the confirmed date in an upcoming release announcement.
We plan to activate this after the 10.0.3 release, look for the confirmed date in an upcoming release announcement.
Spec file
Sample file

### Other Fixes and Performance Improvements

### Changes If You Do NOT Sign In With Your Companyâs Identity Provider

After the 10.0.1 deployment, on July 9, 2025, you must use Multi-Factor Authentication to sign intoG3 RMS, see the following steps.
If you use a generic email, like reservations@hotelABC.com, to log intoG3 RMS, and if you donât have access to that email inbox, then you can't accessG3 RMS. Therefore, contact your supervisor or corporate revenue management representative and ask them to add you as a unique user with your email.
After you enter your password and click Sign In,G3 RMSemails you a verification code. Enter the code inG3 RMSand click Submit.
Your verification code lets you accessG3 RMSfor 90 days, if you are on the same computer and browser, and you are not in private mode.

### Improved Announcements

This was initially announced for  9.8.1 but  is now in this 10.0.1 release.
Based on your feedback, the announcements that you see after you sign in toG3 RMShave a new look and functionality:
- Announcements display automaticallyonlyif they are critical or require action, like an emergency fix.
Announcements display automaticallyonlyif they are critical or require action, like an emergency fix.
- You can close the announcement without having to choose to not see it again.
You can close the announcement without having to choose to not see it again.
- To view the announcements, you continue clicking the bullhorn in the top right of each page, but the icon now gives you more information:: You have three unread announcements.: You have two announcements, but you have already read them.: No current announcements.
To view the announcements, you continue clicking the bullhorn in the top right of each page, but the icon now gives you more information:
- : You have three unread announcements.
: You have three unread announcements.
- : You have two announcements, but you have already read them.
: You have two announcements, but you have already read them.
- : No current announcements.
: No current announcements.

### Configure Rate Shopping Schedule - Improvements

Based on your feedback, we made the following changes on theRate Shopping Scheduletab within Rate Shopping configuration to provide you a faster, easier setup:
- Simpler and clearer labels that help you understand the impact of each step.
Simpler and clearer labels that help you understand the impact of each step.
- Require that theStop usingâ¦ value is greater than or equal to theShop frequencyvalue. For example, if the shop frequency is every 3 days, the minimum value you can enter for when the system should stop using older rate shopping data is 4 days.
Require that theStop usingâ¦ value is greater than or equal to theShop frequencyvalue. For example, if the shop frequency is every 3 days, the minimum value you can enter for when the system should stop using older rate shopping data is 4 days.

### Room Classes with Large ADR Variances - Improved Pricing

IDeaS recommends thatRoom Classes contain room types with similar pricing. For Room Classes that donât meet that recommendation, their large ADR variances between room types could sometimes negatively impact the systemâs pricing decisions. This enhancement reduces that negative impact, ensuring the best possible pricing decisions.
Note: If your property has Room Classes with a high ADR variation, you might see changes in pricing after the release.

### Data Not Retained for Non-Optimized and Non-Uploaded Linked Products

In the Pick Up/Change and Differential Controls and the Pricing Override History reports, you view pace data for products priced byG3 RMS. Soon, you can no longer view that data for Linked non-Optimized Products that are set up to not Upload.

### Other Fixes and Performance Improvements

## 9.8 Releases

The following items were released in the 9.8.4 release.

### Limited Data Build - Create the Projections from Similar Properties

Your company can now create theProjectionsfor a Limited Data Build property by basing them on similar properties from your portfolio. You need a minimum of three  similar properties to use this feature. This saves you time compared to coming up with values for properties without sales projections.
You can base the projections either on specific properties or filter the properties based on the following criteria:
- Size (minimum and maximum number of rooms).
Size (minimum and maximum number of rooms).
- Distance from the Limited Data Build property.
Distance from the Limited Data Build property.
- Attributes, if set up by your company.
Attributes, if set up by your company.
- Business Mix between Transient and Group.
Business Mix between Transient and Group.
- ADR Range.
ADR Range.
Based on the selected propertiesG3 RMSbuilds the monthly projections to help you review them at a high level. Once you have reviewed and, if needed, adjusted the monthly values,G3 RMSgenerates daily projections.
Notes:
- You must have access to the similar properties to use them for projections.
You must have access to the similar properties to use them for projections.
- If your company doesn't allow using the data from other properties in your portfolio, contact your IDeaS representative to keep this feature turned off.
If your company doesn't allow using the data from other properties in your portfolio, contact your IDeaS representative to keep this feature turned off.

### Forecast Investigator Informs You When the Actual Versus Expected Chart Lacks Data

TheActual versus Expected On Books (Transient Only)chart now displays a message telling you when there's not enough historical data. To display information in this chart,G3 RMSneeds reservations data for at least 180 days, excluding days set as ignored. This helps you understand why no data displays.

### FasterSyncIf You Applied Only Pricing Overrides

After you save an override and if you made no other changes, clickingandSync AllorSync All and Uploadnow triggers a shorter process. Instead of syncing for the full optimization window,G3 RMSfocuses on the period impacted by the overrides, including stay-through demand. This shortens the Sync and therefore allows you to make other changes sooner.

### Rate Shopping â You Must Enter a Rate Adjustment Value for Other and Tax

To save aRate Adjustment, you now must enter a value for both the Other and the Tax fields. Previously, you could leave one of the two values empty. This change helps you understand which valuesG3 RMSuses if you have values for a specific property that differ from the default values for all properties.
Note: If your property had an existing Rate Adjustment with a blank value, we have replaced those blank values with 0.00. This is howG3 RMStreated a blank value before this change.

### Coming Soon - Changes If You Do NOT Sign In With Your Companyâs Identity Provider

After the 10.0.1 deployment, July 7 and 8, 2025, you must use Multi-Factor Authentication to sign intoG3 RMS, see the following steps.
If you use a generic email, like reservations@hotelABC.com, to log intoG3 RMS, and if you donât have access to that email inbox, then you can't accessG3 RMS. Therefore, contact your supervisor or corporate revenue management representative and ask them to add you as a unique user with your email.
After you enter your password and click Sign In,G3 RMSemails you a verification code. Enter the code inG3 RMSand click Submit.
Your verification code is valid for 90 days when you accessG3 RMSon the same computer and browser, and you are not in private mode.

### Other Fixes and Performance Improvements

The following items were released in the 9.8.3 release.

### Business Analysis Dashboard - View Projected Booking Pace Data

This was initially announced for the 9.8.2 release. Now we enable it in phases during 9.8.3, between May 28 and June 12. Contact your IDeaS representative to learn when it's enabled for you.
You can now view the booking pace thatG3 RMSexpects for a selected period. On the Pace Data tab, theExpected Booking Pacedisplays as a dotted line to the right of the System Data, continuing from the On Books values. Seeing whenG3 RMSexpects that the remaining demand books helps you understand the systemâs forecast. For example, if the expected booking pace differs greatly from the Occupancy On Books STLY, thenG3 RMSlikely found that the more recent pace is a better fit for the forecast than past yearâs pace.
You can also select toShow Expected Booking Pace as of a number of days ago. This adds another dotted line with the systemâs Previous Expected Booking Pace. This helps you understand changes in the systemâs forecast. The larger the difference is between the current and the previous expected booking pace, the likelier it is thatG3 RMSchanged the remaining demand forecast.
Note that the expected booking pace is available:
- At the property and the Forecast Group level.
At the property and the Forecast Group level.
- For a maximum of 120 days.
For a maximum of 120 days.

### Rate Shopping Configuration - Ignore Channel

In the Channel Settings tab, you can now tellG3 RMSto ignore competitor pricing data from a specific channel. This is helpful when your shopping data includes a channel with prices that are not in parity with other channels. You can ignore any channel except the Default Channel.
Now when you askG3 RMSto Ignore Competitor Data (in the Competitor Settings tab) you must define the competitor and the channel. That ensures that the system can differentiate the two Ignore options.
Notes:
- If you have an existing Ignore Competitor Data setting,G3 RMSassumes it applies to all channels.
If you have an existing Ignore Competitor Data setting,G3 RMSassumes it applies to all channels.
- We enable this change for clients in phases between May 28 and June 13, 2025. Contact your IDeaS representative to learn when it's enabled for you.
We enable this change for clients in phases between May 28 and June 13, 2025. Contact your IDeaS representative to learn when it's enabled for you.
We plan to activate this on Wednesday, June 13, 2025,  8:00 AM CST.

#### Updates for Ignore Channel configuration

One new file and one updated file show whenG3 RMShas been configured to:
- Ignore shopped rates from a specific channel.
Ignore shopped rates from a specific channel.
- Ignore shopped rates for a specific competitor and channel for a period.
Ignore shopped rates for a specific competitor and channel for a period.
New file: RateShoppingIgnoreChannelConfiguration
Shows which Channel's shopped rates thatG3 RMSignores.
- Bucket=Configuration
Bucket=Configuration
- File level=Property
File level=Property
- Default delivery frequency=Monthly
Default delivery frequency=Monthly
- Period=all available configuration
Period=all available configuration
- Spec file
Spec file
- Sample file
Sample file
Updated file: new column added to RateShoppingIgnoreCompetitorDataConfiguration
A new Channel column shows which channelG3 RMSignores.
- Spec file
Spec file
- Sample file
Sample file

### Hot Start - a Faster Way to Build a NewG3 RMSProperty

For properties with less than 365 days of historical data,G3 RMSnow offers a faster and easier alternative to a Limited Data Build, called Hot Start.
If you are responsible for setting upG3 RMSduring the initial build, you can clickin the top right to open Important Information and, after the release date, verify which Build Type your property uses.

##### Benefits of Hot Start:

For your properties with minimal historical data, a Hot Start Data Build saves you significant time and effort so you can see an immediate ROI:
- Less configurationâno need to provide sales projections and patterns configuration like a Limited Data Build requires.
Less configurationâno need to provide sales projections and patterns configuration like a Limited Data Build requires.
- Requires less historical data enabled by faster system learning.
Requires less historical data enabled by faster system learning.
- Supports automatedG3 RMSconfiguration to help you rapidly build your property.
Supports automatedG3 RMSconfiguration to help you rapidly build your property.
- Supports splitting market segments at the rate code level (sometimes called analytical Market Segments, AMS), an advanced configuration option not available with Limited Data Builds.
Supports splitting market segments at the rate code level (sometimes called analytical Market Segments, AMS), an advanced configuration option not available with Limited Data Builds.
- No downtime during the transition to Standard Data Build.G3 RMSautomatically detects and transitions your property when it has at least 365 days of historical data.
No downtime during the transition to Standard Data Build.G3 RMSautomatically detects and transitions your property when it has at least 365 days of historical data.

##### Minimum data requirements:

- 2 months of history (reservations and inventory), that is representative of the full year.
2 months of history (reservations and inventory), that is representative of the full year.
- 20% or more average occupancy for that period.
20% or more average occupancy for that period.
- Competitor shopping data for a 365-day window is recommended but not required.
Competitor shopping data for a 365-day window is recommended but not required.
To learn more about Hot Start, contact your IDeaS representative

### Pricing Ceiling/Floor Configuration â Continue Working WhileG3 RMSSuggests Prices

After you haveG3 RMSSuggestnew Ceiling/Floor values, you can now go to other pages and continue working. Then, come back to the Ceiling/Floor page later and review the draft of the suggested values. This allows you to get more work done in less time, especially if you have a large property with a complex pricing setup.

### Group Wash by Group - Performance Improvements

Following the9.8.2 performance improvements, you see the following changes on the Group Wash by Group pages:
- TheBy Occupancy Datetab now loads the current date and the next 14 days, reducing the time to load the page initially. If needed,  extend the number of days with the slider.
TheBy Occupancy Datetab now loads the current date and the next 14 days, reducing the time to load the page initially. If needed,  extend the number of days with the slider.
- TheIndividual Grouptab now pulls the data only for your selected filteroptions. If you have fewer filter options selected, this significantly reduces the initial load time.
TheIndividual Grouptab now pulls the data only for your selected filteroptions. If you have fewer filter options selected, this significantly reduces the initial load time.

### Coming Soon - Create the Projections for a Limited Data Build from Similar Properties

Your company can soon create theProjectionsfor a Limited Data Build property by basing them on similar properties from your portfolio. You need between  3 and 5 similar properties to use this feature. This saves you time compared to coming up with values for properties without sales projections.
You can base the projections either on specific properties or filter the properties based on the following criteria:
- Size (minimum and maximum number of rooms).
Size (minimum and maximum number of rooms).
- Distance from the Limited Data Build property.
Distance from the Limited Data Build property.
- Attributes, if set up by your company.
Attributes, if set up by your company.
- Business Mix between Transient and Group.
Business Mix between Transient and Group.
- ADR Range.
ADR Range.
Based on the selected propertiesG3 RMSbuilds the monthly projections to help you review them at a high level. Once you have reviewed and, if needed, adjusted the monthly values,G3 RMSgenerates daily projections.
Notes:
- You must have access to the similar properties to use them for projections.
You must have access to the similar properties to use them for projections.
- If your company doesn't allow using the data from other properties in your portfolio, contact your IDeaS representative to keep this feature turned off.
If your company doesn't allow using the data from other properties in your portfolio, contact your IDeaS representative to keep this feature turned off.

### Coming Soon - Changes If You Do NOT Sign In With Your Companyâs Identity Provider

After the 10.0.1 deployment, July 7 and 8, 2025, you must use Multi-Factor Authentication to sign intoG3 RMS, see the following steps.
If you use a generic email, like reservations@hotelABC.com, to log intoG3 RMS, and if you donât have access to that email inbox, then you can't accessG3 RMS. Therefore, contact your supervisor or corporate revenue management representative and ask them to add you as a unique user with your email.
After you enter your password and click Sign In,G3 RMSemails you a verification code. Enter the code inG3 RMSand click Submit.
Your verification code is valid for 90 days when you accessG3 RMSon the same computer and browser, and you are not in private mode.

### Other Fixes and Performance Improvements

The following items were released in the 9.8.2 release.

### Business Analysis Dashboard - View Projected Booking Pace Data

POSTPONEDThe Projected Booking Pace data  will be released at a later date, view the future release notes for updates.

### Improved Performance on MultipleG3 RMSPages

To enable you to complete your work inG3 RMSfaster, we improved the performance on the following pages:Pricing,Group Wash by Group,Demand and Wash Management, and Group Floor Management. We will review otherG3 RMSpages for future improvements.

### Data Feed - New Discontinued Room Type Column in the RoomClassConfiguration File

The data feed files now include data for room types that you discontinued. Based on your suggestion you get a new column at the end of the RoomClassConfiguration file. It shows discontinued room types, meaning those for which you donât see on books and decisions for current dates. This file is part of the Core subscription, so all Data Feed customers benefit from it.
- Spec file
Spec file
- Sample file
Sample file
We plan to activate this change on Wednesday, May 7, 2025,  8:00 AM CST.

### Coming Soon - Data Not Retained for Non-Optimized, Non-Uploaded Linked Products

In the Pick Up/Change and Differential Controls and the Pricing Override History reports, you view pace data for products priced byG3 RMS. Soon, you can no longer view that data for those Linked non-Optimized Products that are set up to not Upload. Review theData Detailsfor these Pricing options.

### Other Fixes and Performance Improvements

The following items were released in the 9.8.1 release.

### Configure Permissions â New Location and Functionality

After this deployment, when you click to configure Permissions, Roles, Users, or Authorization Groups, the pages open in a new browser tab, with an updated look and improved functionality. This is the first step in allowing you to manage the permissions for all IDeaS products from one location, called Universal Admin. We will enable that in a future release.
In this release, the changes depend on which IDeaS products you use:
The appearance of the pages changes, but with the same functionality as before. To access other Permission pages, click their name of the left. To accessG3 RMS, return to that browser tab.
Some steps differ slightly, for help click the?icon in the top right of a page.
Help topics, same as theG3 RMSpages, are now separate from theG3 RMScontent. To view a Help topic other than Permissions, open Help from the browser tab inG3 RMS.
You manage the Permissions pages as a separate Product, called Universal Admin. Any role inG3 RMSwith access to a Permissions page displays both Universal Admin and G3 in the Product column, see the preceding Roles screenshot .
When you add or edit a role for users with access to managing Permissions, you add Universal Admin as another product.
You can now manage permissions for both in one location:
- All your existing users, their roles and permissions, and any Authorization Groups are transferred to the new pages.
All your existing users, their roles and permissions, and any Authorization Groups are transferred to the new pages.
- Users with access to bothG3 RMSand Optix retain the permissions from their Role inG3 RMS, but with the added permissions for the Optix product.
Users with access to bothG3 RMSand Optix retain the permissions from their Role inG3 RMS, but with the added permissions for the Optix product.
- When you add or edit a role you can now add Optix permissions as another product.This saves you time managing users for these two IDeaS products.
When you add or edit a role you can now add Optix permissions as another product.This saves you time managing users for these two IDeaS products.
Note: For most clients, we enable this change in phases, scheduled from April 14 to April 30, 2025. Contact your IDeaS representative to learn when it's enabled for you. A few clients will get this change later. IDeaS will inform these clients directly.

### Improved Announcements

POSTPONEDThe enhanced Announcements will be released at a later date, view the future release notes for updates.

#### Download Summary Counts by Property from Last 30 Days Trends Tab

Large enterprise clients that have access to this dashboard can now export the data of the following charts to Excel to view summary counts by property and category:
- Received Before 4 AM - Completed After 8 AM
Received Before 4 AM - Completed After 8 AM
- Received After 4 AM - Completed After 8 AM
Received After 4 AM - Completed After 8 AM
Use this to determine which properties have frequent problems and if is there a common issue.

#### New Discontinued Room Type Column in the RoomClassConfiguration File

The data feed files soon include data for room types that you discontinued. Based on your suggestion you get a new column at the end of the RoomClassConfiguration file. It shows discontinued room types, meaning those for which you donât see on books and decisions for current dates. This file is part of the Core subscription, so all Data Feed customers benefit from it.
We plan to activate this on Wednesday, May 7, 2025. Look for the confirmed date in an upcoming release announcement.
- Spec file
Spec file
- Sample file
Sample file

### Other Fixes and Performance Improvements

## 9.7 Releases

The following items were released in the 9.7.4 release.

### Business Insights Dashboardâ View Cancellations and No Shows Separately

You can now view the data for No Shows separately from Cancellations. This helps you understand how each contributes to overall Wash. After this deployment, Cancellations data won't include No Show data.
To view No Show data, you can select No Shows and No Shows Last Year, under Values.Note - updated March 20, 2025: We release this on April 1March 31, 2025.

### Channel Forecast Dashboard Displays Data by Day

On theChannel Forecastdashboard, you can now:
- View data by Channel or Source and also by a Channel and Source combination. For example, Expedia is a Source with bookings under the Channel OTA and GDS. Previously you could display only total data for the Source Expedia, soon you can display costs for OTA-Expedia and GDS-Expedia separately.
View data by Channel or Source and also by a Channel and Source combination. For example, Expedia is a Source with bookings under the Channel OTA and GDS. Previously you could display only total data for the Source Expedia, soon you can display costs for OTA-Expedia and GDS-Expedia separately.
- View Forecasted & On Books data at a monthly total, and also at a day level, for up to 31 days.
View Forecasted & On Books data at a monthly total, and also at a day level, for up to 31 days.
Note:G3 RMSnow considers Channel as the parent of Sources. If you set up costs only at the Source level, you need to configure your default Sources in theForecast Settingstab.

### Secure Help

We are securing the Help behind IDeaS universal sign-in, which means that you need to be signed into your IDeaS account to access Help. If you are already signed intoG3 RMS, you can continue to access Help using the Help icons.
If you arenât signed in and you click a Help link, such as from a browser bookmark, you will be directed to the IDeaS login page. After signing in, you will continue to the requested Help page.

### G3 RMSCan Suggest Floor/Ceiling Values for Independent Products

If you useIndependent Products, you can soon useG3 RMSto suggest the Floor and Ceiling values in Pricing Configuration. Currently itâs only available for thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..
We plan to activate these two changes on March 26, 2025,  8:00 AM CST.
Note: The updates for Ignore Channel are postponed to 9.8.1, with a new activation date of April 17, 2025.

#### New RateShoppingOccupancyBasedCMPC file

A new file will report theOccupancy Based constraintconfiguration from Rate Shopping Configuration.
- File name = RateShoppingOccupancyBasedCMPC
File name = RateShoppingOccupancyBasedCMPC
- Level = Property
Level = Property
- Bucket = Configuration
Bucket = Configuration
- Frequency = Monthly
Frequency = Monthly
- Period = All available configuration
Period = All available configuration
- History file = None
History file = None
- Spec file
Spec file
- Sample file
Sample file

#### New Property Code Column in the UserReport File

A new Property Code column in the UserReport file shows the code for each property that is assigned to the User. The property codes help match up the information in this file to other files with the same codes.
- File spec
File spec
- Sample file
Sample file

### Coming Soon - Rate Shopping Configuration - Ignore Channel

In the Channel Settings tab, you can now tellG3 RMSto ignore competitor pricing data from a specific channel, or from a competitor and channel.
This is helpful when your shopping data includes a channel with prices that are not in parity with other channels. Or when a competitor doesnât display on a channel due to contract issues.
We tentatively plan to start activating this on April 17, 2025. Look for the final dates in the 9.8.1 release notes.

### Coming Soon â New Location and Functionality for Managing Permissions

Soon, when click to configure Permissions, Roles, Users, or Authorization Groups, the pages open in a new browser tab, with an updated look and improved functionality. This is the first step in allowing you to manage the permissions for all IDeaS products from one location, called Universal Admin. We enable that in a future release.
In this coming release, the changes depend on which IDeaS products you use:
The appearance of the pages changes, but with the same functionality as before. To access other Permission pages, click their name of the left. To accessG3 RMS, return to that browser tab.
Some steps differ slightly, for help click the?icon in the top right of a page.
Help topics, same as theG3 RMSpages, will be separate from the remainingG3 RMScontent. To view a Help topic other than Permissions, open Help from the browser tab inG3 RMS.
You will manage the Permissions pages as a separate Product, called Universal Admin. Any current role inG3 RMSwith access to a Permissions page will display both Universal Admin and G3 in the Product column after this release, see the Roles screenshot above.
When you add or edit a role for users with access to managing Permissions, you add Universal Admin as another product.
You can now manage permissions for both in one location:
- All your existing users, their roles and permissions, and any Authorization Groups are transferred to the new pages.
All your existing users, their roles and permissions, and any Authorization Groups are transferred to the new pages.
- Users with access to bothG3 RMSand Optix retain the permissions from their Role inG3 RMS, but with the added permissions for the Optix product.
Users with access to bothG3 RMSand Optix retain the permissions from their Role inG3 RMS, but with the added permissions for the Optix product.
- When you add or edit a role you can now add Optix permissions as another product.This saves you time managing users for these two IDeaS products.
When you add or edit a role you can now add Optix permissions as another product.This saves you time managing users for these two IDeaS products.
Note: For most clients, we enable this change in phases, tentatively scheduled to last from April 14 to April 30, 2025. We will have a final schedule by March 31, contact your IDeaS representative then to learn when it's enabled for you. A few clients will get this change later. IDeaS will inform these clients directly.

### Other Fixes and Performance Improvements

The following items were released in the 9.7.3 release.

### Benchmarking Alliance - New Partner for Market Performance Data

With a subscription to Benchmarking Alliance, you can now see your marketâs Occupancy, ADR, and
RevPAR data inG3 RMS. You can compare your propertyâs performance to the marketâs, helping you improve your revenue strategy.
You can see the market data in the:
- At a Glance dashboard, Summary table: in the Market Performance row you see monthly totals for this and the last year.
At a Glance dashboard, Summary table: in the Market Performance row you see monthly totals for this and the last year.
- Data Extraction report: you can add the market data by occupancy date at the Property level.
Data Extraction report: you can add the market data by occupancy date at the Property level.
Note:G3 RMSdoesnât use this data in its optimization for forecasting and decisions.
Contact your IDeaS representative to learn more about integrating the Benchmarking Alliance data intoG3 RMS.

### Pricing Configuration Allows Supplements by Percentage

Same as for Offsets, you can now set up Supplements by  a Fixed value and by a percentage.
Notes:
- This is optional. To change from fixed to percentage values you must go into Pricing configuration.
This is optional. To change from fixed to percentage values you must go into Pricing configuration.
- We enable this change for clients in phases. Contact your IDeaS representative to learn when it's enabled for you.
We enable this change for clients in phases. Contact your IDeaS representative to learn when it's enabled for you.

### Coming Soon - Secure Help

We are securing the Help behind IDeaS universal sign-in, which means that you will need to be signed into your IDeaS account to access Help. If you are already signed intoG3 RMS, you can continue to access Help using the Help icons.
If you arenât signed in and you click a Help link, such as from a browser bookmark, you will be directed to the IDeaS login page. After signing in, you will continue to the requested Help page.

### Coming Soon âG3 RMSCan Suggest Floor/Ceiling Values for Independent Products

If you useIndependent Products, you can soon askG3 RMSto suggest the Floor and Ceiling values in Pricing Configuration. Currently itâs only available for thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration..
We tentatively plan to activate these three changes on March 26, 2025,  8:00 AM CST. We will confirm the date in the 9.7.4 release announcement.

#### New RateShoppingOccupancyBasedCMPC file

A new file will report theOccupancy Based constraintconfiguration from Rate Shopping Configuration.
- File name = RateShoppingOccupancyBasedCMPC
File name = RateShoppingOccupancyBasedCMPC
- Level = Property
Level = Property
- Bucket = Configuration
Bucket = Configuration
- Frequency = Monthly
Frequency = Monthly
- Period = All available configuration
Period = All available configuration
- History file = None
History file = None
- Spec file
Spec file
- Sample file
Sample file

#### Updates for Ignore Channel configuration

One new file and one updated current file show whenG3 RMShas been configured to:
- Always ignore shopped rates from a specific channel.
Always ignore shopped rates from a specific channel.
- Ignore shopped rates for a specific competitor and channel for a period.
Ignore shopped rates for a specific competitor and channel for a period.
New file: RateShoppingIgnoreChannelConfiguration
Shows which Channel's shopped ratesG3 RMSignores.
- Bucket=Configuration
Bucket=Configuration
- File level=Property
File level=Property
- Default delivery frequency=Monthly
Default delivery frequency=Monthly
- Period=all available configuration
Period=all available configuration
- Spec file
Spec file
Updated file: new column added to RateShoppingIgnoreCompetitorDataConfiguration
A new Channel column shows which channelG3 RMSignores.
- Spec file
Spec file

#### New Property Code Column in the UserReport File

A new Property Code column in the UserReport file shows the code for each property that is assigned to the User. The property codes help match up the information in this file to other files with the same codes.
- File spec
File spec
- Sample file
Sample file

### Other Fixes and Performance Improvements

The following items were released in the 9.7.2 release.

### My Forecast â Enter Values  by Business Type

On theBudget and My Forecastconfiguration tab, you can now select to enter your own Forecast data by Business Type (Transient and Group). Previously you could only select Business View.  My Forecast data continues to display in the following:
- At A Glance dashboard
At A Glance dashboard
- Business Analysis Data Details dashboard
Business Analysis Data Details dashboard
- Data Extraction report
Data Extraction report
- Data Feed - MyForecast file
Data Feed - MyForecast file
We enable this on Wednesday, February 19, 2025, at 8:00 AM CST.

### Other Fixes and Performance Improvements

The following items were released in the 9.7.1 release.

### Reinstate StandardG3 RMSData Retention and Remove Same Time 2019 Data

On Thursday, January 23, 2025, we reinstate thestandard data retention policythat we suspended due to COVID-19.
Over several months after that date, we slowly remove any older data, including all 2019 data, that you can see inG3 RMS, for example, in the Business Analysis dashboard.

#### Scheduled Data Extraction Reports

In existing scheduled Data Extraction reports, we automatically remove any columns that contain 2019 data.

#### Data Feed

For Data Feed users, we remove the columns with ST19 data from the following files on January 23, 2025, 8:00 AM CST (columns are highlighted in red):
- MarketSegment_2019 Columns Removal.xlsx
MarketSegment_2019 Columns Removal.xlsx
- RoomType_2019 Columns Removal.xlsx
RoomType_2019 Columns Removal.xlsx

### Automated Overbooking Reduction Based on Closed Competitors

You can use this optional functionality to automatically lower the overbooking based on the number of competitors that are closed. This can reduce the risk of being unable to relocate, or walk, guests when your market is very busy.
You define a percentage of closed competitors. When that threshold is reached,G3 RMSreduces overbooking. If no competitor has a price available for a one-night length of stay, the system gradually reduces property overbooking to zero. If competitors open up again,G3 RMSincreases overbooking too.
Note that the % threshold considers:
- All your shopped competitors, even those not checked for Use Rate Shopping Data or Use in Competitive Market Position Constraints.
All your shopped competitors, even those not checked for Use Rate Shopping Data or Use in Competitive Market Position Constraints.
- A competitor with no price for a one-night stay for any room type or any channel. For example, if there is a price for only 1 room type and 1 Channel, but not others,G3 RMSconsiders the competitor open.
A competitor with no price for a one-night stay for any room type or any channel. For example, if there is a price for only 1 room type and 1 Channel, but not others,G3 RMSconsiders the competitor open.

### Rate Shopping Configuration â Improved Constraint Warning Message

The warning that you have too few competitors set up for your Competitive Market Position Constraint now also displays for theOccupancy-Based type, not only the Standard type.
We deploy this change on Friday, January 24, 2025.

### Limited Data Build - Download of Monthly File Includes Your Entries from Projections Builder

After you enter and save monthly projections in the Projections Builder, you can now download a monthly file that includes your Projections. That allows you share your setup with others in your organization.

### Pricing Configuration â Ceiling and Floor Download File Has Same Name for All Products

When you download the Ceiling and Floor values, the file now has a consistent name for all products, making it easier to find the right file to update and upload. The name starts with Pricing_Configuration_Transient and includes the  Product Name and the date of the download.

### Other Fixes and Performance Improvements
