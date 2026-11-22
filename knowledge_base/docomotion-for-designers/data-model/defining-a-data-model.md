---
title: "Data Model: Definition"
source: https://www.docomotion.com/support/docomotion-for-designers/data-model/defining-a-data-model/
section: docomotion-for-designers
last_modified: 2024-01-10T07:58:38
---

# Data Model: Definition

A Data Model is a Data tag list based on Salesforce fields. Data Models enable users, in the Designer, to create forms with variable data tags that will be populated with the Salesforce fields data in runtime when generating output from the Form.

Each Data Model is created based on a Salesforce Object called the Main Object (such as Contact, Contract, Order etc.) and relations of this Object with related Objects. The Main Object is the object from which users generate the output.

Data Models can be created as standalone entities or as part of a new Form. More than one Form can be based on each Data Model.

Docomotion enables adding to a Data Model three types of Data Tags:

- Data tags derived from Salesforce fields that are fixed (cannot be changed).
- Data tags derived from Salesforce fields that are interactive and can be changed by responders to interactive forms.
- Interactive Data tags that are used to collect feedback data received from interactive forms without the need to change / update / add Salesforce data. For example, a survey that uses elements such as radio buttons, checkboxes, dropdown lists etc, to collect the end user feedback. This information is stored and analyzed in Docomotion.
