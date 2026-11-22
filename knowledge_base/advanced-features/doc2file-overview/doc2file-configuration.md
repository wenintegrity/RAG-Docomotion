---
title: "Doc2File Configuration"
source: https://www.docomotion.com/support/advanced-features/doc2file-overview/doc2file-configuration/
section: advanced-features
last_modified: 2026-01-20T06:40:59
---

# Doc2File Configuration

### **Configuring ‘Doc2File’**

In order to use the Doc2Files add-in that enables editing files relating to Salesforce Objects, you need to enable downloading files and configure the save options for the add-in.

**Enable ‘Download Files:**

1. - In the App Launcher select Docomotion, and click the System Settings tab to display the Docomotion Configuration page.
   - In the ‘Download Files’ section, check **Enable Feature**. This action creates the Doc2FilesTemp library in Salesforce Files, and the configuration options are displayed.

**Save Options Configuration:**

1. - Select Enable saving Doc2Files: This option enables Save as Version in the Doc2Files add-in, saving the file in Salesforce under the same name.
   - Select Enable saving Doc2Files as new Document: This option enables Save as File in the Doc2Files add-in, saving the file in Salesforce under a new name.
   - Choose the file types you want to support (e.g., DOCX, DOC, RTF).
   - Select Show All File Versions if you want the Download Files With External Name pane in the Object’s page to display all document versions.
   - Select Enable Autosave if you want to enable autosave in the add-in. In Auto Save Interval (mins), you can edit the time interval for autosave in minutes (e.g., every 10 minutes).
   - Click Save to save the configuration.
2. **User Permissions:**

   - Provide all users who need to download files with access permissions of Library Administrator for the Doc2Files library (see ‘[Manage Library Membership from Files Home](https://help.salesforce.com/s/articleView?id=sf.collab_files_manage_library_membership.htm&type=5)‘).
