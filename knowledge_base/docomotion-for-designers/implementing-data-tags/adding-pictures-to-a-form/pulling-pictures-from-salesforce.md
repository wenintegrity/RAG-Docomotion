---
title: "Pulling pictures from Salesforce files to a form"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-pictures-to-a-form/pulling-pictures-from-salesforce/
section: docomotion-for-designers
last_modified: 2024-01-10T08:55:33
---

# Pulling pictures from Salesforce files to a form

### Importing Images from Salesforce Files to a Form in Salesforce Lightning

Introduction:

In Salesforce Lightning, you can seamlessly integrate images stored in Salesforce files into your forms by following a few straightforward steps. The procedure below outlines the process from creating a custom field to adding the image tag to your form in the Designer.

Procedure:

**Step 1: Add a Custom Text Area (Long) Field**

1. Navigate to the object from which you want to generate the output.
2. In the object’s “Fields & Relationships,” click on “New.”
3. Select the “Text Area (Long)” data type and click “Next.”
4. Enter a name for the new custom field and click “Next.”
5. Click “Next” to establish field-level security, then click “Save.”

**Step 2: Create a URL for the Image File**

1. In “Files,” locate the image file you want to add to the form.
   - Note: If the file is not already present, you can upload it to Salesforce.
2. Click the arrow next to the record line and select “Public Link.”
3. In the “Public Link Sharing” page, click “Create Link.” The “Create unrestricted public link?” page is displayed.
4. Click “Create.” The “Public Link Sharing” page reappears.

**Step 3: Add the Link to the Custom Field**

1. In the “Public Link Sharing” page, click “Copy Link.”
2. Open a new browser tab, paste the link, and view the displayed image.
3. Right-click the image and choose “Copy image address.”
4. Go to the object to which you added the custom field.
5. In the “Details” tab, scroll to the new custom field and paste the copied address.

**Step 4: Add the Image Custom Field to the Data Model**

1. Open the data model of the form to which you want to add the image.
2. Add the new custom field to the data model as an applicative tag (interactive is not supported). Refer to “Defining a Data Model.”

**Step 5: Add the Image Tag to the Form in the Designer**

1. Open the form in the Designer.
2. Insert the image field tag as a picture.
