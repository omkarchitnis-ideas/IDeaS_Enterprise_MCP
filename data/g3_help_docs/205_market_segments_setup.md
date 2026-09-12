# Market Segments Setup

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Market-Segments/Market-Segments-Simple-Configuration.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Market-Segments/Market-Segments-Simple-Configuration.htm`
- **Ingestion Date:** `2026-09-11 22:14:26`

---

# Market Segments Setup

Use this Market Segments topic if your setup page looks like in following picture:
This can be because yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.doesn't support splitting market segments, because your property usesSynthetic Data, or due to your subscription. If your screen looks different and is split into two sections, this text doesnât apply to you. View theMarket Segments setupinstead.

### What Help Do You Need with Setting Up Market Segments?

- I want an overview of the topic.
- For the initial implementation, I need to assign attributes to market segments.
- I assigned attributes to all market segments and need tocreate and commit Forecast Groups.
- I need to understand theG3 RMSattributes.

### Why You Need to Set up Market Segments

To achieve the best possible forecasts and decisions,G3 RMSforecasts different types of business differently. The market segments thatG3 RMSimports from yourreservation systemrepresent different types of business. Why not use them to forecast?
Market segments are not ideal for forecasting purposes because they often have low volumes of booking data. Low data volumes lead to higher uncertainty in forecasts. Therefore,G3 RMScombines market segments with similar characteristics and patterns into Forecast Groups:
- G3 RMSdetects  market segments with similar patterns.
G3 RMSdetects  market segments with similar patterns.
- You define their characteristics by assigning attributes that describe their behavior. For example, whether they are fixed-priced or derived offthe primary priced product.
You define their characteristics by assigning attributes that describe their behavior. For example, whether they are fixed-priced or derived offthe primary priced product.
Together, you andG3 RMSconvert the original market segments into Forecast Groups. The goal is to provideG3 RMSwith Forecast Groups that contain robust amounts of booking data.

## Setup Steps

Market Segment setup is a four-step process:

### 1. Plan for Setup

- Know what type of business your market segments contain. The data inG3 RMScomes from yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system.. It usually covers the past one or two years.If needed, educate yourself about your market segments. You might find information in corporate documentation or in yourreservation system
- Become familiar withMarket Segment Attributesto understand howG3 RMScategorizes business.
- Review your market segments one by one inG3 RMSand consider the appropriate attributes.

### 2. Assign Attributes to Market Segments

The code and name of your market segments are listed as imported from yourreservation system. You need to assign the appropriate Attributes and Forecast Type to describe the behavior of market segments.
- Click, thenForecasts, and thenMarket Segments.
- If you are accessing this page for the first time, you are asked to initialize the market segments list. ClickInitializeto continue. If you are returning to the page after initialization, click the refresh icon. That ensures that all unassigned market segments display in the left pane.
- Click the Edit   iconnext to a market segment to open theEdit MSwindow.
- If you want to change theMarket Segment Name, click the Edit icon. This is optional, the name does not display outside of the Market Segment setup page.
- Select the appropriateAttributesandForecast Type. Based on common sense rules,G3 RMSlimits the attribute options and only shows valid combinations. For example,G3 RMSconsiders all Qualified business as Fenced, so Fenced is not an option for Qualified business. Likewise,G3 RMSforecasts demand and wash for all Unqualified business. Therefore, its Forecast Type of "Demand and Wash" cannot be changed. Point to each Attribute to view its definition or refer toMarket Segment Attributes.
- ClickAssign.
- Finish assigning attributes for all market segments.
- If you have market segments with  fixed price rate codes that change to a discount off BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) when the BAR price is below the fixed price,  first ensure that the market segment is either Unqualified or Linked to BAR. Then, define the exact pricing of the rate codes in theRate Protecttab. Note that Rate Protect is not available if your property uses Synthetic Data.
- Review and fix mistakes, if necessary.
The Equal to BAR attribute directly impacts the pricing decisions. Only use it for business that is booked at the value ofthe selected Base Product, by default,BAR. Don't use it for discounted business, such as advance purchase rates.

#### What if I Have Duplicate Market Segments?

What if you made changes to your market segments, andG3 RMSlists both the old and the new market segment? If you renamed a market segment and it remained the same otherwise, make sure both have the same attributes and end up in the same Forecast Group. What if you changed your market segment structure, for example, splitting one old market segment into two new ones? In that case, the attributes likely differ between the old and new ones.

### 3. Complete Other Required Setup Work

After assigning attributes, finish the steps below before continuing with the next step in theForecast Groupstab.
- Set up Room Classes
- Set up Pricing
- Set up Rate Shopping

### 4. Create and Commit Forecast Groups

Once your IDeaS representative lets you know  that you can proceed,use theForecast Groupstab to create and commit Forecast Groups.G3 RMSdetermines which market segments to combine based on both attributes and booking patterns. After you commit the Forecast Groups, the system is inDecision CreationA one-way status when the RMS receives data from the reservation system, creates forecasts and outputs (like pricing), but does not send outputs to the selling system.system modeand produces the first forecasts and decisions.
