flow "slack_send_message" {

  variable "package" {
    default = "runflow"
  }

  variable "slack_token" {
    default = ""
  }

  task "http_request" "extract_metadata" {
    method = "GET"
    url = "https://pypi.org/pypi/${var.package}/json"
    timeout = 5
  }

  task "hcl2_template" "transform_metadata" {
    source = metadata.info.version
    context = {
      metadata = call(task.http_request.extract_metadata.response, "json")
    }
  }

  task "slack_api_call" "notify_version" {
    client = {
      token = var.slack_token
    }
    api_method = "chat.postMessage"
    channel = "#random"
    text = "Latest version of ${var.package} is ${task.hcl2_template.transform_metadata.content}."
  }

  task "file_write" "output_slack_response" {
    filename = "/dev/stdout"
    content = task.slack_api_call.notify_version.response
  }

}
