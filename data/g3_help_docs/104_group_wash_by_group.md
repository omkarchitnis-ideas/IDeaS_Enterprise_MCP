# Group Wash by Group

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Wash/Group-Wash-by-Group.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Wash/Group-Wash-by-Group.htm`
- **Ingestion Date:** `2026-09-11 22:13:17`

---

# Group Wash by Group

Use Group Wash by Group to review and manage group data:
- Review data such as picked up 
 versus remaining block during
 regular reviews of group business, for example, in a weekly group 
 pick-up meeting. SeeData Details.
- Review and, if needed, override the groupwashThe drop in occupancy due to cancellations, no-shows, group cut-offs, etc. For future dates, the percentage is the expected drop for the Total Demand. For past dates, it is the expected wash as of the last optimization.byIndividual 
 Group.
- If you have many groups and don't want to override wash for each group, you can applyGroup Occupancy Forecast Overrides.
For an overview of howG3 RMScalculates and uses  wash, seeDemand and Wash Management.

### Group Occupancy Forecast Overrides

Mostclientsreview and, if needed, override wash for each individual group. But if you manage many groups, that can become very time consuming. Therefore,G3 RMSoffers Group Occupancy Forecast Overrides. With this override type, you enter the expected final pickup by Forecast Group. Then,G3 RMScontrols and adjusts the remaining demand and wash for all groups in that Forecast Group. Seethe examplefor details.
These overrides can save time, but you should use them carefully:
- They are less precise than Wash overrides at the individual group level, seethe comparison.
- You need to review them closely because they don't adjust as conditions change, seebest practices.
- Before you use them, ensure that yourRoom Class Capacity Ratiosetup is correct.

## Dashboard Steps

Use the By Occupancy Date tab on the Group Wash by Group page 
 to view and manage group business by occupancy dates and drill down to 
 group details. You can also use this tab to add or modify wash overrides for specific 
 dates.
- Clickand thenGroup 
	 Wash by Group.If you visit this page often, clicknext to the name to add it to the Quick Access menu.
- Click the arrows before or after the date button to select 
	 the previous or next consecutive month.
- Use the date slider to change the selected dates in the month. Click the 
	 start date or end date and drag it to the right or left to specify a date range.
- ClickGroup Block Graphto see a visual where each bar represents a
	 group and its length matches the  group's stay dates. Colors represent the market segment. Hover over a bar to view details.
- In the tables 
	 below the graph, view the Daily Status row for data that impacts certain days, like a Special Event.
- Compare the room values for Block, Transient Block (if used), Non-Block, and Total 
	 Property business for each date.  Use any of the following options to compare:Click to opena row for more detail.Clickto view or enter Notes.Clickto view or add Wash Overrides by Forecast Group.
- Click to opena row for more detail.
- Clickto view or enter Notes.
- Clickto view or add Wash Overrides by Forecast Group.

## Override Wash Steps

### Override Wash for Individual Groups

SeeSteps to Override		 Wash for Individual Groupsto learn how to apply wash 
		 overrides to the on-books business.

### Steps to Add, Change or Delete Group Occupancy Forecast Overrides

Group Occupancy Forecast Overrides are an optional functionality, see thewash overviewand thebest practicesto learn more.

#### Day by Day Group Occupancy Forecast Override

- For the appropriate Forecast Group and date, override the system's expectation of the final Occupancy Forecast with your new value.You canrename the Forecast Groupsto ensure they are easily understood by you and your team.
You canrename the Forecast Groupsto ensure they are easily understood by you and your team.
- The unsaved changes icondisplays in theDaily Statusrow.
- To change an existing override, enter the new override value.
- Click the blue arrownext to the Forecast Group name.
- Click the calendarto change the Expiration Date.
- Click Deleteto remove a Group Occupancy Forecast Override.
- ClickSave.G3 RMStries toadjust wash and remaining demandbased on your override. If your override value exceeds thePhysical CapacityThe total number of guest rooms at a property, including out of order rooms., the system warns you. ClickOk, adjust your override and save the new value.G3 RMSremoves the unsaved changes iconand confirms that the changes are saved.
- G3 RMStries toadjust wash and remaining demandbased on your override. If your override value exceeds thePhysical CapacityThe total number of guest rooms at a property, including out of order rooms., the system warns you. ClickOk, adjust your override and save the new value.
- G3 RMSremoves the unsaved changes iconand confirms that the changes are saved.

#### Multiday Group Occupancy Forecast Override

- ClickGroup Multiday.
- Select the start and end dates for your override. If needed, add an Expiration Date.
- Enter the override value next to the appropriate Forecast Group.
- ClickApply. Or click toRemoveexisting overrides.
- The unsaved changes icondisplays in theDaily Statusrow for each override date.
- ClickSave.G3 RMStries toadjust wash and remaining demandbased on your override. If your override value exceeds thePhysical CapacityThe total number of guest rooms at a property, including out of order rooms., the system warns you. ClickOk, adjust your override and save the new value.G3 RMSremoves the unsaved changes iconand confirms that the changes are saved.
- G3 RMStries toadjust wash and remaining demandbased on your override. If your override value exceeds thePhysical CapacityThe total number of guest rooms at a property, including out of order rooms., the system warns you. ClickOk, adjust your override and save the new value.
- G3 RMSremoves the unsaved changes iconand confirms that the changes are saved.

## Data Details

The first two icons in the following table display inG3 RMSin theDaily Statusrow. Point to an icon for information, click it for more details, or to edit information.  Use the tables 
	 below the Daily Status row to compare rooms data for Block, Transient Block (if used), Non-Block, and Total 
	 Property business. Click to opena row for more details.
The following data displays:
