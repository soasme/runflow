# File: file_read_from_git.hcl
flow "file_read_from_git" {

  task "file_read" "this" {
    filename = "requirements-dev.txt"

    fs = {
      # Set fs.protocol to "git"
      protocol = "git"

      # Set fs.path to the path to the git repo.
      path = "."

      # Set fs.ref to a valid Git sha, such as hash, tag, branch, HEAD, etc.
      # This is optional.
      ref = "26551afd8"
    }
  }

  task "file_write" "this" {
    filename = "/dev/stdout"
    content = task.file_read.this.content
  }

}
