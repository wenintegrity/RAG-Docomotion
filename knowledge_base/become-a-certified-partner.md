---
title: "Become A Certified Partner – Final Exercise"
source: https://www.docomotion.com/support/become-a-certified-partner/
section: 
last_modified: 2026-08-18T07:41:35
---

# Become A Certified Partner – Final Exercise

### Before you start

- Create a Salesforce environment; This can be a [trailhead organization](https://trailhead.salesforce.com/content/learn/modules/trailhead_playground_management/create-a-trailhead-playground) or a [developer organization](https://developer.salesforce.com/signup).
- Install and configure the Docomotion package as described in ‘[Install Docomotion](https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/)‘
  - [Assign Permissions](https://staging6.dev.docomotion.com/docs/configuration/assigning-permissions/)
  - [Authorize Docomotion](https://www.docomotion.com/support/authorizing-to-interact-with-salesforce-data/)
- Install Docomotion Designer – [Click here for the instructions](https://www.docomotion.com/support/designer-installation/)
- [Click here](https://www.docomotion.com/wp-content/uploads/2024/01/Account-Summary.zip) to download the ‘Sample Form’ template and save it on your PC.
- [Import the form](https://www.docomotion.com/support/importing-and-exporting-forms/)

**Step 1: Import exam form**

- In Salesforce Docomotion > Form tab click New.
- Click Import.
- Select the form zip file from the local machine.
- The Designer client will import the form into the org and open it to edit.

**Step 2: Adjust the form based on instructions (that appear here and in the form, and may be deleted once implemented)**

- Change the form margins to 1cm.
- Change the tables to adjust to the new margins.
- Add a container to the second paragraph in the annex page with reverse logic of the first container.
- Save the form back to Salesforce using the Upload to Cloud icon.
- Close the Designer client before moving to the next steps.

**Step 3: Adding a field into the Data Model**

- Modifying the Data Model
  - For details of how to create a Data Model see [Defining a Data Model](https://www.docomotion.com/support/create-a-data-model/).
  - From the Form page click on the define data model button.
  - Under the Interactive tab add the Account phone field.
  - Click Save.

**Step 4: Create an Interactive collection**

- In Salesforce > Docomotion click the Interactive Collection tab.
- In the Interactive collection object tab click New.
- Enter a name for the new Collection.
- Click Save.
- Create the Interactive Collection. Add the following elements:
  - Text box for Email address
  - Signature for adding a signature area.
  - For details regarding [Interactive Collections](https://www.docomotion.com/support/interactive-collection/).
- Linking the Interactive Collection to the Form
  - Open the Form in Salesforce and scroll down to the Interactive Related Forms section.
  - Click New Interactive Related Form and select the Interactive Collection you created.
  - Click Save.

**Step 5: Adding Interactive Capabilities to the Form**

- Adding the Interactive Elements to the Form in the Designer
  - When you open the Form in the Designer, you will now see the Interactive Collection Elements in the Data Model pane under the Interactive tab.
  - From the Interactive tab in the Data Model pane, select the interactive elements and insert into the Form.
  - Account phone tag
  - Email Tag
  - Signature tag
  - Submit tag
  - When you finish designing the Form click the Upload to Cloud icon .

**Step 6: Activate the form**

- In order to generate output from the Form you designed, you need to activate the Form.
- After uploading the design from the Designer client, an Activate button will be available in the Form page.
- For details on how to activate a Form, see ‘[Form page](https://www.docomotion.com/support/form-page/)‘.

**Step 7: Generating the interactive Form**

- Select an Account record.
- Click Lightning Generate Document.
- In the Docomotion Generation screen:
  - Select output format: HTML
  - Select the Output Channel: Link.
  - Click Generate.
- You will be redirected to a Signature record containing a client URL, send this URL back to us for review to Certifications@Docomotion.com with the subject line: “Hands-on Exam Submission”.
- For details of how to generate output see [Generating Output](https://www.docomotion.com/support/generate-a-document/).
