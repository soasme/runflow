---
sidebar: auto
---

# Pushbullet Push Task

This task sends a push notification to Android devices.

Added since v0.9.0.

::: tip
This feature requires installing pushbullet.py:
```bash
$ pip install runflow[pushbullet]
```
:::

## Example: Push Note

<<< @/examples/pushbullet_push_note.hcl

## Example: Push Link

<<< @/examples/pushbullet_push_link.hcl

## Example: Push File

<<< @/examples/pushbullet_push_file.hcl

## Argument Reference

* `title` - (Required, str) The title of notification.
* `body` - (Optional, str) The body of notification.
* `url` - (Optional, str) The url of notification. If present, the push type is `link`.
* `file_type` - (Optional, str) The type of attached file. Example value: `"image/png"`, `"image/jepg"`, etc. If present, the push type is `file`.
* `file_name` - (Optional, str) The name of attached file. Example value: `"cat.jpg"`. If present, the push type is `file`.
* `file_url` - (Optional, str) The url of attached file. Example value: `"https://i.imgur.com/IAYZ20i.jpg"`. If present, the push type is `file`.
* `channel` - (Optional, str) If specified, the recipient is the given channel filtered by name.
* `email` - (Optional, str) If specified, the recipient is the given chat filtered by email.
* `client` - (Required, map) The Pushbullet client.
  * `api_key` - (Required, str) The API key.
  * `https_proxy` - (Optional, str) The proxy url. Must be in HTTPS.

## Attributes Reference

* `iden` - The identity of push object.
