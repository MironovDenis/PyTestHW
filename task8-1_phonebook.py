"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной

1. Вывод всех контактов
2. Поиск контакта
3. Добавить контакт (сразу сохранять в файл)
4. Выход по требованию пользователя

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

import os

def all_contacts():
    with open('phonebook.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)

def find_contact():
    name = input("Введите запрос поиска: ").title()
    with open('phonebook.txt', 'r', encoding='utf8') as data:
        trigger = 1 
        for line in data:
            if name in line:
                trigger = 0 
                print(line)
        if trigger:
            print('совпадений не найдено')

def add_contact():
    print('Введите новый контакт: ')
    with open('phonebook.txt', 'a', encoding='utf8') as data:
        data.write('\n' + input('Новый контакт: ').title())

def del_contact():
    name = input("Введите запрос на удаление: ").title()
    with open('phonebook.txt', 'r', encoding='utf8') as data:
        with open('phonebook_temp.txt', 'w', encoding='utf8') as new_data:
            for line in data:
                if name not in line:
                    new_data.write(line)
    with open('phonebook_temp.txt', 'r', encoding='utf8') as in_data:
        with open('phonebook.txt', 'w', encoding='utf8') as out_data:
            for line in in_data:
                out_data.write(line)
    path = "d:/GEEKBRAINS/Python/Sem_Test/phonebook_temp.txt"
    os.remove(path)

def correct_contact():
    name = input("Введите запрос на изменение: ").title()
    with open('phonebook.txt', 'r', encoding='utf8') as data:
        with open('phonebook_temp.txt', 'w', encoding='utf8') as new_data:
            for line in data:
                if name in line:
                    new_name = input("Введите корректные данные: ").title()
                    line = line.replace(name, new_name)
                    new_data.write(line)
                elif name not in line:
                    new_data.write(line)
    with open('phonebook_temp.txt', 'r', encoding='utf8') as in_data:
        with open('phonebook.txt', 'w', encoding='utf8') as out_data:
            for line in in_data:
                out_data.write(line)
    path = "d:/GEEKBRAINS/Python/Sem_Test/phonebook_temp.txt"
    os.remove(path)

def main_menu():
    while True:
        key = int(input('--> '))
        if key == 1:
            all_contacts()
        elif key == 2:
            find_contact()
        elif key == 3:
            add_contact()
        elif key == 4:
            del_contact()
        elif key == 5:
            correct_contact()
        elif key == 6:
            print("Выход")
            break
        else:
            print("Некорректный ввод")


print(  "- Нажмите 1 для вывода всех контактов\n"
        "- Нажмите 2 для поиска контактов\n"
        "- Нажмите 3 для добавления контакта\n"
        "- Нажмите 4 для удаления контакта\n"
        "- Нажмите 5 для изменения контакта\n"
        "- Нажмите 6 для выхода")
print()

main_menu()
