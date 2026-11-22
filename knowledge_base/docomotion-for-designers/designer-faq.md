---
title: "Designers FAQs"
source: https://www.docomotion.com/support/docomotion-for-designers/designer-faq/
section: docomotion-for-designers
last_modified: 2024-01-12T07:23:59
---

# Designers FAQs

Can I open a previous version of my Form?

You cannot use a previous version of a Form after the Form was Published.
You can discard changes of an Active Form and start editing from the latest published version.

Why does the comma I entered as a separator in a Blocked Table appear in bold?

The separator receives the formatting of the previous text. If the text was in bold the separator will also appear in bold.

####

Why do I see different colors (for text and shapes ) when previewing a Form in the designer and when generating the output?

When using a default color, in some cases the rendering engine will display white color instead of the default blue or black colors (defined in the Word template).
To overcome this behavior, select a specific color instead of using defaults.

Why can I change a segment that I added to the Form in the Designer as linked?

This only happens with pictures and with footnotes. The system enables you to change ***pictures*** and***footnotes***that were added as linked segments (and should not be editable). So if you want to add pictures or footnotes as linked segments make sure you do not change them.

####

I can't see the full screen of the Designer

The full Designer window is not properly displayed at zooms of above 100%. Make sure you are not working in higher zooms.

####

When I click 'Open Designer', nothing happens. What should I do?

Check that the Designer is installed. If not, [install the Designer](https://www.docomotion.com/support/docomotion-for-administrators/designer-installation/).

####

Why does the Properties window in the Designer appear truncated?

To see the Properties window properly you need to set up the Windows display to 100%.
Click **Control Panel > Appearance and Personalization > Display,**select**Smaller – 100% (default)**and click**Apply.**

I'm trying to Export/Import a Form and get an error message

You need to close the Designer process in order to use the Export / Import tool.
Open the Windows Task Manger. locate the Designer Client process and click **End the Process**.

I cannot see the Docomotion Tab

You need a user license in order to use Docomotion (Refer to ‘[Licenses Management](https://www.docomotion.com/support/docomotion-for-administrators/licenses-management/)‘). If you do not have the proper authorization for managing Salesforce licenses, check with your system administrator.

The Designer UI doesn't display properly in Window 10

- For optimal screen display of the Designer:

  1. Right-click the desktop and, from the menu, select **Display Settings**.
  2. **Scale and Layout** is set to 100%.
     (If not, click **Custom Scaling** and set it back to 100% (this requires signing out and then back in).
  3. Make sure your screen resolution is set to the resolution marked **Recommended** by Windows 10).

How can I rename a Form?

To Rename a File in Salesforce Lightning:

1. In Salesforce Lightning, navigate to the Forms tab and open the Form for which you want to change the name.
2. Modify the page URL as follows:
   1. Remove: ‘lightning/r/doco\_\_Form\_\_c/’
   2. Replace: ‘view’  with: ‘e?nooverride=1’
3. This will display the Edit Form page.
4. Ensure that you only modify the Name field.
5. Once you have made the necessary changes, click Save.
