# File: template.hcl
flow "render-template" {
  variable "out" {
    default = ""
  }

  task "template" "this" {
    source = <<EOT
${ answer }
${ final.answer }
${ var.out }
EOT
    context = {
      answer = 42
      final = {
        answer = 42
      }
    }
  }

  task "file_write" "this" {
    filename = var.out
    content = task.template.this.content
  }
}

