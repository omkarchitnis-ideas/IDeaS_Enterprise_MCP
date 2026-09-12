# Special Events Upload

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Special-Events/Special-Events-Upload.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Special-Events/Special-Events-Upload.htm`
- **Ingestion Date:** `2026-09-11 22:13:05`

---

# Special Events Upload

If you manage multiple properties in the same market, the Special Events Upload provides a convenient way to set up or edit Special Events. For example, you might have properties located close to each other that are affected by the same weather events, sporting events, or citywide conferences. Use the Special Events Upload to add new Special Events, change the setup of existing, or delete Special Events.
When you upload the template, the Special Events in the template replace all the Special Events that exist in the properties that you included in the template. Keep in mind that the template reflects the complete set of Special Events for the included properties and will override all existing Special Events setup.

## Setup Steps

- Click, thenForecasts, and thenSpecial Events Upload.
- Select a radio button to filter for the properties to manage Special Events:Filter by Property: allows you to select a subset of all the properties that you manage.Filter by Property Group: allows you to select from theProperty Groupsthat you manage. Click the Property Groups link to create new Property Groups.
- Filter by Property: allows you to select a subset of all the properties that you manage.
- Filter by Property Group: allows you to select from theProperty Groupsthat you manage. Click the Property Groups link to create new Property Groups.
- In thePropertyorProperty Groupspane, select the properties or groups with Special Events to add or edit. 
	 Press Ctrl+click to select multiple properties or groups. You must include all the properties for which you want to add, edit or delete Special Events.
- Click>to move all selected items to the pane on the right or click>>to add all the properties or property groups.
- ClickExport.The template  contains the setup details for  all existing Special Events   for the selected properties.
- Save the spreadsheet to a location on your computer.
- Add a new row for new events, delete an existing row, or modify existing events in these columns in the Special Event Configuration worksheet:
- Save the modified file in an XLSX format.
- In the Special Event Upload module, clickChoose File.
- Navigate to and select the saved template from your computer.
- ClickImport.
During the importG3 RMSvalidates the Special Event template to check for data and formatting errors. If no errors are found, all the Special Event data is saved inG3 RMSand can be viewed by month and by property in Special Events Management.
If the import process fails, no data imports. You can re-import the template after correcting the errors listed afterLast import errorson the Special Event Upload page.  The error message identifies the row numbers where errors occurred. Click the export iconin the error message to export the error list.
After you upload the template, you can make changes to Special Events for individual properties inSpecial Events.

## Best Practices

### Don't Change the Template Columns

- Do not change the first row that contains column headings.
- Do not change the column order.
- Do not change the cell formatting.
- Do not change the Client Code.
- Do not add Property Names or Codes. Before you export the template, include all the properties for which you want to add, edit or delete Special Events.
- The Event Category must match one that you already set up inG3 RMS, for each property. You cannot create new Categories using the template.
- If you change the name of an existing Special Event,G3 RMSconsiders it a new Special Event. If it was part of a recurring Special Event,G3 RMSwill split the renamed event from its other instances. SeeForecast Changes from Entering Past Special Eventsfor more information about the impact.
- To delete a Special Event, delete its row in the exported template. Do not delete rows for Special Events that you want to keep inG3 RMS.
- Use the selectors to choose acceptable values for the Impacts Forecast, Guest Room Forecast, and Function Space Forecast columns.
- If needed for your own work, you can enter new worksheets that do not contain template data.G3 RMSignores this extra worksheet when you import the template.

### Include Valid Data

- Copy and paste rows and update the Property Name or Code to add the same Special Event to multiple properties.
- The Start Date and End Date format must be dd-mmm-yyyy, for example: 09-Oct-2021 or 21-Mar-2025.
- The Pre-Event Days and Post-Event Days columns must contain a value. If no days before or after the event are affected, use "0" in the column.
- Complete all columns for each row.
- Keep the length of the Special Event name to less than 50 characters, or the name will be trimmed when you upload the template.
- You can only add Special Events for properties that you include in the exported template.
- If you add a Special Event to one or more properties, you do not need to add it to all properties that you included in the template.
- To add a recurring Special Event, add one row for each instance of the event, each with a unique date range.
- To create recurring instances of the same Special Event at a property, the Property Name or Code, Event Category, Event Name, and Impact Forecast settings must match.
