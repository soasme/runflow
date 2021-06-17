# File: sqlite3_exec.hcl
flow "sqlite3_exec" {

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
    exec_many = true
  }

  task "sqlite3_exec" "insert_one" {
    dsn = var.db
    sql = "INSERT OR IGNORE INTO kvdb (key,value) VALUES (?, ?);"
    parameters = [
      "k3", "v3",
    ]
  }
}
