---
title: "Quickstart Templates"
source: https://www.docomotion.com/support/docomotion-for-administrators/quickstart-templates/
section: docomotion-for-administrators
last_modified: 2025-03-19T08:22:59
---

# Quickstart Templates

## Quickstart Tempalates- Overview:

Pre-built, ready-to-use document templates designed to help new users quickly understand and implement Docomotion’s capabilities in their Salesforce environment. These templates are ready-to-use examples that work with standard Salesforce fields, making them compatible with any Salesforce org where Docomotion is installed.

Note: These templates are sample use cases showcasing how to pull data from multiple Salesforce objects, apply data masking, and leverage script tags and business logic. You can import them to explore their configurations, learn best practices, and adapt them to your organization’s needs.

- Prerequisites

Before importing these example templates, ensure you have:

1. [Docomotion Installed](https://www.docomotion.com/support/docomotion-for-administrators/installing-the-docomotion-package/)
2. [Appropriate Permissions](https://www.docomotion.com/support/docomotion-for-administrators/assigning-permissions/): You must have either the **Admin** or **Designer** permission set
3. [Designer Client](https://www.docomotion.com/support/docomotion-for-administrators/designer-installation/): The Docomotion Designer client must be installed on your computer
4. **Authorization**: Your Salesforce org must be authorized for interactive template testing (refer to the [Docomotion Authorization Guide](https://support.docomotion.com/authorization-guide))

## Import Instructions:

1. Navigate to **Salesforce > Docomotion > Forms**
2. In the **Recent Forms** section, click **New** to open the New Form page
3. Click **Import**
4. Select the **zipped file** containing the form and click **Open.**
5. The **Import/Export** window will display the **Source Package Information**. Click **IMPORT** to proceed.
6. If conflicts arise with existing data, you’ll see a Conflict Resolution window. Choose from:
   - **Overwrite**: Updates the destination org’s data with the zip file’s data (be cautious with Data Models & Word Templates).
   - **Create New**: Generates a new entity using the zip file’s content.
   - **Link**: Retains existing data instead of using the zip file’s content.

### Available Templates

Browse our collection of Quickstart Templates designed for various common business scenarios. Each form includes a downloadable zip file (for import) and a sample PDF showing the final output.

**Account Statement**

- Salesforce Object: Account
- Description: account overview featuring general account details, a contacts directory, opportunity pipeline summary, recent activities, and open cases tables.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Account-Overview.zip)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Account-Overview.pdf)

**Contact Donation Letter**

- Salesforce Object: Contact
- Description: Personalized donation acknowledgment letter with customizable branding that automatically populates with donor information and contribution details, perfect for non-profit organizations looking to strengthen donor relationships.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Contact-Donation-Letter.zip)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Contact-Donation-Letter.pdf)

**Contact Survey**

- Salesforce Object: Contact
- Description: An **interactive** customer satisfaction survey that can be generated as an **HTML output** format.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Contact-SurveyInteractive.zip)  (To Generate as an HTML output format)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Contact-SurveyInteractive.pdf)

**A Ready-to-Sign Quotation**

- Salesforce Object: Quote
- Description: Professional quote template featuring customer details, itemized product/service listing with pricing, customizable terms and conditions, and built-in e-signature functionality for immediate approval (can be generated as **HTML**).
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Sample-QuoteInteractive.zip) (To Generate as an HTML output format)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Sample-QuoteInteractive.pdf)

**Opportunity NDA Template**

- Salesforce Object: Opportunity
- Description: A Non-Disclosure Agreement (NDA) with interactive fillable fields, and embedded e-Signature capabilities – —ideal for capturing client signatures in real time.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Opportunity-NDA-TemplateInteractive.zip)  (To Generate as an HTML output format)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Opportunity-NDA-TemplateInteractive.pdf)

**Opportunity Sample Quote**

- Salesforce Object: Opportunity
- Description: A quotation form featuring customer details, a product list table, and built-in e-signature functionality. Displays a free shipping notice when the total crosses a certain threshold.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Opportunity-Sample-Quote.zip)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/Opportunity-Sample-Quote.pdf)

**Opportunity (Java Script Example)**

- Salesforce Object: Opportunity
- Description: Advanced interactive form demonstrating **JavaScript** capabilities to collect inputs from clients and dynamically update values.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/JavaScript-ExampleInteractive.zip)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/JavaScript-ExampleInteractive.pdf)

**Proposal**

- Salesforce Object: Opportunity
- Description: A simple business proposal form pulling Account and Opportunity details, including prepared-for/by sections, contact lists, pricing, and e-signatures.
- Download Form (.zip) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/ProposalInteractive.zip)
- View Sample Output (.pdf) – [here](https://www.docomotion.com/wp-content/uploads/2025/02/ProposalInteractive.pdf)

  With these Quickstart Templates, you can **accelerate your onboarding**, explore and **learn from examples** to build your own custom solutions using **Docomotion**.
