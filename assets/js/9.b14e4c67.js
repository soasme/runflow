(window.webpackJsonp=window.webpackJsonp||[]).push([[9],{366:function(t,e,a){"use strict";a.r(e);var s=a(44),o=Object(s.a)({},(function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h1",{attrs:{id:"built-in-functions"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#built-in-functions"}},[t._v("#")]),t._v(" Built-In Functions")]),t._v(" "),a("h2",{attrs:{id:"datetime"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#datetime"}},[t._v("#")]),t._v(" "),a("code",[t._v("datetime()")])]),t._v(" "),a("p",[a("code",[t._v("datetime()")]),t._v(" takes year, month, day, hour, minute, second, microsecond to construct a\n"),a("a",{attrs:{href:"https://docs.python.org/3/library/datetime.html#datetime-objects",target:"_blank",rel:"noopener noreferrer"}},[a("code",[t._v("datetime.datetime")]),a("OutboundLink")],1),t._v(".")]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v("> datetime(2020, 1, 1)\ndatetime(2020, 1, 1, 0, 0, 0)\n\n> datetime(2020, 1, 1, 0, 0, 0)\ndatetime(2020, 1, 1, 0, 0, 0)\n")])])]),a("p",[t._v("Note this function creates a Naive datetime object.")]),t._v(" "),a("h2",{attrs:{id:"todatetime"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#todatetime"}},[t._v("#")]),t._v(" "),a("code",[t._v("todatetime()")])]),t._v(" "),a("p",[a("code",[t._v("todatetime()")]),t._v(" takes a string to construct a\n"),a("a",{attrs:{href:"https://docs.python.org/3/library/datetime.html#datetime-objects",target:"_blank",rel:"noopener noreferrer"}},[a("code",[t._v("datetime.datetime")]),a("OutboundLink")],1),t._v(".")]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> todatetime("2020-01-01T00:00:00Z")\ndatetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)\n')])])]),a("h2",{attrs:{id:"call"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#call"}},[t._v("#")]),t._v(" "),a("code",[t._v("call()")])]),t._v(" "),a("p",[a("code",[t._v("call()")]),t._v(" takes four parameters.")]),t._v(" "),a("ol",[a("li",[t._v("The object.")]),t._v(" "),a("li",[t._v("The method name of object.")]),t._v(" "),a("li",[t._v("The list of arguments (optional).")]),t._v(" "),a("li",[t._v("The keyword of arguments (optional).")])]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> call("xyz", "upper")\n"XYZ"\n\n> call("xyz.abc", "replace", ["abc", "ABC"], {})\n"XYZ.ABC"\n')])])]),a("h2",{attrs:{id:"tojson"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#tojson"}},[t._v("#")]),t._v(" "),a("code",[t._v("tojson()")])]),t._v(" "),a("p",[a("code",[t._v("tojson()")]),t._v(" takes one parameter and formats it in JSON.")]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> tojson({ key = "value" })\n"{\\"key\\": \\"value\\"}"\n')])])]),a("p",[a("code",[t._v("tojson()")]),t._v(" supports more controlling parameters using "),a("code",[t._v("...")]),t._v(" syntax.")]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("p",[t._v("Set indentation "),a("code",[t._v("indent")]),t._v(":")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> tojson({ key = "value" }, { indent = 2 }...)\n"{\\n  \\"key\\": \\"value\\"\\n}"\n')])])]),a("p",[t._v("Set separators "),a("code",[t._v("separators")]),t._v(":")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> tojson([1,2,3], {separators=[",  ", ":  "]}...)\n"[1,  2,  3]"\n')])])]),a("p",[t._v("Sort keys "),a("code",[t._v("sort_keys")]),t._v(":")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> tojson({ "k2": 2, "k1": 1 }, { sort_keys = true }...)\n"{\\"k1\\": 1, \\"k2\\": 2}"\n')])])]),a("h2",{attrs:{id:"concat"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#concat"}},[t._v("#")]),t._v(" "),a("code",[t._v("concat()")])]),t._v(" "),a("p",[a("code",[t._v("concat()")]),t._v(" concats multiple lists.")]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> concat(["echo"], ["hello", "world"])\n["echo", "hello", "world"]\n')])])]),a("h2",{attrs:{id:"join"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#join"}},[t._v("#")]),t._v(" "),a("code",[t._v("join()")])]),t._v(" "),a("p",[a("code",[t._v("join()")]),t._v(" joins multiple strings by a separator.")]),t._v(" "),a("p",[t._v("Examples:")]),t._v(" "),a("div",{staticClass:"language- extra-class"},[a("pre",{pre:!0,attrs:{class:"language-text"}},[a("code",[t._v('> join(" ", ["echo", "hello", "world"])\n"echo hello world"\n')])])])])}),[],!1,null,null,null);e.default=o.exports}}]);