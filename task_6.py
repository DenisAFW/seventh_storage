# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import stat
from random import choices, randint
from string import ascii_letters, digits
import os
from pathlib import Path


def make_files_on_dir(extension: str, min_name: int = 6, max_name: int = 30,
                      min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

        with open(f'{name}.{extension}', 'wb', ) as f:
            f.write(data)
    fullname = f'{name}.{extension}'
    os.rename(fullname, f'results/{fullname}')


if __name__ == '__main__':
    make_files_on_dir('txt', count=1)
