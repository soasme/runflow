flow "qrcode_generate_example" {
  task "qrcode_generate" "runflow-org" {
    data = "https://runflow.org"
    filename = "/tmp/runflow-qrcode.png"
  }
}
