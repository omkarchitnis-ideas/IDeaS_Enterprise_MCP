# Group Status Codes

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Integrations/Group-Status-Codes.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Integrations/Group-Status-Codes.htm`
- **Ingestion Date:** `2026-09-11 22:12:38`

---

# Group Status Codes

Group Status Codes, like definite or prospect, tellG3 RMSif it should deduct a group's blocked rooms from the available capacity. For example, a 100-room hotel has a group block with 30 rooms. If the group block is definite andG3 RMSdeducts the block, it considers 70 rooms as theavailable capacity to sellPhysical Capacity plus Overbooking minus On Books and minus Out of Order. This value is the number of rooms that the RMS can sell before the property or room type is sold out.. If group is prospect (like a tentative inquiry for prices) and the system doesn't deduct, available capacity to sell is 100 rooms. Because the status codes impact capacity and therefore forecasts, decisions, and group evaluations,G3 RMSneeds to understand what each code means.
G3 RMSreceives Group Status Codes from yourReservation SystemThe primary reservation system, like a PMS or CRS, that provides data to the RMS%]. The data from that one system is used by the RMS to forecast, optimize and produce controls. The controls are sent to all selling systems, which for some integrations may exclude the reservation system., but it can't know what they mean. For example, because you shortened Definite toDEFin your reservation system. Therefore, you use the Group Status Codes page to tell the system which codes areAdjust(deduct from capacity) and which areNon-Adjust(don't deduct from capacity). Usually IDeaS maps the codes for you using the information from theIntegration Questionnaire. In that case the page is for your information and for when there are new status codes.

### New Group Status Codes

If you know about a new Group Status Code, you can add it and map it on the Group Status Codes page beforeG3 RMSfinds it in the reservation data. Otherwise, you get anUnmapped Group Status Code Alert. Click the link in the Alert to go to the Group Status Codes page to complete the mapping.

## Setup  Steps

After you save the Group Status Code mapping, only IDeaS can change it and a correction might be a chargeable service. Therefore ensure that the mapping is correct. If you  need to change the mapping after your initial setup, contactIDeaS Support.

### Mapping Group Status Codes

- Click, thenExternal Data, and thenGroup Status Codes.Unmapped Group Status Codes display in the left pane. Mapped codes display on the right.
- If you need to enter a Group Status Code that the system has not yet identified:Click the add icon.Enter theGroup Status Codename in the first column. The name must exactly match the name in the reservation system.
- Click the add icon.
- Enter theGroup Status Codename in the first column. The name must exactly match the name in the reservation system.
- For each Group Status Code, select the appropriateGroup Status Typeto indicate the type of group business that the code represents based on its Adjust or Non Adjust status:PROSPECT-Non Adjust: The group business with this status is prospective.G3 RMSshould not deduct its rooms from inventory and should not consider it in its optimization.TENTATIVE-Non Adjust: The group business with this status is tentative.G3 RMSshould not deduct its rooms from inventory and should not consider it in its optimization. However, ifG3 RMSreceives TENTATIVE-Non Adjust data from your reservations system, it better  understands the conversion to Definite and how to distribute the forecasted group demand to specific dates. Seegroup forecastsfor details.DEFINITE-Adjust: The group business with this status is definite.G3 RMSshould deduct its rooms from inventory and use the blocked rooms in its optimization. You should also use this type for tentative status codes that deduct from inventory.CANCELLED-Adjust: The group business with this status has canceled. In its optimization,G3 RMSmust consider that the group block is no longer on books.LOST/REGRET: The group business with this status has declined or has been lost to a competitor. In its optimization,G3 RMSmust consider that the group block is no longer on books.
- PROSPECT-Non Adjust: The group business with this status is prospective.G3 RMSshould not deduct its rooms from inventory and should not consider it in its optimization.
- TENTATIVE-Non Adjust: The group business with this status is tentative.G3 RMSshould not deduct its rooms from inventory and should not consider it in its optimization. However, ifG3 RMSreceives TENTATIVE-Non Adjust data from your reservations system, it better  understands the conversion to Definite and how to distribute the forecasted group demand to specific dates. Seegroup forecastsfor details.
- DEFINITE-Adjust: The group business with this status is definite.G3 RMSshould deduct its rooms from inventory and use the blocked rooms in its optimization. You should also use this type for tentative status codes that deduct from inventory.
- CANCELLED-Adjust: The group business with this status has canceled. In its optimization,G3 RMSmust consider that the group block is no longer on books.
- LOST/REGRET: The group business with this status has declined or has been lost to a competitor. In its optimization,G3 RMSmust consider that the group block is no longer on books.
- Verify your mapping. The mapping is permanent. Be sure to verify your selections before saving. You must map all unmapped Group Status Codes before you can save your work.
- ClickSave.
