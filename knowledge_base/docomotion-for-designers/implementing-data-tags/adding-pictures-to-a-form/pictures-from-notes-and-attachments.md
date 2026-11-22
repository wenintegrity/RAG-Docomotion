---
title: "Adding Pictures from Notes & Attachments or Salesforce Files"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-pictures-to-a-form/pictures-from-notes-and-attachments/
section: docomotion-for-designers
last_modified: 2024-01-12T07:20:17
---

# Adding Pictures from Notes & Attachments or Salesforce Files

### Integrating Pictures from Salesforce Attachments and Files

In Salesforce, you can enrich your forms by seamlessly incorporating images from both Attachments and Salesforce Files. The process involves updating the Data Model, editing the form in the Designer, and ultimately activating and publishing the form.

### Adding Pictures from Attachments

**Step 1: Updating the Data Model**

1. Add the Attachment>Attachment ID field to the Data Model for the Form:
   - From any object, click on “Children Relations,” drill down into Attachments, and select “Attachment ID.”
   - Click “Save.” For detailed instructions on editing a Data Model, refer to ‘[Creating a Data Model’.](https://www.docomotion.com/support/docomotion-for-designers/data-model/create-a-data-model/)

**Step 2: Editing the Form**

1. Note that the Data Model pane now includes the Attachment ID tag you added, along with the Attachment.content tag.
2. In the Word workspace, create a table for inserting pictures, optionally including additional columns like Full Name or Customer Number.
3. Place the cursor inside the cell and double-click the Attachments.content tag. The tag is inserted into the table cell.
   - If the table has only one cell, you can define it as a vertical table. Refer to “Working with Tables.”
4. Upon finishing the form design, click the Upload to Cloud icon.

**Step 3: Activating and Publishing the Form**

1. To generate output from the designed form, activate it (refer to “Activating a Form”) and then publish it (see “Publishing the Form”).

### Adding Pictures from Salesforce Files

**Step 1: Updating the Data Model**

1. Add the ContentDocumentLinks>ContentDocumentLink ID field to the Data Model for the Form:
   - From any object, click on “Children Relations,” drill down into ContentDocumentLinks, and select “ContentDocumentLink ID.”
   - Click “Save.” For detailed instructions on editing a Data Model, refer to ‘[Creating a Data Model’](https://www.docomotion.com/support/docomotion-for-designers/data-model/create-a-data-model/)

**Step 2: Editing the Form**

1. Note that the Data Model pane now includes the ContentDocumentLink ID tag you added, along with the ContentDocumentLink.content tag.
2. In the Word workspace, create a table for inserting pictures, optionally including additional columns.
3. Place the cursor inside the cell and double-click the ContentDocumentLink.content tag. The tag is inserted into the table cell as an image tag.
   - If the table has only one cell, you can define it as a vertical table. Refer to “Working with Tables.”
4. Upon finishing the form design, click the Upload to Cloud icon.
