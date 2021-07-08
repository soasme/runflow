flow "pushbullet_push_link" {

  variable "pushbullet_api_key" {}

  task "pushbullet_push" "link" {
    title = "This is the title"
    url = "https://runflow.org"
    client = {
      api_key = var.pushbullet_api_key
    }
  }
}
