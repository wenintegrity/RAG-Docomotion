---
title: "Enabling Additional Documents Feature"
source: https://www.docomotion.com/support/docomotion-for-designers/forms/adding-additional-documents/
section: docomotion-for-designers
last_modified: 2024-01-23T10:18:14
---

# Enabling Additional Documents Feature

When generating output, you can automatically incorporate PDF and HTML documents from Salesforce. Refer to the ‘[Generate Output through the Generate Document Button](https://www.docomotion.com/support/docomotion-for-generators/generate-a-document/)‘ for details.

In the Form Generation settings, you have the option to configure the Form to include documents directly from a record’s Files-related list or add required files/documents from the Include Additional Documents object. Review the ‘[Form Default Generation Settings](https://www.docomotion.com/support/docomotion-for-designers/forms/form-settings/)‘ section for guidance.

- You cannot include additional documents if the output format is Mail Body.

### Adding Documents from a Record’s Files Related List

If the Form is configured to add **Additional Documents From Files**, the Additional Documents pane in the Form Generation page includes all the documents from the Files-related list. A Generator user can select the documents to add to the output.

If the Required option is selected, all the documents in the Files-related list are automatically added to the output.

### Adding File From the Include Additional Documents Object

You can add to the Include Additional Documents object documents from one of the following sources:

- Document object
- Files available in libraries

You can add the documents to a form or to a record.

If you want to add documents to an object’s record, you need to add the Include Additional Documents lookup to the object’s page layout. This custom lookup is provided out-of-the-box in the following objects: Account, Case, Contact, Lead, and Opportunity. In other objects, you need to add the lookup to the object.

- The Form object’s layout includes this custom lookup by default.

### Adding Documents to a Form

1. In the Forms tab select the form to which you want to add documents.
2. Scroll down to Include Additional Document and click New.
3. Click the search icon to display a list of available documents for this form.
4. Select Documents to display documents from the Document object and Files to display files from libraries. Note: You can also select a specific folder to display the files inside this folder.
5. Click the document you want to add to the form. The document is displayed in the Document File Name field.
6. In the Display order field add the default order of the document when added to the output (you can change the order when generating output).
7. You can check the Required box to designate the document as required. In this case, the document will be added to the generated output and the output generator cannot remove the document from the generated output.
8. Click Save.

### Adding Documents to an Object’s Record

You can add documents to a record if the Object that was configured to include additional documents. (see Configuring Objects to Include Additional Documents).
Notice that Documents added to records cannot be designated as required.

**To add documents to a record:**

1. In the tab of the object select the record to which you want to add documents
2. Scroll down to Include Additional Document and click New Additional Document.
3. Click the Search icon to display a list of available documents for this object.
4. Select Documents to display documents from the Document object and/or Files to display documents from libraries.
5. Click the document you want to add to the record. The document is displayed in the Document File Name field.
6. In the Display order field add the default order of the document when added to the output (you can change the order when generating output).
7. Click Save.

### Adding the Include Additional Documents Section to the Page Layout

To add documents to an object’s record, the page layout of the object needs to include the Include Additional Documents section.

**To add the Additional Documents field to the page layout of an object:**

1. Access the object’s page layout through a record of the object to which you want to the Additional Documents section (for example, select a Contact record and go to Edit Layout).
2. Select Related Lists in the left pane.
3. Find Additional Documents and drag and drop to the required location.
4. Click Save.

### Add Lookup from Additional Documents to an Object

To add documents to the object, you need to add the Additional Documents custom lookup to the Object.
The following Salesforce Objects: Account, Case, Contact, Lead, Opportunity include the Custom Lookup by default. For other objects, you need to add Lookup from Additional Documents to the Object.

**To add Lookup from Additional Documents to an Object’s layout:**

- Note that in Lightning, adding any Related List to the page layout does not automatically display it in the Lightning page. Verify that you have added the Related Tab to your Lightning page layout, and add the Related Lists component to this Related Tab. Only after this, are all related lists you added to the page layout for the record in the Object manager automatically displayed.

**We will add the lookup to the Order object:**

1. Go to the Additional Documents object: Custom Fields &Relations (these lookups exist by default for OOTB objects).
2. Click New.
3. Select Custom Relations.
4. Select the object to which you want to add the lookup (in our example: Order).
5. Click Next.
6. Click Next: The lookup to the new object (Order) now appears in the list.

### Add the New button to the Include Additional Document Layout

When using Salesforce Lightning you also need to add the New button to Include Additional Documents in the layout of the object.

**To add the New button:**

1. In the Include Additional Document section of the page layout, click the setup icon .
2. The Related List Properties – Include Additional Document window is displayed.
3. In the Buttons tab>Custom Buttons, from the Available Buttons pane select New and add to the Selected Buttons.
4. Click OK.
