# Модуль поиска контакта

def search_data(word, data):
    if len(data) > 0:
        my_list = []
        for item in data:
            if word in item:
                my_list.append(item)
        if my_list == []:
            return None
        else:
            return my_list
    else:
        return None