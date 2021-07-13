flow "qrcode_generate_color" {
  task "qrcode_generate" "runflow-org" {
    data = "https://runflow.org"
    filename = "/tmp/runflow-qrcode.png"
    image = {
      back_color = "pink"
      fill_color = tuple([55, 95, 35])
    }
  }
}
