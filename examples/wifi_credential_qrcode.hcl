flow "wifi-credential-qrcode" {

  variable "ssid" {
    default = "default"
  }

  variable "password" {
    default = "default"
  }

  variable "encryption" {
    default = "WPA2"
  }

  variable "output" {
    default = "/tmp/credential.png"
  }

  task "hcl2_template" "login" {
    source = "WIFI:S:${var.ssid};T:${var.encryption};P:${var.password};;"
  }

  task "qrcode_generate" "card" {
    data = task.hcl2_template.login.content
    filename = var.output
  }
}
