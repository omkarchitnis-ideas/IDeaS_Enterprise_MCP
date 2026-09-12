# Restrictions

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Linked-Products/Linked-Products-Restrictions.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Linked-Products/Linked-Products-Restrictions.htm`
- **Ingestion Date:** `2026-09-11 22:14:29`

---

# Restrictions

The Restrictions tab for linked products is only active if your property usesRestriction Configuration. The tab has two purposes:
- Avoid duplication: in Restriction Configuration, you define values for rate codes so thatG3 RMScan generate restrictions for them. And in Pricing Configuration, you define the values for the rate codes of linked products, so thatG3 RMScan price them. That means that, for linked products, you might define their rate code value twice. To avoid that, use the Restrictions tab to tell the system for which rate codes it should use the configured linked product value to produce restrictions.
- Ensure correct restrictions forOptimized Products: ifG3 RMSoptimizes the value for a linked product, the price of the product can vary. For example, it can be 5 percent off theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.for today and 10 percent offthe primary priced productfor tomorrow. But Restriction Configuration allows you to set only one value, so restrictions for optimized linked products might be incorrect unless you add their rate codes to the Restrictions tab.
After you select these rate codes in the Restrictions tab for your linked products, you can define their value only in the new Product Restrictions tab in Restriction Configuration. This new tab shows all the Rate Codes you selected in the Restrictions tab for linked products.

## Setup Steps

### Defining Products

- Click, thenDecisions, and thenPricing.
- Select an action:Click the add iconto add a new product.Click the edit iconto change an existing product.
- Click the add iconto add a new product.
- Click the edit iconto change an existing product.
- ClickNextafter completing the product'sDefinition.
- ClickNextafter completing the product'sDefaults.
- ClickNextafter completingSeasons, if needed. The Restrictions tab opens and displays the rate codes that you set up in Restriction configuration.
- Select the rate codes for whichG3 RMSuses the values defined by linked product configuration when generating restrictions.Select one or more rate codes and click>to add them to the product.Click>>to add all rate codes to the product.Note: after you select a rate code, it no longer displays in Restriction configuration.
- Select one or more rate codes and click>to add them to the product.
- Click>>to add all rate codes to the product.Note: after you select a rate code, it no longer displays in Restriction configuration.
- ClickDoneto save your changes and return to theAvailable Productspage.
