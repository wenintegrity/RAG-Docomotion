---
title: "Document Generation via API: Generate Form Document"
source: https://www.docomotion.com/support/connect/generate-via-api/
section: connect
last_modified: 2025-06-01T06:53:03
---

# Document Generation via API: Generate Form Document

## **Overview**

This guide explains how to integrate with Docomotion Connect APIs to programmatically generate documents. We’ll cover synchronous and asynchronous generation, storage options, and Input Forms integration.

### **API Authentication**

Docomotion Connect requires a Salesforce OAuth access token for all API calls.

### **Required Header:**

Authorization: Bearer YOUR\_SALESFORCE\_ACCESS\_TOKEN

Refer to [Salesforce OAuth documentation](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm) for obtaining tokens.

## **API Endpoints**

**Form Generation:**

- POST /services/apexrest/doco/docomotion-connect/forms/generate

**Input Form Generation:**

- POST /services/apexrest/doco/docomotion-connect/input-forms/generate

## **Synchronous Generation (Direct Download)**

Returns a direct download URL immediately.

### **Request Payload Example**

```

					{
  "FormId": 123,
  "FormVersion": 1,
  "Filename": "Policy_Document",
  "Format": "PDF",
  "DataSource": {
    "url": "https://yourapi.com/data/policy/12345",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer your-data-token",
      "Content-Type": "application/xml"
    }
  }
}

```

## **Response**

- **Status:** 200 OK

{

  “success”: true,

  “message”: null,

  “documentURL”: “https://docomotion.com/temp/doc\_abc123.pdf”

}

### **Key Points:**

- **No** **Storage** **object** in synchronous mode.
- XML response must follow defined structure.

## Asynchronous Generation (Cloud Storage)

Use for large documents or cloud storage.

⚠️

#### Requirements:

- Storage object mandatory.
- Include {filename} placeholder in path.
- Authentication token required in
- DataSource headers.
- Request Payload Example (Google Drive)

  Request Payload Example (Google Drive)

### Request Payload Example (Google Drive)

```

					{
  "FormId": 123,
  "FormVersion": 1,
  "Filename": "Policy_Document",
  "Format": "PDF",
  "Storage": {
    "storage_type": "GoogleDrive",
    "path": "/Documents/Policies/{filename}"
  },
  "DataSource": {
    "url": "https://yourapi.com/data/policy/12345",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer your-data-token"
    }
  },
  "Callback": {
    "Url": "https://yourapi.com/webhooks/docomotion-complete",
    "Token": "your-webhook-secret"
  }
}

```

## **Response**

- **Status:** 202 Accepted

{

  “ExpHours”: 72.0,

  “AsyncId”: “a0nJ9000002UAflIAG”

}

### **Callback Webhook**

Upon completion:

{

  “AsyncId”: “a0nJ9000002UAflIAG”,

  “Status”: “Completed”,

  “DocumentUrl”: “https://drive.google.com/file/d/abc123/view”,

  “Message”: null

}

### **Status Values:**

- Completed: Successful generation
- Failed: Document generation issue
- Error: System or processing error

## Input Forms Generation (With Clauses)

⚠️**Critical**:

- ONLY asynchronous mode.
- Requires Storage object.Request Payload

### Request Payload

```

					{
  "FormId": 456,
  "FormVersion": 1,
  "Filename": "Contract_with_Clauses",
  "Format": "PDF",
  "Storage": {
    "storage_type": "GoogleDrive",
    "path": "/Contracts/{filename}"
  },
  "DataSource": {
    "url": "https://yourapi.com/data/contract/789",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer your-data-token"
    }
  },
  "InputForms": [
    {
      "Source": "https://yourapi.com/clauses/standard-terms.docx",
      "Placeholder": "STANDARD_TERMS",
      "PageBreak": true,
      "Order": 1
    }
  ],
  "Callback": {
    "Url": "https://yourapi.com/webhooks/contract-complete",
    "Token": "your-webhook-secret"
  }
}

```

## **Error Handling**

**Common HTTP Status Codes**

- 200 OK: Sync successful
- 202 Accepted: Async initiated
- 400 Bad Request: Invalid request
- 401 Unauthorized: Invalid token
- 500 Internal Server Error: Server error

### **Example Errors**

```

					{

  "success": false,

  "message": "❌ Unsupported format: XLS. Allowed formats: PDF, DOCX."

}

{

  "success": false,

  "message": "❌ Form ID 999 not found."

}

```

### **Environment Configuration**

Securely store configuration:

# Salesforce

SF\_BASE\_URL=https://yourorg.my.salesforce.com

SF\_ACCESS\_TOKEN=your\_access\_token

# Docomotion

DOCOMO\_FORM\_ID=123

DOCOMO\_VERSION=1

# API

API\_BASE\_URL=https://yourapi.com

API\_TOKEN=your\_secure\_token

WEBHOOK\_SECRET=your\_webhook\_secret

### **Security Best Practices**

✅ Use HTTPS for all API calls/data sources
✅ Validate webhook tokens
✅ Store credentials securely
✅ Use temporary URLs for XML data
✅ Implement request timeouts
✅ Never log credentials
✅ Validate file formats

### **Quick Reference**

**Mandatory Payload Elements**

✅ Authorization header
✅ DataSource.headers auth token
✅ {filename} placeholder in storage paths
✅ Storage object for async
✅ Input Forms always async

**Sync vs Async Matrix**

| **Use Case** | **Mode** | **Storage** | **Response** | **Status** |
| --- | --- | --- | --- | --- |
| Small docs, immediate | Sync | ❌ | URL | 200 |
| Large docs, cloud | Async | ✅ | AsyncId | 202 |
| With Input Forms | Async | ✅ | AsyncId | 202 |

**DataSource Methods**

- Supports GET and POST

**Storage Types**

- GoogleDrive, OneDrive, URL

**Supported Formats**

- PDF, DOCX
