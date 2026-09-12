# Best Practices for Overbooking

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Overbooking/BP-Overbooking-Management.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Overbooking/BP-Overbooking-Management.htm`
- **Ingestion Date:** `2026-09-11 22:14:45`

---

# Best Practices for Overbooking

## Understand How Room Type Overbooking Impacts Property Overbooking

Property overbooking isnotthe sum of all room type overbooking, but it is limited by room type overbooking. The total property overbooking can never be more than the sum of all room type overbooking. When you limit room type overbooking, you might also limit the overall property overbooking. Property overbooking has a significant impact on the systemâs forecasts and can impact other decisions like pricing, sincethe RMSoptimizes all decisions together.
If you useRun-of-House overbooking, you can override overbooking only at the property, not the room type level.

## Understand Howthe RMSShares Wash Within a Room Class

The RMScalculates overbooking for a room type based on its expected wash. That wash doesn't change when you restrict the room type's overbooking through configuration, ceiling default, or a ceiling override. And when the system calculates property overbooking, it must consider the wash ofallroom types.
Thus,the RMSshares the wash of a room type with restricted overbooking, adding it to the overbooking of other room types in the same Room Class. This sharing  only works if the receiving room type allows overbooking without any ceiling. Seescenarios for Overbookingfor examples.
