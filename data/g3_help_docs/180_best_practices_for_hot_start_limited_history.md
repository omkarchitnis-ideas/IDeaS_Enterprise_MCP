# Best Practices for Hot Start - Limited History

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/LDB/BP-Hot-Start-Limited-History.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/LDB/BP-Hot-Start-Limited-History.htm`
- **Ingestion Date:** `2026-09-11 22:14:09`

---

# Best Practices for Hot Start - Limited History

## Consider the Differences in Managingthe RMS

The following are differences in managingthe RMSwith Hot Start - Limited History compared to a Standard build. They vary, based on your property's characteristics, for example, how much your demand varies by season.
- Special Events: Add repeating events onlyafterthe RMShas at least one past instance in its available history. This ensures it can better forecast future instances.
Special Events: Add repeating events onlyafterthe RMShas at least one past instance in its available history. This ensures it can better forecast future instances.
- Same as for Standard build properties, we recommend that you regularly (at least monthly) review the system's forecasts and decisions, seereview processfor details. And all properties reduce the frequency of reviews as they learn to trust the system's forecasts. But because your property might start with as little as two months of history, consider in your reviews that:To forecast unconstrained transient demand,the RMSinitially relies more on actual booking pace than historical demand, regardless of how far out the date is. Seetime to arrivalfor Standard build forecasting.The RMSlikely can't detect seasonal demand differences. If needed,override demand.Lack of seasonality in demand might impact the pricing. If needed, ensure a certain pricing position in your market, seeconstraintsfor details.For business types with a long booking window, the system might not fully understand the patterns of when it books and when wash occurs, seedemand calculation and useto learn more.
Same as for Standard build properties, we recommend that you regularly (at least monthly) review the system's forecasts and decisions, seereview processfor details. And all properties reduce the frequency of reviews as they learn to trust the system's forecasts. But because your property might start with as little as two months of history, consider in your reviews that:
- To forecast unconstrained transient demand,the RMSinitially relies more on actual booking pace than historical demand, regardless of how far out the date is. Seetime to arrivalfor Standard build forecasting.
To forecast unconstrained transient demand,the RMSinitially relies more on actual booking pace than historical demand, regardless of how far out the date is. Seetime to arrivalfor Standard build forecasting.
- The RMSlikely can't detect seasonal demand differences. If needed,override demand.
The RMSlikely can't detect seasonal demand differences. If needed,override demand.
- Lack of seasonality in demand might impact the pricing. If needed, ensure a certain pricing position in your market, seeconstraintsfor details.
Lack of seasonality in demand might impact the pricing. If needed, ensure a certain pricing position in your market, seeconstraintsfor details.
- For business types with a long booking window, the system might not fully understand the patterns of when it books and when wash occurs, seedemand calculation and useto learn more.
For business types with a long booking window, the system might not fully understand the patterns of when it books and when wash occurs, seedemand calculation and useto learn more.
- With Hot Start - Limited History you can benefit fromthe RMScompleting some of the configuration for you. But with the limited history, you might see less detailed results in the suggested setup. For example, the suggestedCeiling and Floorvalues might not include any seasonal variation. Review all automated configuration carefully and, if needed, manually adjust it.
With Hot Start - Limited History you can benefit fromthe RMScompleting some of the configuration for you. But with the limited history, you might see less detailed results in the suggested setup. For example, the suggestedCeiling and Floorvalues might not include any seasonal variation. Review all automated configuration carefully and, if needed, manually adjust it.
