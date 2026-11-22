---
title: "Handling Error Messages"
source: https://www.docomotion.com/support/docomotion-for-administrators/error-messages/
section: docomotion-for-administrators
last_modified: 2025-03-20T07:55:53
---

# Handling Error Messages

## Error Messages

1. **Salesforce System Message – Unable to Access Page**

   - **Subject:** Access Denied
   - **Description:** When generating output from a custom object through the email output channel, you might encounter the following message: “The value of the “p3\_lkid” parameter contains a character that is not allowed or the value exceeds the maximum allowed length. Remove the character from the parameter value or reduce the value length and resubmit. If the error persists, report it to our Customer Support team. Provide the URL of the page you were requesting as well as any other related information.”
   - **How to Fix / Workaround:** Edit the Custom Object and enable the following optional features:
2. **Error -1000**

   - **Subject:** Access Denied
   - **Description:** Docomotion run time error (Authorization problem). Docomotion Runtime engine requires enabling security settings for interacting with Salesforce data.
   - **How to Fix / Workaround:** Provide authorization. In Docomotion, System Settings tab, in the Authorization panel, Click Authorize. For more information, refer to ‘[Authorizing to interact with Salesforce data](https://www.docomotion.com/support/docomotion-for-administrators/authorizing-to-interact-with-salesforce-data/)‘.
3. **Generation output error**

   - **Description:** If you are running a trial version, a possible reason is that the Docomotion package trial has expired. Contact Docomotion to purchase a license.
   - **How to Fix:** Contact Docomotion to purchase a license.
4. **Errors 2005 / 2006**

   - **Subject:** Publish / Activation Failed
   - **Description:** When trying to activate a Form, you get an error message. A possible reason is that you need to allow Docomotion to interact with the session.
   - **How to Fix / Workaround:** Authorize Docomotion to interact with Salesforce data (see Authorize). If the error persists, follow these steps: In Salesforce Setup, navigate to Administer > Security Settings > Session Settings and make sure Lock sessions to the IP address from which they originated and Lock sessions to the domain in which they were first used are not checked. For more information, refer to Configuring Salesforce Session Settings.
5. **Storage limit exceeded**

   - **Subject:** Out of Storage
   - **Description:** You have exceeded your organization storage limitation.
   - **How to Fix / Workaround:** Free up file storage space in your organization. For more information, refer to the FAQ: How do I clean up space?
6. **Error 4001**

   - **Subject:** No Edit Right on Record
   - **Description:** You are trying to generate output using the Notes and Attachments Output Channel but do not have edit rights to the specific record.
   - **How to Fix / Workaround:** Ask your System Administrator to provide you with the required access permissions to the record.
7. **Error 4002**

   - **Subject:** Internal Salesforce Error
   - **Description:** When attempting to generate to ‘Chatter file’ channel.
   - **How to Fix / Workaround:** Verify feed tracking for this object is enabled.
8. **Error 4003**

   - **Subject:** Timeout / Other
   - **Description:** Getting the Output file from the Docomotion Engine has failed.
   - **How to Fix / Workaround:** Try again later. If repeated, contact Docomotion Support.
9. **Error 4409**

   - **Subject:** Cannot open a Form
   - **Description:** A possible reason is that the Notes&Attachments information related to the Form was deleted.
   - **How to Fix/Workaround:** Restore the information from the recycle bin or import from another environment.
10. **Error 4413**

    - **Subject:** Cannot open the Designer
    - **Description:** A possible reason is that you do not have full control of the Docomotion folder (by default located in the C drive).
    - **How to Fix/Workaround:** Ask your system administrator for full control of the folder security properties. If the problem persists try reinstalling the local MS-Office using a Microsoft msi file.
11. **Error 4448**

    - **Subject:** Form cannot be opened
    - **Description:** A possible reason is that the Form files are in use.
    - **How to Fix/Workaround:** In the Task Manager, end the Docomotion Designer process and any WINWORD.exe running process. If the problem persists, try restarting your PC.
12. **Error 8000**

    - **Subject:** Generation Output Error
    - **Description:** You are trying to generate output from a form.
    - **How to Fix / Workaround:** Open and save the form and reactivate/republish it.
13. **Error 9002**

    - **Subject:** Data tag value
    - **Description:** The value in one of the tags mapped to Salesforce data received during generation does not fit the format defined inside the Designer. For example, the Designer masking requires a NUMBER and the value in Salesforce is different from NUMBER (negative number, text, empty, etc.), or the logic includes unpermitted mathematical operations (such as dividing by zero).
    - **How to Fix / Workaround:** Make sure that all tag properties fit the Salesforce format. To deal with empty values, we recommend wrapping the mathematical operations with an IF condition. For example: ‘If ‘Price’ <> EMPTY’.
14. **Error 9120**

    - **Subject:** Barcode value
    - **Description:** The Form includes a barcode tag. During generation, no value exists to fill this tag or the value received is not in the proper format.
    - **How to Fix / Workaround:** Check the value mapped for this tag.

## **Warning Messages :**

1. **Data Model Structure**

- - **Subject:**The Data Model or files structure have been changed.
  - **Description**:

    In some cases, after upgrading to version V21 and v21.6, the **Data Model** may require a quick verification. There is a simple way to check if any action is needed. **This issue has been successfully resolved in version V21.9.**

    ### **How to Verify Your Data Model:**

    1. Go to the **Forms** object in Docomotion.
    2. Click on your form and open **Form Settings**.
    3. Select **Define Data Model**.
    4. Without making any changes, click **Save**.
    5. If you see the following message:

    **Warning:**
    *“The Data Model or files structure have been changed. Please open the Designer, check the Form, and save to Salesforce.”*

    This means the Data Model needs to be repair.

    ### **What to Do Next?**

    If you receive this message after following the steps above, open a ticket at [Docomotion Support](https://support.docomotioninc.com/) and include:

    - **Form ID**

    ### **Important Notes:**

    - If the warning already existed before saving, or if you recently removed a field from the Data Model, this message may appear—but it does not necessarily indicate an issue. It simply means some fields in the form are no longer in the Data Model.
    - **Upgrading to the latest package V21.9 solves this issue when creating a Data Model from scratch**. This means that if you generate a new Data Model, this issue will no longer occur.
