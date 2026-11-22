---
title: "Interactive Collection Elements"
source: https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/interactive-collection-input-elements/
section: docomotion-for-designers
last_modified: 2024-01-12T07:02:39
---

# Interactive Collection Elements

**Text:** The Text element is an input field designed for entering text data. It supports masking to ensure the proper formatting of manually entered data. Through the use of an appropriate script, real-time validation can be implemented to control specific entry types or values.

*Interactive Text Example:* This element is useful for fields like Remarks or Email. Validation, such as ensuring the correct email syntax (e.g., jsmith@forms.com), can be applied using scripts for criteria like the presence of ‘@’ and dots. For more details, refer to the Editing Interactive Elements section.

**Picklist:** Allows users to select a single option from a predefined set of options.

**Multi Picklist:** Allows multiple selections from a predefined set of options.

**Checkbox / Radio Button:** A Checkbox is employed for selecting specific options within a list of choices.

**Date:** Allows users to add a date by selecting it from a calendar.

Note: Date is available in HTML output but not in PDF.

**DateTime:** The DateTime textboxes enable users to add both date and time. Users can select the date from a calendar and input the time either by choosing from a list or typing directly into the textbox.

Note: DateTime is available in HTML output but not in PDF.

**Upload File:** The Upload File button permits recipients to attach files to the Interactive Form.

**Upload File:** Allows recipients to attach files to the submitted output. Files uploaded by interactive form recipients can be updated with custom metadata if you defined them to be stored as Salesforce Files.

**Signature:** Allows recipients to add a graphical signature to the submitted output.

**Embedded Images:**Allows recipients to embed images to the submitted output.

- You can define the properties of the elements during the designing process. Refer to ['Interactive Data-Tags Properties](https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/interactive-data-tags-properties/)

- 'Upload File ', "Signature' & 'Embedded Image' elements are available when the selected format is 'HTML' and the output channel is Link. See '[output formats and channels](https://www.docomotion.com/support/docomotion-for-generators/output-formats-and-channels/)'
