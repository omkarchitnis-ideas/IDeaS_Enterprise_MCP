# Sales and Catering Status Codes

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Pricing/Status-Codes-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Pricing/Status-Codes-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:14:39`

---

# Sales and Catering Status Codes

Properties with an integration to their sales and catering system (like Delphi) use this tab todefinethe Status Codes  from that system. For example, if group blocks with a Tentative status are on books, deducting inventory from the available capacity.
Information about non-deducting groups from the sales and catering system combined with information about deducting groups from thereservation system(defined inGroup Status Codes)helpG3 RMSimprove its forecast of group business, seegroup forecastingfor details.WithFunction Spaceenabled, the data about non-deducting groups also improves the forecast of function room demand.

## SetupSteps

- Click, thenDecisions, and thenGroup Pricing Configuration.If you use Function Space, clickand thenConfiguration.
- ClickSales and Catering Status Codes. A table with your Sales and Catering Group Status Codes displays.
- For each status code,selectthe checkbox that describes its behavior:Deducts Inventory: group blocks with this status are on books, reducing the available capacity.Final: groups with this status can't change to another status anymore. Examples are Definite, Canceled, or Lost. Prospect is not a final status since it can become Tentative, Definite or Canceled.Tentative: a status that might change to Deducts Inventory, for example, Prospect or Unconfirmed. For groups with this status,G3 RMScalculates the probability of changing to Deducts Inventory.Prospect:with Function Space,groups with this status are included in the dataon theForecast Reviewpage, if you clickedto displayUtilization On Books with Prospects.Note:Leave a status code unchecked if none of these options apply.For example, if a code like Option or Inquiry defines a status before a group turns Prospect and then Tentative.
- Deducts Inventory: group blocks with this status are on books, reducing the available capacity.
Deducts Inventory: group blocks with this status are on books, reducing the available capacity.
- Final: groups with this status can't change to another status anymore. Examples are Definite, Canceled, or Lost. Prospect is not a final status since it can become Tentative, Definite or Canceled.
Final: groups with this status can't change to another status anymore. Examples are Definite, Canceled, or Lost. Prospect is not a final status since it can become Tentative, Definite or Canceled.
- Tentative: a status that might change to Deducts Inventory, for example, Prospect or Unconfirmed. For groups with this status,G3 RMScalculates the probability of changing to Deducts Inventory.
Tentative: a status that might change to Deducts Inventory, for example, Prospect or Unconfirmed. For groups with this status,G3 RMScalculates the probability of changing to Deducts Inventory.
- Prospect:with Function Space,groups with this status are included in the dataon theForecast Reviewpage, if you clickedto displayUtilization On Books with Prospects.
Prospect:with Function Space,groups with this status are included in the dataon theForecast Reviewpage, if you clickedto displayUtilization On Books with Prospects.
Note:Leave a status code unchecked if none of these options apply.For example, if a code like Option or Inquiry defines a status before a group turns Prospect and then Tentative.
- ClickSave.
