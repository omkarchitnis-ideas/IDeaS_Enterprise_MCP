# Last Room Availability (LRA) Restrictions

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Restrictions/LRA-Restrictions.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Restrictions/LRA-Restrictions.htm`
- **Ingestion Date:** `2026-09-11 22:12:53`

---

# Last Room Availability (LRA) Restrictions

In corporate rate agreements, hotels negotiate not only price and room type, but also LRA status. LRA status is a valuable benefit for corporate business. It is designed to ensure better availability of the negotiated rate, meaning the hotel must accept the rate even over high-demand periods.
ForG3 RMS, LRA means that the negotiated rate remains available to book as long as the negotiated room type is available, even if the Last Room Value (LRV) is higher than the negotiated rate for that account. 
Only after the LRV is above theBARBest Available Rate. The lowest non-restricted product with flexible cancellation policy that anyone can book. The RMS optimizes the pricing of the BAR product. Other products, like Advanced Purchase or packages, can be linked to the BAR price.price point and all rates for the room type are closed can the negotiated rate be closed. Thus, the only way to close the LRA account is to close BAR (or your name for theprimary priced productMain pricing decision that the RMS optimizes. Usually this is the lowest non-restricted product with flexible cancellation policy that anyone can book. The default name is Best Available Rate (BAR), but you can change it in Pricing Configuration.) as well. ViewBest Practices for LRVto learn how to set up yourselling systemto ensure the LRV correctly restricts LRA business.
G3 RMSconsiders all market segments with the attributeSemi-Yieldableas LRA business.

### LRA Impact

During its optimization,G3 RMSautomatically checks for dates when lower-value LRA demand might displace higher-value BAR demand.G3 RMSlooks at remaining LRA versus BAR demand and overall capacity. The system can also check if the LRA demand books earlier than BAR demand. Based on that information, the system forecasts dates with LRA impact.
For example, you have 10 available rooms to sell.G3 RMSforecasts 10 rooms demand for LRA and 10 rooms for BAR. Based on historical booking pace, if the system expects the LRA demand to book before BAR, then there is LRA impact, because LRA demand will displace BAR demand.
On dates where you applied a specific pricing override,G3 RMSdoes not check for LRA impact.
WhenG3 RMSdetects LRA impact, the system displays a âPrice Impactedâ warning iconinPricingand theBusiness Analysis Dashboard, for impacted dates. This icon informs you that you may miss revenue opportunities.

### Options forManaging Dates with LRA Impact

You have two different options for managing LRA impacted dates:

#### 1. Review and Apply Restrictions

By default,G3 RMSdoes not intervene when it displays LRA impact icons. You might accept that you are potentially missing out on higher revenues on individual dates because you value the overall business that the LRA accounts bring throughout the year. In that case, you don't need to take action. The icons only inform you how often LRA impact happens and, in general, help you gain a better understanding about the costs versus the benefits of your LRA accounts.
If you want to limit the potential displacement of higher-rated business by LRA demand, you can manually apply restrictions to the room type in yourselling systemuntilG3 RMSremoves the LRA impact icon.
WhenG3 RMSexpects that the remaining LRA demand is no longer large enough to displace higher-value business, the system removes the icon.

#### 2. Set upG3 RMSto Send Restrictions

If you wantG3 RMSto take an active role in preventing LRA business from displacing higher-value business, you can enable LRA restrictions.With LRA restrictions,G3 RMSautomatically sends controls to yourdesignated reservation system (typically the CRS or PMS)that restrict BAR at the level that you select, when the system detects LRA impact. Yourreservation systemthen applies identical controls.
To use LRA restrictions, yourreservation systemmust support the functionality and your IDeaS representative must enable the feature. You can then use Last Room Availability Restrictions Setup to tellG3 RMSthe level, either rate category or rate code, at which yourreservation systemcan accept LRA restrictions.
WhenG3 RMSdetects LRA impact, it does the following:
- Sends controls to thereservation systemthat restrict BAR.
- Applies identical controls to the LRA managed rate codes that you identify in LRA Restrictions Setup
- Displays the Price Restricted iconinPricingand theBusiness Analysis Dashboard, and it does not display a pricing decision.
 On dates whereG3 RMSdisplays the Price Restricted icon, you cannot apply pricing overrides for that arrival date, Room Class, and LOS combination. BAR and LRA business cannot book for the impacted Room Class and, if applicable, LOS.
- Removes the controls later in the booking cycle, when there is less danger of BAR being displaced by LRA demand. The property can then capture more revenue from the remaining, higher-value BAR demand, while remaining LRA demand should be lower.

## Setup Steps

- Set up yourreservation systemto yield other rate codes, in this case, the LRA rate codes, together with BAR. This setup means that LRA rate codes are not controlled by the LRV but receive the same controls as BAR.
- Set up all public rate codes to yield with other rate codes, not just BAR and LRA. For example, for an arrival date with LRA impact, the LRV for a given Room Class and LOS is $100, your LRA rate is $110, and the optimal BAR price point is $150.G3 RMSsends a control to restrict the BAR price point, and LRA is closed because you set up thereservation systemto yield LRA equally to BAR. If you have other public rates (for example, an advanced purchase option at $135 that is not yielded the same as BAR), they remain open, and you may violate your LRA agreement. Therefore, it is important that you yield other public rates the same as BAR. Alternatively, you can fence them, so they are no longer public and do not display in a public rate search (for example, with an access code).
- Create a case forIDeaS supportor contact your IDeaS representative to enable LRA restrictions.
- After IDeaS enables LRA restrictions, set up the level and rate codes for restrictions. Clickand
	thenLast Room Availability Restrictions.
- Select the level at which yourreservation systemcan accept LRA restrictions. SeeRate Code and Rate Category Restriction Levelsbelow for information about levels for restrictions.
- If you applied restrictions at the rate code level, you must first add the rate codes that require restrictions in the Rate Headers tab ofRestriction Setup. Here you define rate plans at a high level, with a name, description, the full date range for which the plan is available, and the type, either a fixed value or a value derived off the BAR decision. You may already have completed Restriction Setup because some of your selling systems cannot use LRV to control rates. If all your selling systems accept LRV, and you have not completed Restriction Setup, you do not need to complete the second tab, Rate Details to set up LRA restrictions.
- Select the Available Rate Categories or Available Rate Codes, depending on your level.Filter the list by typing a string of characters from the name in theSearchfield.Click>to add selected categories or codes to the LRA Restricted list, or click>>to add all categories or codes to the LRA Restricted list.
- Filter the list by typing a string of characters from the name in theSearchfield.
- Click>to add selected categories or codes to the LRA Restricted list, or click>>to add all categories or codes to the LRA Restricted list.
- ClickSave.
WhenG3 RMSsends LRA restrictions, the system displays the âPrice Restrictedâ iconinPricingand theBusiness Analysis Dashboard.

## Best Practices

### Review Your Pricing Overrides

On dates where you applied a specific pricing override,G3 RMSdoes not check for LRA impact.

### Choose an Optimization Method

When you use LRA restrictions, you can also choose an alternate optimization method that may provide better results than the default method. SeeOptimization Controlsfor more information.

### Choose Rate Category or Rate Code Level Restrictions

In LRA Restrictions Setup, you choose to apply LRA restrictions at either the rate category or rate code level. Apply restrictions at the rate category level if your selling systems can receive restrictions at that level and if restrictions are delivered to all sales channels. For example, if all public rates exist in a rate category âPUBLIC,â and LRV results in a MinLOS = 2 restriction to this rate category in the selling system, the restriction must apply to all onward sales channels, like Online Travel Agencies,  where these rates are sold.
In many cases, restrictions have to be applied at the rate code level for the restrictions to reach all sales channels. For example, BAR and ADVP are the only two public rate codes that you sell on channels that are subject to LRV or hurdles. These public rate codes must be restricted when the LRA flag is active. Applying restrictions at the rate category level does not ensure that restrictions cascade to these rate codes individually and out to the channels. In cases like this, rate code level restrictions are required.
To apply restrictions at the rate code level, you must first add the rate codes that require restrictions in the Rate Headers tab ofRestriction Setup.
