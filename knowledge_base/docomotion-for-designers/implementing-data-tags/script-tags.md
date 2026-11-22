---
title: "Script Tag"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/script-tags/
section: docomotion-for-designers
last_modified: 2026-10-11T07:42:36
---

# Script Tag

Script Tags are tags that contain business logic scripts, that are put into operation, during Runtime when generating output, the required business logic.

Script Tags can be added to Forms in the following manner:

- **Scripts can be added to the document directly**. When you add a script to a document it is added as empty.
  A Script tag is represented by an **‘S’** icon. When a Script tag is empty of scripts, a red star is appended to the Script icon.

- **By Data Tag conversion** –Data tags can be converted to Script Tags. The scripts are added as empty.

- When adding table tags it is recommended to add the tag and then use the Data Tag conversion option. This conserves the table hierarchy.

### **To directly add a Script tag to a document:**

1. In the Designer, click the document location for entering the Script Tag.
2. In the **Data Repository Data Tags** panel, double-click **Script** **Tag** ; the Script Tag Properties window appears.
3. You can add script logic now or click **OK** to save the data tag as a script and add the script logic later.

- If you selected an RTA tag you have an option to override the font family and the size of the text by setting a different font or size in the Designer: Select Font Family Set in Designer to override the font Set Font Size Set in Designer to override the font size

When you save the new script tag it appears in the Data Tags/Form pane.

### **To convert a Data tag to a Script tag:**

1.  In the Form Data Tags panel, right-click (or double-click) the required **Data** **Tag** (a data tag that has already been placed into the document) and from the menu, select **Properties**; the Tag Properties window appears.

2.  Select one of the following Tag Type options:

- Text
- Bar Code

To select Multimedia and Picture tags, complete the procedure and then in the new Script tag, access the Script Tag Properties window.

3.  Click the **Convert To Script Tag** button.

4.  You can add script logic now or click **OK** to save the data tag as a script and add the script logic later.

### **Adding Content to a Script**

Before you start adding content to a script prepare the logical groundwork for the script – design the conditions, tag values, and images that comprise the script. For example, define what you want to happen if the condition is not filled.

**Example:**

The following script will be added to a form letter to be sent to the accounts. The script will enable one of two announcements to appear in the form letter.

- **Delivery/Installation Status = “Completed”**: will display the following symbol .”
- **Delivery/Installation Status not “Completed”**: will display the following symbol .

Following is an example of the steps of creating a**text** script. In addition to adding content, you also have the option to define Masking Types and Display Maximum Lengths.

### **Modifying the Appearance of the Action Value**

After defining an action value, you can modify the appearance of the value.

**To customize the visual appearance of an action:**

1. In the Script Editor Tree, double-click an ***Actions****>**Visual*** option (e.g. Font Attributes); the Visual Editor appears (in this scenario, Font Attributes appears).
2. Modify the Visual Editor according to need.
   3.  If necessary, double–click additional ***Action****>**Visual*** options and in the Visual Editor, modify according to need.

### **Defining an Alternative Action**

Define the alternate action or condition that occurs (either as a value or as a symbol), when the conditions are not met (optional action).

**To define an alternative action:**

1. In the Script Editor, select the condition.
2. In the Script Editor Tree, double-click **Else**; the Else line appears in the Script Editor pane.
3. You can do one or more of the following:
   – Double-click **Actions > Value > SET VALUE**; the Line Editor appears. Set the condition. For example: for Operand 1, select Constant, add a message and click **Save**.
   – Double-click **Actions > Value > SET SYMBOL**; the Set Symbol Line Editor appears. Select the symbol and click *OK*.

The additional action(s) appear in the Script Editor.

### **Saving the script**

1. When you have completed the script, click **Save**.
2. In the Script Tag Properties window, click **OK**.

**Please note:** Blank fields are not imported into Docomotion forms. Consequently, you cannot compare a field directly to a blank value. To check for empty fields, use IF Xfield <> ‘Empty’. Conditions comparing a blank field against a specific value—such as IF Xfield <> ‘test’—will not evaluate to true or exclude blank fields.
