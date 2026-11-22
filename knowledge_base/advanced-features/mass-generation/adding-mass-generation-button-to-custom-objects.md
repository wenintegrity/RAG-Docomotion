---
title: "Adding Mass Generation Button to Custom Objects"
source: https://www.docomotion.com/support/advanced-features/mass-generation/adding-mass-generation-button-to-custom-objects/
section: advanced-features
last_modified: 2024-01-10T09:13:16
---

# Adding Mass Generation Button to Custom Objects

### **Adding the Mass Generation Button to Custom Objects**

Step 1: In Salesforce Lightning go to **Setup>Apex Classes** click **New**

step 2: Define your custom object at the code below and copy it to the Apex Class you just created.

```

					console.log( 'Code is Poetry' );public with sharing class RedirectToGeneration {
    public String message { get; set; }
    public Boolean isSuccess { get; set; }
    public Boolean showMessage { get; set; }
    public List&lt;SObject&gt; objectsList;
    public String objectsIds;

    public RedirectToGeneration(ApexPages.StandardSetController cntlr) {
        message = 'Select one or more Records';
        isSuccess = false;

        objectsList = cntlr.getSelected();
        List&lt;Id&gt; objectIdsList = new List&lt;Id&gt;(new Map&lt;Id, SObject&gt;(objectsList).keySet());
        objectsIds = String.join(objectIdsList, ',');
    }

    public Object redirectToGenerationPage(){
        String previousPageUrl = ApexPages.currentPage().getParameters().get('vfRetURLInSFX');
        Boolean isPrevPageList = previousPageUrl != null ? previousPageUrl.contains('/list?') : false;
        String returnUrl = '/lightning/cmp/doco__documentGenrator?c__recordIds=' + objectsIds + '&amp;c__isPrevPageList=' + isPrevPageList;
        PageReference pgReturnPage = new PageReference(returnUrl);
        pgReturnPage.setRedirect(true);
        return pgReturnPage;
    }
}

```

Step 3: Created a VisualForce Page

```

					&lt;apex:page standardController="Custom_Object__c" recordSetVar="accs" extensions="RedirectToGeneration" action="{!redirectToGenerationPage}"&gt;
    &lt;html xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" rendered="{!showMessage}"&gt; 
        &lt;apex:slds /&gt;
        &lt;div class="slds-scope"&gt;
            &lt;apex:form &gt;
            &lt;/apex:form&gt;
        &lt;/div&gt;
    &lt;/html&gt;
    &lt;script&gt;
        
            
    &lt;/script&gt;
&lt;/apex:page&gt;

```

Step 4: Create the list button and redirect it to the new VisualForce Page.
