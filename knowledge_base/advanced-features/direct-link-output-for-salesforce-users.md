---
title: "Direct Link Output for Salesforce Users"
source: https://www.docomotion.com/support/advanced-features/direct-link-output-for-salesforce-users/
section: advanced-features
last_modified: 2024-01-10T09:15:05
---

# Direct Link Output for Salesforce Users

### **Direct Link Output for Salesforce Users:**

The new API feature provides the ability to generate Link output directly for Salesforce Users without creating Contact/Account records. This can be a good alternative to the previous method that required the creation of Contact/Account records for all users that need to sign documents.

**Parameters:**

- **formId (Integer):** The form number to generate.
- **formName (String):** The name of the Form.
- **sobjectId (Id):** ID of the record to generate on.
- **isActiveVersion (Boolean):** If the form is on an active state set true; if publish set false.
- **fileName (String):** The name of the output.
- **whoId (Id):** The ID of the signer field.
- **addRecipient (String):** Additional email recipient.
- **orgWideAddressId (String):** ID of the org-wide email address.
- **chatter (Boolean):** Whether to create a chatter entry for the signature or not.
- **toInsert (Boolean):** Whether to insert the data into the database or not.
- **whoIdsMap (Map<Integer, Id>):** A map that maps formId (Integer) to whoId (Salesforce Id).

**Example:**

```

					Integer formId = 2; // form number to generate
String formName = 'AccountTest123'; // The name of the Form
Id sobjectId = '0017R00002yeduZQAQ'; // ID of the record to generate on
Boolean isActiveVersion = false; // if the form is on an active state set true if publish set false
String fileName = 'test'; // the name of the output
Id whoId = '0057R00000DWB0ZQAX'; // the ID of the signer field (User)
String addRecipient = 'ruslanm@docomotion.com'; // Additional email recipient
String orgWideAddressId = '0D27R000000XbbK'; // ID of the org-wide email address
Boolean chatter = false; // Whether to create a chatter entry for the signature or not.
Boolean toInsert = true; // Whether to insert the data into the database or not.
Map&lt;Integer, Id&gt; whoIdsMap = new Map&lt;Integer, Id&gt;();
whoIdsMap.put(2, '0057R00000DWB0ZQAX');
whoIdsMap.put(2, '0057R00000DWB0ZQAX');
doco.RenderAPI.createLink(formId, sobjectId, whoId, chatter, toInsert, fileName, isActiveVersion, addRecipient, orgWideAddressId);
doco.RenderAPI.createLink(formName, sobjectId, whoId, chatter, toInsert, fileName, isActiveVersion, addRecipient, orgWideAddressId);

```
