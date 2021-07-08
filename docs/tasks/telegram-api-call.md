---
sidebar: auto
---

# Telegram API Call Task

This task can interact with Telegram API.

## Example: Send Telegram Message

<<< @/examples/telegram_send_message.hcl

The telegram bot will send you a new message:

![preview of the telegram message](/images/telegram-send-message-example.png)

::: details Click me to view the run output
Run:
```bash
$ runflow run examples/telegram_send_message.hcl --var telegram_token=$TELEGRAM_TOKEN --var chat_id=$CHAT_ID
[2021-07-08 23:14:41,337] "task.telegram_api_call.this" is started.
[2021-07-08 23:14:42,602] "task.telegram_api_call.this" is successful.
```
:::

## Argument Reference

* `api_method` - (Required, str) The API method, for example `send_message`. See the full [methods](https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html) page.
* The rest of the arguments are the method parameters of the corresponding `api_method` listed on the [page](https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html). For example, when the `api_method` is [`send_message`](https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram.Bot.send_message), you should set:
  * `chat_id` - (Required, int or str) Unique identifier for the target chat or username of the target channel (in the format @channelusername).
  * `text` - (Required, str) Text of the message to be sent.
  * `parse_mode` - (Optional, str) Send Markdown or HTML.
  * ...
* `client` - (Required, map) The client settings.
  * `token` - (Required, str) The token for telegram bot.
  * `base_url` - (Optional, str) Telegram Bot API service URL.
  * `base_file_url` - (Optional, str) Telegram Bot API file URL.

## Attributes Reference

* `result` - The returning value of Telegram bot method call.
