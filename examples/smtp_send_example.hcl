# File: examples/smtp_send_example.hcl

flow "smtp_send_example" {

  variable "smtp_username" {}

  variable "smtp_password" {}

  task "smtp_send" "gmail" {
    email_from = "alice@example.org"
    email_to = "bob@example.org"
    email_to_cc = "charlie@example.org"
    email_to_bcc = "david@example.org"

    subject = "Sent from Runflow smtp_send task"
    message = "Hello, this mail is sent from Runflow smtp_send task"
    html_message = <<-EOT
      <h1>HTML Message</h1>
      <p>Hello, this mail is sent from Runflow smtp_send task</p>
    EOT

    client = {
      host = "smtp.gmail.com"
      port = 465
      username = var.smtp_username
      password = var.smtp_password
      timeout = 30
    }
  }
}
