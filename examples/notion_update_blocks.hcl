flow "notion_update_blocks" {
  variable "notion_token" {
    default = ""
  }

  task "notion_api_call" "append_blocks" {
    client = {
      auth = var.notion_token
    }
    api_method = "blocks.children.append"
    block_id = "ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea"
    children = [
      {
        object = "block",
        type = "heading_2",
        heading_2 = {
          text = [
            {
              type = "text",
              text = {
                content = "Runflow is awesome",
              },
            },
          ],
        },
      }
    ]
  }
}

