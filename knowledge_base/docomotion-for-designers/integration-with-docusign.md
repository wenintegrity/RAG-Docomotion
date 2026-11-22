---
title: "Integration with DocuSign"
source: https://www.docomotion.com/support/docomotion-for-designers/integration-with-docusign/
section: docomotion-for-designers
last_modified: 2024-01-16T14:10:25
---

# Integration with DocuSign

DocuSign for Salesforce is an eSignature solution that integrates with Salesforce. DocuSign makes any workflow or approval simple, secure and fully digital. With DocuSign you can send, sign and track agreements and approvals anytime, anywhere, and from any device. If you are looking for a ‘simple electronic signatures’ solution please refer to Docomotion’s built-in e-Sign Solution (Available at our [Platinum](https://www.docomotion.com/pricing/) package).

After integrated DocuSign and Docomotion, you can use Docomotion to generate a highly designed document based on  information from any standard or customized object in Salesforce that can be signed with DocuSign.

**To set up Docomotion to work with DocuSign:**

- Install Docomotion.
- Install [DocuSign from the AppExchange](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000001taX4EAI) and follow the instructions in the [DocuSign For Salesforce Administration Guide](https://support.docusign.com/guides/docusign-for-salesforce-administrator-guide).

### Workflow for Generating a Document for Signing with DocuSign

**Step 1: Generating an Output Document**

1. Use single record generation.
2. In the generation screen select:
   **Output Format: PDF**
   **Output Channel: Notes & Attchement**

**Step 2: Send Output Document to DocuSign**

Using the **Send with DocuSign** button, Salesforce users can send documents to be signed from records in the Salesforce object.

Note: As part of the out-of-the-box DocuSign for Salesforce package, you can easily configure page layouts for the following Salesforce objects with the Send with the DocuSign button:

- Accounts
- Contacts
- Opportunities
- Leads
- Contracts
- Cases

For more information on how to configure the docusign button refer to: [Docusign For Salesforce Administration Guide](https://support.docusign.com/guides/docusign-for-salesforce-administrator-guide).

The output document appears in the DocuSign Status window.

1. Click **Add Recipients** to add all required signer / reviewers.
2. Click **Next**.
3. In the **Envelope** page, select the required location for all signatures.
4. Click **Send**.

Signature location

### **Automatic Definition of Signature Areas in the Designer**

Instead of adding the signature locations in DocuSign you can define the locations in the Docomotion Designer.

When designing the Form in the Designer, add the following text **s1**  where you want the tag information for the first signer to appear.

You can add location for more than one signer by using**s2** etc.

Use a white font so that the text is not visible in the output.

Signature location in Docomotion Designer
