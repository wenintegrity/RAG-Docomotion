---
title: "Tag Properties and Masking in Data Handling"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/advanced-tag-properties-and-masking-in-data-handling/
section: docomotion-for-designers
last_modified: 2024-01-23T10:55:00
---

# Tag Properties and Masking in Data Handling

After inserting a text data tag into a Form, you can view and modify its properties, including the option to add masking that defines the presentation of the data in the output.

**Configuring a Text Data Tag:** To view and modify tag properties:

1. In the Form Data Tags panel, right-click the data tag and select Properties.
2. Choose the Text tag.
3. Apply a text mask to the data tag, selecting one of the optional mask types.

**Text Masking Types:**

1. **String:**

   - Options: All Upper Case, All Lower Case, Name, Title.
   - Define case usage of words.
2. **Number:**

   - Options: Decimal Point, Separator, Thousands Separator, Negative Value Format.
   - Define the look of a number.
3. **Date:**

   - Options: Calendar Language, Calendar Type, Date Format, Separator.
   - Define the appearance of a date tag.
4. **Date & Time:**

   - Options: Calendar Language, Calendar Type, Time Zone, Date & Time Format, Date Separator.
   - Define the appearance of a date and time tag.
5. **Amount in Words:**

   - Options: Currency Type, Language.
   - Define the look of an amount presented as words.

**Applying a Mask to a Text Data Tag:**

1. Open the Type dropdown menu and select Text.
2. Set the Maximum Length.
3. Select the Masking Type and choose a suitable mask type.
4. Click OK to save the changes.

**Additional Details:**

- The Mask option allows you to define the visual format of the data tag values.
- The Tag Properties window displays masking options, providing examples in the Sample pane.
- String, Number, Date, Date & Time, and Amount in Words masks have specific configurations.

**String Masks:**

- Define case usage of words (using Latin alphabets).
- Options: All Upper Case, All Lower Case, Name, Title.

**Number Masks:**

- Define the look of a number.
- Options: Decimal Point, Separator, Thousands Separator, Negative Value Format.

**Date Masks:**

- Define the appearance of a date tag.
- Options: Calendar Language, Calendar Type, Date Format, Separator.

**Date & Time Masks:**

- Define the appearance of a date and time tag.
- Options: Calendar Language, Calendar Type, Time Zone, Date & Time Format, Date Separator.

**Amount in Words Masks:**

- Define the look of an amount presented as words.
- Options: Currency Type, Language.

- Note: Ensure the data tag in the Salesforce Data Model is of the correct type for Date and Date & Time masks to function correctly.
