import sqlite3


class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"成功连接到数据库 {self.db_file}")
        except sqlite3.Error as e:
            print(f"连接数据库时出错: {e}")
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            print(f"已关闭数据库 {self.db_file} 的连接")

    def cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()