---
sidebar: auto
---

# Http Request Task

Http Request Task enables fetching data from an http url.

Added in v0.4.0.

## Basic Usage (GET)

* Task type: `http_request`
* Provide method, url, timeout, headers, params.

<<< @/examples/http_get.hcl

Run:

```
$ runflow run http_get.hcl --var out=/tmp/out.txt
[2021-06-12 21:44:06,597] "task.http_request.this" is started.
[2021-06-12 21:44:07,461] "task.http_request.this" is successful.
[2021-06-12 21:44:07,478] "task.file_write.this" is started.
[2021-06-12 21:44:07,481] "task.file_write.this" is successful.

$ jq '[.name, .full_name]' /tmp/out.txt
[
  "runflow",
  "soasme/runflow"
]
```

## Basic Usage (POST)

* Task type: `http_request`
* Provide method, url, timeout, headers, json or data (can only provide one of json or data).

<<< @/examples/http_post.hcl

Run:

```
$ runflow run http_post.hcl --var out=/tmp/out.txt
[2021-06-12 21:50:00,090] "task.file_read.this" is started.
[2021-06-12 21:50:00,092] "task.file_read.this" is successful.
[2021-06-12 21:50:00,193] "task.http_request.this" is started.
[2021-06-12 21:50:01,053] "task.http_request.this" is successful.
[2021-06-12 21:50:01,055] "task.file_write.this" is started.
[2021-06-12 21:50:01,058] "task.file_write.this" is successful.

$ cat /tmp/out.txt
<h1>
<a id="user-content-runflow" class="anchor" href="#runflow" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Runflow</h1>
...(truncated)
<p>Please report an issue at: <a href="https://github.com/soasme/runflow/issues">https://github.com/soasme/runflow/issues</a>.</p>
```

## Argument Reference

The following arguments are supported:

* `method` - (Required, str) The HTTP request method. One of `"GET"`, `"POST"`, `"PUT"`, `"DELETE"`, `"PATCH"`.
* `url` - (Required, str) The HTTP request url.
* `headers` - (Optional, map) The HTTP request headers.
* `json` - (Optional, map) The HTTP request JSON data. Must not be used with `data`.
* `data` - (Optional, map) The HTTP request form data. Must not be used with `json`.
* `timeout` - (Optional, int) The timeout on HTTP connection.

The following attributes are supported:

* `response` - The [httpx.Response object](https://www.python-httpx.org/quickstart/).

Here lists some possible variable references you may use in other tasks:

* `task.http_request.TASK_NAME.response.content` - Get HTTP response binary content.
* `task.http_request.TASK_NAME.response.encoding` - Get HTTP response encoding.
* `task.http_request.TASK_NAME.response.text` - Get HTTP response text.
* `call(task.http_request.TASK_NAME.response, "json")` - Get HTTP response json object.
* `task.http_request.TASK_NAME.response.status_code` - Get HTTP response status code.
* `task.http_request.TASK_NAME.response.headers.content-type` - Get HTTP response status code.
* `task.http_request.TASK_NAME.response.cookies.session-id` - Get HTTP response cookie.
