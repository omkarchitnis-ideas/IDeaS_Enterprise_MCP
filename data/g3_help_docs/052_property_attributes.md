# Property Attributes

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Property/Property-Attributes.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Property/Property-Attributes.htm`
- **Ingestion Date:** `2026-09-11 22:12:42`

---

# Property Attributes

Enterprise clients use Property Attributes to help define theirProperty Groupsand, for Permissions, Authorization Groups, which are combinations of multiple properties. The attributes help them characterize their properties, for example, by country, region, or type of hotel.
The steps to use this functionality are:
- Create  attributes and, if applicable, add specific values. For example, for a "Type of Hotel" attribute the values might be City, Rural, 
 Suburb, Airport and Resort.
- Define the attributes for each property inProperty Attribute Assignments.
- Use the attributes to combine properties  intoProperty Groups. They allow you to review combined property data inInformation Managerand on dashboards.
- Use attributes to create Authorization Groups (under Configure Permissions) in which users are assigned to groups of properties.
Before you create Property Attributes, consider which attributes best meet your needs to manage user access and view data.

## Setup Steps

### Adding Property Attributes

- Click, thenProperty, and thenProperty Attributes.
- Enter theNameof the attribute.
- Select theTypeof attribute:Character: Character attributes allow you to create a predefined list of text values or allow users to type values in a text entry field. For example, "Country" would be defined as a Character attribute.Boolean: Boolean attributes allow you to select a value of eitherNo(false) orYes(true). For example, "On-site Restaurant" could be defined as a Boolean attribute with a value of Yes (the Hotel has an on-site restaurant).Numeric: Numeric attributes allow you to create a predefined list of numeric values or allow users to type a numeric value in a text entry field. For example, "Number of Rooms" would be defined as a Numeric attribute.
- Character: Character attributes allow you to create a predefined list of text values or allow users to type values in a text entry field. For example, "Country" would be defined as a Character attribute.
- Boolean: Boolean attributes allow you to select a value of eitherNo(false) orYes(true). For example, "On-site Restaurant" could be defined as a Boolean attribute with a value of Yes (the Hotel has an on-site restaurant).
- Numeric: Numeric attributes allow you to create a predefined list of numeric values or allow users to type a numeric value in a text entry field. For example, "Number of Rooms" would be defined as a Numeric attribute.
- For Character or Numeric attributes:SelectPredefinedto create a specific list of values from which users can choose.Click the add icon.Enter anAttribute Value.SelectSet Defaultfor the Attribute Value that will display as the default value inProperty Attribute Assignments.Continue adding values until the Attribute Values pane displays all required values.SelectUser Definedto allow users to type values in a text entry field.Enter aMax Character Lengthto limit the number of characters or numbers allowed in the text entry field. The maximum value you can set is 16 characters.Enter aDefault Valuefor the Attribute Value that will display as the default value inProperty Attribute Assignments.
- SelectPredefinedto create a specific list of values from which users can choose.Click the add icon.Enter anAttribute Value.SelectSet Defaultfor the Attribute Value that will display as the default value inProperty Attribute Assignments.Continue adding values until the Attribute Values pane displays all required values.
- Click the add icon.
- Enter anAttribute Value.
- SelectSet Defaultfor the Attribute Value that will display as the default value inProperty Attribute Assignments.
- Continue adding values until the Attribute Values pane displays all required values.
- SelectUser Definedto allow users to type values in a text entry field.Enter aMax Character Lengthto limit the number of characters or numbers allowed in the text entry field. The maximum value you can set is 16 characters.Enter aDefault Valuefor the Attribute Value that will display as the default value inProperty Attribute Assignments.
- Enter aMax Character Lengthto limit the number of characters or numbers allowed in the text entry field. The maximum value you can set is 16 characters.
- Enter aDefault Valuefor the Attribute Value that will display as the default value inProperty Attribute Assignments.
- For Boolean attributes, select aView Byvalue of eitherNo(false) orYes(true).
- ClickSave.

### Editing Property Attributes

You can edit the name, predefined values, and default value for Property Attributes. The type of Property Attribute cannot be changed.
- Click, thenProperty, and thenProperty Attributes.
- Click the attribute to be edited in the list of attributes in the left pane.
- Edit theName, if needed.
- For Character or Numeric attributes, change any of the following, as needed:Click the add iconto add a new Attribute Value.Edit existing attribute titles in theAttribute Valuefield.To remove an Attribute Value, click the delete icon.Edit theMax Character Lengthfor User Defined values.Edit theDefault Valueor select a newSet Defaultbutton.
- Click the add iconto add a new Attribute Value.
- Edit existing attribute titles in theAttribute Valuefield.
- To remove an Attribute Value, click the delete icon.
- Edit theMax Character Lengthfor User Defined values.
- Edit theDefault Valueor select a newSet Defaultbutton.
- For Boolean attributes, change the value of eitherNo(false) orYes(true).
- ClickSave.

### Deleting Property Attributes

You can delete a Property Attribute provided it meets the following criteria:
- The attribute is not associated with a property. SeeProperty Attribute Assignmentsfor removing Property Attribute associations.
- The attribute is not used as a filter in any rule-basedProperty Groupthat is owned byActiveusers.
- The attribute can be deleted if it is a filter in a rule-based Property Group that is owned byInactiveusers. In this case, the Property Group will also be deleted when the attribute is deleted.
- The attribute is not used as a filter in any Authorization Group.
- Click, thenProperty, and thenProperty Attributes.
- Locate the attribute to be deleted in the list of attributes in the left pane.
- Click the delete icon.
