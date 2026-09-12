# Vendor Integration Mapping

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Integrations/Vendor-Integration-Mapping.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Integrations/Vendor-Integration-Mapping.htm`
- **Ingestion Date:** `2026-09-11 22:12:46`

---

# Vendor Integration Mapping

Use the Vendor Integration Mapping page to enableG3 RMSto send decisions to yourSelling SystemAny distribution system, like a PMS, CRS or a Channel Manager, that is used to sell your transient guest room inventory. Ideally, the RMS sends all controls to your selling systems, but this might vary based on their capabilities. For some integrations, the selling systems might not include the reservation system that provides the RMS with data.when some room types or rate codes don't match between the systems. In that case, use this page to tellG3 RMSwhich code in theselling systemmatches the one inG3 RMS.
Note: Mostclientscan skip this setup. Because, when Room Types don't match, you can usuallycomplete this mapping in the selling systemwhich resolves the issue. You, or someone at your property, should know if that's the case. If you are in doubt, check with the support contacts of yourselling system.

## Setup  Steps

### Map Room Types

- Click, thenDecisions, and thenVendor Integration Mapping.
- Select theVendorfor which you want to complete Room Type Mapping.
- ClickAdd Room Type Mapping.
- Select a room type code from theRoom Typemenu.
- Enter the room type for the selected vendor in theVendor Room Typefield.
- Repeat the steps above until all Room Types are mapped for that vendor.
- ClickSave.
- If you have multiple selling systems, continue selecting vendors and mapping room types until you have accounted for all your selling systems.

### Map Rate Codes

- Click, thenDecisions, and thenVendor Integration Mapping.
- Select theVendorfor which you want to complete either Rate Code Mapping.
- ClickAdd Rate Code Mapping.
- Select a rate code from theRate Codemenu.
- Enter the rate code for the selected vendor in theVendor Rate Codefield.
- Repeat these steps until all Rate Codes are mapped.
- ClickSave.
- If you have multiple selling systems, continue selecting vendors and mapping rate codes until you have accounted for all your selling systems.

## Scenarios for Using Mapping

### Room Type Mapping

Use Room Type Mapping ifG3 RMSis sending room type level decisions for your property, and any of these scenarios apply:
- The number of room types inG3 RMSdoes not match the number in theselling system. For example, you have seven room types inG3 RMSbut less than or more than seven in theselling system.
- The room type codes used byG3 RMSdo not match those in theselling system. For example, your PMS has a âDBLâ room type.G3 RMSuses the same name, because itâs getting data from your PMS. But in yourselling systemitâs called â1Dâ.

### Rate Code Mapping

Use Rate Code Mapping ifG3 RMSis sending BAR by Day rate code level restrictions for your property, or ifG3 RMSis sending BAR by LOS decisions, and any of these scenarios apply:
- The rate codes from the PMS do not match the codes for the same rate plan in one or more of your selling systems. For example, the rate code "BCOMBAR" in the PMS is coded "BDCBAR" in your CRS.
- All the rate codes do not exist in theselling system. For example, the PMS has ten rate codes, but only five of those codes exist in the CRS.

### Vendor Integration Mapping for Your PMS/CRS

One of your reservations systems, PMS orCRS, provides the data toG3 RMS, including the room type and rate codes. Therefore, in most cases, when sending decisions back tothat  system, you don't need to complete Vendor Integration Mapping.
However, if your property uses the Daily Continuousor BAR by Day pricing methodand it's Opera-based (OPMS, ORS or MyFidelio), there are a few scenarios when you need to complete the mapping:
- Your property has set up a second rate code (other than the Opera daily BAR rate code) and both rate codes need to receive Daily BAR Decisions. This should be a rare scenario, since the rates can be derived (i.e. the Daily BAR Rate code -0).
Your property has set up a second rate code (other than the Opera daily BAR rate code) and both rate codes need to receive Daily BAR Decisions. This should be a rare scenario, since the rates can be derived (i.e. the Daily BAR Rate code -0).
- The Daily BAR rate codes between any of the following systems donât match: ORS,  OPMS, MyFidelio.
The Daily BAR rate codes between any of the following systems donât match: ORS,  OPMS, MyFidelio.
- A second rate code needs to receive decisions from a different room type. For example, for a rate code that requires a mandatory upgrade and a price for a higher value room type must be sold at the price of the next lowest priced room type, like AmEx Centurion.
A second rate code needs to receive decisions from a different room type. For example, for a rate code that requires a mandatory upgrade and a price for a higher value room type must be sold at the price of the next lowest priced room type, like AmEx Centurion.

### Mapping the Codes in the Selling System

Many selling systems allow you to map to the codes from thereservation systemthat providedG3 RMSwith the room type and rate codes. In these cases, room type or rate code mapping is not required. If you are in doubt, check with the support contacts for yourselling system.
In this example, the PMS is the reservation system and the CRS is a selling system that allows the below mapping:

### Mapping Examples

In this example, the number of rate codes is the same in the PMS (the reservation system)  and CRS. Mapping is required because the codes are different, and the selling system uses the CRS, not the PMS rate codes for integration. In Vendor Integration Mapping, select the PMS rate code, then enter the equivalent CRS Rate Code.
In the example above, ifG3 RMSwas required to send MinLOS restrictions to BDCBAR, the BCOMBAR rate from the PMS would be mapped to the BDCBAR rate code used in the CRS.
In the next example, some rate codes match exactly, but not all exist in the CRS. The PMS and CRS receive rate code MinLOS restrictions fromG3 RMS. There are five rate codes to receive restrictions in the PMS, but only three of these exist in the CRS.
In this case, set up the mapping for only those that exist in the CRS, and restrictions will be generated against these.
In Vendor Integration Mapping, select the PMS rate code, then enter the equivalent CRS Rate Code. You can apply this mapping either with or without room type mapping.
You might need to map a one-to-one relationship between room types or rate codes betweenG3 RMSand selling systems. However, you can also set up a singleG3 RMSroom type or rate code to map to several rate codes or room types in your selling systems (for example, if multiple room types should receive the same decisions). For example, Room Type A inG3 RMScan be mapped to Room Type B and Room Type C in a selling system:
- Room Type A = Room Type B
- Room Type A = Room Type C
You cannot send decisions from multiple room types or rate codes inG3 RMSto a single selling system room type or rate code. For example, Room Type A and Room Type B inG3 RMScannot both be mapped to Room Type C in selling systems:
- Room Type A â  Room Type C
- Room Type B â  Room Type C
