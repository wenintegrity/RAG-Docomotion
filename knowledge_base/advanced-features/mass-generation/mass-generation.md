---
title: "Mass Generation Feature"
source: https://www.docomotion.com/support/advanced-features/mass-generation/mass-generation/
section: advanced-features
last_modified: 2024-11-12T11:36:40
---

# Mass Generation Feature

[Video](https://youtu.be/updXaNSLRtk)

### **Mass Generate from Salesforce Reports:**

The mass generation feature empowers users to generate output from multiple records in bulk.

1. Click the “Generate from Report” tab.
2. The left pane displays the hierarchical structure of the reports, and the right pane lists available reports.
3. Select a report. *Important*: Ensure the first column in your report is the Object ID.
4. Click “Next” to display the mass generation page.
5. Select the relevant Form.
6. Select the Output Format.
7. Select Output Channel(s).
8. Click the ‘Generate’ Button. Upon completion, a success message is displayed.

   Some Notes:

   - In downloading a PDF output channel, a hyperlink to the output is provided.
   - In the Mail Body output format, if a file name is specified in Default Generation Settings, it serves as the default email subject. However, you have the option to enter alternative text for the subject, overriding the default settings.
   - In case the Form or the record includes additional documents, the **Additional Documents**panel is displayed. The record documents appear as an unified collection, **Record Additional Documents Collection,**in the **Available Contents** pane. If you want to include the documents in the output, drag and drop to the required location in the **Included Content** pane (which includes, by default, the generated Form and Form required documents).
   - Docomotion Mass Generation works asynchronously, so you do not need to wait for the success message. You can always close this window or close Salesforce. At the end of the process, you will receive a notification email.

### Utilizing the Mass Generation Checkbox for Aggregated Document Output

1. At the “Document Generation” Screen, select the “Combine” checkbox.
2. Select the Output Format. The PDF, DOCX, and HTML output formats are available.
3. Select the Output Channel(s). The ‘Download’ and ‘Document output’ channels are available..

- Notice: The maximum size of a combined output file (including attached documents and pictures) 12 MB.

- Notice: Alternative methods to generate in bulk are available. You can use the "Mass Generation" Feature from a list-view or the Related lists. Refer to '[Adding Mass Generation Button to Standard Objects](https://www.docomotion.com/support/advanced-features/mass-generation/adding-mass-generation-button-to-custom-objects/)'.
