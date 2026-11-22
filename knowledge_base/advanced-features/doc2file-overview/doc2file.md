---
title: "Doc2File Setup"
source: https://www.docomotion.com/support/advanced-features/doc2file-overview/doc2file/
section: advanced-features
last_modified: 2024-01-10T09:06:44
---

# Doc2File Setup

**Adding the Doc2Files Add-in to the MS-Word UI**

To utilize the Doc2Files Docomotion Word add-in, you need to add it to your workstation. Here are the steps for different scenarios:

**Adding to Your Local Workstation:** To integrate the Doc2Files Docomotion Word add-in locally, follow these steps based on your MS-Word version:

1. Open Word Options>Trust Center and click Trust Center Settings…
2. In Trusted Add-in Catalogs, enter the path to the network folder where you located the add-in XML file provided by Docomotion support, and click Add catalog. The Add-in will be available in the SHARED FOLDER tab of the Office Add-ins window.
3. Click Insert to add the Docomotion add-in to My Add-ins.

**Adding to All Users in the Organization (Word 365):** For Word 365 users, system administrators can deploy the add-in via the admin center, making it immediately accessible to all users with no client configuration. Refer to the Publish Office Add-ins using Centralized Deployment via the Office 365 admin center for details. After deployment, the Add-in is available in the ADMIN MANAGED tab of the Office Add-ins window.

**Setting up Doc2Files in Docomotion:** To use the Doc2Files add-in for editing files stored in Salesforce object records, follow these steps:

- Enable the feature in Docomotion System Settings.
- Configure save options.
- Add the Download Files pane to the pages of objects from which you want to download files.

Ensure you have Library Administrator permissions for the Doc2Files library.

**Enabling the Doc2Files Add-in:**

1. Create a new folder for temporary files in Salesforce Files.
2. In the Docomotion main window, go to the System Settings tab.
3. Scroll down to the Doco2File (optional) section.
4. Check Enabled.
5. Enter the name of the folder created for temporary files.
6. Select supported file types.
7. Choose save options: Save as Version, Save as File, and enable Autosave with defined intervals (e.g., every 10 minutes).

**Adding Download Files to the Object Page:**

1. Open the page of the Object with the file(s) you want to edit.
2. In Setup, select Edit Page.
3. Drag and drop the Managed Custom component: DownloadFilesWithExternalName to the Object’s page.
4. Click Save.

**Using Doc2Files:** After deploying the add-in, click Insert > My Add-ins and select the Docomotion add-in to display the File Information floating pane in Word.

**File Information:**

- Details about the file in Salesforce, including file name, creator, and the associated object and record.

**Save Options:**

- Options depend on the organization’s add-in setup:
  - Save as Version: Save the file in Salesforce under the same name.
  - Save as File: Save the file under a new name specified.
  - Auto-save, if configured, saves the file in Salesforce at regular intervals.

**Messages Area:**

- Displays system information messages such as operations performed or errors.

**To Edit a Salesforce Document:**

1. Access the Salesforce record and select the document from the Download Documents pane.
2. Click the Download icon next to the file you want to edit (the file is downloaded to your local workstation).
3. Save the file under the exact name (DO NOT CHANGE THE FILE NAME).
4. Open the file in MS-Word with the Doc2Files Add-in.
5. Edit the document as needed.
6. Save the edited document in PDF or WORD format:
   - Click Save to save in Salesforce under the same file name.
   - Click Save As to select a new file name.

Note: If autosave is configured, the document is automatically saved in Salesforce at regular intervals under its original name. The file is uploaded and saved in Salesforce, either overwriting the existing file or creating a new Salesforce file in the same location.
