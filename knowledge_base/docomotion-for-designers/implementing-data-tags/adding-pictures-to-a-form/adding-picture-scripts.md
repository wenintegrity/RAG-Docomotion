---
title: "Adding Picture Script Tags to Forms"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-pictures-to-a-form/adding-picture-scripts/
section: docomotion-for-designers
last_modified: 2024-01-10T16:34:08
---

# Adding Picture Script Tags to Forms

### Adding Picture Script Tags to Forms

Introduction:

In Docomotion, you have the ability to enhance forms by dynamically incorporating images through Picture Script Tags.

- For detailed information on using scripts see ['Adding Scripts'](https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/implementing-scripts/).

- You can also add a picture tag as a picture script directly: right-click the tag in the Data Model panel and select **Insert Tag as >Picture**. The Picture script is added with picture dimensions according to design dimensions.

**Procedure:**

To add a Picture Script, follow these steps:

1. **Add a data-tag:**

   - Click on the location in the form where you want to insert the picture(s).
   - In the Data Repository panel, double-click the Script Tag button.
2. **Script Tag Properties:**

   - The Script Tag Properties window will appear.
   - Enter a Tag Name.
   - From the Tag Type drop-down, select Picture to reveal the Picture Options panel.
3. **Picture Dimensions:**

   - Choose a Picture Dimensions option based on your requirements:
     - Display according to design dimensions.
     - Increase size proportionally.
     - Display according to source dimensions.
     - Increase/Decrease size proportionally.

   Note: “Display according to design dimensions” and “Increase size proportionally” are available only if the picture tag is the sole object in the paragraph and is outside tables or forms.
4. **Additional Options:**

   - If you select “Increase size proportionately,” consider checking “Omit if not Enough Space in Current Page” in the White space management area.
   - Enable Hyperlink if you want the picture to act as a link to a web address.

     Note: When you select Hyperlink the Value: SET ADDRESS will be displayed in the Script Editor, enabling you to add a web address when editing the script.
5. **Script Editing:**

   - Click New to open the Script Editor.
   - Add a Comment to provide context for the picture script.
6. **Define Conditions:**

   - In the Script Editor Tree, under Statements, double-click “If” to define conditions.
   - Add the picture(s) to the script when the conditions are met.
7. **Alternative Options:**

   - Optionally, define an alternative picture or condition that applies when the main condition is not met.
8. **Saving and Conversion:**

   - Save the script when complete.
   - Click OK in the Script Tag Properties window to convert the script tag into a picture tag.
9. **Testing:**

   - Test preview the form to ensure the script produces the desired results.

Adding Pictures to the Script:

There are two ways to script the “Met” or “Not Met” conditions:

1. **Setting the picture path as a constant:**

   - In the Script Editor pane, select the “If” statement.
   - Under PictureDataTag Actions Visual, double-click “Insert Picture” and choose the Constant option.
2. **Setting the picture path into a specific Data tag:**

   - Enter the data tag into the form.
   - Convert the data tag to a script tag.
   - In the Script Editor, define conditions.
   - Under PictureDataTag Actions, click “INSERT PICTURE” and select the Data Tag option.

### To set the picture path as a constant:

1. In the Script Editor pane, select the condition (“If” statement).
2. In the Script Editor Tree, under PictureDataTag Actions Visual, double-click Insert Picture; the Script Line Editor appears in the Line-INSERT PICTURE view.
3. Select the Constant option and in the Operand 1 field, enter the picture path and image name; the path appears in the Script Editor pane.

### To set the picture path directly into a specific Data tag:

1. Enter the data tag into the form.
2. In the Data Tags/Form panel, right-click the new image tag and select Properties; the Tag Properties window appears.
3. Click Convert To Script Tag and OK; the data tag is converted to an empty script tag IScript Empty .
4. Right-click the new Script tag and select Properties; the Script Tag Properties window reappears.
5. For Tag Type panel, from the drop-down menu, select Picture.
6. In the Script panel, click New; the Script Editor.
7. In the Script Tree, under Statements, click If; the Script Line Editor appears.
8. Enter the conditions for which the picture appears in the Form.
9. In the Script Tree, under PictureDataTag Actions, click INSERT PICTURE, the Script Line Editor appears in the Line-INSERT PICTURE view.
10. Activate the Operand 1, select the Data Tag option and in the Operand 1 field, select the picture path data tag.
11. Click Save; the image path data tag appears in the Script Editor.
