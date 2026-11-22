---
title: "API Specification: Generate Input Form Documents"
source: https://www.docomotion.com/support/connect/generate-input-form-documents/
section: connect
last_modified: 2025-05-29T06:29:24
---

# API Specification: Generate Input Form Documents

To generate a document based on an **input form template** and your data source, you use the **Generate Input Form Documents** API endpoint.

The endpoint is **POST /docomotion-connect/input-forms/generate**.

This endpoint generates a document based on a specified input form template and data source. **This endpoint operates only in asynchronous mode**. Consequently, the `Storage` **field is required** in the request payload.

The response to a successful request provides an `AsyncId` for tracking the generation process.

The **Request Payload** is a JSON object. It is similar to the standard generation payload but includes an `InputForms` array:

**Best Practice:** Validate required business fields before sending the payload to avoid template errors. If using temporary files or presigned URLs, ensure cleanup is handled to prevent storage bloat.

**Security Note:** SSL\_VERIFY\_PEER should only be false in local development. Always verify SSL certificates in production.

Support multiple REST clients by using consistent request examples in Postman, curl, or generic tools like axios or fetch.

```

					{
    "FormId": 354,
    "FormVersion": 1,
    "Filename": "document_1",
    "Format": "PDF",
    "Storage": {
        "storage_type": "GoogleDrive",
        "path": "/docs/form1/{filename}"
    },
    "DataSource": {
        "url": "http://10.30.51.201:4444/api/data/1",
        "method": "POST",
        "headers": {
            "token": "AABBCC"
        }
    },
    "InputForms": [
        {
            "Source": "https://www.cte.iup.edu/cte/Resources/DOCX_TestPage.docx",
            "Placeholder": "PH1",
            "PageBreak": true,
            "Order": 1
        }
    ],
    "Callback": {
        "Url": "https://webhook.site/b0c37002-8b2a-4552-b06e-342e4b88475c",
        "Token": "AABBCC"
    }
}

```

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| **InputForms** | Object | Yes | Details of the input form template, provided as an array of objects. |
| **Filename** | String | No | The desired name for the generated file without the extension (Default: Auto-generated). |
| **Format** | String | Yes | The output format (e.g., **DOCX**, **PDF**). |
| **Storage.storage\_type** | String | Yes | The type of storage (e.g., GoogleDrive, S3). **Required as this endpoint is async only**. |
| **Storage.path** | String | Yes\* | The storage path. Supports the {filename} placeholder. Required. |
| **DataSource.url** | String | Yes | The URL of the external data source API. |
| **DataSource.method** | String | Yes | The HTTP method (e.g., POST, GET) to use when fetching data from the URL. |
| **DataSource.headers** | Object | Yes | Key-value pairs of headers for the data source request. **Requires at least an auth token**. |
| **Callback.Url** | String | No | A webhook URL for async notification when generation is complete. |
| **Callback.Token** | String | No | An authentication token to include in the callback request. |

\* The `Storage.path` is marked Yes\* in the source table, but given the context that Storage is required, it should be considered required when using this endpoint.

## **Responses**

Synchronous mode returns: {documentURL}. Asynchronous mode returns: {AsyncId, ExpHours}. In async flows, either handle the callback or poll the status endpoint using: /status/{AsyncId}. To troubleshoot errors, capture the raw HTTP requests/responses, including timeouts and redirect behavior. Log common issues like 401 Unauthorized, 404 Not Found, or 500 Internal Server Error.

### **Asynchronous Mode Response**

**Status Code:** 202 Accepted

**Body:**

```
{
  "ExpHours": 97.0,
  "AsyncId": "a0nJ9000002UAflIAG"
}
```

**Description:** Returns an AsyncId to track the document generation job and ExpHours indicating how long it is kept.

### **Form Not Found Error**

**Status Code:** 400 Bad Request

**Body:** ❌ Unsupported format: asd. Allowed formats are: PDF, DOCX.

**Description:** Returned when the FormId in InputForms does not match an existing form template.

### **500 Internal Server Error**

**Status Code:** 500 Internal Server Error

**Body:** “Failed to process request due to an unexpected error”

**Description:** Unexpected server-side error during processing.
