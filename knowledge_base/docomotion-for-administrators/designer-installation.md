---
title: "Designer Installation"
source: https://www.docomotion.com/support/docomotion-for-administrators/designer-installation/
section: docomotion-for-administrators
last_modified: 2024-04-17T07:32:39
---

# Designer Installation

The Designer serves as a crucial component within Docomotion, allowing you to seamlessly design, test, and compile forms. With the Designer, you can create new forms, which can be entirely unique or derived from existing forms, making use of pre-existing Word templates. Within the Designer interface, you have the capability to design the structure of forms, test their functionality, and compile them to meet your specific requirements.

- Prerequisites

The required software for the client running the Designer is MS Windows:

- Windows 10 or Windows 11
  - Recommended Windows 10 display settings:
    - Scale and Layout: 100%
    - Resolution: Marked recommended by the operating system/
- MS-Office 64 bit – Verify your version by navigating to File > Account, and selecting ‘About Word’.
- Word 2010 SP2 / Word 2013 SP1, Word 2016, Office 365, Office 2019 Version 1902 (64-bit).
- Microsoft .Net Framework 4.6.1 or above.

### Installation Guide for the Designer

1. Open the ‘Docomotion’ app and navigate to the ‘System Settings’ tab. This will bring up the Docomotion Configuration page.
2. Locate the ‘Download Designer’ section on the page and click on the ‘Download’ button. Note: If you don’t see the ‘Download Designer’ section, ensure that you have completed the initial setup configuration, including setting the region.
3. Click ‘Next,’ and the License Agreement window will appear. Read the terms in the license agreement and select ‘I accept the terms in the license agreement.’
4. Click ‘Next’ again, and the Destination Folder window will appear. Here, you can customize the installation folder and choose the Designer Client UI language from the drop-down list.
5. Click ‘Next’ once more. In the ‘Ready to Install the Program’ window, click ‘Install.’ You can monitor the installation progress in the window.
6. Once the installation is complete, the InstallShield Wizard Completed window will appear. Click ‘Finish’ to close the window.

### Troubleshooting

Should any issues arise during the installation process, please refer to the following steps for troubleshooting:

1. To begin, the Designer can only be accessed from your Salesforce ORG. Press the “Open Designer” button to initiate.

2. Ensure that the Office version is 64-bit (not 32-bit) by opening Word and navigating to File > Account. Then, select About Word to confirm.

3. If necessary, perform a quick Word repair by following the steps provided in this link: <https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b>.

4. Grant full security access to the Docomotion Folder/Properties/Security/Edit/ and mark the “Full control” checkbox.

5. In the C:\Docomotion\Designer Client directory, mark “Run this program as an administrator” for Designer ( Right Click on Designer Client.exe file   Select Properties and Compatibility tab ).

6. If the issue persists, please attach Designer logs to the support ticket. Logs can be found here:  C:\Docomotion\Designer Client\logs
