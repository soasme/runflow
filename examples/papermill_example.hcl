flow "papermill_example" {
  variable "input_dir" {
    default = "/tmp"
  }
  variable "output_dir" {
    default = "/tmp"
  }
  task "papermill_execute" "this" {
    input_path = "${var.input_dir}/sysexit0.ipynb"
    output_path = "${var.output_dir}/sysexit0-out.ipynb"
  }
}
