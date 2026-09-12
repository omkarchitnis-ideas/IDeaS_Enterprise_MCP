# Out of Order Overrides

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Integrations/Out-of-Order-Overrides.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Integrations/Out-of-Order-Overrides.htm`
- **Ingestion Date:** `2026-09-11 22:14:28`

---

# Out of Order Overrides

Use Out of Order Overrides to  giveG3 RMSthe correct out of order information when it should ignore that information from yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.. This functionality has two purposes:

### Removing Out of Order Rooms fromG3 RMS

Sometimes you add out of order rooms in your reservation system, but you don't want the reduced inventory to impact pricing inG3 RMS. For example, you add out of order rooms because of  staffing concerns. Or because of the booking window of owner inventory (residences that your property can rent when the owners don't occupy them).

### Adding Out of Order Rooms toG3 RMS

The functionality is helpful for:
- Properties that are 100% closed and can't, or don't want to, place rooms Out of Order in theirreservation system.
- Properties that are partially closed and place rooms Out of Order because they can't use the recommended Out-of-Service (or similar non-deduct) status. Out of Order rooms reduce capacity and impact decisions. To avoid that, such properties can use this functionality to reduce the number of Out of Order rooms inG3 RMS. SeeRestricted Inventoryfor details about how to manage closures inG3 RMS.
Note that Out of Order Overrides impact theEffective CapacityThe property's physical capacity minus the out of order rooms.and therefore optimization outcomes, for exampleoverbooking. If you use overrides to place 100% of your capacity out of order,G3 RMSassumes that no rooms are for sale.

## Override Steps

- Clickand thenOut of Order Overrides
- If necessary, use theFrom,To,Day of Week,Inventory Group, andRoom Typefilters to change the displayed data  for which you want to add or change
	 overrides.
- CheckEnable overrides to existing valuesif you want to override to a value that is currently displayed. If you don't check it, you can't click a field and save the existing value as an override. That means that in the next processing the value gets overridden with the value from yourreservation system.
- In the table, click the cell for the date and room type of the override. To apply the same override value to more than one date at once, clickMultiday Override.
- Enter the override value. Press the Tab key to navigate to other room types.
- Unsaved changes are highlighted in yellow. Click theicon and select the room types to revert the changes for that day. ClickCancelto revert all changes.
- ClickSave. The dates with overrides are highlighted in orange. You can also view Out of Order Overrides on the Summary tab of theBusiness Analysisdashboard. An Out of Order value with an override is highlighted in orange.
- Click Deleteand select the room types to remove overrides for that day. To remove overrides for more than one day at once, clickMultiday Override.
- Click the Export to Excel iconto export the data to a spreadsheet.
