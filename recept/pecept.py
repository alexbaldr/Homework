
from pprint import pprint
cook_book = {}
def read():
    with open("rec.txt","r", encoding="UTF-8") as file:
        string1 = ["ingredient_name", "quantity", "measure"]
        
        for line in file:
            line = line.strip()
            cook_book[line] = []
            counter = int(file.readline().strip())
            for i in range(counter):
                i = file.readline().strip().split('|')
                keys_dict = dict(zip(string1,i))
                cook_book[line].append(keys_dict)
            file.readline()
    return(cook_book)          


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (int(ingredient['quantity'])*person_count)}
    return(shop_list)


pprint(read())
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))