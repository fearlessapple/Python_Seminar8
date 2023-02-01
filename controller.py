from push_data import *
from read_data import *
from print_data import *
from search_data import *

def start():
    print("Доступные действия: 1 - получить всю информацию о учениках; 2 - добавить ученика; 3 - поиск ученика; 4 - выход.")
    choice = input("Введите цифру: ")
    while True:
        match choice:
            case '1':
                data = read_data()
                print_data(data)
                start()
            case '2':
                push_data()
                start()
            case '3':
                info = input("Введите данные для поиска: ")
                data = read_data()
                item = search_data(info, data)
                if item != None:
                    print_data(item, True)
                else:
                    print("Данные не обнаружены")                
                start()
            case '4':
                print("Спасибо, до свидания!")
                break
            case other:
                print("Введите корректную цифру!")
                start()