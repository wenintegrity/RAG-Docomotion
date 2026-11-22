---
title: "Automating using Flow Builder"
source: https://www.docomotion.com/support/advanced-features/automating-using-flow-builder/
section: advanced-features
last_modified: 2024-11-12T09:36:48
---

# Automating using Flow Builder

[Video](https://youtu.be/lhsrwvuvbrk)

The user needs to create an assignment that collects all the relevant records (separated with commas), and adds  Docomotion’s new action: ‘Invoke Mass Generation’.  (From version 18).

### Configuring Output Generation Flows Using Flow Builder

1. In the Flow Builder, create a new flow (refer to the ‘[Build a Flow](https://help.salesforce.com/s/articleView?id=sf.flow_build.htm&type=5)‘ Salesforce guide).
2. Choose the action type: Apex Action.
3. Select the Apex action based on the desired output:

   - Generate Document: Output is generated to the specified channel in the selected format.
   - Generate Link: A link to the output is sent to the Signer.
   - Mail Body: The output is generated as an email body and sent to the specified recipient.
   - Mail Attachments: The output is generated in the selected format, attached to an email of the specified template, and sent to the recipient.
4. Add a label to the action.
5. Set the required Input Values. (Note: Store Output Values is not supported).

   You can either enter values directly or search for resources.

   Note: The Input Values options will change based on the chosen Apex class. Refer to Input Values (Flow Builder)/Apex Variables (Process Builder).

| **Apex Variable** | **Description** | **Type** | **Generate**  **Document** | **Generate**  **Link** | **Email**  **Body** | **Email**  **with Attachments** |
| --- | --- | --- | --- | --- | --- | --- |
| Format PDF, HTML, DOCX | The format of the generated output | string | **√** |  |  | **√** |
| Form # | Number of the Form to generate from. Should be the same object as the **Generate on** variable. | number | **√** | **√** | **√** | **√** |
| Generate on | Salesforce ID or The reference to the object that invokes the process (or its lookups) | Salesforce ID or  Reference to record ID (\*) | **√** | **√** | **√** | **√** |
| Channel – Document, Attachment, Chatter | The output channel for the generated output: Document, Attachment, Chatter | string | **√** |  |  |  |
| Signer | To add, click **Add Row** and select the variable.   The recipient of the email | Salesforce Contact ID  or  Reference to Contact record ID |  | **√** |  |  |
| Use Active Version | Output can be generated also if the Form is in Active (not Published) state | boolean |  |  | **√** | **√** |
| Email Recipient ID | To add, click **Add Row** and select the variable.   ID of the person to receive the output as an email | Salesforce Contact ID  or  Reference to Contact record ID |  |  | **√** | **√** |
| Email Additional Recipient | To add, click **Add Row** and select the variable.   Additional email to receive output | String with valid email   or  Reference to email field |  | **√** | **√** | **√** |
| Insert Template ID | ID of the Salesforce email template to which the output is added as an attachment. | Salesforce Email Template ID |  |  |  | **√** |
| File name/Subject | (optional) To add, click **Add Row** and select the variable. | string | **√** | **√** | **√** | **√** |
