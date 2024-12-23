import sqlite3


def get_book_info():
    title = input("请输入图书标题: ")
    author = input("请输入图书作者: ")
    publication_date = input("请输入出版日期 (YYYY-MM-DD): ")
    return title, author, publication_date


def validate_input(title, author, publication_date):
    if not title or not author or not publication_date:
        return False
    # 可以添加更复杂的验证，例如检查日期格式是否正确
    return True


def insert_book(db_connection, title, author, publication_date):
    try:
        query = "INSERT INTO books (title, author, publication_date) VALUES (?,?,?)"
        db_connection.execute_query(query, (title, author, publication_date))
        print("图书信息已成功录入！")
    except sqlite3.Error as e:
        print(f"录入图书信息时出错: {e}")