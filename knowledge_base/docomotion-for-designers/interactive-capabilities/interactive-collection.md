---
title: "Interactive Collection"
source: https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/interactive-collection/
section: docomotion-for-designers
last_modified: 2024-01-12T07:00:11
---

# Interactive Collection

### **Creating an Interactive Collection in Salesforce**

1. In Salesforce, open the Docomotion App.
2. Click the **Interactive Collection**tab.
3. In the Interactive Collection page, click New, enter a name, and click **Save**.
4. Create the Interactive Collection with elements like radio button selection, text box, upload, and signature.
5. For a comprehensive understanding of the available elements, refer to the ‘[Interactive Collections Elements](https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/interactive-collection-input-elements/)‘ section for detailed information on each element.

### **Adding an Interactive Collection to a Form**

1. In Salesforce, Docomotion click the Forms.
2. Select the required Form to which you want to add the Collection.
3. At the ‘Interactive Related Forms’ area click ‘New Interactive Related Form’.
4. Click the Lookup icon to display the Lookup window, and select the Collection you want to add.
5. Click Save.

### **Interactive Collection When Generating Output**

1. When Generating an output a field ‘doco.Signer\_[object] is created under the object.
2. A **Signature** record is created and an email is sent to the recipient with a link.

### **Interactive Collection When the recipient submits the form.**

1. The Signature record in Salesforce is updated and a sealed PDF is created and sent back to the recipient.
2. Signature record will then include the following:

   Meta data

   - Time stamp
   - IP address
   - Browser information (Client URL Link, Friendly Client URL, Friendly Client URL Link field)

   Attachments (depends on the elements the collection includes):

   - Locked PDF (with signature)
   - Attached files
