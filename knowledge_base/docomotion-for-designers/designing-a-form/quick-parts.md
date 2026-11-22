---
title: "Quick parts"
source: https://www.docomotion.com/support/docomotion-for-designers/designing-a-form/quick-parts/
section: docomotion-for-designers
last_modified: 2024-01-10T08:45:04
---

# Quick parts

### **Quick Parts**

Quick Parts in Word are intelligent fields, such as page numbers and generation dates, that dynamically populate within a document during generation. To insert one of these fields, follow these steps: Click on Insert > Quick Parts > Field.

You have the option to add the following fields: Date, Page, NumPages, and SectionPages. When editing, these fields are visually indicated in the document with a grey background, which remains invisible in the generated output.

**Date Field:**

- Represents the generation date, automatically updated during output generation with the server date.
- You can also utilize the Date or Date&Time data tag and format it in Salesforce. Refer to Date&Time Masking.

*Example:*

- **In Document (During Editing):** Add Date
- **In Generated Output:** Displayed according to the specified Date Format pane.

*Tip:* You can modify the order of the month and date in the Date Format pane by adjusting the display order of ‘D’ and ‘M.’

**Page Numbering:**

- Comprises Page (current page number) and NumPage (total pages in the generated document).
- These fields are updated during output generation based on the added data and the actual number of generated pages.
- Add these fields only in the Header/Footer areas.
- To create a complete page numbering format, insert the fields along with fixed text as per design requirements.

*Example:*

- **In Document (During Editing):** Add Page 1 of 1
- **In Generated Document (With Additional Pages):** Page 1 of 2

**Page Numbering in Sections:**

- - If using sections, utilize the SectionPages field to number pages separately in each section.
  - SectionPages: Total pages in the current section. Page: Current page number.
  - For accurate presentation, reset the page numbering of the section to start from 1.
  - Right-click the Page field and select Format Page Numbering.
  - Choose Start at 1.
