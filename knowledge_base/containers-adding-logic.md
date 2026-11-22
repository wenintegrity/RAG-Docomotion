---
title: "Adding Logic To a Form"
source: https://www.docomotion.com/support/containers-adding-logic/
section: 
last_modified: 2026-10-11T07:43:22
---

# Adding Logic To a Form

[Video](https://www.youtube.com/watch?v=o-Q1RoOBpNI)

**Scripts in Docomotion: Enhancing Output Logic**

Scripts in Docomotion play a crucial role in implementing the business logic for generating output during runtime. They facilitate actions based on conditional logic and calculations, eliminating the need for complex programming. Key functionalities of scripts include:

1. **Visual Enhancement:**

   - Change the appearance of a value visually, such as enlarging text for accessibility or color-coding.
2. **Dynamic Text Modification:**

   - Modify text based on conditional changes, insert pictures, or multimedia, e.g., dynamic marketing messages.
3. **Calculations and Functions:**

   - Perform calculations with tag values and apply various logical or mathematical functions like trim, round, or absolute.

Scripts can be applied to Forms and Subforms (Segments). The script logic involves defining conditions and specifying actions based on whether the conditions are met or not. These conditions and actions can be applied to different tag types, including Text, Picture, Barcode, and Multimedia.

### Getting Started with Scripts:

#### 1. Script Editor

- Utilize the Script Editor to create and edit scripts.
- The Script Editor includes panels for statements/actions, an editor panel, data tag name, and save functionality.

#### 2. Script Logic

- Begin script creation by defining conditions and actions.
- Define what happens when the condition is met or not met.
- Conditions and actions are applied to different tag types.

### Script Line Editor:

#### 1. Line If/If Else – Statement

- Design script logic using the Line area with Operand 1, operators, and Operand 2.
- Right-click to add/delete expressions or conditions.

#### 2. Edit Expression

- Enable the Edit Expression area by clicking an expression in the Line area.
- Define conditional logic or values based on script tag changes, expressions, constants, operands, and functions.

#### 3. Operand Types

- Choose from Data Tag, Constant, Function, or Expression as operand types.
- Data Tag: Select from available repository tags.
- Constant: Enter numerical or alphanumeric values.
- Function: Define a function for the operand.
- Expression: Compose a combination of values, constants, operators, and functions.

#### 4. Operators

- Mathematical operators (=, ≠, >, <, ≥, ≤) and logical operators (AND, OR) are available.
- Create logical equations forming the basis of scripts.

**Please note:** Blank fields are not imported into Docomotion forms. Consequently, you cannot compare a field directly to a blank value. To check for empty fields, use IF Xfield <> ‘Empty’. Conditions comparing a blank field against a specific value—such as IF Xfield <> ‘test’—will not evaluate to true or exclude blank fields.

### Script Editor Statement/Actions Trees:

#### 1. Statements:

- Comment: Enter statements describing the intentions of the script.
- If (Condition), Else If (Condition), Else (Condition): Define conditions and alternative actions.

#### 2. Text Actions:

- Value: Set Value (Expression) or Set Symbol.
- Visual: Set Font Attributes, Font Color, Typeface, Weight, Size, Slant, Underline.

#### 3. Other Actions:

- Barcode Script Actions for bar code data tags.
- Multimedia Script Actions for multimedia tags.
- Picture Script Actions for picture data tags.

### Best Practices:

- Familiarize yourself with the Script Editor and Line Editor.
- Utilize the Help pane for explanations of operands and functions.
- Regularly save scripts using the provided tools.

With Docomotion scripts, you can dynamically enhance the behavior and appearance of your generated output without the need for extensive programming.
