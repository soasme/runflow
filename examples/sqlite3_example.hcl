# File: sqlite3_example
flow "sqlite3_example" {

  variable "db" {
    default = ":memory:"
  }

  task "sqlite3_exec" "create_table" {
    dsn = var.db
    sql = <<EOT
    CREATE TABLE IF NOT EXISTS kvdb (
        key string PRIMARY KEY,
        value string
    );
EOT
  }

  task "sqlite3_exec" "insert_many" {
    dsn = var.db
    sql = "INSERT OR IGNORE INTO kvdb (key,value) VALUES (?, ?);"
    parameters = [
      ["k1", "v1"],
      ["k2", "v2"],
    ]
    exec_many = True
  }

  task "sqlite3_exec" "insert_one" {
    dsn = var.db
    sql = "INSERT OR IGNORE INTO kvdb (key,value) VALUES (?, ?);"
    parameters = [
      "k3", "v3",
    ]
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

  task "template" "kall" {
    source = "${task.sqlite3_row.kall.rows | tojson }"
  }

  task "command" "print_k1" {
    command = "echo 'k1: ${task.sqlite3_row.k1.rows[0][1]}'"
  }

  task "command" "print_all" {
    command = "echo ${task.template.kall.content}"
  }
}
