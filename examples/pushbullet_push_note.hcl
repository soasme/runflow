flow "pushbullet_push_note" {

  variable "pushbullet_api_key" {}

  task "pushbullet_push" "note" {
    title = "This is the title"
    body = "This is the note"
    client = {
      api_key = var.pushbullet_api_key
    }
  }
}
