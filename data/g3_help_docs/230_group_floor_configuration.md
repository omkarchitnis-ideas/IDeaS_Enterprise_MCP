# Group Floor Configuration

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Pricing/Group-Floor-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Pricing/Group-Floor-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:14:42`

---

# Group Floor Configuration

If you have enabled theGroup Floorfunctionality, use this setup to define when and howG3 RMSsets Group Floor overrides. The Configuration includes defining the minimum difference between the highest guaranteed group rate and theFinal PriceThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing..

## Setup Steps

- Click, thenDecisions, and thenGroup Floor Configuration.
- Select the Room Classes thatG3 RMSchecks when it considers Group Floor overrides. Click > to add selected Room Classes, or click >> to add all Room Classes.
- Select the group Market Segments thatG3 RMSchecks when it considers Group Floor overrides. Click > to add selected Market Segments.
- Enter theMinimum Peak Block Threshold. See Data Details for more information.
- Enter the percentage value that defines theShoulder Night Threshold.
- Select if the Minimum Difference Type should be aFixedvalue or aPercentage.
- Enter theMinimum Difference Value. See Data Details for more information.
- SelectStop applying group floorif you don't have to honor thebest priceguarantee close to arrival, for example, after the group cut-off date.
- If you selected this option, define whenG3 RMSshould begin ignoring the group floor setup:On the day of arrival.A specific number ofdays to arrival.OnCut-off date, if your reservation system sendsG3 RMSthat date.
- On the day of arrival.
On the day of arrival.
- A specific number ofdays to arrival.
A specific number ofdays to arrival.
- OnCut-off date, if your reservation system sendsG3 RMSthat date.
OnCut-off date, if your reservation system sendsG3 RMSthat date.
- Click toSavethe changes. TheSyncflag displays.
Click toSavethe changes. TheSyncflag displays.

## Data Details
