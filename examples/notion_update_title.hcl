flow "notion_update_title" {
  variable "notion_token" {
    default = ""
  }

  task "notion_api_call" "update_title" {
    client = {
      auth = var.notion_token
    }
    api_method = "pages.update"
    page_id = "ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea"
    properties = {
      "title": {
        "id": "title",
        "type": "title",
        "title": [
          {
            "type": "text",
            "text": {
              "content": "Runflow Test"
            }
          }
        ]
      }
    }
  }
}
