---
title: "Adding Charts"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-charts/
section: docomotion-for-designers
last_modified: 2024-01-10T08:56:12
---

# Adding Charts

A chart is a graphical representation of data, in which the data is represented by symbols, such as bars in a bar chart, lines in a line chart, or slices in a pie chart. A chart can represent numeric data, functions or some kinds of qualitative structure and provides different info.

Charts are placed into Forms using the chart tag.

A chart image can be automatically generated from the variable data, supplied by the XML file, thereby implementing the business logic on the chart values.

Chart tags are independent of Script tags but can use scripts for data manipulation purposes.

To work with charts, you must first install Microsoft Chart Controls for Microsoft.NET Framework 3.5 (MSCHARTS).

You can add column, line, pie or stacked column type charts, 2 or 3 dimensional, define the resolution (in dpi) of the chart and format each chart type.

It is possible, depending on the chart type, to change the font size, color and font type for X and Y axis, titles, values and description. In some cases it is also possible to change the location or directionality of the text.

### **Column /Line type Chart**

When adding a Line or Column chart the following formatting options are available for the X Axis: it is possible to restrict the number of values displayed on the X-Axis to the number of values that can be clearly displayed on the axis. It is also possible to choose between setting the axis as a Data Tag axis type displaying data tag (runtime) values and Numeric axis type displaying numeric values (with a configurable Start Value and Interval).

The Y-axis values can also be restricted to the number of values that can be clearly displayed on the axis. It is also possible to choose whether to display or hide values on the Chart.

When adding Column or Line Charts you can use more than one data series.

### **Pie Chart**

When creating a Pie chart you use only one data series.

### **Stacked Column Chart**

You can add Stacked Column charts for one or more data series.

### **Adding a Chart to form**

**Defining General Properties for the Chart Tag:**

1. **Chart Placement:**

   - Navigate to the desired location within the document where the chart(s) should be placed.
   - Access the Data Repository panel and double-click the Chart Tag button.

   *Result:* The Chart Properties window will be displayed in the General view.
2. **Basic Information:**

   - Provide essential details for the chart.
     - Enter a Name to identify the chart.
     - Add a Description for further context.
3. **Type and Dimension Selection:**

   - Specify the nature of the chart by selecting options for Type and Dimension.
     - Choose between Two-dimensional or Three-dimensional representation.
4. **Resolution Configuration:**

   - Adjust the chart resolution by selecting from the drop-down list in dots per inch (dpi).
5. **Legend Positioning:**

   - In the Legend area, determine how the legend should be positioned and aligned.
     - Note: Legend positioning is not applicable for Stacked Column charts.
6. **Appearance Tab:**

   - Switch to the Appearance tab to further customize the chart’s visual representation.
   - The content of the Appearance tab varies based on the specific chart type chosen during the initial setup.

**Configuring Chart Appearance:**

*Example: Click “Example” to preview the selected formatting.*

**Column / Line Chart Appearance:**

*To customize the appearance of a Column/Line chart:*

1. Open the Chart Properties window and navigate to the Appearance tab.
2. In the Title > Label field, provide the chart’s name, and choose the font size, style, and color for the label.

**X-Axis Formatting:** 3. Click Axis X; the Axis X elements will be displayed.

4. Enter the Axis X Label Name and select font details for the X label.
5. Choose the Fixed Number of Intervals option for clear X-axis display.
6. Opt for Indexed Values to customize X-axis values based on chart design.
7. Select a Type option for Text on the X-axis:

   - a. Number – Equidistant elements along the X-axis.
   - b. Start Value – Define the starting value along the X-axis (default is 10).
   - c. Interval value – Define intervals between elements along the X-axis (default is 10).
   - d. Data Tag – Design the chart based on input data.
8. Define the text format: Font type, size, style, color, and orientation (rotation angle in degrees).

**Y-Axis Formatting:** 9. Click Axis Y; the Axis Y view will appear.

10. Enter the Y Axis Label Name and select label format details.
11. Choose Fixed Number of Intervals to ensure clear Y-axis display.
12. Select Show Value to display Y-axis values for each chart segment.
13. Define the text format for the Y-axis: Font type, size, style, and color.
14. Click “Example” to preview the selected formatting.

**Pie Chart Appearance:**

*To customize the appearance of a Pie chart:*

1. In the Chart Properties window, switch to the Appearance tab.
2. In the Title – Label field, input the chart name and select font details for the label.
3. Click “Example” to preview the selected formatting.

**Stacked Column Chart Appearance:**

*To customize the appearance of a Stacked Column chart:*

1. In the Chart Properties window, go to the Appearance tab.
2. In the Title – Label field, provide the chart name and select font details for the label.
3. Click Description; the Description Label and Text elements will appear.
4. Enter the required name for the label and select font details for the X label.
5. Select font details for the text.
6. Click Point; the “red” Set buttons will appear.
7. Click Value; the Value view will appear.
8. Enter the value label name and select font details.
9. Choose Fixed Number of Intervals to ensure clear Y-axis display.
10. Select Show Value to display Y-axis values for each chart segment.
11. You can type a string in Append String, which will appear in the output for each chart segment.
12. Define the text format: Font type, size, style, and color.
13. Click “Example” to preview the selected formatting.

**Configuring Data Series:**

*To define Data Series for a chart:*

1. Click the Data tab; the Data-Series view will appear.
2. Adding Series:

   - Enter the series name.
   - To add or remove a series, right-click Series in the left pane.
   - Enter a Legend text and select the legend color.
3. Click Point; the RED Set buttons will appear.

   - After defining scripts, buttons change to GREEN: Edit X Value and Edit Y Value.
   - For “Fixed Interval/Data Tag” in the Appearance tabbed view, both Set X Value and Set Y Value buttons are active.
   - For “Fixed Interval/Number,” only the Set Y Value button is active.
4. If active, click Set X Value/Set Description; the Script Editor: Input Tag “Chart” window will appear.
5. In the Statements panel, double-click SET CHART DATA; the Script Line Editor window will appear.
6. In the Line-SET CHART DATA pane, click Expression, select Operand Type, and specify the Data Tag.
7. Click Save. For detailed Script Editor information, see Adding Scripts – Overview.
8. If active, click Set Y Value/Set Value; the Script Editor: Input Tag “Chart” window will appear. Repeat steps 7-9.
9. Define the font for the Data Label: Set Font type, Font Size, Style, and Text Color.
10. For Stacked Column charts, define the font for the Data Label: Set Font type, Font Size, Style, and Text Color.
