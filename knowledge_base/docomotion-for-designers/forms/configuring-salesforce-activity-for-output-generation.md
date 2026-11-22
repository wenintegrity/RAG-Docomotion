---
title: "Configuring Salesforce Activity for Output Generation"
source: https://www.docomotion.com/support/docomotion-for-designers/forms/configuring-salesforce-activity-for-output-generation/
section: docomotion-for-designers
last_modified: 2024-01-10T07:43:17
---

# Configuring Salesforce Activity for Output Generation

Docomotion provides the ability to create a Salesforce activity to track the generation operation when generating output. For standard main objects, this activity is associated with the main object of the form.

For Junction objects, you have the flexibility to route the activity to a higher level, such as a lookup or master-detail relationship.

Starting from Salesforce API version 37.0 and onwards, new standard relation objects, like AccountContactRelation, are supported. Docomotion extends its activity routing selection to include these objects as well.

To configure output generation activity settings, follow these steps:

1. In Docomotion, navigate to the Forms tab and select the desired form; this will take you to the Form page.
2. Scroll down to the “Activity Settings” section.
3. Enable the “Add activity after Generate” checkbox.
4. Enter a name for the activity in the “Activity Subject” textbox.
5. Choose a status for the activity from the “Activity Status” drop-down list.

   Note: You have the option to add custom values to the Task object status field for further flexibility.
6. For Junction and Relation objects, specify a routing option:

   - In a junction object, choose whether to save it in the junction object itself or at a higher level.
   - In relation objects, you need to select one of the parent objects.

After generating output, the related activity list of the object will display the associated activity. Click on the new activity to view its details, and the Comments field will provide tracking information.
