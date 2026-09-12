# Vendor Mapping

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Rate-Shopping/Rate-Shopping-Vendor-Mapping.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Rate-Shopping/Rate-Shopping-Vendor-Mapping.htm`
- **Ingestion Date:** `2026-09-11 22:12:52`

---

# Vendor Mapping

After you change to a new rate shopping vendor, use Vendor Mapping to helpG3 RMSunderstand how your previous shopping data relates to the new  (if market data is enabledBy default, the RMS can use market data (Rate Shopping, Demand360, or Reputation) to improve its forecasts and controls (like pricing or LRV). If needed, the system can ignore such data in its optimization. For details, open the Important Information topic and review the Market Data section.). This tab only displays whenG3 RMSdetects shopped data from more than one vendor and requires information about the new vendor's data.
For an overview, reviewall steps and the benefits of Rate Shopping setup.

### Purpose of Mapping Vendors

When you change vendors,G3 RMSreceives new, vendor-specific room types, competitors and channels. While the channels and competitors shopped may be the same with both vendors, the codes and names used by each vendor may differ.  The Vendor Mapping feature helpsG3 RMSknow how the previous shopped data relates to the new.
Vendor Mapping also minimizes any disruption toG3 RMSfrom the vendor change. The system needs to gather a minimum number of data points to use the new rate shopping data, while the data thatG3 RMSreceived from the previous vendor still exists in the system.  Using Vendor Mapping to map the room types, competitors and channels from the two vendors allowsG3 RMSto continue using the matching data from the previous vendor in its analytics while it begins receiving the new rate shopping extracts.
If you set up aCompetitor Price Change Notification, consider disabling the Notification until the new vendor's data is populated inG3 RMS, to avoid receiving a large number of notifications.

## Setup Steps

- Click, thenExternal Data, and thenRate Shopping.
- Click theVendor Mappingtab. The previous vendor's data displays in the two left-hand columns. The new vendor's data is available in the two right-hand columns.
- Map the data from the previous vendor to the data from the new vendor by Room Type, Competitors and Channel. You must complete all sections in Vendor Mapping. Any previous vendor data that you do not map to the new vendor will be deleted fromG3 RMSwhen you save this setup. See Data Details below for information about the columns.
- After you verify that your mappings are correct, clickSave. Any data from the previous vendor that you did not map to the new vendor will be deleted fromG3 RMS.

## Data Details

### Mapping Room Types:

### Mapping Competitors:

### Mapping Channels:
