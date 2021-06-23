# File: file_read_from_github.hcl
flow "file_read_from_github" {

  task "file_read" "this" {
    filename = "requirements-dev.txt"

    fs = {
      # Set fs.protocol to "github"
      protocol = "github"

      # Set fs.org to the github organization
      org = "soasme"

      # Set fs.repo to the github repository
      repo = "runflow"

      # Set fs.sha to a valid Git sha, such as hash, tag, branch, HEAD, etc.
      # This is optional.
      sha = "v0.5.0"
    }
  }

  # Output to the console
  task "file_write" "this" {
    filename = "/dev/stdout"
    content = task.file_read.this.content
  }

}

