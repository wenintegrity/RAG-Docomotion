---
title: "Preparing a Data Source API"
source: https://www.docomotion.com/support/connect/data-source-api/
section: connect
last_modified: 2025-05-20T07:18:24
---

# Preparing a Data Source API

Docomotion Connect requires an external data source, an API endpoint, that can provide the runtime data to populate the document template.

- This API endpoint should provide data in **XML format**.
- Method: GET or POST
- Example URL: https://your-domain.com/api/data/1
- URL Example: http://{yourdomain}/api/data/1
- Response Structure (XML):

The data source API can use either the **GET** or **POST** HTTP method.

An example URL for such an API might be https://your-domain.com/api/data/1.

The required **Response Structure** from your data source API must be in **XML**.

For **Single Generation**, the expected XML structure would typically wrap the main object’s data within root tags, like this:

```

					&lt;ROOT&gt;
  &lt;Account&gt;
    &lt;Name&gt;711 account&lt;/Name&gt;
    &lt;Id&gt;0015J00000IS6UiQAL&lt;/Id&gt;
  &lt;/Account&gt;
&lt;/ROOT&gt;

```

For **Mass Generation**, the XML would contain multiple instances of the main object data within the root tags:

```

					&lt;ROOT&gt;
    &lt;Account&gt;
        &lt;Name&gt;Account 1&lt;/Name&gt;
        &lt;Id&gt;0015J00000IS6UiQAL&lt;/Id&gt;
    &lt;/Account&gt;
    &lt;Account&gt;
        &lt;Name&gt;Account 2&lt;/Name&gt;
        &lt;Id&gt;0015J00000IS6UiQAL&lt;/Id&gt;
    &lt;/Account&gt;
    ...
&lt;/ROOT&gt;

```
