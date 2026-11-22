---
title: "Release Notes v23"
source: https://www.docomotion.com/support/release-notes/rn-v23/
section: release-notes
last_modified: 2025-12-18T11:38:07
---

# Release Notes v23

## v23

**Highlights: Interactive Documents, Reinforced Security, and Enhanced Performance.**

Version 23 represents a major milestone for Docomotion. This release introduces a fully upgraded **Dynamic Word** experience, transitions our architecture to meet the strictest **Salesforce Security Standards**, and improves generation performance for complex document packages.

Below is an overview of the key changes.

---

## 1. The New Dynamic Word Experience

*Transforming documents into interactive, bi-directional interfaces.*

We have bridged the gap between document drafting and your Novidea/Salesforce platform. The Dynamic Word Add-in has been completely re-engineered to support true two-way synchronization.

- **Bi-Directional Sync:** Edit fields (dates, amounts, clauses) directly in Word, and use the **Push Back** capability to instantly update the Salesforce record.
- **The Logger (Audit Trail):** Every interaction is tracked. The new **Dynamic Response** log records “Data Before” vs. “Data After” and attributes changes to specific users for full compliance.
- **Lifecycle Management:** Save a version, clone a file, or publish (Save as Final) without leaving the Word interface.
- **SSO Support:** Seamless login to the Add-in using your organization’s Single Sign-On credentials.

[Read the full Dynamic Word Guide](https://www.docomotion.com/support/advanced-features/dynamic-word)

---

## 2. Critical Security & Architecture Enhancements

*Aligning with Salesforce’s highest compliance standards.*

In this release, Docomotion has completed significant security upgrades to meet Salesforce’s latest OAuth and permission model requirements.

- **Connected App Architecture:** Docomotion now operates through a **Connected App** to ensure secure authorization and controlled access between Salesforce and external components.
- **Designer Authorization:** Opening the Designer now triggers a strict authorization process to validate the user’s access token.
- **Strict Permission Sets:** Access is now governed by the new `Docomotion Auth` permission set, which must be assigned to relevant users.

> Action Required: Admins must configure the Connected App and assign the new Permission Sets preferably before upgrading.
>
> [View the Upgrade & Configuration Checklist](https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/)

---

## 3. Field-Level Security (FLS) Protocols

*Granular control over data access during generation.*

Administrators must now explicitly define how the system behaves when a user attempts to generate a document containing fields they do not have permission to access.

You can configure the generation behavior **Globally** (System Settings) or **Per Form**:

- **Continue (Default):** Generate the document but leave restricted fields blank.
- **Warning:** Alert the user via a dialog box regarding missing permissions before allowing generation to proceed.
- **Block:** Prevent generation entirely if restricted data is detected.

[Read Technical Details on Security Mode](https://www.docomotion.com/support/docomotion-for-administrators/field-level-security/)

---

## 4. Asynchronous Generation Enhancements (Live Editor & Email)

*Expanded Support for Related List Images*

We have upgraded our generation engine to remove previous limitations regarding image handling.

The **Live Editor** and **Email with Attachment** channels now fully support **images sourced from Salesforce Related Lists**.

Previously unavailable for these formats, this capability allows you to include dynamic images from your Salesforce records directly in your Live Editor previews and email outputs.

Additionally, we have optimized performance for complex templates:

- **Immediate Image Rendering:** Related list images appear instantly within the Live Editor.
- **Background Processing:** “Additional Documents” (appended Word/PDFs) are now generated asynchronously in the background, ensuring the main editor loads faster without delay.

[**Read the Complete Live Editor Knowledgebase Page**](https://www.docomotion.com/support/docomotion-for-generators/live-editor/)

Customers upgrading to version 23 must switch from the legacy Generate window to the new Generate window.
This requires adding the new **Generate** button to your Salesforce **Page Layout**, as the legacy button will be migrated and is no longer intended for use.
Please note:

- The **data model can remain Legacy**. There is no requirement to migrate your data model.
- **All existing forms will continue to work as before**.
- Forms that previously used the legacy Generate button will now be generated using the **new Generate button**, with no functional impact.

### Important: Best Practices & Upgrade Strategy

To ensure a seamless transition to Version 23, please adhere to the following recommendations:

- Customers upgrading to version 23 must switch from the legacy Generate window to the new Generate window.
  This requires adding the new **Generate** button to your Salesforce **Page Layout**, as the legacy button will be migrated and is no longer intended for use.
  Please note:

  - The **data model can remain Legacy**. There is no requirement to migrate your data model.
  - **All existing forms will continue to work as before**.
  - Forms that previously used the legacy Generate button will now be generated using the **new Generate button**, with no functional impact.

  Instructions for adding the new Generate button to your Page Layout are available here:
  <https://www.docomotion.com/support/docomotion-for-administrators/adding-the-generate-button/>
  We recommend completing this update as part of your version 23 upgrade process to ensure a smooth and supported generation experience.
- **Sandbox First:** As with all releases, please perform the upgrade on your **Sandbox environment** first. This allows you to validate your specific use cases and configurations before deploying to Production.
- **Pre-Upgrade Preparation:** We strongly recommend completing the **Permission Set creation and assignment** in your current environment *before* installing the new package. Doing this prior to the upgrade ensures that your users maintain uninterrupted access immediately after installation.

For more details please read our ‘[Upgrade to V23](https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/)‘ guide
