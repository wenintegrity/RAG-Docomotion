---
title: "Mandatory Security Updates for Connected Apps and ECAs"
source: https://www.docomotion.com/support/docomotion-for-administrators/connected-apps-and-ecas/
section: docomotion-for-administrators
last_modified: 2026-06-16T08:45:44
---

# Mandatory Security Updates for Connected Apps and ECAs

## Overview

Salesforce is implementing mandatory security updates for Connected Apps and External Client Apps (ECAs) to enhance platform protection. To ensure your document generation services continue to run without interruption, you are requested to conduct the following security update before May, 11th 2026:

**Urgency:** Immediate Action Required
**Impact:** Without this update, critical features like Async Generation and Generate Links will stop functioning.

### For Customers on Docomotion Versions Below 23

#### **Option 1:**

**Update Type:** Upgrading Docomotion and Designer to the latest version.

**Important — Upgrading from a version below v23**

If your organization was running a version below **v23** prior to upgrading to **v24**, please follow these steps:

1. **Upgrade Docomotion and Designer to the latest version** – Install the latest Docomotion package from the Salesforce AppExchange. We also recommend testing the new version in a lower environment before deploying it to production.
2. **Complete the required v23 upgrade steps** – After upgrading to the latest Docomotion version, follow the instructions described in the **“[Upgrading to Version v23](https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/)“** guide – [Link](https://www.docomotion.com/support/docomotion-for-administrators/upgrading-to-version-v23/)
3. **Uninstall the previous Designer version** – Before installing the new Designer version, please uninstall the existing Designer installation from the Windows **Control Panel**. This helps ensure a clean and smooth upgrade process.
4. **Install the latest Designer version** – Open **Docomotion System Settings**, download the latest Designer version.
5. **Authorize the Designer** – From any **Form** page, click **Open Designer** and complete the authorization process when prompted by the login window.

#### Option 2 – For environments with Docomotion version below 23:

**Update Type:** Manual Authorization

To maintain service continuity, you must complete a manual Token Re-Authorization using our secure hosted page.
 **The Authorization Flow:**

**1. Authentication links**: You are required to complete the 2 steps of the authorization process.

**2. Initiate Step 1**:   [Authorization Link for Step 1](https://oapi6.docomotioninc.com/v12/oauth/authorize) – Click on the link and click authorize. (Check “Sandbox” if it is a sandbox)

**3. Complete Step 1:** You will be redirected to the Salesforce login screen. Sign in with your credentials.
Once authenticated, execute step 2.

**4. Initiate Step 2:** [Authorization Link for Step 2](https://salesforce-ir.docomotioninc.com/v12/oauth/authorize) – Repeat the same for Step 2.

**5. Complete Step 2:**  Again, you will be redirected to Salesforce to sign in. Sign in to finalize the handshake.

Once you have completed this process, our backend will automatically generate the necessary Salesforce security tokens.

### For Customers on Docomotion Version 23 and Above

**Update Type:**Designer Upgrade

If you are running version 23 or above, no manual re-authorization is required. Please access your Docomotion System Settings, and download and upgrade the new designer version for all template designers.

**Confirmation:**
Please confirm in a return email that you have conducted the update according to the instructions above.

**Need Assistance?**
If you have questions about your current version or need help with the authorization process, please contact our support team
