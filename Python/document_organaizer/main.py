documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    'passport': ['2207 876234'],
    'invoice': ['11-2'],
    'insurance': ['10006']
}

HELP = """
p - команда для поиска владельца по номеру документа,
s - команда показывает полку на которой хранится документ,
l - команда выводит все документы, которые есть в списке,
a - команда добавляет информацию о новом документе и его владельце, а также добавляет документ на нужную полку,
d - команда удаляет всю информацию о документе, владельце из списка и удаляет документ с полки,
as - команда добавляет новую пустую полку,
m - команда переместит документ на другую необходимую полку полку
h - команда снова откроет список доступных команд,
exit - команда завершит работу программы.
"""


def people(number_doc):
    """ This function helps find a person with his document"""
    for i, el in enumerate(documents):
        docs_arr = list(documents[i].items())
        number = docs_arr[1][1]
        if number == number_doc in docs_arr[1][1]:
            print(f"Владелец документа с номером {number_doc}: {docs_arr[2][1]}")
            break
    else:
        print("Документа с таким номером не существует")
    print()


def shelf(number_doc):
    """This function shows name of directory of document"""
    for i, el in enumerate(directories):
        list(directories.items())
        if number_doc in list(directories.items())[i][1]:
            print(f"Документ с номером {number_doc} находится на полке {list(directories.items())[i][0]}")
            break
    else:
        print("Документа с таким номером не существует")
    print()


def list_doc():
    """This function shows all list of documents"""
    for docs in documents:
        print(f"Тип документа: {docs['type']}, Номер документа: {docs['number']}, Имя владельца: {docs['name']}")
    print()


def add(type_doc, number_doc, name):
    """This function adds new information to documents and directories"""
    dict_new = {"type": type_doc.lower(), "number": number_doc, "name": name}
    documents.append(dict_new)
    if type_doc in directories.keys():
        directories[type_doc.lower()].append(number_doc)
    else:
        directories[type_doc.lower()] = [number_doc]
    print()


def delete(number_doc):
    """This function removes all information from documents and directories"""
    for i, el in enumerate(documents):
        docs_arr = list(documents[i].items())
        if number_doc == docs_arr[1][1]:
            documents.remove(documents[i])
            print(f"Вся информация о документа с номером {number_doc} была удалена.")
            break
    else:
        print("Документа с таким номером не существует")
        print()
    for key, value in directories.items():
        if number_doc in value:
            directories[key].remove(number_doc)
            if directories[key] is None:
                directories[key] = []
                break
            else:
                pass


def add_shelf(type_doc):
    """This function adds new shelf to directories with empty array"""
    if type_doc not in directories:
        directories[type_doc.lower()] = []
        print(f"Полка с названием {type_doc} добавлена!")
    else:
        print("Полка с таким названием уже существует.")
    print()


def move(type_doc, type_doc_old, number_doc):
    if type_doc in directories.keys():
        if type_doc_old in directories.keys():
            for value in directories.values():
                if number_doc in value:
                    move_body(type_doc, type_doc_old, number_doc)
                    break
            else:
                print("Документа с таким номером не существует!")
        else:
            print("Полки с таким названием не существует!")
    else:
        print("Полки с таким названием не существует!")

    print()


def move_body(type_doc, type_doc_old, number_doc):
    """This function move document from previous directory to new"""
    if number_doc in directories[type_doc_old]:
        directories[type_doc_old].remove(number_doc)
        if directories[type_doc_old] is None:
            directories[type_doc_old] = []
        else:
            pass
        for key in directories.keys():
            if key == type_doc:
                directories[key].append(number_doc)
    else:
        print(f"Документ с номером {number_doc} отстутствует на полке {type_doc_old}")

    print()


helper = input("Вам нужен список доступных функуий? (да/нет): ")
if helper.lower() == "да":
    print(HELP)

while True:
    command = input("Введите команду: ").lower()
    if command == "p":
        number_doc = input("Введите номер документа: ")
        people(number_doc)
    elif command == "s":
        number_doc = input("Введите номер документа: ")
        shelf(number_doc)
    elif command == "l":
        list_doc()
    elif command == "a":
        name = input("Введите имя: ")
        type_doc = input("Введите тип документа: ")
        number_doc = input("Введите номер документа: ")
        add(type_doc, number_doc, name)
    elif command == "d":
        number_doc = input("Введите номер документа: ")
        delete(number_doc)
    elif command == "as":
        type_doc = input("Введите название полки, которую надо добавить: ")
        add_shelf(type_doc)
    elif command == "m":
        print("Доступные полки: \n")
        for key in directories.keys():
            print(key.capitalize())
        print()
        type_doc = input("Введите новую полку: ").lower()
        type_doc_old = input("Введите текущую полку: ").lower()
        number_doc = input("Введите номер документа: ")
        move(type_doc, type_doc_old, number_doc)
    elif command == "h":
        print(HELP)
    elif command == "exit":
        exit()
    else:
        print("Такой команды в списке нет")
    from pprint import pprint
    print('-' * 80)
    pprint(directories)
    print('-' * 80)
    pprint(documents)
    print('-' * 80)
