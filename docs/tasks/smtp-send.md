# SMTP Send Task

This task sends an email.

## Example Usage

<<< @/examples/smtp_send_example.hcl

## Argument Reference

* `subject` - (Required, str) The subject of email.
* `message` - (Optional, str) The content of email in plain text. Can be used with `html_message`.
* `html_message` - (Optional, str) The content of email in HTML. Can be used with `message`.
* `email_from` - (Required, str) The email sender's address.
* `email_to` - (Required, str) The email receiver's address.
* `email_to_cc` - (Optional, str) CC address.
* `email_to_bcc` - (Optional, str) BCC address.
* `attachments` - (Optional, List[str]) A list of paths to attachment files.
* `client` - (Required, map) The SMTP client.
  * `host` - (Required, str) The SMTP server address.
  * `port` - (Required, int) The SMTP server port.
  * `username` - (Required, str) The login username.
  * `password` - (Required, str) The login password.
  * `local_hostname` - (Optional, str) If specified, local_hostname is used as the FQDN of the local host in the HELO/EHLO command.
  * `timeout` - (Optional, int) The timeout in seconds.
  * `source_address` - (Optional, str) Allows binding to some specific source address in a machine with multiple network interfaces.
