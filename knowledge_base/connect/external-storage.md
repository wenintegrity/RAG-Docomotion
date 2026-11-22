---
title: "External Storage Setup Guide"
source: https://www.docomotion.com/support/connect/external-storage/
section: connect
last_modified: 2025-05-20T07:04:47
---

# External Storage Setup Guide

## Authentication Requirements

To access Docomotion Connect APIs, you must first authenticate using a Salesforce Connected App:

1. Enable OAuth for your Salesforce Connected App
2. Obtain an access\_token using a standard OAuth flow (password, web-server, or JWT)
3. Include the authorization header with all API calls:  `Authorization: Bearer <access_token>`

**Note:** Using only the Connected App keys is not sufficient for authentication.

## Connecting to External Storage

To store your generated documents in Google Drive or OneDrive:

1. Navigate to System Settings
2. Select Drive Provider from the menu options
3. Choose your preferred storage provider:
   - Google Drive
   - OneDrive
4. Click the Authorize button
5. Complete the authentication steps in the provider’s interface
6. Upon successful authorization, you will be returned to Docomotion with a confirmation message

After completing these steps, your external storage connection will be established, and Docomotion will be able to store generated documents in your selected cloud storage service.
