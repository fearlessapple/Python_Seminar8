def print_data(data, search = False):
    if len(data) > 0:
        if not search:
            del data[0]
        for item in data:
            print(f'id: {item[0]}, Фамилия: {item[1]}, Имя: {item[2]}, Класс: {item[3]}, Статус: {item[4]}, Ряд: {item[5]}, Парта: {item[6]},Город: {item[7]}, Улица: {item[8]}, Дом: {item[9]}, Квартира: {item[10]}, Примечание: {item[11]}')
    else:
        print("Справочник пуст!")
 