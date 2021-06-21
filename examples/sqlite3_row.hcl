# File: sqlite3_row
flow "sqlite3_row" {

  variable "db" {
    default = "sqlite3://:memory:"
  }

  task "sql_row" "k1" {
    dsn = var.db
    sql {
      statement = "SELECT * FROM kvdb where key=:key"
      parameters = { key = "k1" }
    }
  }

  task "sql_row" "kall" {
    dsn = var.db
    sql {
      statement = "SELECT * FROM kvdb limit 20"
    }
  }

  task "file_write" "out" {
    filename = "/dev/stdout"
    content = tojson({
      k1 = task.sql_row.k1.rows
      kall = task.sql_row.kall.rows
    })
  }
}
