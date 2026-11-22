---
title: "Data Model Schema (JSON)"
source: https://www.docomotion.com/support/connect/data-model-schema/
section: connect
last_modified: 2025-06-01T06:31:15
---

# Data Model Schema (JSON)

## **What is the JSON Data Model?**

The JSON data model tells Docomotion Connect what your data looks like and how different pieces of information connect to each other. Think of it as a blueprint for your data structure.

## **Basic Structure**

Your JSON is a list of objects. Each object represents a type of data (like Customer, Order, Product, etc.):

```

					[
  {
    "id": "Customer",
    "displayName": "Customer",
    "isMain": true,
    "fields": [...]
  },
  {
    "id": "Order",
    "displayName": "Order",
    "isMain": false,
    "fields": [...]
  }
]

```

## **The Main Object (Starting Point)**

**Every JSON must have exactly ONE main object** with “isMain”: true. This is where document generation starts.

**Example:**

```

					{
  "id": "Policy",
  "displayName": "Insurance Policy",
  "isMain": true,
  "fields": [...]
}

```

**🚨** **Critical Rule:** The `id` value (“Policy”) must **exactly match** the “Object Name” field you entered when creating your form in Docomotion Connect. If these don’t match, your data model won’t work.

## **Field Types**

### **Required Properties**

Every field **must** include these properties (in this order):

- “id” – Technical name (case-sensitive)
- “type” – Data type or target object (case-sensitive)
- “displayName” – Human-readable label
- “isPrimaryKey” – true or false
- “isRelation” – true or false
- [“relationName”] – Only for related-list fields

### **Simple Fields**

Store basic information directly on the object:

```

					{
  "id": "PolicyNumber",
  "type": "String",
  "displayName": "Policy Number",
  "isPrimaryKey": true,
  "isRelation": false
}

```

### **Available Types:**

- String – Text (names, addresses, etc.)
- Number – Numbers (prices, quantities, etc.)
- Date – Dates
- Boolean – True/false values

### **Primary Key**

Every object needs exactly one field with “isPrimaryKey”: true – this uniquely identifies each record.

## **Relationships Between Objects**

### **Lookup Fields (Single Connection)**

When one object references another single object (no relationName):

```

					{
  "id": "CustomerId",
  "type": "Customer",
  "displayName": "Customer",
  "isPrimaryKey": false,
  "isRelation": true
}

```

### **Related Lists (Multiple Records)**

When showing multiple child records, include a **relationName**:

```

					{
  "id": "PolicyId",
  "type": "Policy",
  "displayName": "Policy",
  "isPrimaryKey": false,
  "isRelation": true,
  "relationName": "Vehicles"
}

```

## Key Difference:

- Lookup fields (single) → omit relationName
- Related-list fields (multiple) → include relationName to name the child collection

⚠️ **Capitalization matters:** It’s relationName (camelCase) – not RelationName or relation\_name

### Type Matching Rule

⚠️ **Critical**: For any relation (“isRelation”: true), the “type” value **must exactly match** the “id” of another object in your JSON array. Case-sensitive!

### How This Works in Templates

With the above structure, in your document templates you can use:

**Simple fields:**

`Policy Number:
 {{Policy.PolicyNumber}}
Total Price:
 {{Policy.TotalPrice}}
Customer Name:
 {{Policy.Customer.Name}}`
Repeating lists:
`{{#each Policy.Vehicles}}

Vehicle: {{this.VehicleName}}
{{/each}}`

## Connection to Form Creation

**Remember**: When you created your form template in Docomotion Connect, you entered an “Object Name” field. That exact name must be the id for your main object in this JSON. This is how Docomotion Connect knows which object to start with when generating documents.

N**ext Step**: After creating your JSON file, upload it in Docomotion Connect:

1. Go to your form → Click “Define Data Model”
2. Click “Upload JSON file”
3. Select your JSON file
4. Configure your data model

## Quick Checklist

✅ One main object with “isMain”: true
✅ Every object has a primary key with “isPrimaryKey”: true
✅ Simple fields have “isRelation”: false
✅ Lookup fields have “isRelation”: true (no relationName)
✅ Related lists have “isRelation”: true AND “relationName”: “ListName”
✅ Main object’s id matches exactly the “Object Name” from your form

### Common Mistakes to Avoid

❌ Wrong relationName capitalization – it’s relationName not RelationName
❌ Type mismatches – relation “type” must exactly match target object’s “id”
❌ JSON syntax errors – validate your JSON before uploading
❌ Missing required properties – every field needs id, type, displayName, isPrimaryKey, isRelation

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| Object Properties | | | |
| **id** | String | ✅ | Unique API/technical name |
| **displayName** | String | ✅ | Human-readable name |
| **isMain** | Boolean | ✅ (one object only) | Root object / entry point |
| **fields** | Array | ✅ | List of field definitions |
| Field Properties | | | |
| **id** | String | ✅ | Field API name |
| **displayName** | String | ✅ | Field label |
| **type** | String | ✅ | Data type (String, Date, Number, Boolean) |
| **isPrimaryKey** | Boolean | ✅ (one field only) | Indicates the primary key |
| **isRelation** | Boolean | ✅ (for relations) | Indicates a reference field |
| **relationName** | String | ✅ (for relations) | Alias for the related list |
