---
title: "Pictures"
source: https://www.docomotion.com/support/docomotion-for-designers/designing-a-form/adding-pictures/
section: docomotion-for-designers
last_modified: 2024-09-02T11:56:05
---

# Pictures

### Adding Pictures

This section refers to regular pictures added to the document during editing, their connection to paragraphs, and their location in the document. For details regarding using picture tags see **[Adding Picture Scripts](https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/adding-pictures-to-a-form/)**.

Select the type of picture and how to add it to the document according to business/design requirements during document setup.

To add the picture to the document select **Insert>Pictures** and choose the picture file.

### Picture Formatting and Text Wrapping

You have the flexibility to customize their appearance through the Format toolbar. This toolbar provides options for adjusting picture size, text layout, and positioning within the document’s object order.

**Text Wrapping:**

Text Wrapping is a crucial feature that allows you to specify the relationship between a picture and the adjoining paragraphs. To set the text wrapping, follow these steps:

1. In Line with Text:

   - The picture becomes part of the paragraph, increasing the row height.
   - Location selection is disabled, as the picture moves with the paragraphs.
2. Behind Text:

   - The picture is placed in a layer behind the connected text.
   - The picture’s location can be changed relative to the paragraph.
3. In Front of Text:

   - The picture is placed in a layer in front of the connected text.
   - Similar to “Behind Text,” the location can be adjusted relative to the paragraph.

**Position:**

The picture’s position is always determined relative to the connected paragraph and based on the selected text wrapping.

Anchor/Connect to Paragraph:

For pictures with text wrapping of “In Front of” or “Behind text,” the position can be freely chosen while remaining connected to the paragraph. Use the anchor to establish this connection:

- Drag the anchor to connect the picture to another paragraph.
- To lock the picture to a specific paragraph, select “Lock anchor” in the Layout dialog.

**Changing Positions:**

For pictures with “In Front of Text” and “Behind Text” text wrapping, you can freely set the position, but it needs to be defined relative to the page, column, and paragraph. This is essential for maintaining the picture’s position in dynamic data documents. Follow these steps:

1. Select the picture.
2. From the right-click menu, choose “Size and Position.”
3. In the Position tab, always select “Absolute Position.”
4. Choose one of the following position options.

   Horizontal> Absolute position to the right of Page, Vertical > Absolute position below Page
   Horizontal> Absolute position to the right of Column, Vertical > Absolute position below Paragraph

*Note*: Other position definitions are not supported.
