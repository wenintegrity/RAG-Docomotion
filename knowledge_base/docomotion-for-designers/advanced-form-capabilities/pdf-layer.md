---
title: "PDF Layer"
source: https://www.docomotion.com/support/docomotion-for-designers/advanced-form-capabilities/pdf-layer/
section: docomotion-for-designers
last_modified: 2024-11-18T07:53:24
---

# PDF Layer

[Video](https://youtu.be/Afl22R1VTto)

Use an existing PDF file in your template to integrate it as a predefined template structure. This is a valuable feature for use cases where it is important to meet document regulatory requirements (such as goverment documents) or for cases where you want to save time and effort.

You can easily add your data model fields (applicative and interactive) on top of the PDF layer and generate a PDF format or a HTML link.

How to use PDF Layer

1. Create a new form, and check the ‘PDF Layer’ option in the form settings.  For your attention, only by checking the PDF Layer checkbox, you will be benefited from this feature.

The Rest of the settings can be the same as they were previously for Form creation.

2. Open the Docomotion Designer and click the ‘PDF Layer’ option from the menu bar.

3. In the ‘PDF Layer’ menu, you have two options:

- Insert PDF: Upload a PDF from your local PC.
- Undo PDF Layer: Remove the currently selected PDF.

4. Select ‘Insert PDF’, select the PDF file, and click ‘Open’. Allow a few seconds for PDF dimension calculation until the ‘PDF Layer’ dialog box appears.

5. In the dialog box, choose the ‘Fitting Mode’ and click ‘OK’:

- Fit to PDF: Adjust page dimensions to match the uploaded PDF (Recommended).
- Fit to Word: Adjust the uploaded PDF dimensions to the Word document dimensions.

The inserted PDF becomes images in the section in each header of your ‘Designer’ page.

6. Create your layer using various field elements such as static text, applicative fields, and interactive fields.

7. To add a field, Right-Click the required field. and choose ‘Insert as Shape’.

8. Place the shape and Align it properly.

9. Repeat step 8 and add all the fields to the form.

Insert a ‘Checkbox’ field from the interactive collection.

Insert a ‘Free Text’ field from the interactive collection.

Insert an Applicative field named ‘Contact Description’, to bring the default value.

And last, Insert a ‘Submit’ Button from the interactive collection.

12. Save your form by clicking on the cloud icon.

13. Now let’s generate the document. Select the form, and generate a document in HTML format with Link Channel.

14. As a recipient, open the link to the document. Edit and complete the relevant missing data, sign and submit the document to update Salesforce. The signed document is stored in Salesforce.

Limitations and additional Information:

- Inserting a PDF will add Section breaks; do not remove them.
- PDF size is limited to 10 pages and up to 4MB.
- Page margins will be automatically set to ‘0’; avoid manual changes.
- Keep the header free from elements; place elements in the form body.
- The ‘Live Editor’ feature is currently not supported.
- The ‘Preview Document’ feature is currently not supported.
- Form Segments are not supported.
