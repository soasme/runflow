(window.webpackJsonp=window.webpackJsonp||[]).push([[31],{389:function(t,e,s){"use strict";s.r(e);var a=s(44),r=Object(a.a)({},(function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("h1",{attrs:{id:"qrcode-generate-task"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#qrcode-generate-task"}},[t._v("#")]),t._v(" QRCode Generate Task")]),t._v(" "),s("p",[t._v("This task generates a QRCode image file.")]),t._v(" "),s("p",[t._v("Added since v0.10.0")]),t._v(" "),s("div",{staticClass:"custom-block tip"},[s("p",{staticClass:"custom-block-title"},[t._v("TIP")]),t._v(" "),s("p",[t._v("This feature requires installing "),s("code",[t._v("qrcode[pil]")]),t._v(":")]),t._v(" "),s("div",{staticClass:"language-bash extra-class"},[s("pre",{pre:!0,attrs:{class:"language-bash"}},[s("code",[t._v("$ pip "),s("span",{pre:!0,attrs:{class:"token function"}},[t._v("install")]),t._v(" runflow"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("qrcode"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n")])])])]),t._v(" "),s("h2",{attrs:{id:"generate-qrcode-png-file"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#generate-qrcode-png-file"}},[t._v("#")]),t._v(" Generate QRCode PNG File")]),t._v(" "),s("ul",[s("li",[t._v("Set "),s("code",[t._v("data")]),t._v(", usually it's an URI.")]),t._v(" "),s("li",[t._v("Set "),s("code",[t._v("filename")]),t._v(".")])]),t._v(" "),s("div",{staticClass:"language-hcl extra-class"},[s("pre",{pre:!0,attrs:{class:"language-hcl"}},[s("code",[t._v("flow "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"qrcode_generate_example"')]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  task "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"qrcode_generate"')]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"runflow-org"')]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("data")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"https://runflow.org"')]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("filename")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"/tmp/runflow-qrcode.png"')]),t._v("\n  "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),s("details",{staticClass:"custom-block details"},[s("summary",[t._v("Click me to view the run output")]),t._v(" "),s("p",[t._v("Run:")]),t._v(" "),s("div",{staticClass:"language-bash extra-class"},[s("pre",{pre:!0,attrs:{class:"language-bash"}},[s("code",[t._v("$ runflow run examples/qrcode_generate_example.hcl\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-13 "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("14")]),t._v(":52:18,608"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.qrcode_generate.runflow-org"')]),t._v(" is started.\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-13 "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("14")]),t._v(":52:21,824"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.qrcode_generate.runflow-org"')]),t._v(" is successful.\n")])])])]),t._v(" "),s("p",[t._v("After running the flow, it should generate such an image:")]),t._v(" "),s("p",[s("img",{attrs:{src:"/images/runflow-qrcode.png",alt:"runflow-qrcode"}})]),t._v(" "),s("h2",{attrs:{id:"set-colors-for-qrcode"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#set-colors-for-qrcode"}},[t._v("#")]),t._v(" Set Colors For QRCode")]),t._v(" "),s("ul",[s("li",[t._v("Set "),s("code",[t._v("image.back_color")]),t._v(" as the background color of the image file.")]),t._v(" "),s("li",[t._v("Set "),s("code",[t._v("image.fill_color")]),t._v(" as the filling color of the image file.")])]),t._v(" "),s("div",{staticClass:"language-hcl extra-class"},[s("pre",{pre:!0,attrs:{class:"language-hcl"}},[s("code",[t._v("flow "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"qrcode_generate_color"')]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n  task "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"qrcode_generate"')]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"runflow-org"')]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("data")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"https://runflow.org"')]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("filename")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"/tmp/runflow-qrcode.png"')]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("image")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n      "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("back_color")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"pink"')]),t._v("\n      "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v("fill_color")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("=")]),t._v(" tuple("),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("55")]),t._v(", "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("95")]),t._v(", "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("35")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(")\n    "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n  "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),s("details",{staticClass:"custom-block details"},[s("summary",[t._v("Click me to view the run output")]),t._v(" "),s("p",[t._v("Run:")]),t._v(" "),s("div",{staticClass:"language-bash extra-class"},[s("pre",{pre:!0,attrs:{class:"language-bash"}},[s("code",[t._v("$ runflow run examples/qrcode_generate_color.hcl\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-13 "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("14")]),t._v(":52:18,608"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.qrcode_generate.runflow-org"')]),t._v(" is started.\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("2021")]),t._v("-07-13 "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("14")]),t._v(":52:21,824"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"task.qrcode_generate.runflow-org"')]),t._v(" is successful.\n")])])])]),t._v(" "),s("p",[t._v("After running the flow, it should generate such an image:")]),t._v(" "),s("p",[s("img",{attrs:{src:"/images/runflow-qrcode-color.png",alt:"runflow-qrcode"}})]),t._v(" "),s("h2",{attrs:{id:"argument-reference"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#argument-reference"}},[t._v("#")]),t._v(" Argument Reference")]),t._v(" "),s("ul",[s("li",[s("code",[t._v("filename")]),t._v(" - (Required, str) The path to the output image file.")]),t._v(" "),s("li",[s("code",[t._v("data")]),t._v(" - (Required, str) The data string to be encoded.")]),t._v(" "),s("li",[s("code",[t._v("version")]),t._v(" - (Optional, int) An integer from 1 to 40 that controls the size of the QR Code. The smallest version 1 is a 21x21 matrix. When not set or set to null, the size will be automatically calculated.")]),t._v(" "),s("li",[s("code",[t._v("error_correction")]),t._v(" - (Optional, int) The error correction used for the QR Code. When set to 0, about 7% or less errors can be corrected. When set to 1, about 15% or less errors can be corrected. When set to 2, about 25% or less errors can be corrected. When set to 3, about 30% or less errors can be corrected. Default is 1.")]),t._v(" "),s("li",[s("code",[t._v("box_size")]),t._v(' - (Optional, int) How many pixels each "box" of the QR code is. Default is 10.')]),t._v(" "),s("li",[s("code",[t._v("border")]),t._v(" - (Optional, int) How many boxes thick the border should be. It should be a number greater than 4. Default is 4.")]),t._v(" "),s("li",[s("code",[t._v("image")]),t._v(" - (Optional, map) Advanced settings for the image generation.\n"),s("ul",[s("li",[s("code",[t._v("back_color")]),t._v(" - (Optional, str or tuple) The background color.")]),t._v(" "),s("li",[s("code",[t._v("fill_color")]),t._v(" - (Optional, str or tuple) The filling color.")])])])]),t._v(" "),s("h2",{attrs:{id:"attributes-reference"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#attributes-reference"}},[t._v("#")]),t._v(" Attributes Reference")]),t._v(" "),s("ul",[s("li",[s("code",[t._v("image")]),t._v(" - A PIL image instance.")])]),t._v(" "),s("h2",{attrs:{id:"references"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#references"}},[t._v("#")]),t._v(" References")]),t._v(" "),s("ul",[s("li",[s("RouterLink",{attrs:{to:"/tasks/tutorials/gen-wifi-password-qrcode.html"}},[t._v("Generate WiFi Credential QRCode Card")])],1)])])}),[],!1,null,null,null);e.default=r.exports}}]);