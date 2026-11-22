---
title: "Generate a Link Output Channel Flow"
source: https://www.docomotion.com/support/docomotion-for-generators/generate-a-link-output-channel-flow/
section: docomotion-for-generators
last_modified: 2024-01-21T06:19:53
---

# Generate a Link Output Channel Flow

### **Step 1: User Generates Output**

Inside the Generation Screen:

1. Select a recipient for the Form and the Link Output Channel.
2. Click Generate.

Note: When generating output from a Lead object, use the field doco.Signer\_Lead instead of doco.Signer.

A Signature record is created, and an email is sent to the recipient with a link. The email generation is based on a workflow rule for the creation of a Signature record, included in the Docomotion package by default (refer to [Using Email Templates](https://www.docomotion.com/support/docomotion-for-designers/email-templates/)).

### **Step 2: Recipient/Client Receives Email**

1. When the recipient clicks on the link, an HTML Form is generated based on the latest Salesforce data.
2. The form opens in the device’s default browser for the recipient to fill and add attachments if necessary.

Note: The link is based on the latest published version of the form, and it has a configurable expiration period. Refer to ‘[System Settings](https://www.docomotion.com/support/docomotion-for-administrators/configuring-docomotion/)‘ for setting the link expiration date. Users attempting to open the link after the expiration date will receive an error message.

### **Steps 3:** **Recipient** **Fills in the Document and Submits**

The interactive form can include the following capabilities:

- Signature
- Upload file

### **Step 4: Signature Record Updated**

1. When the recipient submits the form, the Signature record in Salesforce is updated.
2. A sealed PDF is created and sent back to the recipient.

The Signature record will include:

- Metadata
- Timestamp
- IP address
- Browser information (Client URL Link, Friendly Client URL, Friendly Client URL Link field)
- Attachments (optional) :
  - Locked PDF (with signature)
  - Attached files
