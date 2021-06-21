# File: sqlite3_exec.hcl
flow "sqlite3_exec" {

  variable "db" {
    default = "sqlite:///:memory:"
  }

  task "sql_exec" "create_table" {
    dsn = var.db
    sql {
      statement = <<-EOT
        CREATE TABLE IF NOT EXISTS kvdb (
            key string PRIMARY KEY,
            value string
        );
      EOT
    }
  }

  task "sql_exec" "insert_many" {
    dsn = var.db
    sql {
      statement = "INSERT OR IGNORE INTO kvdb (key,value) VALUES (:key, :value);"
      parameters =  [
        {
          key = "k1"
          value = "v1"
        },
        {
          key = "k2"
          value = "v2"
        },
      ]
    }

    sql {
      statement = "INSERT OR IGNORE INTO kvdb (key,value) VALUES (:key, :value);"
      parameters = {
        key = "k3"
        value = "k3"
      }
    }
  }
}
