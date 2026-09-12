# Best Practices for Hierarchy Setup

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Linked-Products/BP-Linked-Products-Hierarchy.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Linked-Products/BP-Linked-Products-Hierarchy.htm`
- **Ingestion Date:** `2026-09-11 22:14:54`

---

# Best Practices for Hierarchy Setup

## Avoid Conflicts

You see anInvalid Hierarchywarning  ifthe RMSdetects that it can't apply the hierarchy. Ensure that these rules apply:
- TheFloorThe minimum, or lowest, price that your property is willing to sell.values of the (lower-priced)Productmust be less than or equal to the Floor values of the (higher-priced) product that itRelates to. SeeCeiling/Floorto learn about the setup.
- TheCeilingThe maximum, or highest, price that your property is willing to sell.values of theProductmust be less than or equal to the Ceiling values of the product that itRelates to.
- The Ceiling values of theProductmust be greater than or equal to the Floor values of the product that itRelates to. In other words, they must have an overlap.  In the below example, Advance Purchase (theProduct) has an adjustment range of 12 to 20 percent offthe primary priced productand Semi-Flexible (theRelates toproduct) a range of 0 to 10 off. That means there is no overlap between them. If you change the ranges to 0 to 15 and 10 to 25, then there is an overlap between 10 and 15.
- If used, the Minimum Difference can't be more than the difference between the Floor of theProductand the Ceiling of the product that itRelates to. In our example, if Advance Purchase has a Floor of 30 offthe primary priced productand Semi-Flexible a Ceiling of 0, then the maximum value of the Minimum Difference is 30.
When you change the pricing setup of a product,the RMSchecks if that creates a conflict in a hierarchy. If a conflict exists, the system deletes the hierarchy. Review, and if needed, create a new hierarchy.
