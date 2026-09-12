# Manual Upload

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Pricing/Manual-Upload.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Pricing/Manual-Upload.htm`
- **Ingestion Date:** `2026-09-11 22:13:25`

---

# Manual Upload

Use the Upload option to send pricing overrides to yourselling systemimmediately, without waiting for the nextprocessing. For example,  flight disruptions at an airport property cause rapid changes in demand. The system can't know that and might not react quickly enough. In that case, override pricing, review and commit a What If Scenario,and use the Upload button.G3 RMSimmediately sends the new pricing decisions to yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.and, depending on your integration, otherselling systemsAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.as well.

## Upload Steps

- Clickand thenPricing.
- ClickUpload. The system confirms that the changes uploaded with a message.

## Best Practices

### Run a What If to Understand Consequences

Always consider that pricing overrides can have unintended consequences. UseWhat Ifto understand the impact of your overrides. Review Best Practices for  Overriding Pricing before uploading.
If you upload an override, the impact on forecasts and other decisions is not calculated until the next optimization. That means that you might upload suboptimal decisions. For example, your Room Classes are priced separately byG3 RMS. You override and upload a price increase for Standard from $100 to $200. If you forget to increase your higher-priced Room Classes, Standard might be priced above Deluxe and Suite until the next processing.

### Understand What ChangesG3 RMSSends

G3 RMSsends all overrides and all changed decisions for the full optimization window:

#### Linked Products

When you click Upload after an override of thePrimary Priced ProductMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.,G3 RMSalso updates and uploads the prices of anyLinked Productthat is based on it. For an optimized product, the system uses the last optimized value. For a linked product, it updates the value based on the configured adjustment.

#### Adding a Floor or Ceiling override

- If you save and upload a Floor or Ceiling override that doesn't change the pricing decision,G3 RMSdoesn't send the change. As an example, the current price is $100, and your Floor override is $90. The Floor or Ceiling override are sent during the next processing.
- If you save and upload a Floor or Ceiling override that changes the current price decision,G3 RMSsends the change. For example, the current price is $100, and your Floor override is $110 or your Ceiling override is $90.

#### Removing an override

After you remove an override, clicking the Upload option doesn't send a new pricing decision.G3 RMScreates and sends a new pricing decision in the next processing.
 To make the change immediately,run and commit a What-If scenario, then use the Upload button. Alternatively,save and upload a Specific Override.

#### Upload after committing Forecast Groups

When you use the Upload button after creating and committing Forecast Groups,G3 RMSsends all decisions that changed in the commit process.

### Know When You Can Use Manual Upload

The Upload button is grayed out until you save a pricing override. For Floor and Ceiling overrides you also need to clear theSyncflag.
If you don't see the Upload button, you might not have thepermissionsTogether, Role and User management define the Permissions (under Configure). 
- Roles define the access to the RMS functionality, like a role that can add pricing overrides but can only view the pricing configuration. 
- And each user is assigned a role with the appropriate access.to use it. If you verified that you have permission but still don't see it, contact your IDeaS representative to enable the functionality.
You cannot use the Upload option whenG3 RMSis in read-only mode because another pricing upload or scheduled processing is already in progress. The lock icondisplays next to theSystem DateDisplaying in the top right of each G3 RMS page, it's the time when  the RMS last received data from your reservation system. If the data is late, you get an Alert.during this time.
The Upload button can become active even if you didn't override pricing. That can happen if you run a Sync and, as a result, your pricing decisions change. If you click Upload, it includes all decisions that changed due to running a Sync.
