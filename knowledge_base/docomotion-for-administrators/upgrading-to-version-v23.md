---
title: "Docomotion Pre-Configuration & Upgrade Guide (Version 23)"
source: https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/
section: docomotion-for-administrators
last_modified: 2026-09-14T06:01:24
---

# Docomotion Pre-Configuration & Upgrade Guide (Version 23)

## Important: Best Practices & Upgrade Strategy

To ensure a seamless transition to Version 23, please adhere to the following recommendations:

- Customers upgrading to version 23 must switch from the legacy Generate window to the new Generate window.
  This requires adding the new **Generate** button to your Salesforce **Page Layout**, as the legacy button will be migrated and is no longer intended for use.
  Please note:

  - The **data model can remain Legacy**. There is no requirement to migrate your data model.
  - **All existing forms will continue to work as before**.
  - Forms that previously used the legacy Generate button will now be generated using the **new Generate button**, with no functional impact.

  Instructions for adding the new Generate button to your Page Layout are available here:
  <https://www.docomotion.com/support/docomotion-for-administrators/adding-the-generate-button/>
  We recommend completing this update as part of your version 23 upgrade process to ensure a smooth and supported generation experience.
- **Sandbox First:** As with all releases, please perform the upgrade on your **Sandbox environment** first. This allows you to validate your specific use cases and configurations before deploying to Production.
- **Pre-Upgrade Preparation:** We strongly recommend completing the **Permission Set creation and assignment** in your current environment *before* installing the new package. Doing this prior to the upgrade ensures that your users maintain uninterrupted access immediately after installation.

## **Introduction**

In Version 23, Docomotion completes a significant security upgrade to align with Salesforce’s highest compliance standards. To achieve this, we have transitioned from legacy authentication methods to a **Connected App** model.

**Why this upgrade is necessary:** Historically, many integrations used persistent sessions that, while convenient, lacked the deep visibility required by modern enterprise security. In v23, the Connected App acts as a metadata framework and secure gateway for all interactions.

By utilizing strictly managed **OAuth flows**, external components—such as the Docomotion Designer—now authenticate using secure, revocable credentials. This architectural pivot provides your organization with granular control over access and a significantly safer risk profile.

## **Preparation for Installation or Upgrade to V23**

If you are **upgrading from an earlier version (below v23)**, it is strongly recommended to **complete the first part of this guide – creating the Permission Set and assigning all relevant users – in your current (pre-upgraded) environment**.

This preparation will save time during the upgrade process and ensure that user access is already configured once Version 23 is installed.

**Step-by-Step Configuration**

1. **Create a Permission Set for Docomotion**

1. Go to **Setup → Permission Sets**.
2. Click **New**.
3. Enter a recognizable name, such as:
   → **Docomotion Auth**.
4. Save the new Permission Set.
5. Assign the relevant permissions according to your organization’s security policy.
6. Add all users who should have access to Docomotion.

Access Permission Set

New Permission Set

Enter New Permission Set

Manage Assignments

Add Assignment

### **Step 2: Upgrade and Configure the Docomotion Connected App**

1. Upgrade to latest Docomotion V23 Package: **https://appexchange.salesforce.com/appxListingDetail?listingId=a0N30000000pvVBEAY**
2. In **Setup → App Manager**, locate **Docomotion System Integration**.
3. Click **Manage**, then **Edit Policies**.
4. Under **Permitted Users**, select
   → **Admin approved users are pre-authorized**.
5. Click **Save**.
6. Scroll down to **Manage Permission Sets**.
7. Assign the **Docomotion Auth** Permission Set you created earlier.
8. Click **Save**.

### **Step 3:** **Configure Default Integration Settings**

1. Open the **App Launcher** (grid icon in Salesforce), search for **Docomotion**, and select **System Settings** .
2. Navigate to **Default Integration Settings**.
3. Click **Refresh User List**.
4. Choose the **Default Integration User**.
5. **Click** **‘Refresh Integration Settings****‘.**
6. Click **Save.**

### **Step 4: Re –** **Install  ‘Designer Client’**

1. Navigate to the ‘System Settings’ tab.
2. Locate the ‘Download Designer’ section on the page and click on the ‘Download’ button.
3. Click ‘Next,’ and the License Agreement window will appear. Read the terms in the license agreement and select ‘I accept the terms in the license agreement.’
4. Click ‘Next’ again, and the Destination Folder window will appear.
5. Click ‘Next’ once more. In the ‘Ready to Install the Program’ window, click ‘Install.’ .
6. Once the installation is complete, the InstallShield Wizard Completed window will appear. Click ‘Finish’ to close the window

## **Designer Authorization**

Every time you open the **Docomotion Designer**, an **authorization process** is required.
This validates your Salesforce access token through the Connected App.

If the **refresh token** is no longer valid (for example, after a session timeout or Salesforce policy update), you will need to **re-authorize** before accessing the Designer again.

1. When prompted, click **Yes** to reauthorize the connection.
2. The Designer will open automatically after authorization.

Authorization Message

To **extend or shorten** the refresh token validity period, contact your **Salesforce Administrator**, who can update token expiration settings in the Connected App configuration.

### Verification

✅ All configuration steps are now complete.
✅ Docomotion is securely connected through the Salesforce Connected App.
✅ You are ready to use Version 23.
