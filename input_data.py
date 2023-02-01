from write_data import count_data

def input_data():
    my_dict = dict()
    Id = count_data("name.csv") 
    my_dict["id"] = Id     
    my_dict["surname"] = input('Введите Фамилию: ')
    my_dict["name"] = input('Введите Имя: ')
    my_dict["class"] = input('Введите Класс: ')
    my_dict["status"] = input('Введите Статус: ')
    my_dict["row"] = input('Введите Ряд: ')
    my_dict["col"] = input('Введите Номер парты: ')
    my_dict["city"] = input('Введите Город: ')
    my_dict["street"] = input('Введите Улица: ')
    my_dict["house"] = input('Введите Дом: ')
    my_dict["apartament"] = input('Введите Квартира: ')
    my_dict["other"] = input('Введите Примечание: ')
    return my_dict