# File: template.hcl
flow "render-template" {

  variable "global" {
    default = "global"
  }

  task "hcl2_template" "this" {
    # Set the source for the template.
    # You can interpolate variable via `${...}` syntax.
    source = <<EOT
${ answer }
${ final.answer }
${ var.global }
${ 40 + 2 }
${ sum([20, 20, 2]) }
EOT

    # Set the context for the template rendering.
    # It will be merged with global context.
    context = {
      answer = 42
      final = {
        answer = 42
      }
    }
  }

  task "file_write" "this" {
    filename = "/dev/stdout"
    content = task.hcl2_template.this.content
  }
}

