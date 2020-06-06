import requests
from pprint import pprint
import time

TOKEN = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

USER_id = 171691064

b = set()

class USER:
    def __init__(self, token):
        self.token = token

    def get_grups(self):

        params = {
        'access_token': TOKEN,
        'v': 5.107,
        "user_id": USER_id,
        "extended": 0
                }
        response = requests.get(
        'https://api.vk.com/method/groups.get', 
        params)

        data = response.json()["response"]
        get_items = data.get("items")
        global a
        a = set(get_items)     

        return a

    def get_friends(self):
        
        params = {
        'access_token': TOKEN,
        'v': 5.107,
        "user_id": USER_id, 
        "order" : "name",
        "fields": "domain"
                }
        list_of_friends = []
        response = requests.get("https://api.vk.com/method/friends.get", params)
        
        data = response.json()["response"]
        #print(data)
        get_items = data.get("items")
        #print(get_items)
        # УБИРАЕМ ВСЕХ УДАЛЕННЫХ И ЗАБЛОКИРОВАННЫХ ПОЛЬЗОВАТЕЛЕЙ (СКОРЕЕ ВСЕГО ПЕРЕИЗБЫТОЧНАЯ ОПЦИЯ)
        for i in get_items:
            #for  v in i.values():
            if i["first_name"] != 'DELETED': 
                get_id = i["id"]
                list_of_friends.append(get_id)

        for id_f in list_of_friends:   
            params = {
                'access_token': TOKEN,
                'v': 5.107,
                "user_id": id_f,
                "extended": 0,
                "count": 1000
                    }

            repeat = True
            while repeat:
                response = requests.get(
                'https://api.vk.com/method/groups.get', 
                params=params)
            #ВЫВОД ЗАПРОСА ПРИ ПОМОЩИ EXECUTE. САМ МЕТОД НАЧИНАЯ С RETURNа РАБОТАЕТ, 
            #response = requests.get('https://api.vk.com/method/execute?access_token='+TOKEN+'&v=5.107&code=return API.groups.get({"user_id":"'+id_f+'","extended":"0","count":"3"});')
            #r = requests.get('https://api.vk.com/method/execute?access_token='+TOKEN+',"v":"5.107",&code= return API.groups.get({"user_id": {API.friends.get({"user_id":'+ USER_id+',"order" : "name"}),"extended": 0});')
            #a = set(response)
            #list_fds = response.json()["response"]
            #get_items = list_fds.get("items")

                data = response.json()
                if 'error' in data and 'error_code' in data['error'] and data['error']['error_code'] == 6:
                    time.sleep(2)
                else:
                    repeat = False
                if 'error' not in data.keys():
                    list_of_groups = data["response"]
                    get_items_of_groups = list_of_groups.get("items")
                    for i in get_items_of_groups:
                        b.add(i)

    
    def exeptions_of_grups(self):
        x = a & b
        print(x)
        



    def get_json(self):

        return


Evg = USER(TOKEN)

Evg.get_grups()
Evg.get_friends()
print(Evg.exeptions_of_grups())