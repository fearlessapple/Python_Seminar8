from input_data import input_data
from write_data import write_data

def push_data():
    my_dict = input_data()

    write_data([my_dict.get("id"), my_dict.get("surname"), my_dict.get("name"), my_dict.get("class"), my_dict.get("status")], "name.csv")

    write_data([my_dict["id"], my_dict["city"], my_dict["street"], my_dict["house"], my_dict["apartament"], my_dict["other"]], "adress.csv")

    write_data([my_dict["id"], my_dict["row"], my_dict["col"]], "class.csv")