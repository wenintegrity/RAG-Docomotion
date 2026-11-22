---
title: "Live Editor"
source: https://www.docomotion.com/support/docomotion-for-generators/live-editor/
section: docomotion-for-generators
last_modified: 2026-08-26T08:15:39
---

# Live Editor

[Video](https://youtu.be/7m2tQ7Is6rg)

## Overview

Live Editor lets you make last-minute adjustments to a generated document before finalizing or sending it, without modifying the original Form template. You work in an HTML-based editor that displays the document as it will appear in the final output, allowing you to update text, formatting, and images directly.

**Common use cases:**

- Adding a personalized sentence before sending
- Correcting a data value pulled from Salesforce
- Inserting a one-off image or remark specific to this document

## What’s New in Version 23

Starting with Docomotion v23, Live Editor supports **asynchronous generation**. This unlocks features that previously did not work when using Live Editor:

| Feature | Pre-v23 | V23+ |
| --- | --- | --- |
| Additional Documents | ✗ Skipped | ✓ Included |
| Images from Notes & Attachments | ✗ Not rendered | ✓ Rendered |
| Images from Salesforce Files | ✗ Not rendered | ✓ Rendered |

**Note:** If you are on a version prior to v23 and your Form uses any of these async features, Upgrade to v23 for full live editor support.

## Prerequisites

To use Live Editor, the following must be in place:

### Organization Requirements

- **Subscription Tier:** Gold tier or above

### User Requirements

- **Docomotion License:** The user must have an active license.
  See: [Licenses Management](https://www.docomotion.com/support/docomotion-for-administrators/licenses-management/)

- **Permission Set:** The user must be assigned a Docomotion permission set.
  See: [Assigning Permissions](https://www.docomotion.com/support/docomotion-for-administrators/assigning-permissions/)

### System Requirements

- **Authorization:** Docomotion must be authorized to interact with Salesforce data.
  See: [Authorizing Docomotion](https://www.docomotion.com/support/docomotion-for-administrators/authorizing-to-interact-with-salesforce-data/)

## Accessing Live Editor

1. Open the Salesforce record you want to generate from (e.g., Account, Opportunity, Case).
2. Click **Generate Document**.
3. Select your Form, Output Format, and Channel.
4. Click the **Live Editor**

Docomotion generates a working copy and opens the live editor.

## Working in the Editor

### Editor Layout

- **Black horizontal lines** indicate page breaks.
- **Headers and Footers** are visible for context but are **read-only**.
- **Locked Sections:** Some areas may be locked by the Form Designer and cannot be edited, moved, or deleted.

### Toolbar

The toolbar provides standard rich-text editing tools: fonts, colors, alignment, tables, and undo/redo. Hover over any button to see its function.

### Managing Images

**Manual Uploads:**

You can insert images directly from your computer or Google Drive using the toolbar. These images apply only to the current document.

**Images from Salesforce (v23+):**

If your Form includes images pulled from Notes & Attachments or Salesforce Files, these are rendered inside the Live Editor so you can verify them before generating.

See: [Adding Pictures from Notes & Attachments](https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-pictures-to-a-form/pictures-from-notes-and-attachments/)

### Additional Documents (v23+)

Additional Documents allow you to append PDFs or HTML files to your generated output. These do not appear inside the editor canvas, they are packaged into the final output when you click Generate.

See: [Enabling Additional Documents](https://www.docomotion.com/support/docomotion-for-designers/forms/adding-additional-documents/)

## Output Scenarios

### Scenario A: Live Editor with Email

When **Email** is selected as the Output Channel with **Mail Body** as the format, the Live Editor is embedded directly in the **Send an Email** page.

- **Editing:** Modify the email body content directly in the editor.
- **Sender:** Pre-defined in generation settings or select from Salesforce Organization-Wide Email Addresses.
- **Recipients:** Set the primary recipient and manage CC/BCC fields.
- **Attachments:** Manage and verify file attachments before sending.
- **Activity History:** Use the **Related to** field to specify where the email activity should be logged in Salesforce.

### Scenario B: Live Editor with Interactive Forms

You can combine Live Editor with Interactive Forms to create a single document that includes both editable content and interactive fields for the recipient.

**How it works:**

The Applicative Form opens in Live Editor where you can make last-minute edits as usual. When you generate a Link output, the system automatically merges your edited content with the linked Interactive Form. The recipient receives **one unified document** containing the document content followed by the interactive fields (text boxes, checkboxes, dropdowns) they need to complete.

**Setup:**

1. Enable **“Use Live Editor w/ Interactive Form”** in Docomotion System Settings.
2. Create two Forms with the same Data Model:
   - An Applicative Form (the document template)
   - An Interactive Form (with Interactive Tags or Interactive Collection)
3. In the Applicative Form settings, link it to the Interactive Form under the “Interactive Forms” section.

See: [Enabling Live Editor with Interactive Fields](https://www.docomotion.com/support/docomotion-for-designers/forms/enabling-live-editor-with-interactive-fields/)

## Saving and Generating

Live Editor uses a versioning system to protect your work:

| Action | Resulting Version | Description |
| --- | --- | --- |
| Save Draft | Minor Version | Saves your changes without finalizing. You can close and resume later by selecting the draft from the Minor dropdown. |
| Generate | Major Version | Finalizes the document, triggers async processing (Additional Documents, images), and delivers output to the selected channel. |

**Additional buttons:**

- **Reload:** Refreshes the editor (useful if Salesforce data has changed).
- **Preview:** Available depending on your system configuration.

## Limitations

- Headers and Footers cannot be edited in Live Editor.
- Locked Sections cannot be moved, edited, or deleted.
- **Pre-v23:** Async features (Additional Documents, images from Files/Attachments) are not supported in Live Editor. Upgrade to v23 for full functionality.

## Fixing “Live Editor Not Loading” – Blocked Visualforce Domain

**Symptom:** The Live Editor stays blank or fails to load, often with a CSP-related error in the browser console.

**Cause:** Salesforce blocks the Visualforce page’s domain because it isn’t added as a trusted domain for inline frames in your org.

**Fix:**

1. Open the browser console (F12) while the error occurs and find the blocked Visualforce domain (e.g. `https://yourorg–c.vf.force.com`).
2. In Salesforce Setup, search for and open **Session Settings**.
3. Scroll to the **Trusted Domains** section (under “Trusted Domains for Inline Frames”) and click **Add Domain**.
4. Enter the Visualforce domain and save.
5. Refresh and reopen the Live Editor.

**If it still fails:** Check the **Clickjack Protection** section on the same page  – a strict setting can block framing even after adding the trusted domain. Use a setting that allows framing by trusted sites.

Still stuck? Contact Docomotion Support with a screenshot of the console error.
