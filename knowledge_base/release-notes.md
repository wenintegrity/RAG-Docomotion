---
title: "Release Notes"
source: https://www.docomotion.com/support/release-notes/
section: 
last_modified: 2026-06-14T09:46:49
---

# Release Notes

## V24

Release date: 14.06.2026

**Features:**

| Item | Description | Details |
| --- | --- | --- |
| Parallel Multi-Signing | Accelerate signature cycles by sending a document to multiple signers simultaneously. Building upon our classic sequential chain support, you can now route agreements in parallel to execute non-hierarchical deals even faster. | [link](https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/multi-signers-2/) |
| Deep Data Architecture (8-Level Support) | Enhance template versatility by pulling data from deeply nested Salesforce relationships with expanded support for up to 8 data model levels—fully backward compatible. |  |
| Modernized UI/UX for Configuration Screens | A sleek, enhanced redesign of core admin interfaces (including System, Forms, and Segments) built with clean layouts and intuitive navigation to streamline configuration. |  |
| Optimized Segment Architecture | Boost workspace efficiency by utilizing lightweight InputForms placeholders rather than classic SubForms, streamlining template management and reducing layout complexity. | [link](https://www.docomotion.com/support/docomotion-for-designers/advanced-form-capabilities/subforms/) |

**Improvements:**

| Item | Description | Details |
| --- | --- | --- |
| Large File Processing Capacity | Enhanced document generation pipelines to easily process and successfully generate large PDF files exceeding 17MB. |  |
| Live Editor Spacing Precision | WYSIWYG Layout Alignment. Refined layout parity to ensure the structural spacing inside the Live Editor mirrors the finalized generated document perfectly. |  |
| Integration Permission Refinement | Updated the Integration User selection list in Docomotion System Settings to display only users assigned the required Docomotion permission set. |  |

**Bug fixes:**

| Item | Description |
| --- | --- |
| DC-2620 | Fixed PDF generation failure for files over 17MB |
| DC-2332 | Live Editor Shows Extra Spacing Compared to Generated Output |
| DC-2952 | Default Integration Settings showing every user with Docomotion permission set |

## V23

Release date: 25.12.2025

**Features:**

| Item | Description | Details |
| --- | --- | --- |
| The New Dynamic Word Experience | A re-engineered Add-in featuring bi-directional sync to update Salesforce from Word, a full audit trail, lifecycle management within the interface, and seamless Single Sign-On (SSO) support. | [link](https://www.docomotion.com/support/advanced-features/dynamic-word/) |
| Critical Security & Architecture Enhancements | Upgrades to meet Salesforce’s highest standards using a Connected App architecture and strict permission sets. Admins must now configure specific authorizations and permissions before use. | [link](https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/) |
| Field-Level Security (FLS) Protocols | Admins can now define generation behavior (Continue, Warning, or Block) when users attempt to generate documents containing fields they do not have permission to access. | [link](https://www.docomotion.com/support/docomotion-for-administrators/field-level-security/) |
| Asynchronous Generation Enhancements | The Live Editor and Email channels now support Related List images. Performance is improved by rendering images immediately while processing additional documents in the background. | [link](https://www.docomotion.com/support/release-notes/rn-v23/) |

**Bug fixes:**

| Item | Description |
| --- | --- |
| DC-2718 | Fixed a validation issue in the Preview Lightning Component where “0” was not accepted as a valid form number. |
| DC-2686 | Added the ability to filter by null values within the Query Filter, which was previously unavailable. |
| DC-2685 | Fixed a UI bug where the value input textbox failed to appear for Percentage fields. |
| DC-2680 | Resolved a connectivity issue in the Live Editor that caused a “Page not found” error on the first attempt of the day. |
| DC-2805 | Corrected an issue where the FileId was missing from the History Logger record during asynchronous document generation. |

## V22

Release date: 25/05/25

**Features:**

| Item | Description | Details |
| --- | --- | --- |
| Tables in Rich Text Areas | Copy-paste styled tables directly into Salesforce RTA Fields |  |
| API Names in Data Model | Easily view technical names of fields and objects when editing your data model. | [details](https://www.docomotion.com/support/docomotion-for-designers/data-model/create-a-data-model/) |
| One-Click Dual Format Saving | In our Dynamic Word Add-in – The ability to save both formats (Word + PDF) in one click and support Wording and Clauses with Refresh mode. | [details](https://www.docomotion.com/support/advanced-features/dynamic-word/) |

| Item | Description |
| --- | --- |
| DC-1998 | Fixed an issue where clicking “Generate” again after sending a document by email caused duplicate attachments. |
| DC-2350 | Solved a Data Model issue where some fields were lost after saving, affecting template design. |
| DC-2481 | Improved PDF layer to support documents with more than 10 pages (up to 50), now in the correct order. |
| DC-2464 | Fixed an issue where additional files set in the were not attached to the email activity. |

## V21.9

Release date: 01/03/25

**bug-fix:**

| Item | Description |
| --- | --- |
| DC-2350 | Resolved: Corrupted Data Model Creation Issue |

## V21.6

Release date: 12/01/25

**Features:**

| Item | Description | Details |
| --- | --- | --- |
| Multilingual Picklist Support | Enable templates to support multiple languages by utilizing Salesforce Translation Workbench. Allows automatic translation of picklist values based on form settings. | [link](https://www.docomotion.com/support/release-notes/rn-v21-5/) |
| Media File Upload Support | Users can now upload video and audio files through the Upload File functionality. Supports media files up to 10MB in size, enabling multimedia content integration through direct upload links. |  |

**Improvements:**

| Item | Description | Details |
| --- | --- | --- |
| Lock Fields and Areas with Dynamic Word | Enhanced Dynamic Word Add-in capabilities with container locking functionality, matching the behaviour available in Live Editor. Designers can lock containers and areas to prevent unintended modifications while maintaining document integrity when users work with the document in Microsoft Word. | [link](https://www.docomotion.com/support/docomotion-for-designers/advanced-form-capabilities/container/) |
| File Name Prefix Configuration | Configure customizable prefixes for generated document file names through form settings, to establish consistent file naming conventions for all documents created from templates. |  |

**Bug fixes:**

| Item | Description |
| --- | --- |
| DC-2052 | Resolved an issue with unpublishing or activating the Form changes Filter Form Settings |
| DC-606 | Fixed an issue where additional Form documents were not appearing during Mass Generation |
| DC-2210 | Fix an issue when failed to Import\Export – Filter Query related |
| DC-2225 | Docomotion Logger wrong Field ID value when Live editor is used |

## V21

Release date: 30/09/24

**Features:**

| Item | Description | Details |
| --- | --- | --- |
| Dynamic Word | Automates the data refresh process for insurance policy documents, ensuring accuracy and up-to-date information directly from Salesforce records. Reduces manual effort and minimizes errors. | [link](https://www.docomotion.com/support/advanced-features/dynamic-word/) |
| Page Break with Live Editor | Introduces page break functionality for better control over document layout in the Live Editor. | [link](https://www.docomotion.com/support/release-notes/rn-v21/) |
| Styling Rich Text Area (RTA) | Implement styling capabilities in a RTA to support advanced Word document styling, giving users more control over document formatting and styling. | [link](https://www.docomotion.com/support/release-notes/rn-v21/#rta) |
| Unrelated List: Advanced Filtering and Logic | Enhanced functionality, allowing users to create unlimited filters and logic on the same object, using different fields | [link](https://www.docomotion.com/support/release-notes/rn-v21/#unrelated) |

**Improvements:**

| Item | Description | Details |
| --- | --- | --- |
| New Doughnut Chart with Customizable Colors | Added a new Doughnut chart type with customizable colors, enhancing data visualization and presentation capabilities. | [link](https://www.docomotion.com/support/release-notes/rn-v21/#doughnut) |
| New Date Format: DD Month YYYY | Introduced a new date format option displayed as “DD Month YYYY” (e.g., 29 July 1990) for localization. | [link](https://www.docomotion.com/support/release-notes/rn-v21/#date-format) |
| Salesforce API Upgrade | Upgraded to the latest Salesforce API version, ensuring improved compatibility and performance with your Salesforce environment. | [link](https://www.docomotion.com/support/release-notes/rn-v21/#unrelated) |

**Bug Fixes:**

| Issue ID | Resolution |
| --- | --- |
| DC-2098 | Resolved an issue with using PDF layers in the Designer preview mode. |
| DC-2014 | Fixed the issue with using Docomotion fields in the Designer alongside JavaScript functionality. |
| DC-1969 | Addressed issues related to handling multiple signers through the API |

## **V20**

**Features:**

1. Multi-Signers Forms – [Read More](https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/multi-signers/)
2. Protected PDF: Set a level of security to generated PDFs – [Read More](https://www.docomotion.com/support/docomotion-for-generators/pdf-protected/)
3. PDF Layer – phase 2: Enhancing the process of adding fields to a layer – [Read More.](https://www.docomotion.com/support/docomotion-for-designers/advanced-form-capabilities/pdf-layer/)

**Bug fix:**

Removing Dashes from File name.

## **V19**

New Features:

1. PDF Layer
2. Dynamic filtering of data with a condition variable.
3. Quick ‘Document Preview’ Button – New API Integration
4. Direct Link Output for Salesforce Users
5. Live Editor with Interactive Fields
6. New Look for the interactive fields placeholders

---

**V18**

**New Features:**

1. Image Resize
2. New Fields on Form – Language and Category
3. Mass Generation with Flows
4. History Logger
5. Unrelated List
6. Unlock Subforms
7. Enable Lock Container on Live Editor

---

**V17.3**

**New Features:**

1. Migrate Workflow to Flows
2. Increase the size of the RTA image for generated documents
3. Doc2Files Supports PDF saving
4. Control Share Type
5. Support Hebrew on Generation Screen

---

**V16**

**New Features:**

1. Adding additional recipients in email when using API.
2. Adding additional documents in email when using API.
3. Preview document in generation screen.
4. Test preview with an actual Salesforce record.
5. Set Default recipient in Form settings
6. Additional Recipient – Recipient email enables free text.
7. Live Editor Window – Resizing capabilities.

---

[**V15**](https://www.docomotion.com/support/release-notes/rn-v15/)

**New Feature:**

1. Region Switcher – Expanding cloud infrastructure to the EU in addition to the existing infrastructure in the US

**Improvements:**

1. Data Model drill down up to 5 levels (“NLevel” feature)
2. RTA Images

**Bug-fixes:**

1. Improve reliability of existing features:
   - Segments / Subforms
   - Import / Export forms
   - Live Editor

---

**V14**

**New:**

1. New UI for Document Generation
2. Additional Documents Files Filter for API
3. Image Compression
4. Friendly URL Support
5. New Salesforce Lightning UI for Defining Data Models

---

**V12**

**New:**

1. Files uploaded by interactive form recipients can be updated with custom metadata when defined to be attached as Salesforce Files
2. Adding additional documents to the generated output directly from a related record’s Salesforce files
3. Support for Salesforce Organization-wide email addresses
4. Logging Docomotion server events
5. Actual record preview
6. New email recipient options for output generation
7. Doc2Files – Editing Salesforce Files in MS-Word
8. Pulling pictures from Salesforce Files (Salesforce Lightning)
9. New options for storing signed PDF output
10. Dynamically adding Pictures from Salesforce Files
11. Generate output using data from an external data source
12. Storing output in an external database
13. Support for Salesforce New Flow Builder
14. Document versions in Live Editor
15. Accessible PDFs
16. Embedded image in link channel
17. DOCX: New format supported for combined mass generation
18. Salesforce Files: New channel for output generation
19. Support Salesforce Connect’s OData objects

**Improved:**

1. Additional email recipients when generating output via API or Flow/Process Builder (coming soon…)
2. Live Editor: Additional Options
3. Additional documents: Add documents/files from a selected folder/library
4. RTA – Text font and font size can be set in the Designer
5. RTA Support for embedded image
6. Picklist and multi-picklist new UI
7. Send Email button customization
8. Additional Editing Options in the Live Editor
9. Default Subject for Mail Body Output Format in Mass Generation

---

**V11**

1. Live Editor
2. Interactive Date and Time (Date Picker)
3. Image Background for Signature Field
4. Password Protection for PDF generated through Link Channel
5. Mass Generation from 3rd level lookups
6. Full support Table of Contents for PDF output, and link navigation in HTML

---

**V10**

1. Sum inside a dynamic table
2. Add documents to output
3. Filter Forms
4. Lock sections in the Form from being edited in the Live Editor
5. Full support of Service and Sales consoles

---

**V9**

1. Pull package
2. Form creation in Lightning Experience
3. Add event (activity) after generation
4. Mass Generation from Reports
5. Routing option for Notes & Attachments and Chatter when generating output from Relation and Junction objects
6. Adobe installation no longer prerequisite
7. Full support for Rich Text Area type fields in Salesforce

---

**V8**

1. New Generation UI
2. Interface with DocuSign Integration to Salesforce
3. Mass Generation from Related Lists
4. Support for Rich Text Area type fields in Salesforce
5. Validation before Submit (HTML JavaScript)
6. Designate fields as Mandatory to Fill
7. Link Expiration per Form
8. Configurable message After Submit of Interactive Form
9. Support MS-Word Set Target Frame (open in a new tab)
10. Signature popup in mobile

*Version 8 uses Salesforce API version 40. For more information, please contact Docomotion Support.*

---

**V7**

1. You can now add to the output pictures from a record’s Notes & Attachments.
2. Automate output generation using Salesforce Process Builder.
3. Context-sensitive help.

---

**V6**

1. The new Mass Generation feature enables generating output based on multiple records inside Salesforce List View.
2. Support of European numbering format (localization/number masking).
3. Support for Salesforce Date&Time field.
4. Support for Date&Time field localization, based on the time zone of the recipient.
5. Possibility to set a default file name for generated output in the Form’s Default Generation Settings based on Object field.
6. New Designer Validation menu option.
7. Signing device support: ability to open the signature area on the HTML output as a pop-up window.
8. Support of the new Salesforce Lightning® experience.

*If you have Forms designed in previous versions using scripts on Date or Date&Time Salesforce fields (tags), you need to edit the Forms using the new Date or Date&Time masking options.*

---

**V5.6 / V5.9**

1. Adding graphical Signatures to an Interactive Form (this requires using the new Link output channel).
2. New output channel Link. Send an email with a link to an interactive document.
   - Recipients can fill in the document (including adding a signature and attachments).
3. Uploading Files to an Interactive Form
4. Store output in Google Drive.
5. New Email Template option in mail output channel.
6. New Form Generation Settings now enable simplifying the output generation page.
7. Enhanced Designer to enable presenting in the output the Salesforce data of all interactive fields, which can be edited by the recipient and updated in Salesforce.

*To use the Docomotion Designer tool you need to make sure that Microsoft .NET 4.6.1 is installed on your computer.*

---

**V5.5**

1. Word Template Optional (Docomotion no longer requires a Word template for creating a new Form)
2. Insert Page Break in Grouped Table
3. Table of Content (TOC) Supports Show / Hide Containers (Improved)
4. Enhanced Date Format Support (Improved)
5. Support of Image URL without Extension for ALL Output Formats (Improved)

---

**V5.4**

1. Form Lifecycle
2. Table Grouping
3. Multi Language Support of Picklists
4. Date Support
5. Import / Export Scripts in the Designer
6. Simplify Insert Picture in the Designer
7. Interactive Fields Default Value (Improved)
8. Interactive Support without Contact (Improved)
9. Table of Contents Supports Containers (Improved)

---

**V5.3**

1. Exporting / Importing Forms
2. Adding a Table of Contents to a Form
3. Renaming the Generated Output File
4. ‘Upload to Cloud’ Renamed ‘Save to Salesforce’
5. No need to Enable Chatter when Installing Docomotion

---

**V5.2**

1. New License for Generating Output in Silent Mode
2. Sorting Tables
3. Renaming the Generated Output File
4. Improved Form Structure

---

**V5.1**

1. New Quick Start Tab
2. New Generation Screen
3. Supports Generating Output from Mobile
4. Inserting Form Segments as Linked or Unlinked
5. Forms and Data Model Changes
6. New Mail Body Support
7. Generating Output in Silent Mode
8. Nested Table Support
9. Localization Support
10. New Interactive Features
11. Simplified Publishing (Improved)
12. Renaming (Improved)
