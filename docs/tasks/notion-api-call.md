---
sidebar: auto
---

# Notion API Call

This task lets you interact with [Notion](https://notion.so).

Added since v0.10.0

::: tip
This feature requires installing `notion-client`:
```bash
$ pip install runflow[notion]
```
:::

## Authentication

You can create an integration through <https://www.notion.so/my-integrations>.

When a new integration is created, you should be able to obtain a new "Internal Integration Token". Click "Show" to display it.

![screenshot of getting a new internal integration token](/images/notion-integration.png)

Additionally, you should share "Can Edit" permission for the parent page with the Integration you just created.

![screenshot of sharing permission](/images/notion-share.png)

## Example Usage: Update Page Title

* Set `client.auth` with a Notion Integration Token.
* Set `api_method` to `pages.update`.
* Set `page_id` to the ID of the page. In case you're struggling with find the ID of the page, copy the page url, and you will have something like `https://www.notion.so/soasme/Runflow-Test-ee5b6cd7a7a340d79ae5ae28c52b67ea`. Turn the last bit of information `ee5b6cd7a7a340d79ae5ae28c52b67ea` into 8-4-4-4-12 form, e.g. `ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea`.
* Set `properties`. It's strongly recommended you read the Notion documentation [Working with page content](https://developers.notion.com/docs/working-with-page-content) first. You will have a basic understanding of properties then.

<<< @/examples/notion_update_title.hcl

::: details Click me to view the run output
Run
```bash
$ read -s RUNFLOW_VAR_notion_token
**********
$ export RUNFLOW_VAR_notion_token
$ runflow run examples/notion_update_title.hcl
[2021-07-12 22:14:43,328] "task.notion_api_call.update_title" is started.
[2021-07-12 22:14:44,358] "task.notion_api_call.update_title" is successful.
```
:::

## Arguments Reference

* `api_method` - (Required, str) The API methods. Choices include
  * `"blocks.append"`
  * `"blocks.list"`
  * `"databases.list"`
  * `"databases.query"`
  * `"databases.retrieve"`
  * `"pages.list"`
  * `"pages.create"`
  * `"pages.retrieve"`
  * `"pages.update"`
  * `"users.retrieve"`
  * `"users.list"`
  * `"users.list"`
  * `"search"`
* The rest of arguments are the parameters for the `api_method`. For the full reference, please check <https://developers.notion.com/reference/intro>. For example, when the `api_method` is [pages.update](https://developers.notion.com/reference/patch-page), the arguments include
  * `page_id` - (Required, str) The page ID.
  * `properties` - (Required, map) The page properties.
  * `archived` - (Optional, bool) Set to true to archive (delete) a page. Set to false to un-archive (restore) a page.
* `client` - (Required, map) The client settings.
  * `auth` - (Required, string) The Notion integration token.
  * `timeout_ms` - (Optional, int) The timeout in ms. Default is 60_000ms.
  * `base_url` - (Optional, str) The notion base url. Default is `"https://api.notion.com"`.
  * `notion_version` - (Optional, str) The notion API version.
