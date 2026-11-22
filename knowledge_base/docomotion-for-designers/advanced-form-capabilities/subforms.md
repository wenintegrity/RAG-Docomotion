---
title: "Subform (Segment)"
source: https://www.docomotion.com/support/docomotion-for-designers/advanced-form-capabilities/subforms/
section: docomotion-for-designers
last_modified: 2026-06-14T09:12:38
---

# Subform (Segment)

A Segment in Docomotion is a **highly reusable form element** that can be saved under a unique name and seamlessly integrated into any form during the design phase. Built specifically for **reusability**, Segments eliminate the need to recreate recurring sections from scratch – significantly slashing design time and ensuring consistency across your entire form system.

**Segment Types: Linked and Unlinked**

- **Linked Segments:** These segments cannot be edited directly within the form and are only alterable by modifying the original Segment Form. Any changes to a linked segment are automatically reflected in the form and subsequent output.
- **Unlinked Segments:** These segments can be edited directly within the form like any other text. Changes to an unlinked segment do not affect the form or generated output.

**Creating Segments:**

- **In Docomotion:**

  1. Create and edit Form Segments in Docomotion similar to regular forms.
  2. Alternatively, create a Segment from an existing form directly within the Designer.
- **Inside the Designer:**

  1. Open the form you want to create the Segment from.
  2. Select the desired content in the form.
  3. Click on “Segment” in the Designer Toolbar, then choose “Save.”
  4. Enter a name and description for the Segment, and decide whether to add it as linked.
  5. Click “OK,” and the segment is automatically published.

**Adding Segments to a Form:**

- **Unlinked Segment:**

  1. Open the form in the Designer.
  2. Position the cursor where you want to add the Segment.
  3. Click on “Segment” in the Designer Toolbar, then choose “Insert.”
  4. Select the desired Segment; it is inserted into the form and can be edited independently.
- **Linked Segment:**

  1. Open the form in the Designer.
  2. Position the cursor where you want to add the Segment.
  3. Click on “Segment” in the Designer Toolbar, then choose “Insert.”
  4. Select the desired Segment, check the “Linked Segment” checkbox, and click “OK.”
  5. Enter a name for display purposes.
  6. The linked segment is inserted, and its properties are displayed in the Form pane.

**Editing Segments:**

To edit a Segment:

1. Open the Docomotion App in Salesforce.
2. In the Forms tab, select the Segment identified by the icon I\_Segment.
3. Click “Open Designer” to make changes.
4. After editing, upload the modified Segment to the cloud.
5. In the Docomotion Forms tab, select the Segment and click “Publish” to apply the edits.

[Video](https://youtu.be/CM2WgMyU3qg)

### Optimizing Performance with Segment Placeholders (“Use Segments”)

To enhance design efficiency and optimize system performance, Docomotion allows you to control how linked segments are rendered within the Designer workspace. By utilizing the **“Use Segments”** feature, you can significantly accelerate form loading and saving times.

#### The “Use Segments” Checkbox

Located on the **Form page** in Salesforce (under the *Generation Settings* section), this checkbox determines whether the Designer loads full visual content or lightweight placeholders.

- **When Checked (Optimized Approach):** Instead of rendering the complete visual layout of every linked segment, the Designer replaces them with compact placeholders (e.g., **S1**, **S2**, **S3**). This keeps the main template extremely lightweight, reducing the file size in your environment and ensuring nearly instant loading and saving speeds.
- **When Unchecked (Classic Approach):** The Designer renders the full, detailed content of all segments directly within the workspace. This provides a classic “what you see is what you get” (WYSIWYG) editing experience.

#### How to Enable Segment Placeholders:

1. Navigate to the **Forms** tab in Salesforce and select your main Form.
2. In the form details, locate the **Generation Settings** section.
3. Check the **Use Segments** box.
4. Click **Save**.

The next time you click **Open Designer**, your linked segments will appear as streamlined placeholders.
