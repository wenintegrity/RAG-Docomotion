---
title: "Store Output in an External Repository"
source: https://www.docomotion.com/support/advanced-features/external-repository/
section: advanced-features
last_modified: 2024-01-13T09:07:24
---

# Store Output in an External Repository

### **Store Output in an External Repository**

You can configure the system to store the output generated from a Form in an external storage such as Cloud Document Management system.
When output is generated from a Form for which external repositories are configured, the output is automatically saved to all the configured data repositories.
If you want to save the generated output also to Salesforce you need to configure Save to Salesforce in the Form Generation Settings.

Step-by-Step Guide:

**Step 1: Create a Service for External Repository Storage**

Create a dedicated service that will facilitate the storage of data in the external repository. Docomotion will utilize this service to save the generated data to the repository after the output generation process.

**Step 2: Configure Request Activation for the Service**

To set up the request that activates the service and stores the output in the external repository:

1. Open the desired Form for which you want to save the output and navigate to the “External Repositories” section.
2. Click on “New External Repository” and provide the necessary information:

   - External Repository Name: Choose any identifying name (mandatory).
   - Login URL/Username (mandatory)/Password (mandatory): Authentication details required for accessing the repository.
   - Compression:
     - Empty or 1: No compression
     - 2: 7z compression
   - File ID: NA
   - Form: Automatically filled
   - Service URL: URL to the storage service created in Step 1.
   - Storage Type – Authorization Protocol:
     - Type A: OAuth 2.0
     - Token: NA
     - Body Template: Must contain #content#

   Note: During output generation, the placeholder #content# is replaced with the generated output in Base64.
3. Click “Save” to confirm and apply the configuration.
