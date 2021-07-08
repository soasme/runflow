flow "telegram_send_message" {

  variable "telegram_token" {}
  variable "chat_id" {}

  task "telegram_api_call" "this" {
    client = {
      token = var.telegram_token
    }
    api_method = "send_message"

    chat_id = var.chat_id
    text = "Hello World! - Send From Runflow"
    timeout = 10
  }

}
