import sqlite3


class initTable:
    def __init__(self,connection):
        self.__create_tables(connection)
    def __create_tables(self,conn):
        cursor = conn.cursor()
        try:
            # 创建图书信息表
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT,
                    publisher TEXT,
                    author TEXT,
                    status TEXT,
                    UNIQUE (title, author)
                )
            ''')
            print("图书信息表创建成功或已存在。")

            # 创建学生信息表
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_name TEXT NOT NULL
                )
            ''')
            print("学生信息表创建成功或已存在。")

            # 创建借阅信息表
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS borrow_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER,
                    student_id INTEGER,
                    operation TEXT NOT NULL,
                    time TEXT NOT NULL,
                    FOREIGN KEY (book_id) REFERENCES books(book_id),
                    FOREIGN KEY (student_id) REFERENCES students(student_id)
                )
            ''')
            print("借阅信息表创建成功或已存在。")

            conn.commit()
        except sqlite3.Error as e:
            print(f"创建表时出错: {e}")
            conn.rollback()