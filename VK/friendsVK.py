import requests
from pprint import pprint
import time
import json

TOKEN = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

USER_id = 171691064


class USER:
     
    def __init__(self, token):
        self.token = token

    def get_grups(self):

        a = set()
        params = {
        'access_token': TOKEN,
        'v': 5.107,
        "user_id": USER_id,
        "extended": 0
                }
        response = requests.get(
        'https://api.vk.com/method/groups.get', 
        params)
        res = response.json()
        if 'error' in res :
            time.sleep(2)   
        if "error" not in res:
            data = response.json()['response']
            get_items = data.get("items")
        for i in get_items:
            a.add(i)   
        return a

    def get_friends(self):

        b = set()
        params = {
        'access_token': TOKEN,
        'v': 5.107,
        "user_id": USER_id, 
        "order" : "name",
        "fields": "domain"
                }
        list_of_friends = []
        response = requests.get("https://api.vk.com/method/friends.get", params)
        
        get_items = response.json()["response"]["items"]
        # Получаем список с id друзей
        for i in get_items:
            get_id = i["id"]
            list_of_friends.append(get_id)
        #Получаем список групп
        for id_f in list_of_friends:   
            params = {
                'access_token': TOKEN,
                'v': 5.107,
                "user_id": id_f,
                "extended": 0,
                "count": 5
                    }

            #repeat = True
            #while repeat:
            response = requests.get(
                'https://api.vk.com/method/groups.get', 
                params=params)
            data = response.json()
            if 'error' in data: # and 'error_code' in data['error'] and data['error']['error_code'] == 6:
                time.sleep(2)
                #else:
                    #repeat = False
            if 'error' not in data.keys():
                list_of_groups = data["response"]
                get_items_of_groups = list_of_groups.get("items")
                for i in get_items_of_groups:
                    b.add(i)

        return b

    def get_json(self):
        set_of_id = Evg.get_grups() & Evg.get_friends()
        gotten_groups = [] 

       # ПОЛУЧАЕМ ID ГРУПП
        for i in set_of_id:
            params = {
            'access_token': TOKEN,
            'v': 5.107,
            "group_id":i,
            "count":1000
            }
            response = requests.get(
                'https://api.vk.com/method/groups.getMembers', params=params)
            members_count = response.json()
            if 'error' in members_count :
                time.sleep(2)   
            if "error" not in members_count:
                members_count_list = members_count["response"]["count"]
                merged = {"members_count":members_count_list}

        #ПОЛУЧАЕМ ДАННЫЕ ГРУПП
            params = {
                'access_token': TOKEN,
                'v': 5.107,
                "group_ids": i
                }
            response = requests.get(
                    'https://api.vk.com/method/groups.getById', params=params)
            data = response.json()
            if 'error' in data :
                time.sleep(2)   
            if "error" not in data:
                res = response.json()["response"]
                           
            for i in res:
                name = i.get("name")
                group_id = i.get("id")
                dict_of_same_groups = {"name": name,
                        "gid": group_id,
                        }       
                dict_of_same_groups.update(merged)

                gotten_groups.append(dict_of_same_groups)

        with open('groups.json', 'w',encoding = 'UTF-8') as f:
            json.dump(gotten_groups,f,ensure_ascii = False, sort_keys=True, indent=2)            

            return gotten_groups

Evg = USER(TOKEN)
print(Evg.get_grups())
Evg.get_friends()
print(Evg.get_json())