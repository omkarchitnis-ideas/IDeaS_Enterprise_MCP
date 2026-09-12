# Scheduling Reports

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Reports/Scheduled-Reports.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Reports/Scheduled-Reports.htm`
- **Ingestion Date:** `2026-09-11 22:13:45`

---

# Scheduling Reports

Scheduling reports saves you time by automatically sending reports to selected recipientsor servers, and at your preferred frequency.
To schedule a report, you must:
- Have the permission - if you do, you seeScheduled Reportswhen you click, thenReports.
- Use rolling dates for the report's date range.
- Select Excel instead of On Screen format.
- Havereplies-disabled@ideas.comas a trusted address, if delivery is via email. Contact your IT team if you are not receiving the emails that you expect.
- Booking Situation Report
- Data Extraction Report
- Input Override Report
- Market Segment Mapping Report
- Operations Report
- Output Override Report
- Performance Comparison Report
- Pick Up/Change and Differential Control Report
- Pricing Override History Report
- Pricing Report
- Rate Plan Production Report

## Scheduling Steps

### Scheduling Reports

- Click, thenReports, and then 
	 the desired report.
- Set up the report dates and select Excel as the report format. To schedule any report (except Data Extraction and Operations reports), you must use Rolling Dates. See the specific reports for their date selection details.
- ClickSchedule. The Setup  pane 
	 displays.
- Enter aSchedule NameandDescription.
- Select theLanguagein which the report is delivered.
- Start Schedule: Select when the report is sent:After BDE(Business Day End, or NightlyProcessing)After IDP(intraday processing). Also sends the report after anOn-Demandoptimization.Note that to avoid sending scheduled reports without data,G3 RMSsends scheduled reports only if your property is inData Population ModeAn early status when IDeaS builds the RMS for a new property. During this set-up step, the RMS is processing the daily the RMS data extracts on a daily basis. The System Date is today.or higher.
- After BDE(Business Day End, or NightlyProcessing)
After BDE(Business Day End, or NightlyProcessing)
- After IDP(intraday processing). Also sends the report after anOn-Demandoptimization.Note that to avoid sending scheduled reports without data,G3 RMSsends scheduled reports only if your property is inData Population ModeAn early status when IDeaS builds the RMS for a new property. During this set-up step, the RMS is processing the daily the RMS data extracts on a daily basis. The System Date is today.or higher.
After IDP(intraday processing). Also sends the report after anOn-Demandoptimization.
Note that to avoid sending scheduled reports without data,G3 RMSsends scheduled reports only if your property is inData Population ModeAn early status when IDeaS builds the RMS for a new property. During this set-up step, the RMS is processing the daily the RMS data extracts on a daily basis. The System Date is today.or higher.
- Select daily or weeklyRecurrencefor how often the report is sent.
- For weekly delivery, you can select if the report is sent every week and on whichDay of Week. Clear the days that you don't want the report sent, for example on the weekend.
- Select how the report will be delivered:Email Delivery: The report is delivered via email to the users that you select.Select theEmail 
	 Recipientsto whom 
	 you want the report sent and click>to add them to the recipients list.To search for a user in the 
	 list, type their name in theSearch Users...field.FTP DeliveryorSFTP Delivery(if available): The report is placed on an FTP or SFTP server.Enter the Server Name of the FTP or SFTP server. This may be a text address, such as ftpserver.example.com or a numerical address, such as 255.255.255.255.Note: the IDeaS source server On Prem IP address range 130.96.13.1 to 130.96.13.254.Enter the Port number, normally 22. If you use a different number,open a caseto ensure successful delivery.Enter the Folder Path whereG3 RMSplaces the file. The field automatically contains a forward slash, â/â, so if you leave the rest of the field empty, the data will be saved to the root folder.Enter the User Name and Password as the credential for accessing the server.
- Email Delivery: The report is delivered via email to the users that you select.Select theEmail 
	 Recipientsto whom 
	 you want the report sent and click>to add them to the recipients list.To search for a user in the 
	 list, type their name in theSearch Users...field.
- Select theEmail 
	 Recipientsto whom 
	 you want the report sent and click>to add them to the recipients list.
- To search for a user in the 
	 list, type their name in theSearch Users...field.
- FTP DeliveryorSFTP Delivery(if available): The report is placed on an FTP or SFTP server.Enter the Server Name of the FTP or SFTP server. This may be a text address, such as ftpserver.example.com or a numerical address, such as 255.255.255.255.Note: the IDeaS source server On Prem IP address range 130.96.13.1 to 130.96.13.254.Enter the Port number, normally 22. If you use a different number,open a caseto ensure successful delivery.Enter the Folder Path whereG3 RMSplaces the file. The field automatically contains a forward slash, â/â, so if you leave the rest of the field empty, the data will be saved to the root folder.Enter the User Name and Password as the credential for accessing the server.
- Enter the Server Name of the FTP or SFTP server. This may be a text address, such as ftpserver.example.com or a numerical address, such as 255.255.255.255.Note: the IDeaS source server On Prem IP address range 130.96.13.1 to 130.96.13.254.
- Enter the Port number, normally 22. If you use a different number,open a caseto ensure successful delivery.
- Enter the Folder Path whereG3 RMSplaces the file. The field automatically contains a forward slash, â/â, so if you leave the rest of the field empty, the data will be saved to the root folder.
- Enter the User Name and Password as the credential for accessing the server.
- ClickSave.For SFTP and  FTP delivery,G3 RMSchecks connectivity. The system notifies you of any issues, using the credentials that you entered.

### Editing Scheduled Reports

The Scheduled Reports page lists the reports that are scheduled to be sent to selected users at a determined frequency.
To see scheduled reports:
- Click, thenReports, and thenScheduled Reports.The following information displays:
