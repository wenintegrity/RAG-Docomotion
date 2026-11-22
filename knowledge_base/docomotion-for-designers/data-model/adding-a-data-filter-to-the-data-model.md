---
title: "Adding a Data Filter to the Data Model"
source: https://www.docomotion.com/support/docomotion-for-designers/data-model/adding-a-data-filter-to-the-data-model/
section: docomotion-for-designers
last_modified: 2024-01-10T08:01:13
---

# Adding a Data Filter to the Data Model

You can add to the Data Model filters based on Related Lists included in the Data Model. The records imported from Salesforce, are filtered when generating output, according to the query criteria you define.

This means that the records are filtered before they are imported to Docomotion (alternatively you can add filtering logic to the Form in the Designer during the design stage, which filters the records after they are imported into Docomotion).

### To define a Data Model Filter:

1. Click the ‘Filter’ icon next to the relevant **Related List** to display the **Set Query Filter Criteria** for the selected Related List.

2. In the Conditions area, define a condition or several conditions that will be combined by a defined logic:

- - Select the field or Lookup from the drop-down list
  - Select the operator
  - Select the filter value(s).

3. In the Custom Logic field, customize the logic for the filter conditions that you specified. For example, if you enter 1 AND ( 2 OR 3) this criterion evaluates as true when the first condition is true and either the second or the third condition is true.
4. In the Sort Order area, select the relevant sort order.
5. In the Limit area enter the maximum number of records to retrieve.|

*Note*: This dictates the maximum total records the query retrieves according to the selected order, irrespective of the Fields or Lookup the records were retrieved from. These records are the only records used in the generation of output for any Form based on this Data Model.

6. Click Set Query to display the filtering query in the Result Define Query Conditions pane.

7. Click Save Query Filter. The ‘Filter’ icon next to the Related List turns to blue  which means there is a filter defined for the Related List.
