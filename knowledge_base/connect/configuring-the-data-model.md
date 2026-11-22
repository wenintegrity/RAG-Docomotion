---
title: "Configuring the Data Model"
source: https://www.docomotion.com/support/connect/configuring-the-data-model/
section: connect
last_modified: 2025-05-14T05:59:05
---

# Configuring the Data Model

Once the form is created, you need to configure its data model by uploading the JSON schema you prepared.

Click on **Define Data Model**. This will take you to the data model configuration screen.

On this screen, you will find a **JSON File Uploader** section. Here, you need to **Upload the JSON Schema** file that defines your external data structure.

After uploading the JSON, you can **map fields if necessary** within the Docomotion interface.

Remember to **Save your changes**.

**Important Re-upload Rules:**

- The main object’s API name (the id of the object with isMain: true) must remain unchanged if you re-upload the JSON schema.
- If fields are already mapped in Docomotion, you are **only allowed to add new fields or objects** when re-uploading an updated JSON schema. You **cannot modify or delete existing fields or objects**.
