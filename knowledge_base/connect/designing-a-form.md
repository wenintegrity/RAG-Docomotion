---
title: "Template Workflow – From Form Creation to Publication"
source: https://www.docomotion.com/support/connect/designing-a-form/
section: connect
last_modified: 2025-05-20T07:15:21
---

# Template Workflow – From Form Creation to Publication

## Step 1: Create a New Form

Navigate to **Forms > New** and complete all required fields. The **Object Name** field must exactly match the **ID** of the object marked as `isMain: true` in your JSON schema. Save your form when finished.

## Step 2: Configure the Data Model

After saving your form, click the **Define Data Model** button. Use the JSON File Uploader to upload your [prepared schema file](https://www.docomotion.com/support/connect/data-model-schema/). Map fields as needed in the interface, then save your changes.

**Important Schema Rules:**

- The main object’s API name must remain unchanged in all updates
- If fields are already mapped, you can only add new fields or objects – you cannot modify or delete existing ones

**Note:** When re-uploading a schema, you may only extend the existing data model with additional fields. Modifications or deletions to already mapped fields are not permitted.

## Step 3: Design the Document Template

From your Form record, click **Open Designer** to launch the template editor. Configure your document layout and insert fields from your defined data model. When complete, save your template to Salesforce.

## Step 4: Publish the Form

First activate your form, then click the **Publish** button to make it available for API-based document generation.
