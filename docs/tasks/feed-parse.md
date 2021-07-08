---
sidebar: auto
---

# Feed Parse Task

This task parses a RSS feed.

Added since v0.9.0.

::: tip
This feature requires installing feedparser:
```bash
$ pip install runflow[rss]
```
:::

## Example Usage

Set `url` of the RSS feed.

<<< @/examples/feed_parse_example.hcl

::: details Click to view the output
Run:
```bash
[2021-07-08 21:50:11,722] "task.feed_parse.paulgraham" is started.
[2021-07-08 21:50:12,258] "task.feed_parse.paulgraham" is successful.
[2021-07-08 21:50:12,259] "task.file_write.out" is started.
{
  "website": "Paul Graham: Essays",
  "latest_article_title": "How to Work Hard",
  "latest_article_url": "http://www.paulgraham.com/hwh.html"
}
[2021-07-08 21:50:12,260] "task.file_write.out" is successful.
```
:::

## Argument Reference

* `url` - (Required, str) The URL of RSS feed.
* `etag` - (Optional, str) HTTP `ETag` request header.
* `modified` - (Optional, Union[str, datetime, struct_time]) HTTP `Last-Modified` request header.
* `agent` - (Optional, str) HTTP `User-Agent` request header.
* `referrer` - (Optional, str) HTTP `Referrer` request header.
* `request_headers` - (Optional, map) A mapping of HTTP header name to HTTP header value to add to the request, overriding internally generated values.
* `response_headers` - (Optional, map) A mapping of HTTP header name to HTTP header value. Multiple values may be joined with a comma. If a HTTP request was made, these headers override any matching headers in the response. Otherwise this specifies the entirety of the response headers.
* `resolve_relative_uris` - (Optional, bool) Whether to resolve relative uris in the page content.
* `sanitize_html` - (Optional, bool) Whetherto sanitize HTML content.

## Attributes Reference

* `feed` - The RSS feed information, depending on the information provided in the feed, you may have these information:
  * `title` - The title of RSS feed.
  * `description` - The description of RSS feed.
  * `link` - The link of RSS feed.
  * and more.
* `entries` - An array of RSS feed `<item></item>`  For each entry, you may have these information:
  * `title` - The title of RSS feed item.
  * `link` - The link of RSS feed item.
  * `published` - Whether the RSS feed item is published.
  * `id` - The id of RSS feed item.
  * and more.
