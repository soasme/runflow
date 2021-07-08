flow "pushbullet_push_file" {

  variable "pushbullet_api_key" {}

  task "pushbullet_push" "file" {
    title = "This is the title"
    body = "This is the body"
    file_type = "image/jpeg"
    file_name = "cat.jpg"
    file_url = "https://i.imgur.com/IAYZ20i.jpg"
    client = {
      api_key = var.pushbullet_api_key
    }
  }
}
