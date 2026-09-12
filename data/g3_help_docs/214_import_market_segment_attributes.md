# Import Market Segment Attributes

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Market-Segments/Market-Segments-Import.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Market-Segments/Market-Segments-Import.htm`
- **Ingestion Date:** `2026-09-11 22:14:31`

---

# Import Market Segment Attributes

The import feature allows you to assign attributes  for a single property, using an Excel template. Use the template to add market segments or market segment and rate code combinations with their appropriate  attributes. Then, import the completed template intoG3 RMS. The functionality is meant for enterprise clients with standardized attributes and market segments. They import the standardized attributes for each property separately. Then each property assigns their unique attributions using Market Segment setup.
Review theMarket Segments Best Practicesprior to working with this setup. That helps you understand what you need to know about your market segments before you begin. SeeMarket Segment Attributesfor descriptions of the market segment attributes.
After you import the template for the first time and before you clickFinalize, you can modify the template. You can add or change market segments, rate codes, or their attributes. When you re-import the new version, all data that you imported earlier is overwritten. For more information, view best practices for Market Segments import.
After you finalize the attributes, the import option is no longer available. Seechanging market segments after the initial implementationfor more information.
Note that if you have  fixed price rate codes that change to a discount off BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) when the BAR price is below the fixed price, first ensure that the rate code is imported as either Unqualified or Linked toBase Product -BAR. Then, define the exact pricing of the rate code in theRate Protecttab.

## Import Steps

- Click, thenForecasts, and thenMarket Segments.
- If you are opening this page for the first time, a window asks you to refresh the screen. ClickRefreshto have all unassigned market segments display in the three tabs of the left pane.
- ClickImport AMS attribution.
- Navigate to and select the saved template.
- ClickOpen.
- ClickUpload. If successful, market segments defined in the template move from the Unassigned to the Assigned Market Segments pane. Market segments that you did not include in the template remain in the Unassigned Market Segments pane. Assign attributes to these market segments inG3 RMS. Or, modify the template and re-import it.
- Review your completed attributes. SeeReviewfor the available options and importance of this step.
- ClickFinalizeonly after you complete and review the assigned attributes.You can only click this button once.It is not available unless you mapped at least one rate code for every market segment, meaning that no market segments remain in the Group Business Level or Market Segment Level tabs.
- After you click Finalize andG3 RMSloads the data, you can see the new market segments in theForecast Groupstab. Past and future booking data displays inG3 RMSmodules.
- Finish other required setup work:Set up Room ClassesSet up PricingSet up Rate Shopping
- Set up Room Classes
- Set up Pricing
- Set up Rate Shopping
- Use theForecast Groupstab to create and commit the Forecast Groups, which results in the system's first forecast.

### Import Errors

G3 RMSchecks the import for data and formatting errors. If the template is valid, all the data is saved and you can view it inG3 RMSon the Market Segments tab.
If the import process fails, no attributes are imported. Correct the errors indicated in the message. Then re-import the template. The error message identifies the market segments and rate codes where errors occurred. Click the export iconin the error message if you wish to export the error list.

## Template Data

Complete the template with the following information:

## Best Practices

Your IDeaS representative supplies you with the template file to set up your market segment attributes.

### Enter Valid Data

- The file name is customized for the property using predetermined client and property codes.G3 RMSuses these codes to validate that the template is imported to the correctG3 RMSproperty. For this reason, the file name must not be changed.
- The file must contain the correct client code and property code for the property to which it is imported.
- Match the attributes to the accepted attributes listed in the above table. That includes the upper casing and underscores.
- Match the Forecast Type to the accepted attributes listed above, including the upper casing and underscores.

### Include Only One Instance of a Market Segment

Include only one instance of a market segment and leave the RateCode column blank if the market segment is "clean."

### Add Defaults for Split Rate Codes

Add a "DEFAULT" rate code for any market segment that is not "clean" and is split by rate codes.

### Add Attributes for All Market Segments

Add attributes for all market segments and rate codes, including the Defaults.

### One Market Segment Must Be Unqualified and Equal to BAR

Assign the attribute âUNQUALIFIED_EQUAL_TO_BARâ to at least one market segment.

### Add New Market Segments

If you plan to introduce new market segments or market segment and rate code combinations, add them to the template. That ensures that the initial attribute setup covers these expected changes.

### Use Attribute Assignment Rules Instead When Appropriate

Attribute Assignment rules can save time if your rate codes follow a certain naming convention. SeeCreate Attribute Assignment Rulefor more information.

### Use Your Standard Template When Available

Hotel groups can build a standard template that covers the common market segments and rate code combinations. Later, hotels only need to assign attributes to the remaining market segments and rate code combinations that are specific to them.
