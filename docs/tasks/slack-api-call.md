---
sidebar: auto
---

# Slack API Call

This task enables interacting with Slack Web API.

::: tip
This feature requires installing slack-sdk:
```bash
$ pip install runflow[slack]
```
:::

## Send Slack Message to a Channel

To send a slack message to a channel,

* Set `client.token` for authentication:
* Set `api_method` to `"chat.postMessage"`.
* Set `channel`.
* Set `text`.

For example, this flow can extract the latest version of package `runflow` from PyPI and then send a slack message:

<<< @/examples/slack_send_message.hcl{28,29,30}

The slack channel will receive a new message:

![preview of the slack message](/images/slack-send-message-example.png)

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/slack_send_message.hcl --var slack_token=${SLACK_TOKEN}
[2021-07-05 21:04:29,553] "task.http_request.extract_metadata" is started.
[2021-07-05 21:04:29,633] "task.http_request.extract_metadata" is successful.
[2021-07-05 21:04:29,634] "task.hcl2_template.transform_metadata" is started.
[2021-07-05 21:04:29,634] "task.hcl2_template.transform_metadata" is successful.
[2021-07-05 21:04:29,634] "task.slack_api_call.notify_version" is started.
[2021-07-05 21:04:30,285] "task.slack_api_call.notify_version" is successful.
[2021-07-05 21:04:30,286] "task.file_write.output_slack_response" is started.
{'ok': True, 'channel': 'C0HD36738', 'ts': '1625475870.000600', 'message': {'bot_id': 'B026ZLQFHPX', 'type': 'message', 'text': 'Latest version of runflow is 0.8.0.', 'user': 'U026VUUC4VC', 'ts': '1625475870.000600', 'team': 'T0HCXJS4C', 'bot_profile': {'id': 'B026ZLQFHPX', 'deleted': False, 'name': 'Test Runflow', 'updated': 1625475649, 'app_id': 'A027FABBGU9', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'team_id': 'T0HCXJS4C'}}}
[2021-07-05 21:04:30,288] "task.file_write.output_slack_response" is successful.
```
:::

## Argument Reference

* `api_method` - (Required, str) The API method, for example, `chat.postMessage`. See the full [methods](https://api.slack.com/methods) page.
* The rest of the arguments are defined on the exact section of the [slack-sdk](https://slack.dev/python-slack-sdk/api-docs/slack_sdk/web/client.html) page. For example, when the `api_method` is `chat.postMessage`, you should set:
  * `channel` - (Required, str) The channel id. e.g. 'C1234567890'.
  * `text` - (Optional, str) The message you'd like to share. The text is not required when presenting blocks.
  * `blocks` - (Optional, list) A list of either dict values. Blocks are required when not presenting text. e.g. [{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]
* `client` - (Required, map) The client settings. See [client](#Client).
  * `token` - (Required, str) The slack token. The corresponding app of the token should have the scope properly setup.
  * `base_url` - (Optional, str) Default to `"https://www.slack.com/api/"`.
  * `timeout` - (Optional, int) Default to 30 seconds.
  * `headers` - (Optional, dict) The request headers.
  * `user_agent_prefix` - (Optional, str) The prefix for `User-Agent`.
  * `user_agent_sufix` - (Optional, str) The suffix for `User-Agent`.

## Attributes Reference

* `response` - Response object provided by slack-sdk.
  * You can check `response.ok` to see if the slack message is sent.
