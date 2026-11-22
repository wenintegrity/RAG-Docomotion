---
title: "Generate Output through the Generate Document Button"
source: https://www.docomotion.com/support/docomotion-for-generators/generate-a-document/
section: docomotion-for-generators
last_modified: 2024-01-12T07:25:41
---

# Generate Output through the Generate Document Button

Generators can utilize the “Lightning Generate Document” button within a Salesforce record to initiate the document generation process. This merges data from the record and the related objects into the selected Form, resulting in an output document populated with data from that specific Salesforce record and its related records.

To initiate the document generation process, follow these steps:

1. **Select a Record:** In Salesforce, choose the record for which you intend to generate a document.
2. **Click** the “Lightning Generate Document” button.
3. Choose the specific Form you want to use for document generation. If the Form you’re looking for is not visible, switch to the “All” view to display all the published forms associated with the respective object.

   - Users with Docomotion Admin or Designer permissions can view both active and published forms.
4. **Select the Format:** Choose the desired format for the generated document:

   - PDF
   - HTML
   - DOCX
   - Mail Body

   The channels will be available according to the selected format. Refer to ‘[Output formats and channels](https://www.docomotion.com/support/docomotion-for-generators/output-formats-and-channels/)‘ for more details.

   When using the Mail Body output format, and if the Additional Recipients option is enabled, you can add recipients to the email using lookups. The Select Recipient pane will be displayed.
5. **Choose the Output Channel:** Select the appropriate output channel(s):

   - Mail: Send an email with the output as an attachment (automatically selected if you chose Mail Body Format).
   - Link: Create a link to an interactive document.
   - Download: Download to your local workstation.
   - Document: Create a Document Object in Salesforce.
   - Notes and Attachments: Add to the Object record feed.
   - Chatter: Add to the Chatter info.
6. **Recipient Selection (if applicable):** When selecting an email output channel or Mail Body format, choose a recipient. Refer to the section on Generating Output – Select Recipient.

   - If Chatter or ‘Notes & Attachments’ output channels are selected, avoid using special characters to prevent a 4002 error.
7. **Define the Output File Name:** In the Output File box, either retain the file name set in the Generation Settings section or modify it. By default, the file name is the record name unless otherwise defined in the Generation Settings. Be mindful that certain characters are not permitted and will be replaced.
8. **Manage Additional Documents:** If the form includes additional documents, the Additional Documents pane displays them. The selected documents will be **merged to a single generated output**, and their order can be adjusted. Refer to ‘Additional Documents’ for more details.
9. **Generate Document:** Click Generate, and the documents will be generated in the selected format and output channel(s).

- Notice: If certain output formats and channels are not accessible, kindly refer to the '[Form Default Generation Settings](https://www.docomotion.com/support/docomotion-for-designers/forms/form-settings/)'
