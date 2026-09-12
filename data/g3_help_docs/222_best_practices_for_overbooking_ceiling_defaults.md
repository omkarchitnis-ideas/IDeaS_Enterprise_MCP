# Best Practices for Overbooking Ceiling Defaults

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Overbooking/BP-Overbooking-Ceiling-Defaults.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Overbooking/BP-Overbooking-Ceiling-Defaults.htm`
- **Ingestion Date:** `2026-09-11 22:14:37`

---

# Best Practices for Overbooking Ceiling Defaults

## Consider Other Factors Before You Apply Ceiling Defaults

The RMSoptimizes all decisions together, so applying Ceiling Defaults directly influences other decisions in the system. For example,  by lowering overbooking with a ceiling default, you keepthe RMSfrom offsetting wash. The system may forecast occupancy to be below capacity, despite demand that is well above capacity.  It might also increase price and LRV to get the most revenue from the lower occupancy.

### Understand When To Use Ceiling Defaults

A ceiling limits the system's ability to optimize overbooking and to offset wash, see thefactors that impact overbookingabove. But there are valid scenarios for ceiling defaults, like when your property changes the business practice of upgrades.
For example, the practice was to overbook the lower-priced room types and to upgrade for free. Due to the strong demand and wash for those lower-priced room types, their overbooking inthe RMSis likely high.
Now the property wants to restrict free upgrades. It directs the reservations team to sell the higher room types. In that case, a Ceiling Default on the lower-priced room types might be the right temporary solution. Once the system has learned from the data that there is more demand for the higher-priced room types, you remove the Ceiling Default.
Note: you can't set a zero value as the Ceiling Default. If you do not want to allow overbooking for a room type or day of week, useRoom Type Configuration.

### Override the Ceiling Defaults If Needed

You can override a Ceiling Default in two ways:
- A seasonal overbooking inRoom Typesetup overrules a Ceiling Default if both exist for the same room type.
A seasonal overbooking inRoom Typesetup overrules a Ceiling Default if both exist for the same room type.
- Use an overbooking override.And run aWhat Ifto test the impact.
Use an overbooking override.And run aWhat Ifto test the impact.
