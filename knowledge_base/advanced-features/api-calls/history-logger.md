---
title: "History Logger"
source: https://www.docomotion.com/support/advanced-features/api-calls/history-logger/
section: advanced-features
last_modified: 2024-07-22T07:09:07
---

# History Logger

The history Logger allows you to record and save metadata on your document generations.
Data such as: Form Number, Record ID, Channel, Format, Recipient, File ID, and Author.

Our API capabilities allow users to log custom fields using the Mass generation API call or the Single Generation Call.

Methods: [https://www.docomotion.com/support/advanced-features/api-calls/](https://www.docomotion.com/support/advanced-features/api-calls/https://www.docomotion.com/support/advanced-features/api-calls/)

example of an API call with the custom fields to populate:

```

					Integer formId; 
Id sobjectId;
Boolean isActiveVersion;
String fileName;
doco.RenderAPI.Mode aMode;
doco.RenderAPI.Format;
Id whoId;
Id templateId;
String subject;
String addRecipient;
String orgWideAddressId;
String contendDocIds;
Map&lt;String , String&gt; custFieldLog = new Map&lt;String, String&gt;();
custFieldLog.put('doco__CustomField1__c', 'value');
custFieldLog.put('doco__CustomField2__c', 'value');
custFieldLog.put('doco__CustomField3__c', 'value');
custFieldLog.put('doco__CustomField4__c', 'value');
custFieldLog.put('doco__CustomField5__c', 'value');
doco.RenderAPI.rendercreateFile(formId, sobjectId, aMode, format, whoId, fileName, isActiveVersion, templateId, subject, addRecipient, orgWideAddressId, contendDocIds, custFieldLog);


```

Within the “System Settings” menu, you can enable or disable the logger by selecting the corresponding checkbox. Additionally, you can specify the “Logger Type” as one of the following:

- All: Logs every generation
- Mass Generation: Logs only mass generations
- Single Generation: Logs only individual generations

In order to add Logger Tab to the Docomotion application:

Go to ‘Setup’ –> Tabs –> Under ‘Custom Object Tabs’ Press ‘New’ –> Open ‘Object’ Drop Down List –> Choose ‘DocomotionHistory’ –> Choose Some ‘Tag Style’ –> Press ‘Next’ –> On the next Page press ‘Next’ –>  Press ‘Save’

You are all set!
