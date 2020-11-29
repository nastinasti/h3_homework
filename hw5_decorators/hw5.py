# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида "test string" в "<i><b>test string</b></i>"

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            for item in tag_base:
                if item in tags:
                    data = tag_base.get(item)
                    data = data.replace("%text%", text)
                    text = data
            print(text)

        return wrapper

    return decorator


@str_to_html(["italic", "bold", "underline"])
def get_text(text):
    return text


get_text("Hey ho alley")
get_text("Python is just perfectly splendid")

# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

import os


def log_reading(func):
    def wrapper(*args):
        directory = func()
        for file in os.listdir(directory):
            if file.endswith(".log"):
                print(os.path.join(file))

    return wrapper


@log_reading
def get_files():
    file_list = '/home/anastasiia/Desktop/python/hw/h3_homework/homework5_decorators_practice'
    return file_list


log_reading(get_files())
