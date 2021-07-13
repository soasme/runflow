(window.webpackJsonp=window.webpackJsonp||[]).push([[30],{388:function(t,s,e){"use strict";e.r(s);var a=e(44),n=Object(a.a)({},(function(){var t=this,s=t.$createElement,e=t._self._c||s;return e("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[e("h1",{attrs:{id:"pushbullet-push-task"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#pushbullet-push-task"}},[t._v("#")]),t._v(" Pushbullet Push Task")]),t._v(" "),e("p",[t._v("This task sends a push notification to Android devices.")]),t._v(" "),e("p",[t._v("Added since v0.9.0.")]),t._v(" "),e("div",{staticClass:"custom-block tip"},[e("p",{staticClass:"custom-block-title"},[t._v("TIP")]),t._v(" "),e("p",[t._v("This feature requires installing pushbullet.py:")]),t._v(" "),e("div",{staticClass:"language-bash extra-class"},[e("pre",{pre:!0,attrs:{class:"language-bash"}},[e("code",[t._v("$ pip "),e("span",{pre:!0,attrs:{class:"token function"}},[t._v("install")]),t._v(" runflow"),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("pushbullet"),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n")])])])]),t._v(" "),e("h2",{attrs:{id:"example-push-note"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#example-push-note"}},[t._v("#")]),t._v(" Example: Push Note")]),t._v(" "),e("div",{staticClass:"language-hcl extra-class"},[e("pre",{pre:!0,attrs:{class:"language-hcl"}},[e("code",[t._v("flow "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pushbullet_push_note"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n\n  "),e("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("variable"),e("span",{pre:!0,attrs:{class:"token type variable"}},[t._v(' "pushbullet_api_key" ')])]),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n  task "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pushbullet_push"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"note"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("title")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"This is the title"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("body")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"This is the note"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("client")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("api_key")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" var.pushbullet_api_key\n    "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n  "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),e("h2",{attrs:{id:"example-push-link"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#example-push-link"}},[t._v("#")]),t._v(" Example: Push Link")]),t._v(" "),e("div",{staticClass:"language-hcl extra-class"},[e("pre",{pre:!0,attrs:{class:"language-hcl"}},[e("code",[t._v("flow "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pushbullet_push_link"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n\n  "),e("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("variable"),e("span",{pre:!0,attrs:{class:"token type variable"}},[t._v(' "pushbullet_api_key" ')])]),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n  task "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pushbullet_push"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"link"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("title")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"This is the title"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("url")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"https://runflow.org"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("client")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("api_key")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" var.pushbullet_api_key\n    "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n  "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),e("h2",{attrs:{id:"example-push-file"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#example-push-file"}},[t._v("#")]),t._v(" Example: Push File")]),t._v(" "),e("div",{staticClass:"language-hcl extra-class"},[e("pre",{pre:!0,attrs:{class:"language-hcl"}},[e("code",[t._v("flow "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pushbullet_push_file"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n\n  "),e("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("variable"),e("span",{pre:!0,attrs:{class:"token type variable"}},[t._v(' "pushbullet_api_key" ')])]),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n  task "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pushbullet_push"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"file"')]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("title")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"This is the title"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("body")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"This is the body"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("file_type")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"image/jpeg"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("file_name")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"cat.jpg"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("file_url")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token string"}},[t._v('"https://i.imgur.com/IAYZ20i.jpg"')]),t._v("\n    "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("client")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),e("span",{pre:!0,attrs:{class:"token property"}},[t._v("api_key")]),t._v(" "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" var.pushbullet_api_key\n    "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n  "),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),e("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),e("h2",{attrs:{id:"argument-reference"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#argument-reference"}},[t._v("#")]),t._v(" Argument Reference")]),t._v(" "),e("ul",[e("li",[e("code",[t._v("title")]),t._v(" - (Required, str) The title of notification.")]),t._v(" "),e("li",[e("code",[t._v("body")]),t._v(" - (Optional, str) The body of notification.")]),t._v(" "),e("li",[e("code",[t._v("url")]),t._v(" - (Optional, str) The url of notification. If present, the push type is "),e("code",[t._v("link")]),t._v(".")]),t._v(" "),e("li",[e("code",[t._v("file_type")]),t._v(" - (Optional, str) The type of attached file. Example value: "),e("code",[t._v('"image/png"')]),t._v(", "),e("code",[t._v('"image/jepg"')]),t._v(", etc. If present, the push type is "),e("code",[t._v("file")]),t._v(".")]),t._v(" "),e("li",[e("code",[t._v("file_name")]),t._v(" - (Optional, str) The name of attached file. Example value: "),e("code",[t._v('"cat.jpg"')]),t._v(". If present, the push type is "),e("code",[t._v("file")]),t._v(".")]),t._v(" "),e("li",[e("code",[t._v("file_url")]),t._v(" - (Optional, str) The url of attached file. Example value: "),e("code",[t._v('"https://i.imgur.com/IAYZ20i.jpg"')]),t._v(". If present, the push type is "),e("code",[t._v("file")]),t._v(".")]),t._v(" "),e("li",[e("code",[t._v("channel")]),t._v(" - (Optional, str) If specified, the recipient is the given channel filtered by name.")]),t._v(" "),e("li",[e("code",[t._v("email")]),t._v(" - (Optional, str) If specified, the recipient is the given chat filtered by email.")]),t._v(" "),e("li",[e("code",[t._v("client")]),t._v(" - (Required, map) The Pushbullet client.\n"),e("ul",[e("li",[e("code",[t._v("api_key")]),t._v(" - (Required, str) The API key.")]),t._v(" "),e("li",[e("code",[t._v("https_proxy")]),t._v(" - (Optional, str) The proxy url. Must be in HTTPS.")])])])]),t._v(" "),e("h2",{attrs:{id:"attributes-reference"}},[e("a",{staticClass:"header-anchor",attrs:{href:"#attributes-reference"}},[t._v("#")]),t._v(" Attributes Reference")]),t._v(" "),e("ul",[e("li",[e("code",[t._v("iden")]),t._v(" - The identity of push object.")])])])}),[],!1,null,null,null);s.default=n.exports}}]);