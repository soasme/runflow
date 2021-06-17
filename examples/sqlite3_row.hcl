# File: sqlite3_row
flow "sqlite3_row" {

  variable "db" {
    default = ":memory:"
  }

  task "sqlite3_row" "k1" {
    dsn = var.db
    sql = "SELECT * FROM kvdb where key=?;"
    parameters = ["k1"]
    exec_many = false
  }

  task "sqlite3_row" "kall" {
    dsn = var.db
    sql = "SELECT * FROM kvdb limit 20;"
    exec_many = true
  }

  task "bash_run" "echo" {
    command = "echo 'k1: ${task.sqlite3_row.k1.rows[0][1]}\nkall: ${tojson(task.sqlite3_row.kall.rows)}'"
  }
}
