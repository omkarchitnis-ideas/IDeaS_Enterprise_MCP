# On Demand Optimization

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Optimization/On-Demand-Optimization.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Optimization/On-Demand-Optimization.htm`
- **Ingestion Date:** `2026-09-11 22:14:33`

---

# On Demand Optimization

If available with your subscription and integration, On Demand Optimization allows you to manually start a processing if you needG3 RMSto react to significant changes, and you can't wait until the next scheduled processing. Use this option only in exceptional cases as frequent use might cause slower performance ofG3 RMSand your reservation and selling systems. If frequent use negatively impacts performance of these systems, IDeaS might restrict your access.
- Large bookings or cancellations of groups.
- Severe weather events.
- Large changes of out of order rooms.
- When a new special event with a large impact on your market is announced.
- When you use overrides to make strategic changes in demand or pricing.
Clickin the top right to start an On Demand Optimization.  Before processing starts, you select the BDE or IDP window. Use the IDP window unless the change occurs outside of the IDP window. That's because the BDE window means longer processing and Read Only Mode. For both options,G3 RMSsendsupdated decisionsIn an optimizaton, the RMS sends updated, or differential, outputs. That means that it sends only changes in pricing, overbooking or LRV that happened in the last optimization. For a full decision file that replaces all existing decisions, please open a case..
