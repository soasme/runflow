flow "papermill_example" {
  variable "output_dir" {
    default = "/tmp"
  }
  task "papermill_execute" "this" {
    input_path = "examples/sysexit0.ipynb"
    output_path = "${var.output_dir}/sysexit0-out.ipynb"
  }
}
