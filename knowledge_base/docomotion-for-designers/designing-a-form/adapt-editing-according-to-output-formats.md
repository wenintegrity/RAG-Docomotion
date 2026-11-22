---
title: "Adapt Editing According to Output Formats"
source: https://www.docomotion.com/support/docomotion-for-designers/designing-a-form/adapt-editing-according-to-output-formats/
section: docomotion-for-designers
last_modified: 2024-01-10T08:46:37
---

# Adapt Editing According to Output Formats

### **Adapt Editing According to Output Formats**

To achieve optimal results, tailor your editing approach to the generated output format. Editing should adhere to the strictest format rules to ensure compatibility with less strict formats.

**PDF and DOCX Formats:**

- More lenient formats based on page structures.
- Allow control of visual presentation on each page, including the use of floating elements.

**HTML and HTML MAIL BODY Formats:**

- Stricter formats based on a cellular/tabular structure.
- HTML MAIL BODY is stricter than HTML.
- Text is presented as a single long page; page-based components like Pages are not available.

**HTML Format:**

- Recommend using tables (transparent/borderless) for control and placement.
- Tables allow control of elements’ location but have limited text alignment.
- Tables are essential, and their width should adhere to the workspace width (page width minus margins).
- Use Spacing Before/After for line spacing.
- Any font size is acceptable, but the minimal line height is 8 pts.
- Use two-column tables for numbered lists to control space between number and text.

*Example:*

- Leveled numbering can be achieved by creating columns for each level within tables.

**Headers and Footers:**

- Can be used, especially for PDF/DOCX generation with different first pages.
- Note that only the header/footer of the first page appears in the HTML generated output.
- Headers appear once at the beginning, and footers appear once at the end of the HTML output.

**Page Breaks:**

- Not relevant to HTML format but significant for other generated formats.
- Page breaks create a larger space in HTML; in PDF/DOCX, they generate a new page.
- Avoid using section breaks.

**Pictures:**

- Use pictures with “In line with text” layout.
- Avoid “Behind/In front of text” as it is challenging to position in the output.
- Shapes are not recommended; if necessary, use “In line with text” layout.

**HTML Mail Body Format:**

- Strictest format, similar to HTML with additional rules.
- Based on tables and cells, use tables (transparent/borderless).
- Align all tables to the center.
- Avoid cell merging; use a single table for setting up the screen, or multiple tables as needed.
- The width of the table determines the displayed output width, within the workspace area.
- Recommended width is 19 cm.
- Do not use headers, footers, or page breaks.
- Avoid using shapes.

**Pictures (HTML Mail Body):**

- Linked pictures must be from an external source, accessible to all.
- Add pictures to the document as a picture script.
- Linked pictures should be in the exact size they will be added to the document.
- Maintain a 96 DPI resolution (not saved for the web).
- The size of the picture should not exceed the size of the cell it is added to.
