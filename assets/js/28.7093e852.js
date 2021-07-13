(window.webpackJsonp=window.webpackJsonp||[]).push([[28],{386:function(t,e,a){"use strict";a.r(e);var s=a(44),n=Object(s.a)({},(function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h1",{attrs:{id:"notion-api-call"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#notion-api-call"}},[t._v("#")]),t._v(" Notion API Call")]),t._v(" "),a("p",[t._v("This task lets you interact with "),a("a",{attrs:{href:"https://notion.so",target:"_blank",rel:"noopener noreferrer"}},[t._v("Notion"),a("OutboundLink")],1),t._v(".")]),t._v(" "),a("p",[t._v("Added since v0.10.0")]),t._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"custom-block-title"},[t._v("TIP")]),t._v(" "),a("p",[t._v("This feature requires installing "),a("code",[t._v("notion-client")]),t._v(":")]),t._v(" "),a("div",{staticClass:"language-bash extra-class"},[a("pre",{pre:!0,attrs:{class:"language-bash"}},[a("code",[t._v("$ pip "),a("span",{pre:!0,attrs:{class:"token function"}},[t._v("install")]),t._v(" runflow"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("notion"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n")])])])]),t._v(" "),a("h2",{attrs:{id:"authentication"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#authentication"}},[t._v("#")]),t._v(" Authentication")]),t._v(" "),a("p",[t._v("You can create an integration through "),a("a",{attrs:{href:"https://www.notion.so/my-integrations",target:"_blank",rel:"noopener noreferrer"}},[t._v("https://www.notion.so/my-integrations"),a("OutboundLink")],1),t._v(".")]),t._v(" "),a("p",[t._v('When a new integration is created, you should be able to obtain a new "Internal Integration Token". Click "Show" to display it.')]),t._v(" "),a("p",[a("img",{attrs:{src:"/images/notion-integration.png",alt:"screenshot of getting a new internal integration token"}})]),t._v(" "),a("p",[t._v('Additionally, you should share "Can Edit" permission for the parent page with the Integration you just created.')]),t._v(" "),a("p",[a("img",{attrs:{src:"/images/notion-share.png",alt:"screenshot of sharing permission"}})]),t._v(" "),a("h2",{attrs:{id:"example-usage-update-page-title"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#example-usage-update-page-title"}},[t._v("#")]),t._v(" Example Usage: Update Page Title")]),t._v(" "),a("ul",[a("li",[t._v("Set "),a("code",[t._v("client.auth")]),t._v(" with a Notion Integration Token.")]),t._v(" "),a("li",[t._v("Set "),a("code",[t._v("api_method")]),t._v(" to "),a("code",[t._v("pages.update")]),t._v(".")]),t._v(" "),a("li",[t._v("Set "),a("code",[t._v("page_id")]),t._v(" to the ID of the page. In case you're struggling with find the ID of the page, copy the page url, and you will have something like "),a("code",[t._v("https://www.notion.so/soasme/Runflow-Test-ee5b6cd7a7a340d79ae5ae28c52b67ea")]),t._v(". Turn the last bit of information "),a("code",[t._v("ee5b6cd7a7a340d79ae5ae28c52b67ea")]),t._v(" into 8-4-4-4-12 form, e.g. "),a("code",[t._v("ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea")]),t._v(".")]),t._v(" "),a("li",[t._v("Set "),a("code",[t._v("properties")]),t._v(". It's strongly recommended you read the Notion documentation "),a("a",{attrs:{href:"https://developers.notion.com/docs/working-with-page-content",target:"_blank",rel:"noopener noreferrer"}},[t._v("Working with page content"),a("OutboundLink")],1),t._v(" first. You will have a basic understanding of properties then.")])]),t._v(" "),a("div",{staticClass:"language-hcl extra-class"},[a("pre",{pre:!0,attrs:{class:"language-hcl"}},[a("code",[t._v("flow "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"notion_update_title"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("variable"),a("span",{pre:!0,attrs:{class:"token type variable"}},[t._v(' "notion_token" ')])]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("default")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('""')]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"notion_api_call"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"update_title"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("client")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("auth")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" var.notion_token\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("api_method")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pages.update"')]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("page_id")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea"')]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("properties")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"title"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"id"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"title"')]),t._v(",\n        "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"type"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"title"')]),t._v(",\n        "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"title"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("\n          "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"type"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"text"')]),t._v(",\n            "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"text"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n              "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v('"content"')]),t._v(": "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"Runflow Test"')]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n          "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n      "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("details",{staticClass:"custom-block details"},[a("summary",[t._v("Click me to view the run output")]),t._v(" "),a("p",[t._v("Run")]),t._v(" "),a("div",{staticClass:"language-bash extra-class"},[a("pre",{pre:!0,attrs:{class:"language-bash"}},[a("code",[t._v("$ "),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[t._v("read")]),t._v(" -s RUNFLOW_VAR_notion_token\n**********\n$ "),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[t._v("export")]),t._v(" RUNFLOW_VAR_notion_token\n$ runflow run examples/notion_update_title.hcl\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-12 "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("22")]),t._v(":14:43,328"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.notion_api_call.update_title"')]),t._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-12 "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("22")]),t._v(":14:44,358"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.notion_api_call.update_title"')]),t._v(" is successful.\n")])])])]),t._v(" "),a("h2",{attrs:{id:"example-usage-append-block-children"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#example-usage-append-block-children"}},[t._v("#")]),t._v(" Example Usage: Append Block Children")]),t._v(" "),a("p",[t._v('This example appends an H2 element "Runflow is awesome" to the page.')]),t._v(" "),a("ul",[a("li",[t._v("Set "),a("code",[t._v("client.auth")]),t._v(" with a Notion Integration Token.")]),t._v(" "),a("li",[t._v("Set "),a("code",[t._v("api_method")]),t._v(" to "),a("code",[t._v("blocks.children.update")]),t._v(".")]),t._v(" "),a("li",[t._v("Set "),a("code",[t._v("block_id")]),t._v(" to the ID of the page. In case you're struggling with find the ID of the page, copy the page url, and you will have something like "),a("code",[t._v("https://www.notion.so/soasme/Runflow-Test-ee5b6cd7a7a340d79ae5ae28c52b67ea")]),t._v(". Turn the last bit of information "),a("code",[t._v("ee5b6cd7a7a340d79ae5ae28c52b67ea")]),t._v(" into 8-4-4-4-12 form, e.g. "),a("code",[t._v("ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea")]),t._v(".")]),t._v(" "),a("li",[t._v("Set "),a("code",[t._v("children")]),t._v(". It's strongly recommended you read the Notion documentation "),a("a",{attrs:{href:"https://developers.notion.com/docs/working-with-page-content",target:"_blank",rel:"noopener noreferrer"}},[t._v("Working with page content"),a("OutboundLink")],1),t._v(" first. You will have a basic understanding of properties then.")])]),t._v(" "),a("div",{staticClass:"language-hcl extra-class"},[a("pre",{pre:!0,attrs:{class:"language-hcl"}},[a("code",[t._v("flow "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"notion_update_blocks"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("variable"),a("span",{pre:!0,attrs:{class:"token type variable"}},[t._v(' "notion_token" ')])]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("default")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('""')]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"notion_api_call"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"append_blocks"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("client")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("auth")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" var.notion_token\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("api_method")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"blocks.children.append"')]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("block_id")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea"')]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("children")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("\n      "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("object")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"block"')]),t._v(",\n        "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("type")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"heading_2"')]),t._v(",\n        "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("heading_2")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n          "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("text")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n              "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("type")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"text"')]),t._v(",\n              "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("text")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n                "),a("span",{pre:!0,attrs:{class:"token property"}},[t._v("content")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"Runflow is awesome"')]),t._v(",\n              "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v(",\n            "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v(",\n          "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(",\n        "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v(",\n      "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n")])])]),a("details",{staticClass:"custom-block details"},[a("summary",[t._v("Click me to view the run output")]),t._v(" "),a("p",[t._v("Run")]),t._v(" "),a("div",{staticClass:"language-bash extra-class"},[a("pre",{pre:!0,attrs:{class:"language-bash"}},[a("code",[t._v("$ "),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[t._v("read")]),t._v(" -s RUNFLOW_VAR_notion_token\n**********\n$ "),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[t._v("export")]),t._v(" RUNFLOW_VAR_notion_token\nrunflow run examples/notion_update_blocks.hcl\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-12 "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("22")]),t._v(":53:32,327"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.notion_api_call.update_blocks"')]),t._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-12 "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("22")]),t._v(":53:33,315"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.notion_api_call.update_blocks"')]),t._v(" is successful.\n")])])])]),t._v(" "),a("h2",{attrs:{id:"arguments-reference"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#arguments-reference"}},[t._v("#")]),t._v(" Arguments Reference")]),t._v(" "),a("ul",[a("li",[a("code",[t._v("api_method")]),t._v(" - (Required, str) The API methods. Choices include\n"),a("ul",[a("li",[a("code",[t._v('"blocks.children.append"')])]),t._v(" "),a("li",[a("code",[t._v('"blocks.children.list"')])]),t._v(" "),a("li",[a("code",[t._v('"databases.list"')])]),t._v(" "),a("li",[a("code",[t._v('"databases.query"')])]),t._v(" "),a("li",[a("code",[t._v('"databases.retrieve"')])]),t._v(" "),a("li",[a("code",[t._v('"pages.list"')])]),t._v(" "),a("li",[a("code",[t._v('"pages.create"')])]),t._v(" "),a("li",[a("code",[t._v('"pages.retrieve"')])]),t._v(" "),a("li",[a("code",[t._v('"pages.update"')])]),t._v(" "),a("li",[a("code",[t._v('"users.retrieve"')])]),t._v(" "),a("li",[a("code",[t._v('"users.list"')])]),t._v(" "),a("li",[a("code",[t._v('"users.list"')])]),t._v(" "),a("li",[a("code",[t._v('"search"')])])])]),t._v(" "),a("li",[t._v("The rest of arguments are the parameters for the "),a("code",[t._v("api_method")]),t._v(". For the full reference, please check "),a("a",{attrs:{href:"https://developers.notion.com/reference/intro",target:"_blank",rel:"noopener noreferrer"}},[t._v("https://developers.notion.com/reference/intro"),a("OutboundLink")],1),t._v(". For example, when the "),a("code",[t._v("api_method")]),t._v(" is "),a("a",{attrs:{href:"https://developers.notion.com/reference/patch-page",target:"_blank",rel:"noopener noreferrer"}},[t._v("pages.update"),a("OutboundLink")],1),t._v(", the arguments include\n"),a("ul",[a("li",[a("code",[t._v("page_id")]),t._v(" - (Required, str) The page ID.")]),t._v(" "),a("li",[a("code",[t._v("properties")]),t._v(" - (Required, map) The page properties.")]),t._v(" "),a("li",[a("code",[t._v("archived")]),t._v(" - (Optional, bool) Set to true to archive (delete) a page. Set to false to un-archive (restore) a page.")])])]),t._v(" "),a("li",[a("code",[t._v("client")]),t._v(" - (Required, map) The client settings.\n"),a("ul",[a("li",[a("code",[t._v("auth")]),t._v(" - (Required, string) The Notion integration token.")]),t._v(" "),a("li",[a("code",[t._v("timeout_ms")]),t._v(" - (Optional, int) The timeout in ms. Default is 60_000ms.")]),t._v(" "),a("li",[a("code",[t._v("base_url")]),t._v(" - (Optional, str) The notion base url. Default is "),a("code",[t._v('"https://api.notion.com"')]),t._v(".")]),t._v(" "),a("li",[a("code",[t._v("notion_version")]),t._v(" - (Optional, str) The notion API version.")])])])])])}),[],!1,null,null,null);e.default=n.exports}}]);