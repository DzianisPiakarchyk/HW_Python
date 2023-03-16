from controller import phone_book


def greetings():
    print('╔════════════════════════════════════════════════╗')
    print('║ Добро пожаловать в телефонный справочник v1.0! ║')
    print('╚════════════════════════════════════════════════╝')


def menu():
    print("""
1 - Добавить новую запись
2 - Вывести список записей
3 - Изменить существующую запись
4 - Удалить запись
5 - Поиск по фамилии, имени или номеру телефона
6 - Экспорт данных в файл
7 - Импорт данных из файла
0 - Выход
""")


def add_contact():
    number = input("Введите номер телефона: ")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    phone_book[number] = [last_name, first_name, second_name]
    print()
    print(f"Запись для номера {number} успешно добавлена.")


def print_phone_book():
    if len(phone_book) == 0:
        print("Телефонная книга пуста.")
    else:
        for number, item in phone_book.items():
            print("Тел.: {:<10} Фамилия: {:<16} Имя: {:<16} Отчество: {:<16}".format(number, item[0], item[1], item[2]))


def change_phone_record():
    number = input("Введите номер телефона, для которого хотите изменить запись: ")
    if number not in phone_book:
        print("Запись для этого номера не найдена.")
    else:
        print("\nВведите новые данные:")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        second_name = input("Отчество: ")
        phone_book[number] = [last_name, first_name, second_name]
        print(f"Запись для номера {number} успешно изменена.")


def delete_phone_record():
    number = input("Введите номер телефона, запись о котором нужно удалить: ")
    if number not in phone_book:
        print("Запись для этого номера не найдена.")
    else:
        del phone_book[number]
        print(f"Запись для номера {number} успешно удалена.")


def search_phone_book():
    search = input("Введите фамилию, имя, отчество либо номер телефона: ")
    for number, item in phone_book.items():
        if search in item or search == number:
            print(f"Номер: {number}, Фамилия: {item[0]}, Имя: {item[1]}, Отчество: {item[2]}")
        else:
            print(f"{search} в телефонной книге отсутствует.")


def export_phone_book():
    with open('phonebook.txt', "w") as file:
        for number, item in phone_book.items():
            line = ",".join([number] + item)
            file.write(line + "\n")
    print("Данные успешно экспортированы в файл.")


def import_phone_book():
    with open('phonebook.txt', "r") as file:
        for line in file:
            line = line.strip().split(",")
            phone_book[line[0]] = line[1:]
    print("Данные успешно импортированы из файла.")