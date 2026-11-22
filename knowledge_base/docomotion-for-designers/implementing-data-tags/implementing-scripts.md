---
title: "Implementing Scripts"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/implementing-scripts/
section: docomotion-for-designers
last_modified: 2026-10-11T07:40:23
---

# Implementing Scripts

[Video](https://www.youtube.com/watch?v=F2DCroBgO58)

Scripts are integral for executing business logic in runtime-generated output. Integrated during form creation or modification, they embed conditions in the Script Editor, enabling dynamic actions with application data and document content. This facilitates complex manipulations without the need for traditional programming, covering visual transformations, dynamic text modifications, calculations with tag values, and application of logical or mathematical functions.

**Key Script Activities:**

1. **Visual Transformation:**

   - Visual changes such as enlarging text for accessibility or color-coding.
   - Dynamic modification of text and insertion of pictures or multimedia based on conditions.
2. **Calculation Operations:**

   - Performing calculations with tag values using logical or mathematical functions (e.g., trim, round, absolute).

**Script Utilization:**

Scripts can be employed in both Forms and Segments, providing versatility in managing various types of content, including Text, Picture, Barcode, and Multimedia.

**Script Logic:**

To create a script, follow these steps:

1. **Define Condition:**

   - Begin script creation by stating a condition (e.g., customer account numbers should be greater than 1000).
2. **Specify Actions:**

   - Define actions for when the condition is met and an alternative action for when it is not.
3. **Additional Logic:**

   - Introduce alternative conditions leading to alternative actions, providing flexibility in script design.

**Editing Scripts:**

Scripts can be edited for various tag types, including Text, Picture, Barcode, and Multimedia.

**Getting Started with Scripts:**

Familiarize yourself with two main windows before adding scripts:

1. **Script Editor Window:**

   - Facilitates script creation and editing, providing panels for statements, actions, and script content.
2. **Script Line Editor:**

   - A tool for writing and editing script lines, enabling precise control over script logic.

**Script Editor Components:**

1. **Script Editor Statement/Actions Trees:**

   - Type-dependent panels for script statements and actions.
2. **Editor Panel Toolbar:**

   - Tools for refining script information in the Editor panel.
3. **Editor Panel:**

   - Space to enter and view the script.
4. **Data Tag Name:**

   - Identifies the relevant data tag.
5. **Save Button:**

   - Click to save the entered script.

**Script Line Editor:**

1. **Line – Statement Area:**

   - Design the script logic using options from the Edit Expression panel.
2. **Edit Expression:**

   - Enables editing expressions and conditions.
3. **Help Pane:**

   - Provides explanations for operands and functions.

**Operand Types:**

- Data Tag: Represents data repository tags.
- Constant: Numeric or alphanumeric values.
- Function: Defines operations on operands.
- Expression: Combinations of values, constants, variables, operators, and functions.

**Operators:**

- Mathematical and logical operators for creating script equations.

**Operand Types:**

- Data Tag: Dropdown menu displaying data repository tags.
- Constant: Input alphanumeric values.
- Function: Defines operations on operands.
- Expression: Combination of values, constants, variables, operators, and functions.

**Operators:**

- Mathematical (e.g., =, >, <) and logical (e.g., AND, OR) operators for script equations.

### **Defining Script Conditions**

Define the condition(s) that must be met in order to enable the script to perform the defined activities.

### **To define conditions:**

1. In the Script Editor Tree, under Statements, double-click **If.**
2. Define the first condition:
   - Click the left side of the equation; **Expression** is highlighted and Operand1 is enabled.
   - Select an **Operand Type** for Operand1. See *; The selected Operand Type appears on the left side of the Line equation.*
   - Click the Operator sign in the Line area and select the **Operator** from the drop-down list.
   - Select an **Operand Type** for Operand 2; the selected Operand Type appears on the right side of the Line equation.

3.  Click **Save**; the condition appears in the Script Editor.

### **Defining Script Actions**

After conditions have been defined, you can define the actions that occur, when the conditions are met.

You can define actions as values (for example a message displayed to a user) or as symbols.

**To create an action for when a condition is met – set value:**

1. Select the condition.
2. In the Script Editor Tree, under ***Actions*** > ***Value***, double-click**Set Value**; the Script Line Editor appears.

**To create an action for when a condition is met – set symbol:**

1. Select the condition.
2. In the Script Editor Tree, under Actions > Value, double-click Set symbol; the Symbol Editor

**Please note:** Blank fields are not imported into Docomotion forms. Consequently, you cannot compare a field directly to a blank value. To check for empty fields, use IF Xfield <> ‘Empty’. Conditions comparing a blank field against a specific value—such as IF Xfield <> ‘test’—will not evaluate to true or exclude blank fields.

[Video](https://www.youtube.com/watch?v=F2DCroBgO58)
