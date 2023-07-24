# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from task_4 import make_files

data = {
    'txt': 2,
    'zip': 3,
}


def new_make_files(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


print(new_make_files(data))
