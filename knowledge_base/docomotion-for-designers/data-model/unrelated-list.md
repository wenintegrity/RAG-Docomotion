---
title: "Unrelated List"
source: https://www.docomotion.com/support/docomotion-for-designers/data-model/unrelated-list/
section: docomotion-for-designers
last_modified: 2025-10-20T08:00:15
---

# Unrelated List

# Unrelated List – Data Model:

The **Unrelated List** feature allows you to add fields and data from Salesforce objects that are not directly related (via a lookup or master-detail relationship) to your main object.

This powerful feature lets you query any object for supplementary information. For example, you could pull in the 5 most recent Opportunities from an Account, even when generating from a Case record. You can filter, sort, and limit the data returned before tagging it in your form.

## Key Capabilities

- **Query Any Object:** Add data from any standard or custom object, regardless of its relationship to the main record.
- **Dynamic Filtering (v21):** Dynamically filter records using the main record’s ID. This allows you to use `Record.Id` in an ‘Equals’ comparison (e.g., `AccountId = Record.Id`).
- **Multiple Relations (v21):** Add the same object multiple times, giving each instance a unique label and its own distinct filter logic.
- **Sort & Limit:** Control the order and number of records returned.

##

## Add an Unrelated Object

1. Open Define Data Model, click the ‘Add Unrelated Object’ button.

   Click the Unrelated Object button in Available Fields.
2. Use the dialog to search and select your object, then click Choose.
3. Select the object you want to add.

   Select the object you want to add.

   Type to find the object; confirm with Choose.
4. Type to find the object; confirm with Choose.

The object appears in Available Fields (Unrelated Mode).

## Choose & Move Fields

1. Expand Fields/Lookups, select what you need, and move them to Selected Fields.

   Move selected fields to Selected Fields.

2. Verify the unrelated object appears under Unrelated Objects List.

Unrelated object listed under Selected Fields.

Info tooltip shows the selected fields on the unrelated object.

3. Hover the info tooltip to see which fields were added.

## Advanced Filtering & Logic (v21)

In v21, you can assign a unique label to each unrelated relation and create multiple filters/logic on the same object.

Choose object & assign a unique label (v21).

Multiple unrelated relations with different labels (v21).

Unrelated Lists shown in the Designer Data Model tree (v21)

## Dynamic Record Context with `Record.Id` (v21)

1. Open the **Query Filter** of the unrelated object.
2. Set a condition where the **Field or Lookup** is an Id path of the form main object(e.g., Account Id) and **Operator** is **Equals**.
3. Click the **Refresh button** next to the value box to insert the dynamic reference.

   Click the refresh icon to auto-insert Record.Id. At generation time, it resolves to the Id of the record you launched from.

When you generate from a specific record, the filter automatically uses that record’s ID.

**Scope**: This option appears only for Unrelated List filters when the field is an Id path for the form main object.

## Examples

### Latest 5 Opportunities for the current Account

- **Generating from**: Account
- **Unrelated Object**: Opportunity
- **Condition**: `AccountId` equals `Record.Id`
- **Sort**: `LastModifiedDate` Descending
- **Limit**: 5

## Notes & Tips

- **Static vs dynamic**: Regular related-list filters compare to hard-coded values; dynamic `Record.Id` is available on Unrelated Lists (Equals).
- **Context**: `Record.Id` resolves only when generation runs from a single record context.
- **Security**: Results respect the running user’s permissions and sharing.
