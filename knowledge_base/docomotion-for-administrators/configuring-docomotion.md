---
title: "Configuration"
source: https://www.docomotion.com/support/docomotion-for-administrators/configuring-docomotion/
section: docomotion-for-administrators
last_modified: 2025-11-20T12:30:46
---

# Configuration

[Video](https://youtu.be/5EI6N-Divdo)

After you have successfully installed Docomotion, you need to configure Docomotion for your Salesforce org.

### To access the Docomotion Configuration page

In the **App Launcher** select **Docomotion**, and click the
**System Settings** tab to display the Docomotion **Configuration** page.

### On this page

- [Assigning Permissions](#assigning-permissions)
- [Configuring the Generate Document Buttons](#generate-buttons)
- [Download Designer](#download-designer)
- [Authorize (optional)](#authorize)
- [Google Drive (optional)](#google-drive)
- [Link Expiration Period (optional)](#link-expiration)
- [Output Expiration Period for Asynchronous Generation](#output-expiration)
- [Email Validate Block](#email-validate)
- [Live Editor](#live-editor)
- [PDF Password Protection for Interactive Submission](#pdf-password-interactive)
- [Docomotion API Usage (only for API users)](#api-usage)
- [Date and Time Default Formats](#date-time-formats)
- [Send Emails Customization](#send-emails-customization)
- [PDF Accessibility](#pdf-accessibility)
- [Upgrade Metadata](#upgrade-metadata)
- [Signed PDF Settings](#signed-pdf-settings)
- [Download Files](#download-files)
- [Additional Recipient](#additional-recipient)
- [Image Compression](#image-compression)
- [File ShareType](#file-sharetype)
- [Doco Logger](#doco-logger)
- [Use Live Editor with Interactive Form](#live-editor-interactive-form)
- [File Name Settings](#file-name-settings)
- [Multi Signers](#multi-signers)
- [PDF protection settings](#pdf-protection)
- [Fix JSON Tree Storage settings](#fix-json-tree)
- [API Name for Data Model](#api-names-data-model)

### Assigning Permissions

You need to assign each Docomotion user, including Salesforce Administrators, a proper
**permission set**. The permission set determines which operations are available to the user.
See [Assigning Permissions](https://www.docomotion.com/support/installation/assigning-permissions/).

### Configuring the Generate Document Buttons

Add the **Lightning Generate Document** button to the layout of the object to allow users to generate documents.
For more information see
[Configuring Generate Document Buttons](https://www.docomotion.com/docs/configuration/configuring-generate-document-buttons/).

### Download Designer

Download and install the Docomotion Designer tool. Designer is the Windows application that enables you
to design, test and compile templates. Designer requires Microsoft Office 2016 or newer and Windows.
See [Installing the Designer](https://www.docomotion.com/support/installation/installing-designer/).

### Authorize Docomotion to update Salesforce data (optional)

If you plan to use the Live Editor, publish and use Interactive Forms, mass-generate documents or perform
any other asynchronous operation, you need to authorize Docomotion to update Salesforce data.
Only a user authorized to update Salesforce data can perform this step.
See [Authorize](https://www.docomotion.com/support/docomotion-for-administrators/authorizing-to-interact-with-salesforce-data/).

### Google Drive (optional)

Configure Google Drive as an output channel on the generation screen. This allows saving the generated
document directly to Google Drive, per organization or per individual user.

### Link Expiration Period (optional)

If you intend to use Interactive capabilities, you can change the default expiration period for the
**Link** channel. You can also configure a link expiration period for a specific Form
(see [Defining the Default Form Generation Settings](https://www.docomotion.com/support/docomotion-for-designers/forms/form-settings/)).
The Form setting overrides the system setting.

### Output Expiration Period for Asynchronous Generation

When generating asynchronous output or Mass Generation and selecting the **Download** channel,
you can control how long the result files are kept on Docomotion servers before deletion.
This is especially useful if users might navigate away from the page. The default period is 4 days.

### Email Validate Block

If you generate output through the email output channel, you can block generation when the selected
recipient is missing an email address. If this option is not activated, users receive a warning
but can still continue after choosing another recipient or adding an email address.

### Live Editor

Enable or disable the Docomotion Live Editor. Live Editor lets generators make last-minute changes to
the generated document without changing the master template. You can also enable the
**Reload Page** label to refresh data and recalculate page breaks. Authorization is required.

### PDF Password Protection for Interactive Submission

Configure Docomotion so that Interactive PDFs generated through the **Link** channel are
password-protected. The password is based on the Salesforce ID of the related Signature record.

### Docomotion API Usage (only for API users)

For subscriptions that use Silent API Generation, this section shows the monthly API usage count and
allows you to refresh the usage details.

### Date and Time Default Formats

Configure the default Date and Time formats applied to **Date** and **DateTime**
tags when added to the Form by Interactive recipients. Choose a date pattern (for example
`dd MM yyyy`), a separator (dot, hyphen, slash) and a time format (12-hour or 24-hour).

### Send Emails Customization

Control which sending options are available when generating Mail Body output:
enable/disable **Send Email**, **Send with Salesforce** and
optionally make the email body **Read Only** in the new UI.

### PDF Accessibility

Configure accessibility options for generated PDFs: create tagged PDFs, repeat table headers on every page,
and define replacement text for empty table cells to improve screen-reader output.

### Upgrade Metadata

When upgrading from an older Docomotion package version, use this section to allow access to the Salesforce
Metadata API (Remote Site Setting) and upgrade the organizational metadata used by Docomotion.

### Signed PDF Settings

Choose where signed PDFs and uploaded files are stored:
in the **Signature** object or in the **parent record**, and whether they are saved
under **Notes & Attachments** or **Files**.

### Download Files

Enable and configure the behavior used by the Doc2Files / Dynamic Word add-ins to edit and manage files
related to Salesforce objects.

### Additional Recipient

By default, recipients include contacts and leads related to the main object. When this feature is enabled,
you can also select recipients from any related record that has an email field, and optionally select the
current user (owner) as recipient.
For more information see
[Generating output – select recipient](https://www.docomotion.com/support-2-2/generating-documents/generating-output-select-recipient/).

### Image Compression

Enable automatic compression for images uploaded as part of Interactive Forms. Images are proportionally
resized to reduce file size while preserving quality.

### File ShareType

Define the default **ShareType** for generated documents stored in Salesforce Files.
Initial default is **V** (Viewer permission). You can also select **I**
(Inferred permission).

### Doco Logger

Enable the Docomotion Logger. When enabled, each generation creates a record on the
**DocomotionHistory** object with information such as who generated the document,
generation channel and format, Form ID, and more.

### Use Live Editor with Interactive Form

Enable this option to combine a non-interactive form with an additional Interactive Form that is appended
at the end during generation. This lets you edit the original form in Live Editor and still collect
interactive responses from the recipient.

### File Name Settings

By default, Docomotion replaces spaces with dashes in generated file names.
Enable this setting if you prefer to keep spaces in file names.

### Multi Signers

Enable multi-signer processes. When active, you can create multi-step signing flows and configure the
signer order and shared interactive sections in the **Step Signature** related list on the Form.

### PDF protection settings

Protect generated PDF files. You can choose between read-only generation or password-protected PDFs and
define which field in the Form will be used as the password.

### Fix JSON Tree Storage settings

If a Data Model file becomes corrupted, enable this setting to repair the JSON tree storage used by the
Data Model and restore its structure.

### API Name for Data Model

By default, the Data Model shows object and field labels. Enable this option to also display the Salesforce
API names for objects and fields, which is useful for admins and developers.
