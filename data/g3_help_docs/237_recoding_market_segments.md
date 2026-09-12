# Recoding Market Segments

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Market-Segments/Market-Segment-Recoding.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Market-Segments/Market-Segment-Recoding.htm`
- **Ingestion Date:** `2026-09-11 22:14:47`

---

# Recoding Market Segments

Use Market Segments Recoding when you change your market segments, rate codes, or both in yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.and you want to see only the new segmentation inG3 RMS. You might make such changes, like splitting one market segment into several new market segments, to improve tracking of business or because of a hotel brand change.
Recoding is one part of changing market segments and comes after you have discussed the whole process with your IDeaS representative. Recoding itself takes about five days andprocessingstops during that time. Recoding includes two steps:
- You provide the mapping for the old and new market segments and the attributes for the new market segments.
- IDeaS recodes all reservations and groups based on your information, then rebuilds all data (like pace) with the new segmentation.
The benefit of this chargeable activity is that the clean historical data aligns the old with the new data and ensures good business reporting. And the system doesn't start from zero when learns the business patterns of the new market segments. Contact your IDeaS representative if you think your property might benefit from this feature.

## Steps to Recode Market Segments

After you confirmed the recoding and set a date, these are the steps inG3 RMS.
Note: In your reservation system, you need to move reservations from the old to the new market segments and then set old market segments to inactive. Complete that work between steps 3) and 11).
- During Recoding,G3 RMSis not processing data or sending decisions, so apply any last-minute overrides and prepare to manage your business manually.
- Recoding removes all Demand, Wash and Pricing overrides. Save theInput OverrideandOutput Overridereports, so you can  apply the overrides after the process is complete.
- Recoding also cancelsscheduledBooking Situation, Data Extraction, Performance Comparison, and Pick Up/Change and Differential Controls Reports. Note any existing schedules so that you can re-enter them after recoding.
On the start date for the recoding, IDeaS stopsG3 RMSprocessing and places the system inSystem Dormant Mode.G3 RMScreates an Alert.
- Clickand thenInformation Manager. The Alert tab displays.
- Find and click theComplete Market Segments Recoding InformationAlert.
- ClickGo to Market Segments Recoding. TheRecodingmodule opens.
- In theMigration Configurationtab, clickExportto download an Excel file of your current market segments.
- Open the Excel file and map the old market segments to new market segments in columns D, E and F:New Code: the name of the code for the new market segment or rate code.To replace one existing market segment or rate code, type the name next to theCurrent Code.To combine  several old market segments or rate codes into one, type theNew Codenext to each of the current codes that you want to combine.Copy and paste the line and type the new names if you split one old market segment or rate code into several new ones.Leave theNew Codefield empty if there is no change.Don't reuse a discontinued market segment code. For example, if you rename market segment ABC to DEF, and you rename another old market segment to ABC, you get aCyclic Mappingerror during the import.Data is invalid â delete the history: In almost all cases, selectNo. SelectYesonly if the historical data is invalid or older than two years. If you are not sure, contact your IDeaS representative.Is Primary Code for One to Many Splits: If you split one old market segment into several new ones, selectYesfor the new market segment that should receive all the historical data of the old code. SelectNofor the others, andG3 RMSonly assigns future business to them.
- New Code: the name of the code for the new market segment or rate code.To replace one existing market segment or rate code, type the name next to theCurrent Code.To combine  several old market segments or rate codes into one, type theNew Codenext to each of the current codes that you want to combine.Copy and paste the line and type the new names if you split one old market segment or rate code into several new ones.Leave theNew Codefield empty if there is no change.Don't reuse a discontinued market segment code. For example, if you rename market segment ABC to DEF, and you rename another old market segment to ABC, you get aCyclic Mappingerror during the import.
- To replace one existing market segment or rate code, type the name next to theCurrent Code.
- To combine  several old market segments or rate codes into one, type theNew Codenext to each of the current codes that you want to combine.
- Copy and paste the line and type the new names if you split one old market segment or rate code into several new ones.
- Leave theNew Codefield empty if there is no change.
- Don't reuse a discontinued market segment code. For example, if you rename market segment ABC to DEF, and you rename another old market segment to ABC, you get aCyclic Mappingerror during the import.
- Data is invalid â delete the history: In almost all cases, selectNo. SelectYesonly if the historical data is invalid or older than two years. If you are not sure, contact your IDeaS representative.
- Is Primary Code for One to Many Splits: If you split one old market segment into several new ones, selectYesfor the new market segment that should receive all the historical data of the old code. SelectNofor the others, andG3 RMSonly assigns future business to them.
- Save the modified workbook in an XLSX format.
- Click theChoose Filebutton.
- Navigate to and select the saved workbook.
- ClickImport.
- G3 RMSchecks the workbook for data and formatting errors. If it finds errors, it cancels the import and tells you which rows have errors. Click the Excel iconto export the error list. Correct the errors, then import the workbook again. SeeFix the issues that cause import failures.
When you successfully import the market segment mapping intoG3 RMS, theNew AMS Configurationtab displays in the Recoding module. Export the existing market segments and rate codes, assign the appropriate attributes, and then import them back into the system.
- Click theNew AMS Configurationtab.
- ClickExportto download an Excel file of your current market segments and rate codes.
- Open the Excel file and, in columns D and E of theAMS Attributionstab, select the appropriateAttributeandForecast Typeoption for each market segment and rate code. SeeAttributesfor definitions. Click the tab to see your property'sCurrent AMS Configuration.
- Save the modified workbook in an XLSX format.
- Click theChoose Filebutton.
- Navigate to and select the saved workbook.
- ClickImport.
- G3 RMSchecks the workbook for data and formatting errors. If it finds errors, it cancels the import and tells you which rows have errors. Click the Excel iconto export the error list. Correct the errors, then import the workbook again. SeeFix the issues that cause import failures.
If you see theConfirm Shifting of Rate Codeswindow,G3 RMSfound that some rate codes in the imported attribute Excel file now belong to a different market segment than before the import. The system wants you to confirm that you want to move the business of these rate codes between those market segments. ClickYesto confirm. ClickNoto keep the rate codes in their original market segment.
If you see theConfirm Assigning Undefined Rate Codes to Default Attributeswindow,G3 RMSfound rate codes in the imported attribute Excel file that belong to a split market segment and are missing attributes. ClickYesand the system assigns the attributes of the Default Market Segment to these rate codes. ClickNoto change the attributes for any rate code in the template and upload a new version.
- ClickInformation Manager. The Alert tab displays.
- Find and click theComplete Market Segments Recoding InformationAlert.
- ClickI have completed the Market Segments Recoding.
The system changes the market segments and rate codes in all reservations and groups. Then it rebuilds the data that you see inG3 RMS, like pace, for changed market segments and, if needed, rate codes. The process takes about 35 to 90 minutes.
Note that after the rebuild you might see data differences betweenG3 RMSand other systems. Seepace differencesfor details.
After the rebuild completes, IDeaS checks the data to ensure that the recoding changes were applied correctly.
You get theCreate and Commit Forecast GroupsAlert. ClickGo to Market Segments configuration and click Create Forecast Groups. Then click toCreate Forecast Groups. Reviewthis topicfor the detailed steps. After you commit the Forecast Groups,G3 RMSstarts a full optimization and goes into Read Only mode. That takes five to ten minutes.
Return to the Alert and clickI have completed creating and committing Forecast Groups.
If you haven't already, complete the work in yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.. You need to move reservations from the old to the new market segments and set old market segments to inactive. Inform your IDeaS representative when you are done.
IDeaS updates the system with the missing extracts and resumesprocessing. Once theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.is current, we ask you to review.
Review the forecastanddecisions. Then confirm to IDeaS thatG3 RMScan resumeDecision Delivery Mode.
G3 RMSresumes sending decisions to your selling systems. You are back to normal operations.

## Best Practices for Recoding Market Segments

### Fix the Issues that Cause Import Failures

If the worksheet has data or format issues, the import fails. To  avoid failures, ensure the following:
- Don't reuse a discontinued market segment code. For example, if you rename market segment ABC to DEF and you rename another old market segment to ABC, you get a "Cyclic Mapping" error during the import.
- Don't add, delete, move, or rename columns.
- Don't change the name of the worksheet.
- File type remains .XLSX
