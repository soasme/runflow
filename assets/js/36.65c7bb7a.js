(window.webpackJsonp=window.webpackJsonp||[]).push([[36],{394:function(e,t,a){"use strict";a.r(t);var s=a(44),r=Object(s.a)({},(function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[a("h1",{attrs:{id:"telegram-api-call-task"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#telegram-api-call-task"}},[e._v("#")]),e._v(" Telegram API Call Task")]),e._v(" "),a("p",[e._v("This task can interact with Telegram API.")]),e._v(" "),a("h2",{attrs:{id:"example-send-telegram-message"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#example-send-telegram-message"}},[e._v("#")]),e._v(" Example: Send Telegram Message")]),e._v(" "),a("div",{staticClass:"language-hcl extra-class"},[a("pre",{pre:!0,attrs:{class:"language-hcl"}},[a("code",[e._v("flow "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"telegram_send_message"')]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("{")]),e._v("\n\n  "),a("span",{pre:!0,attrs:{class:"token keyword"}},[e._v("variable"),a("span",{pre:!0,attrs:{class:"token type variable"}},[e._v(' "telegram_token" ')])]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("{")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("}")]),e._v("\n  "),a("span",{pre:!0,attrs:{class:"token keyword"}},[e._v("variable"),a("span",{pre:!0,attrs:{class:"token type variable"}},[e._v(' "chat_id" ')])]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("{")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("}")]),e._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"telegram_api_call"')]),e._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"this"')]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("{")]),e._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[e._v("client")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("=")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("{")]),e._v("\n      "),a("span",{pre:!0,attrs:{class:"token property"}},[e._v("token")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("=")]),e._v(" var.telegram_token\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("}")]),e._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[e._v("api_method")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("=")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"send_message"')]),e._v("\n\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[e._v("chat_id")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("=")]),e._v(" var.chat_id\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[e._v("text")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("=")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"Hello World! - Send From Runflow"')]),e._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[e._v("timeout")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("=")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[e._v("10")]),e._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("}")]),e._v("\n\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("}")]),e._v("\n")])])]),a("p",[e._v("The telegram bot will send you a new message:")]),e._v(" "),a("p",[a("img",{attrs:{src:"/images/telegram-send-message-example.png",alt:"preview of the telegram message"}})]),e._v(" "),a("details",{staticClass:"custom-block details"},[a("summary",[e._v("Click me to view the run output")]),e._v(" "),a("p",[e._v("Run:")]),e._v(" "),a("div",{staticClass:"language-bash extra-class"},[a("pre",{pre:!0,attrs:{class:"language-bash"}},[a("code",[e._v("$ runflow run examples/telegram_send_message.hcl --var "),a("span",{pre:!0,attrs:{class:"token assign-left variable"}},[e._v("telegram_token")]),a("span",{pre:!0,attrs:{class:"token operator"}},[e._v("=")]),a("span",{pre:!0,attrs:{class:"token variable"}},[e._v("$TELEGRAM_TOKEN")]),e._v(" --var "),a("span",{pre:!0,attrs:{class:"token assign-left variable"}},[e._v("chat_id")]),a("span",{pre:!0,attrs:{class:"token operator"}},[e._v("=")]),a("span",{pre:!0,attrs:{class:"token variable"}},[e._v("$CHAT_ID")]),e._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[e._v("2021")]),e._v("-07-08 "),a("span",{pre:!0,attrs:{class:"token number"}},[e._v("23")]),e._v(":14:41,337"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("]")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"task.telegram_api_call.this"')]),e._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[e._v("2021")]),e._v("-07-08 "),a("span",{pre:!0,attrs:{class:"token number"}},[e._v("23")]),e._v(":14:42,602"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v("]")]),e._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[e._v('"task.telegram_api_call.this"')]),e._v(" is successful.\n")])])])]),e._v(" "),a("h2",{attrs:{id:"argument-reference"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#argument-reference"}},[e._v("#")]),e._v(" Argument Reference")]),e._v(" "),a("ul",[a("li",[a("code",[e._v("api_method")]),e._v(" - (Required, str) The API method, for example "),a("code",[e._v("send_message")]),e._v(". See the full "),a("a",{attrs:{href:"https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("methods"),a("OutboundLink")],1),e._v(" page.")]),e._v(" "),a("li",[e._v("The rest of the arguments are the method parameters of the corresponding "),a("code",[e._v("api_method")]),e._v(" listed on the "),a("a",{attrs:{href:"https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("page"),a("OutboundLink")],1),e._v(". For example, when the "),a("code",[e._v("api_method")]),e._v(" is "),a("a",{attrs:{href:"https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram.Bot.send_message",target:"_blank",rel:"noopener noreferrer"}},[a("code",[e._v("send_message")]),a("OutboundLink")],1),e._v(", you should set:\n"),a("ul",[a("li",[a("code",[e._v("chat_id")]),e._v(" - (Required, int or str) Unique identifier for the target chat or username of the target channel (in the format @channelusername).")]),e._v(" "),a("li",[a("code",[e._v("text")]),e._v(" - (Required, str) Text of the message to be sent.")]),e._v(" "),a("li",[a("code",[e._v("parse_mode")]),e._v(" - (Optional, str) Send Markdown or HTML.")]),e._v(" "),a("li",[e._v("...")])])]),e._v(" "),a("li",[a("code",[e._v("client")]),e._v(" - (Required, map) The client settings.\n"),a("ul",[a("li",[a("code",[e._v("token")]),e._v(" - (Required, str) The token for telegram bot.")]),e._v(" "),a("li",[a("code",[e._v("base_url")]),e._v(" - (Optional, str) Telegram Bot API service URL.")]),e._v(" "),a("li",[a("code",[e._v("base_file_url")]),e._v(" - (Optional, str) Telegram Bot API file URL.")])])])]),e._v(" "),a("h2",{attrs:{id:"attributes-reference"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#attributes-reference"}},[e._v("#")]),e._v(" Attributes Reference")]),e._v(" "),a("ul",[a("li",[a("code",[e._v("result")]),e._v(" - The returning value of Telegram bot method call.")])])])}),[],!1,null,null,null);t.default=r.exports}}]);