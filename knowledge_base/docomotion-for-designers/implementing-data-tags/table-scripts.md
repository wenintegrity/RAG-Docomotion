---
title: "Table Scripts"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/table-scripts/
section: docomotion-for-designers
last_modified: 2026-10-11T08:15:49
---

# Table Scripts

Table Tags in Docomotion include scripts that implement various logic, such as showing or hiding specific table rows, sorting tables, setting row ranges, and adding page breaks. Below are detailed instructions on utilizing these features:

**Please note:** Blank fields are not imported into Docomotion forms. Consequently, you cannot compare a field directly to a blank value. To check for empty fields, use IF Xfield <> ‘Empty’. Conditions comparing a blank field against a specific value—such as IF Xfield <> ‘test’—will not evaluate to true or exclude blank fields.

### **Hide/Show Table Rows (row-level filtering)**

Use a script on a dynamic table to include only the rows that meet your condition at generation time.

1. In the Form pane, right-click the table (blue T) and choose Properties.
2. Click New to open the Script Editor.
3. Add HIDE ROW() as the first statement.
4. Add an If with your row condition, then SHOW ROW().
5. Save the script and click OK in Table Properties.
6. Example – show only items with a positive Total Price:

```

					HIDE ROW()
If (QuoteLineItems/Total Price &gt; 0 )
    SHOW ROW()

```

### **Hide/Show Table Rows in Grouped Table**

The Group Table script is written differently from other scripts.

It may include both a general HIDE ROW/SHOW ROW logic that affects the entire table per each record in the system,
and several individual scripts which refer to specific rows in the table.
The differences between the two types of commands are described below.

1. Right-click the parent Group Table tag (red ‘G’ tag) in the Data Tags/Form pane and select Properties.
2. In the Table Properties window, click New to access the Script Editor.
3. Under GroupTable Actions>Visual (bottom left), select HIDE ROW/SHOW ROW or HIDE GRAPHICAL ROW/SHOW GRAPHICAL ROW based on the requirement.
4. When creating a HIDE ROW/SHOW ROW command, use the same logic as above. The default is to show the row (in this case, ROW refers to the entire table), so start with HIDE ROW, add the IF condition/s, followed with SHOW ROW when the condition is met.
5. When creating a SHOW or HIDE GRAPHICAL ROW command, the structure is different.
   The logic must always have an IF… ELSE structure, starting with an IF condition for which the command is SHOW GRAPHICAL ROW, followed by an ELSE condition and HIDE GRAPHICAL ROW.

   If multiple conditions are needed, enter the Script Line Editor, position the cursor on the operator, right-click the mouse button and select Add Condition, and use AND or OR between the two conditions.

   Use of ELSE IF is not supported for Graphical Rows. If multiple conditions that are dependent on each other and refer to the same graphical row are needed, they should be separated into two individual scripts separated by END.

   Select the row number. For example, IF (Asset ID=1000) SHOW GRAPHICAL ROW (‘1’), or IF (Description=EMPTY) HIDE GRAPHICAL ROW (‘3’).
6. Save the script and click OK in Table Properties.
7. Notes:
   - Each individual script stands on its own and should automatically be separated from the next script with ‘End’.
     The order of the individual scripts doesn’t matter.
   - SET ROWS RANGE (see separate chapter below) must be positioned first in the script, but is executed after the table is sorted, if the SORT TABLE command is used.
   - SHOW ROW and SHOW GRAPHICAL ROW can not be combined in one individual script, they must appear separately.
   - SORT TABLE (see separate chapter below) must always begin at the left margin, and cannot depend on an IF statement. It is executed first, regardless of its place in the script sequence.

### **Sorting Tables**

Docomotion supports sorting dynamic tables at runtime with up to three sorting levels. Here’s how to add a sorting script:

1. 1. In the Form pane, right-click the table (blue T for a regular table or red G for a grouped table) and choose Properties.
   2. In the Table Properties window, click New or Edit to open the Script Editor.
   3. Under Table Actions/Visual, double-click SORT TABLE.
   4. In the Sort Table window, select the data tag for sorting, type (text, Number, or date), and sorting direction (Ascending or Descending). You can add two more sorting levels.
   5. Save the script and click OK in Table Properties.

### **Setting a Row Range**

Row Range limits the number of Salesforce rows being rendered in the table output.
Only the rows within the range will be printed; all other rows from the data source are suppressed.
Indexing is 1-based (the first data row is 1) and the range follows the table’s current sort order (if you sorted the data, the “first” row means the first after sorting).

**Examples**
1 → render only the first row from Salesforce.
1–3 → render rows 1 through 3 (inclusive).

Define the output rows for a Salesforce table using a script:

1. 1. In the Form pane, right-click the table (blue T) and choose Properties.
   2. In the Table Properties window, click New to open the Script Editor
   3. Double click the SET ROWS RANGE
   4. Set the range according to your needs
   5. Save the script and click OK in Table Properties.

### **Adding Page Breaks**

Scripts can be created to add page breaks in the output for a dynamic table. Here’s how:

1. 1. In the Form pane, right-click the table (blue T) and choose Properties.
   2. In the Table Properties window, click New to open the Script Editor.
   3. Under Table Actions/Behavior, click INSERT PAGE BREAK.
   4. Save the script and click OK in Table Properties.

### **Adding Page Breaks in Grouped Table**

For grouped tables, scripts can be used to add page breaks. Follow these steps:

1. Right-click the **first** Table tag (blue ‘T’ tag under the ‘G’ Group Table tag) in the Data Tags/Form pane and select Properties.
2. In the Table Properties window, click New to access the Script Editor.
3. Under Table Actions/Behavior, select INSERT PAGE BREAK BEFORE or INSERT PAGE BREAK AFTER.
4. Save the script and click OK in Table Properties.
