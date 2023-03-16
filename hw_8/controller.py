phone_book = {}

import view

def run():
    view.greetings()

    while True:
        view.menu()
        action = input('Выберите действие: ')
    
        if action == "1":
            view.add_contact()

        elif action == "2":
            view.print_phone_book()

        elif action == "3":
            view.change_phone_record()

        elif action == "4":
            view.delete_phone_record()

        elif action == "5":
            view.search_phone_book()

        elif action == "6":
            view.export_phone_book()

        elif action == "7":
            view.import_phone_book()

        elif action == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный ввод.")