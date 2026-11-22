---
title: "Importing and Exporting Forms"
source: https://www.docomotion.com/support/docomotion-for-designers/forms/importing-and-exporting-forms/
section: docomotion-for-designers
last_modified: 2024-01-10T07:44:56
---

# Importing and Exporting Forms

**Importing and Exporting Forms in Docomotion:**

Docomotion provides the capability to export and import published Forms between Salesforce organizations, facilitating the seamless transfer of Form designs and configurations.

**Exporting a Form:**

*Action:* To export a published Form, follow these steps:

1. In Salesforce > Docomotion, navigate to **Forms** and select the published Form for export.
2. On the Form page, click **Export**.
3. The “Save as” window opens. Choose the destination to save the zipped exported file and click **Save**.
4. Monitor the export progress in the bar within the Export Form window.
5. When completed, click **OK** to close the confirmation message.

The exported file is now ready for importing into a new destination organization.

**Importing a Form:**

*Action:* To import a Form into another Salesforce organization, both organizations must share similar Object definitions, including names and fields.

1. In Salesforce > Docomotion, click **Forms**.
2. In the Recent Forms area, click **New** to open the New Form page.
3. Click **Import**.
4. In the Open window, select the zipped file for import and click **Open**.
5. The Import / Export window displays Source Package Information.
6. Click **IMPORT** to proceed with the file import.

*Conflict Resolution:* If conflicts arise with existing entities in the destination organization, the Conflict Found window appears. Choose from the following options:

- **Overwrite:** Update the destination organization’s data based on the data in the zip file. Note: Carefully consider the impact on Data Models and Word Templates.
- **Create New:** Create a new entity based on the data in the zip file.
- **Link:** Use existing destination data instead of the zip file content.
