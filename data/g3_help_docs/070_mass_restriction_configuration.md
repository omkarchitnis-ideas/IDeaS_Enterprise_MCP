# Mass Restriction Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/Restriction-Configuration-Mass.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/Restriction-Configuration-Mass.htm`
- **Ingestion Date:** `2026-09-11 22:12:54`

---

# Mass Restriction Configuration

Use the Mass Restriction setup option to set up, change or review your Restriction setup using an Excel workbook. SeeRestriction setupto learn about Restriction setup and understand if you need to use it.
Use Mass Restriction setup to set up restrictions for the first time, or to change or add rate plans. Start by exporting a pre-formatted workbook from your property inG3 RMS. Enter your rate plans and rate details or modify rate details in the workbook, then import it back intoG3 RMSto populate or change your Restriction setup. This tool will only add or amend rate plans and seasons that you update in the uploaded worksheet. All other rate plans or seasons in the system will remain unchanged.
Even if you choose to set up your rate plans directly in Restriction setup without this option, you can still use the export function to review your setup, particularly if you have many rate plans and seasons.
The Mass Restriction setup option is available only at the individual property level. For more information, viewbest practices for Mass Restriction setup.

### Advantages of Using Mass Restriction Setup

Mass Restriction setup provides several features that are not available when setting up directly in Restriction setup:
- View and interact with a large number of rate plans across a range of dates in one worksheet
- Take advantage of Excel features like filters, formulas and copying values, to reduce setup time
- Highlight and send proposed changes to others for approval before committing changes

## Setup Steps

- Click, thenDecisions, and thenMass Restrictions.
- In the Export pane, select a workbook option:SelectBlankto set up new rate plans. The worksheet will populate with the Property Name, Room Class and Room Types but will not include any other rate plan details.SelectAllto download and modify all of your existing rate plans (up to 10,000 rows). The worksheet will populate with the existing rate plan setup.SelectFilterto download a subset of your existing setup. For example, you want to change the rates for one rate plan and one season. Select any combination of the following filters:Select aStart Dateand anEnd Dateto find rate plans that are set up for the specified date range.Select theDerived,YieldableorNon-Yieldablecheckbox to download a subset of existing rate plans. See Worksheet Data above for definitions of these rate plan characteristics.By default,G3 RMSselects all rate plans for download. Remove any rate plans from theRate Plans Selectedlist that you do not want to edit. PressCtrl+click to select the ones to remove, and click<to remove them.
- SelectBlankto set up new rate plans. The worksheet will populate with the Property Name, Room Class and Room Types but will not include any other rate plan details.
- SelectAllto download and modify all of your existing rate plans (up to 10,000 rows). The worksheet will populate with the existing rate plan setup.
- SelectFilterto download a subset of your existing setup. For example, you want to change the rates for one rate plan and one season. Select any combination of the following filters:Select aStart Dateand anEnd Dateto find rate plans that are set up for the specified date range.Select theDerived,YieldableorNon-Yieldablecheckbox to download a subset of existing rate plans. See Worksheet Data above for definitions of these rate plan characteristics.By default,G3 RMSselects all rate plans for download. Remove any rate plans from theRate Plans Selectedlist that you do not want to edit. PressCtrl+click to select the ones to remove, and click<to remove them.
- Select aStart Dateand anEnd Dateto find rate plans that are set up for the specified date range.
- Select theDerived,YieldableorNon-Yieldablecheckbox to download a subset of existing rate plans. See Worksheet Data above for definitions of these rate plan characteristics.
- By default,G3 RMSselects all rate plans for download. Remove any rate plans from theRate Plans Selectedlist that you do not want to edit. PressCtrl+click to select the ones to remove, and click<to remove them.
- ClickExport.
- Save the file to a location on your computer.
- Complete theRestriction Configurationworksheet. Be sure to follow the instructions and example provided in the "Instructions" worksheet and the guidelines listed above.
- Save the modified workbook.
- In the Import pane, clickChoose File.
- Navigate to and select the saved workbook.
- ClickOpen.
- ClickImport.
The Import pane displays the import status and last import date.

### Worksheet Validation

G3 RMSruns a validation process on the workbook as it is imported to check for data and formatting errors. If you have thousands of rows, this process may take several minutes.
If the workbook is valid, the data imports and is available to view in Restrictions setup.
If the import process fails, no data imports. You can re-import the workbook after correcting the errors shown in the error message. The error message identifies the row numbers where errors occurred. Click the export iconto export the error list.
Review thebest practicesor the "Instructions" worksheet in the file for assistance with correcting errors.

## Data Details

The Restriction setup worksheet contains the following data:
