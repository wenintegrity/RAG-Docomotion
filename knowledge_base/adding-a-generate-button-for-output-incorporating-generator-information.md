---
title: "Adding a Generate Button for Output Incorporating Generator Information"
source: https://www.docomotion.com/support/adding-a-generate-button-for-output-incorporating-generator-information/
section: 
last_modified: 2023-12-05T07:44:05
---

# Adding a Generate Button for Output Incorporating Generator Information

This option is only available in the web application and not in the mobile app (Salesforce1).

If you want to generate output that includes information that is updated according to the user who generates the output, you need to create a new button where the **behavior** is “Execute JavaScript” and the **Content Source** is a javascript, and add the button to the output generation page.

This enables you to add data that will be updated according to the javascript.

### **To add a button that enables including generator information:**

1. Add a new user lookup field to the main record.
2. Add the required fields, based on the added user lookup, to the Form.
3. Replace the out-of-the-box generation button with the new javascript button.

### **Example:**

The following example is based on Opportunity object. The field to be used in the Form is: **GENERATOR\_\_c**{!REQUIRESCRIPT(“https://t7c2b3h7.rocketcdn.me/soap/ajax/30.0/connection.js”)} var myObj = new sforce.SObject(‘Opportunity’); myObj.id = “{!Opportunity.Id}”; myObj.GENERATOR\_\_c = “{!User.Id}”; var results = sforce.connection.update([myObj]); location.reload = true; window.open(‘/apex/doco\_\_VF02\_GenerateDocument?id={!Opportunity.Id}’, ‘\_blank’, ‘height=750,width=1000,resizable=yes,scrollbars=yes,toolbar=no,menubar=no’);
