---
title: "API Calls"
source: https://www.docomotion.com/support/advanced-features/api-calls/
section: advanced-features
last_modified: 2026-08-02T08:42:28
---

# API Calls

### **Generating Output with the Render API**

The Render API facilitates document generation from Docomotion forms directly within Salesforce, bypassing the Docomotion user interface. This guide covers the API’s capabilities, including method functionalities, parameters, and a select number of examples to illustrate use cases.

### **Docomotion Licensing and Render API Usage**

A valid Docomotion license is required for each user generating documents via the Render API. Organizations with a Price Per Action (PPA) license can generate documents without individual user licenses, provided users have the Docomotion Generator permission set. Note: The absence of an error message if document generation fails due to licensing restrictions.

Contact Docomotion support for more licensing details or assistance.

### **Render API Overview**

The Render API offers methods for creating document outputs in various formats and modes, accessible through Apex code within Salesforce where Docomotion is installed, prefixed with **doco.**.

**Key Methods**

- **RenderCreateFile**: Synchronously generates a document, ideal for immediate output requirements.
- **RenderCreateFileAsync**: Asynchronously generates a document, suitable for background processing.
- **RenderBlob**: Produces a BLOB of the document, typically for file downloads.
- **CreateLink**: Generates a single signature object for document personalization.
- **CreateLinks**: Generates multiple signature objects for bulk operations.
- **InsertLinks**: Integrates signatures into the generated document.
- **MassGenerate**: Facilitates bulk document generation asynchronously for multiple records.

Each method serves specific scenarios, from individual document generation to mass output production.

### Mandatory Parameters:

- **formId**: Identifier for the Docomotion form.
- **sobjectId**: Salesforce ID of the main object.
- **mode**: Output mode, such as FILE, ATTACHMENT, or EMAIL.
- **format**: Output format, e.g., PDF, DOCX, HTML.

Additional parameters are listed [here](#parameters)

### RenderCreateFile

Generates a document output synchronously.

**Example:** Generating a PDF attachment for a specific account record.

```

					doco.RenderAPI.renderCreateFile(596, '001j000000IzfyB', doco.RenderAPI.Mode.ATTACHMENT, doco.RenderAPI.Format.PDF);

```

### RenderCreateFileAsync

Facilitates document output generation asynchronously.

- **Usage Note**: Especially useful in Apex Triggers or classes not requiring immediate response.

### RenderBlob

Creates a BLOB from the document output for scenarios like file downloads.

**Example:** Creating a BLOB for a PDF document to attach to a Salesforce record.

```

					Integer formId = 8;
Id sobjectId = '003WV000001FD2oYAG';
Blob newBlob = doco.RenderAPI.renderBlob(formId, sobjectId, doco.RenderAPI.Format.PDF);
System.debug('Blob value is: ' + newBlob);
Attachment attachmentPDF = new Attachment();
attachmentPdf.parentId = sobjectId;
attachmentPdf.name = 'testName' + '.pdf';
attachmentPdf.body = newBlob;//.toPDF(newBlob.toString());
insert attachmentPDF;

```

### CreateLink & CreateLinks

Used to create signature objects that can be inserted into documents. **createLink** generates a single signature object, while **createLinks** is used for multiple signatures.

**Usage Note**: These methods are useful when dealing with documents requiring signatures.

**Syntax Example:**

```

					doco__Signature__c signature = doco.RenderAPI.createLink(formId, sobjectId, whoId, true, true);

```

### InsertLinks

This method is used to insert signatures, created by the createLink or createLinks methods (with toInsert = FALSE) or manually, into generated output.

**Parameters:**

- **signatures**: A list of signature objects to be inserted.

**Syntax Example**:

```

					Boolean result = doco.RenderAPI.insertLinks(signatures);

```

### MassGenerate

Enables asynchronous document generation for multiple records, supporting bulk operations.

**Example:** Generating PDF documents for a set of Account records and emailing them.

```

					Set&lt;Id&gt; accountIds = new Set&lt;Id&gt;{'001...', '002...'}; doco.RenderAPI.massGenerate(formId, accountIds, doco.RenderAPI.Mode.EMAIL, doco.RenderAPI.Format.PDF, false);

```

### Parameters:

- **formId**
  - Type: Integer
  - Description: The Docomotion Id of the Form. (not the SF Id). Either formId or formName is required.
  - Mandatory.
- **formName**
  - Type: String
  - Description: Name of the Form. Either formId or formName is required.
- **SobjectIds**
  - Type: Set
  - Description: Set of the SF Ids of the Main Objects of the Form from which you want to generate output.
  - Mandatory.
- **aMode**
  - Type: Mode (ENUM)
  - Description: The output channel we want to use to generate the output.[See ENUM Mode](#ENUM).
  - Mandatory.
- **format**
  - Type: Format (ENUM)
  - Description: The format of the generated output. [See ENUM Format](#ENUM).
  - Mandatory
- **Combine**
  - Type: Boolean
  - Description: Whether to combine outputs into one output or not. Note: Combing output is only supported for Mode.Document, and Format.PDF or Format.Html.
- **whoIdField**
  - Type: String
  - Description: String that contains the field name to be used as a lookup for contact to which to send the email.
- **TemplateId**
  - Type: Id
  - Description: Id of the email template to be used for sending generated output.

### ENUMs: Mode and Format

The API uses Enums to specify output modes and formats, enhancing consistency and usability.

Mode Examples:

- static doco.RenderAPI.Mode ATTACHMENT
- static doco.RenderAPI.Mode CHATTER
- static doco.RenderAPI.Mode DOCUMENT
- static doco.RenderAPI.Mode EMAIL
- static doco.RenderAPI.Mode EMAILBODY
- static doco.RenderAPI.Mode.FILE
- static doco.RenderAPI.Mode GOOGLE
- static doco.RenderAPI.Mode LINK

Format Examples:

- static doco.RenderAPI.Format BMP
- static doco.RenderAPI.Format DOCX
- static doco.RenderAPI.Format GIF
- static doco.RenderAPI.Format HTML
- static doco.RenderAPI.Format HTML4S
- static doco.RenderAPI.Format JPEG
- static doco.RenderAPI.Format PDF
- static doco.RenderAPI.Format PNG
- static doco.RenderAPI.Format TIF
- static doco.RenderAPI.Format TXT

# Mass Generation API

The Mass Generation API enables asynchronous document generation for multiple Salesforce records.

Using the Callable interface, the API can also be invoked from external Salesforce managed packages without requiring direct access to Docomotion's internal Apex classes.

The following operations are supported:

- **massGenerate:** Generates a separate output for each Salesforce record.
- **massGenerateCombine:** Generates one combined output from multiple Salesforce records.

**Availability:** The examples below require Docomotion package version 24.13 or later.

## Generate and Combine Documents into One Salesforce File

Use `massGenerateCombine` to generate one combined document from multiple Salesforce records.

When `parentObjectId` is provided, the generated document is saved as a Salesforce File and automatically linked to the specified Salesforce record.

### Apex Example

```

					Callable doco = (Callable) Type.forName('doco', 'RenderAPI').newInstance();

Set&lt;Id&gt; policyIds = new Set&lt;Id&gt;{
    'a01XXXXXXXXXXXXXXX',
    'a01YYYYYYYYYYYYYYY'
};

Id parentPolicyId = 'a01XXXXXXXXXXXXXXX';

Object jobId = doco.call(

```

The method returns the Mass Generation job ID.

The generation process is asynchronous. The returned value represents the job and not the generated Salesforce File.

**Important:** When `parentObjectId` is provided, `combine` must be explicitly set to `true`. If `combine` is omitted or set to `false`, the request will fail because a parent record can only be used with a combined output.

## Retrieving the Generated File

The generated File becomes available after the asynchronous generation process has completed.

The process status and generated ContentVersion ID can be retrieved from the Mass Generation Execution record.

### Apex Example

```

					doco__Mass_Generation_Execution__c report = [
    SELECT
        doco__Completed__c,
        doco__Content_Version_Id__c,
        doco__Error_Message__c
    FROM doco__Mass_Generation_Execution__c
    WHERE doco__Job_Id__c = :(Id) jobId
    LIMIT 1
];

if (
    report.doco__Completed__c &amp;amp;&amp;amp;
    String.isNotBlank(report.doco__Content_Version_Id__c)
) {
    Id contentVersionId =
        (Id) report.doco__Content_Version_Id__c;

    // The Salesforce File was generated successfully.
    // When parentObjectId was provided, the corresponding
    // ContentDocumentLink has already been created.
}

if (String.isNotBlank(report.doco__Error_Message__c)) {
    System.debug(
        'Mass Generation error: ' +
        report.doco__Error_Message__c
    );
}

```

Applications should check the execution record in a separate transaction, scheduled process, Queueable Apex job, or another appropriate asynchronous process.

Do not continuously query the execution record within the same transaction.

## Generate Separate Documents for Multiple Records

Use `massGenerate` when a separate output should be generated for every Salesforce record.

Unlike `massGenerateCombine`, this method does not accept `parentObjectId` and does not return a generation job ID.

### Apex Example

```

					Callable doco = (Callable) Type.forName('doco', 'RenderAPI').newInstance();

doco.call(
    'massGenerate',
    new Map&amp;lt;String, Object&amp;gt;{
        'formName'   =&amp;gt; 'Policy Schedule',
        'sobjectIds' =&amp;gt; 'a01XXXXXXXXXXXXXXX,a01YYYYYYYYYYYYYYY',
        'mode'       =&amp;gt; 'ATTACHMENT',
        'format'     =&amp;gt; 'PDF',
        'combine'    =&amp;gt; false,
        'whoIdField' =&amp;gt; 'Primary_Contact__c',
        'templateId' =&amp;gt; templateId
    }
);

```

`massGenerate` always returns `null` because the underlying Mass Generation method does not return a value.

## Supported Parameters

## Supported Parameters

### `formId`

- **Type:** Integer
- **Description:** The Docomotion Form ID. Either `formId` or `formName` must be provided.

### `formName`

- **Type:** String
- **Description:** The name of the published Docomotion Form. Either `formId` or `formName` must be provided.

### `sobjectIds`

- **Supported values:** `Set<Id>`, `List<Id>`, `List<String>`, Comma-separated String
- **Description:** The Salesforce record IDs from which the documents will be generated.
- **Example:**

```

					'sobjectIds' =&amp;gt; new Set&amp;lt;Id&amp;gt;{policyId1, policyId2}

or:
'sobjectIds' =&amp;gt; 'a01XXXXXXXXXXXXXXX,a01YYYYYYYYYYYYYYY'

```

### `mode`

- **Type:** String
- **Description:** The output channel used for generation. Example values include: `FILE`, `ATTACHMENT`, `EMAIL`, `EMAILBODY`, `LINK`.

### `format`

- **Type:** String
- **Description:** The generated document format. Example values include: `PDF`, `DOCX`, `HTML`.

### `combine`

- **Type:** Boolean
- **Description:** Determines whether all generated documents should be combined into one output. Must be `true` when using `parentObjectId`.

### `parentObjectId`

- **Type:** Id or Salesforce record ID represented as a String
- **Supported by:** `massGenerateCombine`
- **Description:** The Salesforce record to which the combined File will be linked. When provided, the combined output is saved as a Salesforce File, and a `ContentDocumentLink` is created between the File and the specified record.

### `whoIdField`

- **Type:** String
- **Description:** The API name of the lookup field used to identify the email recipient. Relevant to output modes such as `EMAIL`, `EMAILBODY`, and `LINK`.

### `templateId`

- **Type:** Id
- **Description:** The Salesforce Email Template ID used when generating an email output.

### `callback`

- **Type:** String
- **Supported by:** `massGenerateCombine`
- **Description:** Reserved for future integration capabilities. No callback action is currently performed.
