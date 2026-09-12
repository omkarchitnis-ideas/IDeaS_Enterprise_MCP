# Sync

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Optimization/Sync-Services.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Optimization/Sync-Services.htm`
- **Ingestion Date:** `2026-09-11 22:14:01`

---

# Sync

G3 RMSdisplays a flagin the top right after any changes that make the existing forecasts and decisions no longer optimal. Major changes, like certainRoom Class changes, also trigger the Read Onlymode, where you can't make any changes. If you need to resolve both issues before the nextprocessing, start a Sync.
A Sync includes anOptimizationThe step in the RMS Processing when the system uses the demand forecast (volume and value), the available capacity to sell, your configuration, and your interactions (like events, overrides) to calculate the outputs that maximize your revenues or profits. Outputs include pricing for the primary priced product, LRV, and overbooking. An Optimization also updates the constrained Occupancy Forecast.but differs from a full processing, see theBest Practicesfor details.
- Adding or removing a past instance of a Special Event.
- Resolving theOut of Order rooms present in hotel dataAlert with option C) (don't use the data to forecast).
- Changing the setup for Room Classes, Overbooking, Cost of Walk,Price Ranking and Upgrade Path, Minimum Price Differential (decreases),Rate Shopping, Forecast Groups, Linked Products, and Pricing.
- Adding or changing a Floor or Ceiling override. This means thatG3 RMSneeds to consider a new price range.
- Adding or changing a Specific override on the Base Room Type.
- If you use Profit Optimization, changes to the Channel Configuration.
Note: Changes to Room Classes, Linked Products configuration, and removing past instances of a Special Event also causeG3 RMSto check all of its demand models, seeself-learningfor details. These can lead to unusually large changes to forecasts and decisions, seeSpecial Eventsfor an example.

## Steps to Start a Sync

You need to have thepermissionsTogether, Role and User management define the Permissions (under Configure). 
- Roles define the access to the RMS functionality, like a role that can add pricing overrides but can only view the pricing configuration. 
- And each user is assigned a role with the appropriate access.to start a Sync.
- Click the flagicon in the top right corner of the page. The Sync window opens and displays what triggered the flag.
- Click theSync Allbutton.If you saved a Floor, Ceiling,  or linked products override, you canSync All and Upload.The Sync begins.Review the best practice for when to useSync All and Upload.
- A spinning icondisplays to the right of the flag to indicate that the Sync is running. And the lock iconbefore the flag means that the page is in Read Only mode and you can't save any changes.
- When the Sync is complete, all three icons disappear.

## Best Practices

### Understand the Options to Resolve the Sync Flag

#### Until you start a Sync:

- Forecasts and decisions are suboptimal.
- In aWhat Ifscenario, the results only reflect the overrides added since the last processing.
- You can't make any changes like overrides on pages with the Read Only lock.

#### After the Sync but before the next processing:

- G3 RMSupdates forecasts and decisions for the full optimization window, using the last available  data from theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system..Note: If you made only pricing overrides, the system updates only the date of the last override plus 14 days. For independent products, the system updates  the last override date plus twice the productâs defined Maximum Days for Length of Stay.
- But,unless you clickedSync All and Upload,G3 RMSdidnotsend the revised decisions to theselling system.  That means that decisions betweenG3 RMSand yourselling systemmight not match.
- The Read Only lock is removed and you can make changes.
- In aWhat Ifscenario, the results reflect the revised forecast and decisions.Note that a Sync doesn't considerMinimum Change Valuesfor possible price changes.
Note that a Sync doesn't considerMinimum Change Valuesfor possible price changes.

#### In the next processing:

- G3 RMSuses the newest data from theReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.and uploads any revised decisions to theselling system.

### Know When to Use the Sync All and Upload Option

After you apply a Floor or Ceiling Pricing override, you have to run a Sync before you can manuallyUploadthe new values to yourselling system. In those cases, you have the option to clickSync All and Upload.G3 RMSruns a Sync and then uploads the changes to yourselling system.
