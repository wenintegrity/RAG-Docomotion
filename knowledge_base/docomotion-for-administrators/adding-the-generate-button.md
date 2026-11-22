---
title: "Adding the “Lightning Generate Document” Button"
source: https://www.docomotion.com/support/docomotion-for-administrators/adding-the-generate-button/
section: docomotion-for-administrators
last_modified: 2024-01-22T13:07:59
---

# Adding the “Lightning Generate Document” Button

By default, Docomotion installs a “Lightning Generate Document” button for specific Salesforce objects, including Account, Opportunity, Lead, Contact, and Case. You have the flexibility to incorporate this button into the layout of any Salesforce object.

### Adding the Lightning Generate Document Button to the Object Layout

In order to generate documents, you need to add the Lightning Generate Document button to the Layout of the Object designated as the Main Object of the Form.

1. Open **Setup>Objects** Manager and select the Object to which you want to add the Lightning Generate Document button.
2. From the side menu on the left, select **Page Layout**.
3. In the [Object] Layout page, click Mobile and Lightning Actions, select the button, and drag and drop the button to the **Salesforce Mobile and Lightning Actions** bar.
4. Click Save.

### Adding the Generate Document Component to the Object Layout

You can add a document generation component to the object layout from which you can directly generate output.

1. Select the Object to which you want to add the “Lightning Generate Document” component.
2. Right-click ‘Setup‘ and select Edit Page.
3. In the Components pane on the left under Custom-Managed, locate the documentGenerator component.
4. Drag and drop the component to the required location in the object page layout.
5. Select the component to display the component information.
6. Select the Container Type: Small Screen or Large Screen.
7. Enter the required component height.
8. Click Save.

### **Generating output from a Custom Object**

For a custom object, in addition to the previously mentioned steps, follow these additional steps to enable the email output channel:

- - Allow Activities.

If you are using Slaesforce Classic or an old UI, instructions on the “Generate Document” Button can be find [here](https://www.docomotion.com/support/creating-a-new-generate-document-button/)
