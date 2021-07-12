flow "papermill_example" {
  task "papermill_execute" "this" {
    input_path = "/tmp/sysexit0.ipynb"
    output_path = "/tmp/sysexit0-out.ipynb"
  }
}
