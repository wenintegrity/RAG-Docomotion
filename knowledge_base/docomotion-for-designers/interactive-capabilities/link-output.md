---
title: "Link Output"
source: https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/link-output/
section: docomotion-for-designers
last_modified: 2025-03-06T12:46:06
---

# Link Output

### **The Link output**

The Link output channel is used to send a recipient an email with a link to a Form. When the recipient clicks on the link, the document is generated in Salesforce and the Form opens in  the recipient’s browser. The link has an expiration date. If the recipient clicks on the link after the expiration date an error message appears.

This is useful, for example, if you want to send a customer an interactive HTML document that he/she can fill, sign, attach documents and submit back to Salesforce.

### Configuring Signature Record

1. In order to link automatically the Signature record as a child of the Output Generation Main Object you need to add a lookup from the Signature Object to the Main Object.
2. Edit the Main Object layout and add to the Related Lists the Signatures list.

*Note*that in Salesforce Lightning, adding any Related List to the page layout does not automatically display it on the Lightning page. Verify that you have added the Related Tab to your Lightning page layout, and add the Related Lists component to this Related Tab. Only after this, are all related lists you added to the page layout for the record in the Object manager automatically displayed.

### **Default Expiration Period**

By default, generated links expire after **1 week (168 hours)**. However, this setting can be modified in the [**Docomotion system settings**](https://www.docomotion.com/support/docomotion-for-administrators/configuring-docomotion/), allowing organizations to set a different default expiration period. The maximum allowed expiration period is **9,999 hours**.

**Template-Specific Expiration**

In addition to the system-wide setting, the expiration period can also be configured per **template (form record)**. This enables users to define a custom expiration period for individual documents, with the same maximum limit of **9,999 hours**.

These expiration settings provide flexibility in controlling document availability while ensuring secure and time-limited access.

- Next Step: A Generator User Guide. Refer to  ['Link Output Channel Flow'](https://www.docomotion.com/support/docomotion-for-generators/generate-a-link-output-channel-flow/)
