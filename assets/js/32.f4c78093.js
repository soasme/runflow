(window.webpackJsonp=window.webpackJsonp||[]).push([[32],{390:function(s,t,a){"use strict";a.r(t);var e=a(44),n=Object(e.a)({},(function(){var s=this,t=s.$createElement,a=s._self._c||t;return a("ContentSlotsDistributor",{attrs:{"slot-key":s.$parent.slotKey}},[a("h1",{attrs:{id:"slack-api-call"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#slack-api-call"}},[s._v("#")]),s._v(" Slack API Call")]),s._v(" "),a("p",[s._v("This task enables interacting with Slack Web API.")]),s._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"custom-block-title"},[s._v("TIP")]),s._v(" "),a("p",[s._v("This feature requires installing slack-sdk:")]),s._v(" "),a("div",{staticClass:"language-bash extra-class"},[a("pre",{pre:!0,attrs:{class:"language-bash"}},[a("code",[s._v("$ pip "),a("span",{pre:!0,attrs:{class:"token function"}},[s._v("install")]),s._v(" runflow"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),s._v("slack"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v("\n")])])])]),s._v(" "),a("h2",{attrs:{id:"send-slack-message-to-a-channel"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#send-slack-message-to-a-channel"}},[s._v("#")]),s._v(" Send Slack Message to a Channel")]),s._v(" "),a("p",[s._v("To send a slack message to a channel,")]),s._v(" "),a("ul",[a("li",[s._v("Set "),a("code",[s._v("client.token")]),s._v(" for authentication:")]),s._v(" "),a("li",[s._v("Set "),a("code",[s._v("api_method")]),s._v(" to "),a("code",[s._v('"chat.postMessage"')]),s._v(".")]),s._v(" "),a("li",[s._v("Set "),a("code",[s._v("channel")]),s._v(".")]),s._v(" "),a("li",[s._v("Set "),a("code",[s._v("text")]),s._v(".")])]),s._v(" "),a("p",[s._v("For example, this flow can extract the latest version of package "),a("code",[s._v("runflow")]),s._v(" from PyPI and then send a slack message:")]),s._v(" "),a("div",{staticClass:"language-hcl extra-class"},[a("div",{staticClass:"highlight-lines"},[a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("div",{staticClass:"highlighted"},[s._v(" ")]),a("div",{staticClass:"highlighted"},[s._v(" ")]),a("div",{staticClass:"highlighted"},[s._v(" ")]),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br"),a("br")]),a("pre",{pre:!0,attrs:{class:"language-hcl"}},[a("code",[s._v("flow "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"slack_send_message"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n\n  "),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("variable"),a("span",{pre:!0,attrs:{class:"token type variable"}},[s._v(' "package" ')])]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("default")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"runflow"')]),s._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n\n  "),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("variable"),a("span",{pre:!0,attrs:{class:"token type variable"}},[s._v(' "slack_token" ')])]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("default")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('""')]),s._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"http_request"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"extract_metadata"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("method")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"GET"')]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("url")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"https://pypi.org/pypi/'),a("span",{pre:!0,attrs:{class:"token interpolation"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("$")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("var")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),a("span",{pre:!0,attrs:{class:"token type variable"}},[s._v("package")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")])]),s._v('/json"')]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("timeout")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("5")]),s._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"hcl2_template"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"transform_metadata"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("source")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" metadata.info.version\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("context")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n      "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("metadata")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" call(task.http_request.extract_metadata.response, "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"json"')]),s._v(")\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"slack_api_call"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"notify_version"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("client")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n      "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("token")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" var.slack_token\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("api_method")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"chat.postMessage"')]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("channel")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"#random"')]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("text")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"Latest version of '),a("span",{pre:!0,attrs:{class:"token interpolation"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("$")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("var")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),a("span",{pre:!0,attrs:{class:"token type variable"}},[s._v("package")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")])]),s._v(" is "),a("span",{pre:!0,attrs:{class:"token interpolation"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("$")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("task"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("hcl2_template"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("transform_metadata"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("content"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")])]),s._v('."')]),s._v("\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n\n  task "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"file_write"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"output_slack_response"')]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("filename")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"/dev/stdout"')]),s._v("\n    "),a("span",{pre:!0,attrs:{class:"token property"}},[s._v("content")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("=")]),s._v(" task.slack_api_call.notify_version.response\n  "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n")])])]),a("p",[s._v("The slack channel will receive a new message:")]),s._v(" "),a("p",[a("img",{attrs:{src:"/images/slack-send-message-example.png",alt:"preview of the slack message"}})]),s._v(" "),a("details",{staticClass:"custom-block details"},[a("summary",[s._v("Click me to view the run output")]),s._v(" "),a("p",[s._v("Run:")]),s._v(" "),a("div",{staticClass:"language-bash extra-class"},[a("pre",{pre:!0,attrs:{class:"language-bash"}},[a("code",[s._v("$ runflow run examples/slack_send_message.hcl --var "),a("span",{pre:!0,attrs:{class:"token assign-left variable"}},[s._v("slack_token")]),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),a("span",{pre:!0,attrs:{class:"token variable"}},[s._v("${SLACK_TOKEN}")]),s._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:29,553"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.http_request.extract_metadata"')]),s._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:29,633"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.http_request.extract_metadata"')]),s._v(" is successful.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:29,634"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.hcl2_template.transform_metadata"')]),s._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:29,634"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.hcl2_template.transform_metadata"')]),s._v(" is successful.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:29,634"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.slack_api_call.notify_version"')]),s._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:30,285"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.slack_api_call.notify_version"')]),s._v(" is successful.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:30,286"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.file_write.output_slack_response"')]),s._v(" is started.\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'ok'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" True, "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'channel'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'C0HD36738'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'ts'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'1625475870.000600'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'message'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'bot_id'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'B026ZLQFHPX'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'type'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'message'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'text'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'Latest version of runflow is 0.8.0.'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'user'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'U026VUUC4VC'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'ts'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'1625475870.000600'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'team'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'T0HCXJS4C'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'bot_profile'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'id'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'B026ZLQFHPX'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'deleted'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" False, "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'name'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'Test Runflow'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'updated'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("1625475649")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'app_id'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'A027FABBGU9'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'icons'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("{")]),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'image_36'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'image_48'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png'")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'image_72'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v(", "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'team_id'")]),a("span",{pre:!0,attrs:{class:"token builtin class-name"}},[s._v(":")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'T0HCXJS4C'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("}")]),s._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("2021")]),s._v("-07-05 "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("21")]),s._v(":04:30,288"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("]")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v('"task.file_write.output_slack_response"')]),s._v(" is successful.\n")])])])]),s._v(" "),a("h2",{attrs:{id:"argument-reference"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#argument-reference"}},[s._v("#")]),s._v(" Argument Reference")]),s._v(" "),a("ul",[a("li",[a("code",[s._v("api_method")]),s._v(" - (Required, str) The API method, for example, "),a("code",[s._v("chat.postMessage")]),s._v(". See the full "),a("a",{attrs:{href:"https://api.slack.com/methods",target:"_blank",rel:"noopener noreferrer"}},[s._v("methods"),a("OutboundLink")],1),s._v(" page.")]),s._v(" "),a("li",[s._v("The rest of the arguments are defined on the exact section of the "),a("a",{attrs:{href:"https://slack.dev/python-slack-sdk/api-docs/slack_sdk/web/client.html",target:"_blank",rel:"noopener noreferrer"}},[s._v("slack-sdk"),a("OutboundLink")],1),s._v(" page. For example, when the "),a("code",[s._v("api_method")]),s._v(" is "),a("code",[s._v("chat.postMessage")]),s._v(", you should set:\n"),a("ul",[a("li",[a("code",[s._v("channel")]),s._v(" - (Required, str) The channel id. e.g. 'C1234567890'.")]),s._v(" "),a("li",[a("code",[s._v("text")]),s._v(" - (Optional, str) The message you'd like to share. The text is not required when presenting blocks.")]),s._v(" "),a("li",[a("code",[s._v("blocks")]),s._v(' - (Optional, list) A list of either dict values. Blocks are required when not presenting text. e.g. [{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]')])])]),s._v(" "),a("li",[a("code",[s._v("client")]),s._v(" - (Required, map) The client settings.\n"),a("ul",[a("li",[a("code",[s._v("token")]),s._v(" - (Required, str) The slack token. The corresponding app of the token should have the scope properly setup.")]),s._v(" "),a("li",[a("code",[s._v("base_url")]),s._v(" - (Optional, str) Default to "),a("code",[s._v('"https://www.slack.com/api/"')]),s._v(".")]),s._v(" "),a("li",[a("code",[s._v("timeout")]),s._v(" - (Optional, int) Default to 30 seconds.")]),s._v(" "),a("li",[a("code",[s._v("headers")]),s._v(" - (Optional, dict) The request headers.")]),s._v(" "),a("li",[a("code",[s._v("user_agent_prefix")]),s._v(" - (Optional, str) The prefix for "),a("code",[s._v("User-Agent")]),s._v(".")]),s._v(" "),a("li",[a("code",[s._v("user_agent_sufix")]),s._v(" - (Optional, str) The suffix for "),a("code",[s._v("User-Agent")]),s._v(".")])])])]),s._v(" "),a("h2",{attrs:{id:"attributes-reference"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#attributes-reference"}},[s._v("#")]),s._v(" Attributes Reference")]),s._v(" "),a("ul",[a("li",[a("code",[s._v("response")]),s._v(" - Response object provided by slack-sdk.\n"),a("ul",[a("li",[s._v("You can check "),a("code",[s._v("response.ok")]),s._v(" to see if the slack message is sent.")])])])])])}),[],!1,null,null,null);t.default=n.exports}}]);