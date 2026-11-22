---
title: "Dynamic and Grouped Tables"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/dynamic-and-grouped-tables/
section: docomotion-for-designers
last_modified: 2026-01-29T08:27:34
---

# Dynamic and Grouped Tables

[Video](https://youtu.be/6HNaS4hJ9LA)

Docomotion enhances your Form capabilities by allowing dynamic tables populated with Salesforce information during output generation. These tables utilize data tags from Objects that are Children Relations of the Form’s Main Object.

**Creating a Data Model for Tables:** To add tables to a Form, ensure the Data Model contains data tags from Children Relations (refer to [Defining a Data Model](https://www.docomotion.com/support/docomotion-for-designers/data-model/create-a-data-model/)). In the Form Designer, these tags appear in the Data Repository Panel under blue T.

**Adding Tables to the Form:** Consider reading ‘[Table Design](https://www.docomotion.com/support/docomotion-for-designers/designing-a-form/table-design/)‘ before adding a table.

*Steps to create a table in a Form:*

1. In the Design panel, click where you want to insert the table.
2. Create a table using Word tools with defined dimensions and appearance.
3. Input necessary information into the cells.
4. Format the table and text using Word tools.
5. In the Title row, type titles suitable for the table tags.
6. In the second row, add Table tags, ensuring dynamic table tags are under blue T.

**Advanced Table Features:** In addition to regular tables, Docomotion supports advanced table features:

1. **Block tables:** Present tables as a list.
2. **Grouped tables:** Group data according to Salesforce records.
3. **Nested tables:** Incorporate tables within tables.

### *Table Blocking – Presenting Tables as a List*

The Table Blocking feature creates a horizontal list format. It allows you to take a table field and add it record after record, in one line, with a separator between records. You can include more than one field in a Table Block to repeat a specific sequence; for example, you can have a repeated list for **First Name Last Name**With the output of : John Smith, Jane Doe, Robert Brown.

#### Step-by-Step Instructions

**Step 1:**
**Enter Placeholder Text**: Enter constant text as a placeholder for the block table in the form. The Table must not wrap the end-of paragraph symbol.  To ensure correct wrapping, it is recommended to write two words (as a placeholder), select only the first word, and then apply the TB (Table Block).
For example: type  Firstname lastname

**Step 2:**
**a.** Select the first word  only (so as to ensure the ENTER symbol is excluded), for example: Firstnamelastname.

b. **Insert Component**: In the Data Repository pane, double-click  **B Table Block.**

Double Click to Select the Table Block

**Step 3:**
**Configure Properties:** In the Table Block Container Properties window, name the block table and set separators.
**Tip**: It is recommended to give the TB a meaningful name. Specify the desired separator in the **Regular Separator** field.

Table Block Container Properties

**Confirm**: Click “OK” to add the Table Block to the Form.

**Step 4:**
**Add Fields**: Select the text entered as a placeholder. Replace it with the fields and text you want repeated, in the desired sequence and formatting. If entering a sequence of fields, you may want to add a space between them.

Add Fields

**Step 5:**

**Apply Logic**: Re-open Table Block Properties window and add any necessary logic, similar to what is done on regular Table rows (blue T). This logic determines which records will be selected or omitted from the list.

**Step 6:**
**Save**: Click “Save”.

### *Table Grouping:*

The Table Grouping feature organizes table data items based on Salesforce records. It supports Table Scripts and Tag scripts, allowing specific row and table visibility adjustments.
*Steps to add a Grouped Table:*

1. Create a table in the Design panel.
2. Select the table and double-click the Group Table icon in the Data Repository Tags panel.
3. Add required table scripts and click OK.

*Nested Tables:* Nested Table Structure allows incorporating a dynamic table cell containing another dynamic table with a different structure. The Data Model needs to be hierarchical with Children Relations of Children relations.
*Steps to add a Nested Table:*

1. Create a table in the Design panel and format it.
2. Select the cell for the nested table and add a new table.
3. Add data tags from the first level to the original table cells.
4. Add data tags from the 2nd level to the nested table.
