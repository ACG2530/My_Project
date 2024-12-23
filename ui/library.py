import os

from db.connection import DatabaseConnection
from db.create_table import initTable


class Library:
    def __init__(self):
        self.__db_init()
    def __db_init(self):
        self.db_connection = DatabaseConnection("library.db")
        self.connect = self.db_connection.connect()
        initTable(self.connect)

    def __clear_screen(self):
        os.system('cls')

    def __input_book_info(self):
        c

        print("录入图书信息功能待实现")

    def __search_book_info(self):
        # 实现查询图书信息的逻辑
        print("查询图书信息功能待实现")

    def __delete_book_info(self):
        # 实现删除图书信息的逻辑
        print("删除图书信息功能待实现")

    def __modify_book_info(self):
        # 实现修改图书信息的逻辑
        print("修改图书信息功能待实现")

    def __borrow_book(self):
        # 实现图书借阅的逻辑
        print("图书借阅功能待实现")

    def __return_book(self):
        # 实现图书归还的逻辑
        print("图书归还功能待实现")

    def __rank_borrow_info(self):
        # 实现借阅信息排行的逻辑
        print("借阅信息排行功能待实现")

    def __add_student_info(self):
        # 实现添加学生信息的逻辑
        print("添加学生信息功能待实现")

    def __exit_system(self):
        print("退出系统")
        self.__clear_screen()
        exit(0)

    def __show_menu(self):
        print("=" * 24 + "图书信息管理系统" + "=" * 24)
        print("\t" * 3+"1.录入图书信息")
        print("\t" * 3+"2.查询图书信息")
        print("\t" * 3+"3.删除图书信息")
        print("\t" * 3+"4.修改图书信息")
        print("\t" * 3+"5.图书借阅")
        print("\t" * 3+"6.图书归还")
        print("\t" * 3+"7.借阅信息排行")
        print("\t" * 3+"8.添加学生信息")
        print("\t" * 3+"0.退出系统")
        print("=" * 64)
    def run(self):
        while True:
            # self.__clear_screen()
            self.__show_menu()
            try:
                choice = int(input("请输入你的选择："))
                if choice == 1:
                    self.__input_book_info()
                elif choice == 2:
                    self.__search_book_info()
                elif choice == 3:
                    self.__delete_book_info()
                elif choice == 4:
                    self.__modify_book_info()
                elif choice == 5:
                    self.__borrow_book()
                elif choice == 6:
                    self.__return_book()
                elif choice == 7:
                    self.__rank_borrow_info()
                elif choice == 8:
                    self.__add_student_info()
                elif choice == 0:
                    self.__exit_system()
                else:
                    print("无效的选择，请重新输入！")
            except ValueError:
                print("请输入数字！")

            input("按回车键继续...")


