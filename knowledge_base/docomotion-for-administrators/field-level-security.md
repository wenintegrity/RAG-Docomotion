---
title: "Field-Level Security"
source: https://www.docomotion.com/support/docomotion-for-administrators/field-level-security/
section: docomotion-for-administrators
last_modified: 2025-12-07T07:45:17
---

# Field-Level Security

### Overview

As of **Version 23**, Docomotion introduces enhanced security protocols to handle Field-Level Security (FLS) conflicts. Administrators must now explicitly define how the system behaves when a user attempts to generate a document containing fields they do not have permission to access.

This behavior is managed at two levels:

1. **System Settings:** Sets the default behavior for the entire organization.
2. **Form Level:** Optionally overrides the default behavior for specific forms.

---

### 1. Global Security Mode (System Settings)

The Global Security Mode acts as the default rule for your organization. It determines the system’s reaction when a user lacks access to fields included in a document template

| Mode | Behavior | Best Used When... |
| --- | --- | --- |
| Continue and Leave Restricted Fields Blank (Default) | The system removes the values from restricted fields safely. The document is generated with blanks where the data would have been. | A “best-effort” output is acceptable, and the document is still useful without the restricted data. |
| Warning Before Generation | The user sees a warning dialog listing the specific fields they cannot access. They can choose to proceed (generating with blanks) or cancel. | Administrators want users to be aware of missing data permissions before they generate the file. |
| Block Generation | Generation is completely stopped. An exception is thrown listing the restricted fields referenced in the template. | Missing data is unacceptable for compliance or legal reasons, and the document must not be created incomplete. |

Location: System Settings tab.

### 2. Form-Level Override

You can override the global organization setting for specific forms. This is useful if certain sensitive documents require stricter security (Blocking) while general documents can allow missing fields (Continue).

**Location:** The `Security Mode` field on the Form record.

**Form Options:**

- **Use Admin Definition (Default):** Inherits the mode currently selected in System Settings.
- **Continue / Warning / Block:** Selecting any of these specific options will force the form to use that behavior, ignoring the System Settings.

> **Note on Priority:** A value selected on the Form level **always** takes priority over System Settings.

Location: The Security Mode field on the Form record.

---

### 3. User Experience During Generation

#### 3.1 Generation Window (UI Generation)

When a user generates a document through the Generate Document window, the system will:

- Show a warning dialog if the selected Security Mode requires it.
- Show an error message if generation is blocked and shows unreachable fields.
- Continue quietly if restricted fields are stripped and shows unreachable fields.

#### 3.2 Flow-Based Generation (Automation / Flow)

When documents are generated through a Flow, security feedback cannot appear as pop-up messages. instead:

- Errors or warnings are logged into the **DocomotionHistory**.
- The administrator can review them directly under the record that triggered the generation.

---

### 4. Summary

- **System Settings** define the default security enforcement for all document generations.
- Each form can override this behavior using the **Security Mode** field.
- Form-level definitions always take priority, unless the form is set to **Use Admin Definition**, in which case the global setting applies.
- Warnings and errors appear in the UI when generating manually, or in **DocomotionHistory** when generating from a Flow.
