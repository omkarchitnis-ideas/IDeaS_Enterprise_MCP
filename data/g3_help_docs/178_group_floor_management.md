# Group Floor Management

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Group-Pricing/Group-Floor-Management.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Group-Pricing/Group-Floor-Management.htm`
- **Ingestion Date:** `2026-09-11 22:14:08`

---

# Group Floor Management

Use the Group Floor functionality if you offer abest priceguarantee in group contracts. Such a guarantee promises that the group's contracted price is lower than any price offered to the public. Without Group Floor,G3 RMSmight price  lower than a contracted group's price because it doesn't consider group rates in itspricing calculation.
After you contacted IDeaS to enable Group Floor, the system automatically adds Group Floor Overrides that keep  theFinal PriceThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing.above the guaranteed group price. The override limits the price range for the pricing decision to the values above the group price. UseGroup Floor setupto define when and howG3 RMSsets Group Floor Overrides. That includes defining the minimum difference between the highest guaranteed group rate and the Final Price.G3 RMSsendsAlertsto inform you when it changes the overrides.

## Group Floor Steps

- Clickand thenGroup Floor.
- G3 RMSshows data for theBase Room Typeof theMaster Classfor the next 31 days. You can change the default:Update theFromandTodate to view a different period. The maximum number of days is 31.Select a differentRoom Class.
- Update theFromandTodate to view a different period. The maximum number of days is 31.
- Select a differentRoom Class.
- Click theHighest Group Floor Pricefor the date you want to investigate (seeData Detailsto learn whenG3 RMSdisplays a value in that field):The system highlights the date in yellow and displays block details for all groups staying over that day.The group with the highest price is listed on top and highlighted in red.
- The system highlights the date in yellow and displays block details for all groups staying over that day.
- The group with the highest price is listed on top and highlighted in red.
- A check markindicates thatG3 RMSconsiders the group and the date when determining the need for a Group Floor override.Clear the checkbox before the group if you want the system to ignore that group completely.Clear the checkboxes for a date if you want the system to ignore that day.
- Clear the checkbox before the group if you want the system to ignore that group completely.
- Clear the checkboxes for a date if you want the system to ignore that day.
- Point to theHighest Group Floor Pricevalue to see the group name and its details.
- Click theLegendlink to view an explanation of all icons and colors.
- Click theFinal Pricefor a date to add or remove a pricing override. Thesteps to overrideare the same as on the Pricing page. You canUploadyour new overrides to your selling system or wait for  the next processing.

## Data Details

### Icons

### Data

## Best Practices

### Understand WhenG3 RMSApplies Group Floor Overrides

G3 RMSautomatically applies Group Floor overrides. To determine when to add them, the system goes through the following steps:
- Considers all blocks with aGroup Statustype that adjusts inventory.
- Filters by themarket segmentsthat you set up and by selectedgroups.
- Considers only groups that meet theMinimum Peak Block Thresholdthat you set up.
- Considers only groups that have at least one room sold in the selected Room Classes.
- Of those groups and for each occupancy date, finds the group with the highest price for the Base Room Type.Considers only the peak nights (using theshoulder night threshold) and only if they are selected.Uses the single-occupancy rate.If the Base Room Type has no occupancy in the block, selects the room type with the highest occupancy.
- Considers only the peak nights (using theshoulder night threshold) and only if they are selected.
- Uses the single-occupancy rate.
- If the Base Room Type has no occupancy in the block, selects the room type with the highest occupancy.
- Determines the Group Floor override value based on the selected minimum difference andRounding Rules.If Highest Group Floor Price is 125 and the minimum difference is 10, then the Group Floor override is 135.If Rounding Rules require prices ending in 9, the value is 139.
- If Highest Group Floor Price is 125 and the minimum difference is 10, then the Group Floor override is 135.
- If Rounding Rules require prices ending in 9, the value is 139.
- Sets this value as the Group Floor Override.G3 RMSdoesn't set any override if:The pricing range that you set up is above the calculated Group Floor. Otherwise, the override would expand the pricing range that you defined.A Floor override exists at the same value.
- The pricing range that you set up is above the calculated Group Floor. Otherwise, the override would expand the pricing range that you defined.
- A Floor override exists at the same value.
The system does this during every nightlyprocessingand, if it detects changes to groups, every intraday processing .

### Use Alerts to Monitor Overrides Efficiently

Managing all Group Floor overrides can be time consuming. To help you,G3 RMSprovides two Alerts in Information Manager that tell you when to review Group Floor Management. See theirAlert descriptionsfor more details.

#### Group Floor Override Change

This Alert shows you details of any changes to Group Floor Overrides, either that the system added new ones or that it canceled or changed existing ones.
- Use the link in theAlert Detailsto open Group Floor Management.
- If a new or changed group triggered the Alert, verify ifG3 RMSshould consider the group when determining the need for Group Floor Overrides. Select or clear its checkbox, if needed.
- If a Floor or Specific Override triggered the Alert, verify whether that override is needed and correct. Edit or remove the override.

#### Group Floor Potentially Constraining Pricing

The Final Price changed and now equals the Group Floor Override. The override might constrain pricing and optimal revenue.
- Use the link in theAlert Detailsto open Group Floor Management.
- Review the groups that cause the Group Floor Override. Their group best price guarantee might constrain pricing and optimal revenue. For example, a lower Final Price might result in higher overall revenue.
- Test the outcome. In Pricing, use the filterto view only dates where the Group Floor is equal to the Final Price. Remove the Group Floor Override and runWhat If. If the results show a lower Final Price, compare the outcome against any revenue loss from lowering the group rates.
Note: onlyG3 RMSadds and removes Group Floor Overrides. You can replace a Group Floor Override with a Floor Override.
In this scenario you see a simplified Group Floor Management page. Friday the 23rd is highlighted in yellow, where, at the top, you see 214 as theFinal PriceThe value of the pricing output that the RMS sends to the selling systems. Final Price is based on the Optimal Price, after applying rounding rules, offsets and supplements (if applicable). Final Price also includes your configured tax value, if you are using tax-inclusive (VAT) pricing.for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.. In the table below the price, you see 6 group blocks staying over that Friday.
Groups 1 to 5 have abest-priceguarantee in their contract. Group 6's price, 240, is higher than the Final Price of 214, but since they don't have a best-price guarantee, we don't worry about it. Two groups with such a guarantee,  Group 1 and 3, have prices (225, 230) above the Final Price.
To ensure that the best-price guarantee for those two groups is enforced,G3 RMSautomatically adds a Group Floor Override.  Letâs look at how the system determines that override:
Of the five groups with the best-price guarantee, Group 3 has the highest contracted rate, at 230. However, the gray highlight means that it falls on a shoulder, not on a peak night for the group. For Group Floor overridesG3 RMSonly considers peak nights. Not every group reservation stays over the  shoulder nights, so ignoring those nights helps minimize the potential negative impact of overridingthe primary priced product.
InG3 RMS, shoulder nights display in gray, peak nights in blue. You define shoulder vs. peak with a threshold % inGroup Floor setup, and the setup in this example means that the 23rd is a shoulder night for Group 3. ThusG3 RMSignores Group 3 for determining the Group Floor override for this date. Instead, the system looks for the highest group price among the four remaining groups with a guarantee. In this case, that's Group 1, at 225. The highest-priced group displays in orange.
You also define the minimum difference between the highest group price andthe primary priced product, in this example 10. This determines the Highest Group Floor Price, 235 (225 + 10). The Final Price overrideis at 239, because it considers a rounding rule to the nearest 9. The override also considers your setup for Minimum Change Value and  Offsets.
Following is a real example where Group Floor Overridesexist on three dates (19, 20, 21).
- On  the 21st, the Highest Group Floor Price is below the Final Price and therefore doesn't impact pricing. If the Final Price changes to being equal the Highest Group Floor Price, you receive an Alert, seeUsing Alertsfor details.
On  the 21st, the Highest Group Floor Price is below the Final Price and therefore doesn't impact pricing. If the Final Price changes to being equal the Highest Group Floor Price, you receive an Alert, seeUsing Alertsfor details.
- On the two other dates (19, 20) the Final Price equals the Highest Group Floor Price (which includes the minimum price difference of 5 that is configured for this property).
On the two other dates (19, 20) the Final Price equals the Highest Group Floor Price (which includes the minimum price difference of 5 that is configured for this property).
- On the 18th, the Highest Group Floor Price is above the Final Price but the checkbox is cleared and therefore doesn't impact pricing.
On the 18th, the Highest Group Floor Price is above the Final Price but the checkbox is cleared and therefore doesn't impact pricing.
- Two groups, ASIB and TF151, are also cleared and therefore don't impact pricing, even though on the 21st their price is higher than that of the SCMAX group.
Two groups, ASIB and TF151, are also cleared and therefore don't impact pricing, even though on the 21st their price is higher than that of the SCMAX group.
