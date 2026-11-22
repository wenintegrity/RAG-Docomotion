---
title: "Docomotion RenderAPI – Integration Guide"
source: https://www.docomotion.com/support/advanced-features/api-calls-copy/
section: advanced-features
last_modified: 2026-05-25T08:55:43
---

# Docomotion RenderAPI – Integration Guide

# Docomotion RenderAPI – Integration Guide

Global Methods Reference

## Overview

This guide describes the available global methods exposed by the **Docomotion RenderAPI**. These methods enable external systems and Salesforce implementations to manage document signature processes programmatically.

The following global method is supported:

- `createLinks(String jsonStr)` – Generate signature links

This method is designed for seamless use in Apex, external integrations, or low-code automation tools such as Salesforce Flow Builder.

## 1. createLinks(String jsonStr)

### Purpose

Creates one or more signature links based on a structured JSON payload.

### Method Signature

```
global static List<Signature__c> createLinks(String jsonStr)
```

### Input Requirements

The method expects a valid, structured JSON string containing the required parameters.

#### Mandatory Fields

| Parameter | Type | Description |
| --- | --- | --- |
| `sobjectId` | Id | The Salesforce record ID that the document/signature process is related to. |
| `formId` *OR* `formName` | Integer / String | Identifies the form/template used to generate the document. |

**Crucial Validation:** If any required field is missing or invalid, the method will throw a `Utils.CustomException`.

### Supported Parameters (Detailed Explanation)

#### Core Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `formId` | Integer | Optional\* | Numeric ID of the form template. |
| `formName` | String | Optional\* | Alternative to `formId` (Developer Name of the form). |
| `sobjectId` | Id | Yes | Salesforce record to be used for document generation context. |

*\* Note: One of either `formId` or `formName` must be provided.*

#### Behavior Configuration

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chatter` | Boolean | `false` | If `true`, posts the generated document directly to the record's Salesforce Chatter feed. |
| `toInsert` | Boolean | `true` | Controls whether signature records are automatically inserted into Salesforce database or returned in-memory only. |
| `fileName` | String | — | Applies a custom name to the generated document file. |
| `isActivatedVersion` | Boolean | `false` | Determines whether to explicitly use the currently activated version of the form. |

#### Recipient Handling (Multi-Sign Logic)

| Parameter | Type | Description |
| --- | --- | --- |
| `recipientDetails` | String | Defines recipients for multi-step signing processes. Behavior dynamically depends on the form configuration type:   - **Multi-step + Related List Forms:** Provide comma-separated Salesforce record IDs.    *Example:* `"recipientDetails": "a01XXX,a02XXX,a03XXX"` - **Multi-step + Non-related Forms:** Provide comma-separated email addresses. The quantity must match the number of steps exactly.    *Example:* `"recipientDetails": "user1@example.com,user2@example.com"` |

#### Important Validation Rules for Recipients:

- If `recipientDetails` is provided for a non-multi-step form, an error is thrown.
- For related-list forms, all values within the string must be valid Salesforce record IDs.
- For non-related forms, the number of emails provided must match the defined signing steps exactly.

#### Additional Metadata Fields

These optional fields map and store data directly on custom fields within the `Signature__c` object for custom tracking:

| Parameter | Maps To Field | Description |
| --- | --- | --- |
| `additionalInfo1` | `Additional_Info_1__c` | Custom business metadata (e.g., `"Region: EMEA"`) |
| `additionalInfo2` | `Additional_Info_2__c` | Custom business metadata (e.g., `"Channel: Partner"`) |
| `additionalInfo3` | `Additional_Info_3__c` | Custom business metadata (e.g., `"Priority: High"`) |

### Return Value

Returns: `List<Signature__c>`

- If `toInsert = true`: Records are successfully committed to the database and returned with IDs.
- If `toInsert = false`: Records are returned transiently in memory only.

## Example JSON Payload

```

					{

  "formId": 101,

  "sobjectId": "001XXXXXXXXXXXXXXX",

  "chatter": false,

  "toInsert": true,

  "fileName": "Contract Package",

  "isActivatedVersion": true,

  "recipientDetails": "step1@example.com,step2@example.com",

  "additionalInfo1": "Region: EMEA",

  "additionalInfo2": "Channel: Partner",

  "additionalInfo3": "Priority: High"

}

```

## Example Apex Usage

```

					String payload = JSON.serialize(new Map&lt;String, Object&gt;{

	'formId' =&gt; 101,

	'sobjectId' =&gt; '001XXXXXXXXXXXXXXX'

});

 

List&lt;Signature__c&gt; signatures = RenderAPI.createLinks(payload);

System.debug('Created signatures: ' + signatures.size());

```

## 2. cancelMSprocess(String msSignatureId)

### Purpose

Cancels an active, existing Multi-Sign process and securely updates its status.

### Method Signature

```
global static Boolean cancelMSprocess(String msSignatureId)
```

### Input Requirements

| Parameter | Type | Description |
| --- | --- | --- |
| `msSignatureId` | String | The unique ID of the target Multi-Sign process (`MsSignature__c` record). |

#### Validation Rules

The input must fulfill all conditions below, otherwise a `Utils.CustomException` is thrown:

- Value must not be null or empty.
- Must follow a valid Salesforce ID format structure.
- Must explicitly belong to the `MsSignature__c` object type.

### Behavior

- Invokes the internal backend logic: `SignatureService.cancelMsSignature(msSignatureId)`
- Updates the record status target field: `Status__c = 'cancelled'`
- Commits and saves changes back to Salesforce.

### Return Value

Returns: `Boolean` (`true` when the cancellation completes successfully).

### Example Usage

```
Boolean ok = RenderAPI.cancelMSprocess('a1BXXXXXXXXXXXXXXX');
System.debug('Cancel result successful: ' + ok);
```

## 3. reactivateMSprocess(String msSignatureId)

### Purpose

Reactivates a previously cancelled Multi-Sign process and completely regenerates the document signing links.

### Method Signature

```
global static Boolean reactivateMSprocess(String msSignatureId)
```

### Input Requirements

Maintains identical validation constraints as `cancelMSprocess`:

- Must be a valid, existing `MsSignature__c` Salesforce ID.
- Must not be null or empty.

### Behavior

- Triggers the core backend link regeneration: `SignatureService.reactivateLinksByMsId((Id)msSignatureId)`
- Regenerates all necessary signing links.

**Note:** This method focuses on process regeneration logic and does not explicitly update the `Status__c` tracking field.

### Return Value

Returns: `Boolean` (`true` when reactivation completes successfully).

### Example Usage

```
Boolean ok = RenderAPI.reactivateMSprocess('a1BXXXXXXXXXXXXXXX');
System.debug('Reactivate result successful: ' + ok);
```

## Global Error Handling Recommendation

For all methods, it is highly recommended to wrap execution logic calls within a robust `try/catch` block to handle potential processing interruptions gracefully:

- Invalid or malformed inputs
- Backend downstream service failures
- Salesforce validation errors

```
try {
    Boolean cancelled = RenderAPI.cancelMSprocess(msId);
} catch (Exception e) {
    System.debug('RenderAPI call failed gracefully: ' + e.getMessage());
}
```

## Salesforce Flow Builder Integration (Low-Code Alternative)

These global API methods are natively exposed as **Flow Actions**, making them perfectly suited for QA workflows, declarations, and general low-code automation.

### Available Actions & Technical Mapping

| Flow Action Label | Underlying Backend Method |
| --- | --- |
| Cancel Multi Sign Process | `RenderAPI.cancelMSprocess` |
| Reactivate Multi Sign Process | `RenderAPI.reactivateMSprocess` |

### Flow Input Structure

Each Flow Action expects a standard collection input variable format, where each discrete item requires:

| Field API Name | Type | Required | Description |
| --- | --- | --- | --- |
| `msSignatureId` | Id | Yes | Target ID of the Multi-Sign process record. |

## Summary

By leveraging the Docomotion RenderAPI, developers and system administrators gain:

- Granular program control over automated signature link generation.
- End-to-end lifecycle management of complex multi-sign processes.
- Fluid orchestration capabilities across standard Salesforce automations or external enterprise structures.

**Best Practices Reminder:** Always validate structural inputs prior to calling methods, supply well-formed JSON payloads, and implement programmatic error handling routines.
