---
title: "Form Default Generation Settings"
source: https://www.docomotion.com/support/docomotion-for-designers/forms/form-settings/
section: docomotion-for-designers
last_modified: 2026-03-05T06:53:36
---

# Form Default Generation Settings

As an Administrator or Designer, you can pre-configure how documents are generated to ensure consistency and save time for your users.

**Where to find these settings:** These options are managed within the **Docomotion Form record** in Salesforce.

- **Don’t see the settings?** First, navigate to the **[Form Details Page](https://www.docomotion.com/support/docomotion-for-designers/forms/form-page/)** to learn how to access and manage your Form objects.
- Once you have selected your Form from the **Docomotion Forms** tab, scroll down to the **Default Generation Settings** section.

**Workflow Tip:** You must click **Edit** on the Form record to modify these settings and click **Save** when finished to update the default behavior.

#### Primary Configuration

- **Use this Form as Default:** Set this form as the primary template for its Main Object. It will be pre-selected for users in the Generation Screen to streamline their workflow.
- **Asynchronous Generation:** Ideal for large datasets or complex forms. Users receive a notification once the document is ready, allowing them to continue working in Salesforce while it processes.
- **Format – Default:** Choose the preferred output format (e.g., PDF, DOCX, or Email Body).
- **Channel – Default:** Select the primary delivery method, such as Email, Download, or an Interactive Link.
- **Default File Name:** Select a Salesforce field to dynamically name the generated file (e.g., “Invoice\_{Account\_Name}”).
- **Email Template:** Pre-select a branded email template to be used when sending the document via the Email channel.
- **Default Mail Body Subject:** Customize the email subject line. If left blank, it defaults to the file name.

#### Attachments & Data Handling

- **Additional Documents from Files:** Automatically pull in files from the record’s “Files” related list to be attached to the final output.

  - *Note: If “Required” is selected, all files on the record will be included automatically.*

#### Permissions & Interface Control

- **Permissions for Changing Defaults:** Control which settings (Format, Channel, File Name, Email Template) users are allowed to override during the generation process.
- **Modifying Generation Page Display:** Simplify the user experience by hiding specific options from the Generation Screen, ensuring users only see what is relevant to their task.
