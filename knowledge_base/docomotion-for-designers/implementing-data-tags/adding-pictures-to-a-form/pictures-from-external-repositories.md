---
title: "Pictures from external Repositories"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-pictures-to-a-form/pictures-from-external-repositories/
section: docomotion-for-designers
last_modified: 2026-01-20T06:32:57
---

# Pictures from external Repositories

## Adding Pictures to Salesforce Forms from External Repositories

In Salesforce, you have the capability to include pictures from Salesforce Documents or from Salesforce files. However, it’s important to note that the images need to be stored in an external repository, such as Dropbox, to make them accessible to Docomotion servers.

Procedure:

### **Step 1: Upload Image to Salesforce Object:**

- Add the image URL to an object, like the Product Object, by creating a URL field in the Salesforce Object.
- To add a picture URL to a record in Salesforce Classic:
  - In Documents, click on “New” and select “Picture URL.”
  - Choose the picture file to upload.
  - Check “Externally Available Image” and click “Save” to display the picture.
  - Right-click the picture and copy the image URL.

- Note: When adding an image from Dropbox, ensure to replace "dl=0" at the end of the Dropbox URL with "raw=1."

### **Step 2: Paste URL to Record:**

Paste the copied image URL into the relevant field of the record.

### **Step 3: Data Model Integration:**

Now, you can add these pictures from Salesforce to the Data Model.
