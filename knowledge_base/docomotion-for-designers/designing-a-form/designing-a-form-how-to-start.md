---
title: "Designing a Form – How To Start"
source: https://www.docomotion.com/support/docomotion-for-designers/designing-a-form/designing-a-form-how-to-start/
section: docomotion-for-designers
last_modified: 2025-02-27T14:35:58
---

# Designing a Form – How To Start

[Video](https://youtu.be/EYMT_RKmGRg)

#### Jumpstart your document generation with our collection of pre-built forms: [View Ready-to-Use Templates](https://www.docomotion.com/support/docomotion-for-administrators/quickstart-templates/)

**Best Practices:**

1. Show the Paragraph marks for the advanced layout tasks (Home > Paragraph > Show Marks)
2. Enable ‘Ruler’ to show rulers next to your form
3. Define the Margins to 1cm margin. (Navigate to Layout > Page Setup>Margin )
4. Set ‘Paragraph Spacing’ to zero (Navigate to Style>Normal>Format ) Set ‘Spacing after’ to ‘0’, and ‘Line spacing’ to ‘Single’.

### **Headers and Footers:**

Avoid adding fields in the header/footer when using the Live Editor, as Salesforce fields won’t display in the footer/header in both the Live Editor and edited output.

To add a header or footer, double-click the top of the page, opening the Header & Footer Tools > Design tab in the toolbar. Add design elements like a logo and page numbering. To return to the form’s body, click Close Header and Footer or double-click the body of the form.

**Different First Page:**
In the Design tab of Header & Footer Tools, select Different First Page to customize the header/footer of the first page in each section, useful for introductory pages.

### **Page Break/Section Break:**

Two ways of breaking text are supported:

**Page Break:** Starts a new page with the same header and footer. Use Layouts > Breaks > Page, Insert > Page Break, or Ctrl + Enter.

**Section Break Next Page:** Starts a new page and a new section with different properties. Use Layout > Section Break > Next Page. To delete this break, select it with paragraph marks before and after, and click Delete.

**Headers/Footers with Section Break Next Page:**
This break type allows unique headers/footers for specific sections. By default, the new section’s header/footer is connected to the sections before and after. To disconnect, enter the header/footer area and deselect Link to Previous. Note: This option is not available when generating HTML forms.
