---
title: "(Classic) Creating a New Generate Document Button"
source: https://www.docomotion.com/support/docomotion-for-administrators/creating-a-generate-document-button-classic/
section: docomotion-for-administrators
last_modified: 2024-01-12T06:37:38
---

# (Classic) Creating a New Generate Document Button

### Salesforce Lightning – Adding the Lightning Generate Document Button to the Object Layout

In order to generate documents you need to add the new button with **Action Type: Custom Button**(not**Action Type: Quick Action**) to the Layout of the Object designated as the Main Object of the Form.

1. In the Salesforce window, click the gear icon  and go to Setup. Navigate to the Object where you would like to display the button.
2. Go to Page Layout and pick your layout.
3. In the [Object] Layout page, click Mobile and Lightning Actions, select the button, and drag and drop the button to the Salesforce Mobile and Lightning Actions bar.

### Salesforce Classic – Adding the Generate Document Button to the Object Layout

In order to generate documents you need to add the new button to the Layout of the Object designated as the Main Object of the Form.

1. In the Salesforce window, from the dropdown list select Sales and navigate to the Object where you would like to display the button and select a specific Object.
2. Open the slide menu on the right and select Edit Layout.
3. In the [Object] Layout page, select the button, and drag and drop the button to Customs Buttons.

### Mobile – Adding the Generate Document Button to the Object Layout

1. In the Salesforce window, from the dropdown list select **Sales**and navigate to the Object where you would like to display the button and select a specific Object.
2. Open the slide menu on the right and select **Edit Layout.**
3. In the *[Object] Layout* page, click **Mobile and Lightning Actions**, select the button the with **Action Type: Quick Action** (not **Action Type: Custom Button**), and drag and drop the button to the **Salesforce Mobile and Lightning Actions** bar.

### Creating a New Generate Document Button

You can create the Generate Document button to add to any Object.
After creating the button you need to configure the size of the window that opens after the user clicks the button.

The recommended size depends on screen resolution. For a screen resolution of 1280X1024, it is 900 X 700.

Follow the steps:

1. In the Salesforce window, from the dropdown list select Docomotion, and click Setup to display the In Salesforce Setup sidebar.
2. In Salesforce Setup sidebar, in the App Setup area:
3. For Salesforce objects, navigate to: Customize > [Object, i.e. Contacts] > Buttons, Links and Actions.
4. For custom objects navigate to: Create > Objects > [Object, i.e. MyCustomObject] > Buttons, Links and Actions.
5. Click New Button or Link to display the New Button or Link page.
6. In the Label text box assign the button a name (Generate Document), this will be displayed on the Page Layout for the Object.
7. From the Display Type buttons select the Detail Page Button display type.
8. If you want to work with a Console app, from the Behavior drop-down list select: Display in existing window with sidebar.
9. From the Content Source dropdown list select URL.
10. Paste the following text into the text area: /apex/doco\_\_VF02\_GenerateDocument?id={!Object.Id}
11. Replace the (!Object.Id) text with the Object API Name you want to use (i.e. ‘Contact.Id’).

Tip:
To find the API Name of your Object, go to Setup and search “Objects“.
In the Objects page click on your Object, you will then see your Object’s API Name.The URL should look like this:
/apex/doco\_\_VF02\_GenerateDocument?id={!ObjectTest\_\_c.Id}

Docomotion4CPQ Package:
When using the Docomotion4CPQ package replace doco\_\_ with doco4cpq\_\_.

Community Users URL:
Note that community users should use the following URL:
../apex/doco\_\_VF02\_GenerateDocument?id={!ObjectTest\_\_c.Id}

8. Click Save.

**To configure the Generate Document window size:**

1. In the Salesforce window, from the dropdown list select Docomotion, and click Setup to display the In Salesforce Setup sidebar.
2. In Salesforce Setup sidebar, in the App Setup area navigate to: Customize > [Object, i.e. Contacts] > Buttons, Links and Actions.
3. In the Generate Document: Custom Button or Link Detail page click Window Open Properties.
4. In the Window properties area enter the required Width / Height (900X700) and click Save.
