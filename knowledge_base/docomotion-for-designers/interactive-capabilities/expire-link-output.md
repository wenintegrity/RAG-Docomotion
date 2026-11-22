---
title: "Expiration Link Output"
source: https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/expire-link-output/
section: docomotion-for-designers
last_modified: 2025-03-06T12:41:11
---

# Expiration Link Output

### **The Link output**

The Link output channel is used to send a recipient an email with a link to a Form. When the recipient clicks on the link, the document is generated in Salesforce and the Form opens in  the recipient’s browser. The link has an expiration date. If the recipient clicks on the link after the expiration date an error message appears.

This is useful, for example, if you want to send a customer an interactive HTML document that he/she can fill, sign, attach documents and submit back to Salesforce.

### Configuring Signature Record

1. In order to link automatically the Signature record as a child of the Output Generation Main Object you need to add a lookup from the Signature Object to the Main Object.
2. Edit the Main Object layout and add to the Related Lists the Signatures list.

*Note*that in Salesforce Lightning, adding any Related List to the page layout does not automatically display it on the Lightning page. Verify that you have added the Related Tab to your Lightning page layout, and add the Related Lists component to this Related Tab. Only after this, are all related lists you added to the page layout for the record in the Object manager automatically displayed.

- Next Step: A Generator User Guide. Refer to  ['Link Output Channel Flow'](https://www.docomotion.com/support/docomotion-for-generators/generate-a-link-output-channel-flow/)
