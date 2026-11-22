---
title: "Multi-Signer – Parallel & Sequential Modes"
source: https://www.docomotion.com/support/docomotion-for-designers/interactive-capabilities/multi-signers-2/
section: docomotion-for-designers
last_modified: 2026-06-14T09:14:15
---

# Multi-Signer – Parallel & Sequential Modes

[Video](https://youtu.be/Xv0WLUJCrZ8)

### Overview

The Multi-Signer (MS) feature empowers users to create forms that require multiple digital signatures. Docomotion supports two signing modes:

- **Sequential Mode:** Recipients sign the document one after the other in a predefined chain. This supports up to 10 recipients and is ideal for rigid multi-step approval processes.
- **Parallel Mode (from version 24):** The document is sent to an entire group at the same time (such as a Contact related list). Recipients can sign simultaneously in any order they choose, with no strict sequence required.

### Activate the Multi-Signer Feature

Before using this feature, an administrator must enable it in Salesforce:

1. Navigate to the **Docomotion System Settings** page.
2. Enable the feature by checking the **Activate** checkbox under the **Multi-Signer** section.
3. Choose where the final signed document is saved using the **Location to save document** dropdown. Options include:

   - **MS Signature:** Saves the file directly to the master Multi-Step Signature record.
   - **MS Signature + Parent:** Saves the file to both the signature record and the parent record (e.g., the Account).
   - **Last Signature + Parent:** Saves the file to the last signer’s record and the parent record.
4. *(Optional)* Check the **Keep a PDF of each step** box if you want Docomotion to save separate, standalone PDFs of the document after each individual signature is submitted.

### Step 1: Create a Multi-Signer Form

To initiate a Multi-Signer process, configure your form record as follows:

1. Create a new Form or edit an existing one.
2. **Choose Process Type:** Set the *Process Type* picklist to **Multi Step Process**.
3. **Select Signing Mode:** Locate the *Signing Mode* picklist and choose either **Sequential** or **Parallel**.
4. **Add Interactive Collection:** Add an existing interactive collection or create a new one. *(Optional: For Sequential mode, check the “Can Edit next step Fields” box if you want a signer to be able to edit fields meant for the next recipient in line).*

### Step 2: Define Recipients

How you configure recipients depends on the signing mode you selected in Step 1:

#### For Sequential Mode (Recipient Chain)

Manually construct a step-by-step chain under the **Step Signatures** section by clicking **New Step Signature** for each recipient. Add details using:

- A Lookup field from the Main Object.
- A Text field from the Main Object.
- A Free Email (a static, manually typed address).

#### For Parallel Mode (Related List Mapping)

Instead of creating rigid item-by-item steps, you can dynamically target a whole group:

- Under the **Step Signatures** section, use the new setup functionality to map a **Related List** (for example, the *Account Contacts* list).
- Docomotion will automatically generate a unique signature routing link for every contact found within that related list.

### Step 3: Design the Multi-Signer Form

Open the **Designer Client** to layout your document:

- Each signing step or mapped recipient corresponds to rows within your signature block.
- **Interactive Collection Fields:** Place your signature elements inside the designated Interactive Collection container.
- **Visual Indicator:** In the Designer, the collection container will display a **blue tint**. This visual cue indicates it is a dynamically repeating related list block. It will automatically expand or shrink at generation time to fit the exact number of contacts found in your Salesforce related list.

### Step 4: Generating and Sending the Form

1. On your primary Salesforce record, click the **Lightning Generate Document** button to open the generation screen.
2. Select your Multi-Signer form.
3. Ensure the output channel is set to **Link** (HTML/Link output is required to handle live interactive signature tracking).
4. Review the mapped recipients under the *Email Configuration* section. If necessary, you can modify individual recipient email addresses on the fly before generating.
5. Click **Generate**.

### Step 5: Tracking and Signing Progress

Once generated, Docomotion automatically creates a master **Multi-Step Signature Record** dashboard in Salesforce to monitor live progress:

- **Tracking Dashboard:** From this record, you can instantly see the overall status (*Pending*, *In Progress*, *Completed*), check if any signature links have expired, and see exactly how many people have signed so far.
- **Signing:** Docomotion automatically emails out the signature links to the recipients. When a recipient clicks their link, the document loads with real-time Salesforce data. They scroll down to the signature table, apply their digital signature, and click **Submit**.
- **Real-Time Updates:** As soon as a user signs, the status updates back in Salesforce instantly. Once the final signature is collected, the master record automatically transitions to **Completed**, and the fully signed final PDF is compiled and attached based on your System Settings.

## Important Considerations

- **Interactive Tracking:** The master Multi-Signer Signature record acts as a child related list to your originating parent object, keeping all tracking clean and auditable.
- **Dynamic Generation:** In Parallel Mode, your signature tables inside the document generate lines dynamically based on your live Salesforce data. You don’t need to manually redesign the form if an account has 2 contacts instead of 3.
- **Data Tag Logic:** Docomotion automatically generates a hidden repository tag named *Active Step Number*. You can leverage this data tag in your document scripts or containers to build advanced conditional formatting rules based on which signer is currently interacting with the document.
- **Process Completion:** In both sequential and parallel modes, every recipient must sign the document before the entire process is marked as completed.
- **Signer Limit:** Docomotion supports a maximum of **10 signers** per document workflow, applying to both sequential and parallel signing modes.

[Video](https://youtu.be/5iCQSbT8arA)
