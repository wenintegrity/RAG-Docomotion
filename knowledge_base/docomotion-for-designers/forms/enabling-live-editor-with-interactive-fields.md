---
title: "Live Editor with Interactive Fields (HTML + Link)"
source: https://www.docomotion.com/support/docomotion-for-designers/forms/enabling-live-editor-with-interactive-fields/
section: docomotion-for-designers
last_modified: 2026-02-19T06:44:48
---

# Live Editor with Interactive Fields (HTML + Link)

**Version Requirement:** Available in Docomotion v19 and later.

### **What is this feature?**

Standard HTML + Link generation grab data the moment they are opened, meaning you can’t easily make last-minute edits to the document before sending it.

**This feature gives you the best of both worlds.** It allows you to use the **Live Editor** to customize the document (change text, fix typos, adjust layout) while still including **Interactive Fields** (like signatures or text inputs) for the recipient to fill out.

### **How it works: The “Two-Form” Solution**

To make this work, Docomotion combines two different forms into one seamless experience for the recipient:

1. **The Top Section (Static/Editable):** This is your main document content. You can edit this in the Live Editor before sending. Once sent, it becomes a “snapshot” and won’t change.
2. **The Bottom Section (Live/Interactive):** This contains the fields the recipient needs to interact with (signatures, inputs). This section stays “live” and connected to Salesforce.

### **Step-by-Step Setup Guide**

#### **Step 1: Enable the Feature (Admins Only)**

1. Go to **Docomotion** → **System Settings**.
2. Find the setting: **Use Live Editor with Interactive Form**.
3. Check the box to **Enable** it.
4. Click **Save**.

System Settings - Enabling live editor with interactive fields

#### **Step 2: Configure Your Forms (Designers)**

You need to build two separate forms that share the **same Data Model**.

1. **Create two forms**

- **Form 1 (The Content):** This is the part users can edit.
- **Form 2 (The Interactive Fields):** This hold the interactive fields

1. **Link Them Together**

1. Open the Form for your **Applicative** (Content) form.
2. Scroll to the **Interactive Forms** section.
3. In the dropdown, select the **Interactive Form** you just created.
4. **Save** your form.

Linking forms

#### **Step 3: Generate & Send (End Users)**

When you are ready to send the document:

1. Start the generation process using the **Applicative (Static)** form.
2. For the Output Channel, select **HTML + Link**.
3. Click the **Live Editor** button.
4. Make your last-minute edits (change wording, add personal notes, etc.).
5. Click **Generate**.

**The Result:** The recipient receives one link. When they open it, they see your custom-edited text at the top and the live signature/input fields at the bottom.

Generation Screen

### **Best Practices & Important Notes**

#### **The “Snapshot” Rule:**

Any changes you make in the Live Editor are saved as a “snapshot.” If Salesforce data changes *after* you generate the link, the **Top (Static)** section will **not** update. However, the **Bottom (Interactive)** section will always show live data if tagged.

- **Static Form (Applicative):** Use this for letters, contracts, greetings, or specific wording you might want to tweak manually.
- **Interactive Form:** Use this for data that *must* stay current (e.g., pricing tables linked to live inventory) and fields the user needs to sign or fill out.

#### **Troubleshooting**

Having trouble? Check these common issues.

| **Issue** | **Solution** |
| --- | --- |
| **I can’t select an Interactive form in the settings.** | 1. Check that both forms use the exact **same Data Model**. |
| **The interactive fields are missing.** | 1. Make sure you generated the **Applicative** form (not the Interactive one).  2. Confirm the Output Channel is **HTML + Link**.  3. Verify the feature is enabled in **System Settings**. |
