# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
# import random
#
# STR_CHAR = 'abcdefghijklmnopqrstuvwxyz'
#
#
# def main():
#     # expansion = input('Введите желаемое расширение -> ')
#     len_name = int(input('Введите длину имени файла -> '))
#     file_length = int(input('Введите число желаемых байт -> '))
#     print(gen_name(len_name))
#
#
# def gen_name(length):
#     if 6 < length < 31:
#         filename = random.sample(STR_CHAR, length)
#         name = ''
#         for i in range(len(filename)):
#             name = name + filename[i]
#         return name
#
#
# def gen_bite():
#
#
# if __name__ == "__main__":
#     main()

from random import choices, randint
from string import ascii_letters, digits
import os


def make_files(extension: str, min_name: int = 6, max_name: int = 30,
               min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    make_files('txt', count=1)
