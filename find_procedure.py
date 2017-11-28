# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def get_list_of_sql(): # Ф-ия генерирует исходный список состоящий из *.sql файлов
    lst = os.listdir(path=os.path.join(current_dir, migrations))
    list_of_file = []
    for file_type in lst:
        if 'sql' in file_type:
            list_of_file.append(file_type)
    return list_of_file

def list_upgrade(lst): # Ф-ия создает список состоящий из файлов содержащих строку
    name = input('Введите строку:')
    new_list = []
    for i in lst:
        if name in i:
            new_list.append(i)
        else:
            pass
    return new_list

def show_list_and_len(lst): # Ф-ия выводит значения из списка и колличество значений в списке
    for i in lst:
        print(i)
    print('Всего: {}'.format(len(lst)))

if __name__ == '__main__':
    # ваша логика

    my_list = get_list_of_sql()

    while True:
        new_list = list_upgrade(my_list)
        my_list = new_list
        show_list_and_len(my_list)
        if len(my_list) == 0:
            break
    print('Программа завершена.')

    pass
