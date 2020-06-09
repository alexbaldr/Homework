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

        data = response.json()["response"]
        get_items = data.get("items")
        for i in get_items:
            a.add(i)    

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
        
        data = response.json()["response"]
        get_items = data.get("items")
        for i in get_items:
            if i["first_name"] != 'DELETED': 
                get_id = i["id"]
                list_of_friends.append(get_id)

        for id_f in list_of_friends:   
            params = {
                'access_token': TOKEN,
                'v': 5.107,
                "user_id": id_f,
                "extended": 0,
                "count": 2
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
        x = a & b
        return x
    def get_json(self):
        #ПОЛУЧАЕМ ДАННЫЕ ГРУПП
        x = {35486626, 134709480, 125927592, 4100014, 101522128, 8564, 27683540}
        for i in x:
            params = {
            'access_token': TOKEN,
            'v': 5.107,
            "group_ids": i
            }

            response = requests.get(
                'https://api.vk.com/method/groups.getById', params=params)
            
            res = response.json()["response"]
            for i in res:
                name = i.get("name")
                group_id = i.get("id")
                #print(name,group_id)

        # ПОЛУЧАЕМ ID ГРУПП
        for i in x:
            params = {
            'access_token': TOKEN,
            'v': 5.107,
            "group_id":i,
            "count":1
            }
            repeat = True
            response = requests.get(
                'https://api.vk.com/method/groups.getMembers', params=params)
            members_count = response.json()
            if 'error' in members_count :
                time.sleep(2)   
            else:
                repeat = False
            if "error" not in members_count:
                members_count_list = members_count["response"]["count"]
                #print (members_count_list)

        merged = [{"name": name,
                    "gid": group_id,
                    "members_count": members_count_list}]

        for i in merged:
            gotten_groups = []  
            gotten_groups.append(i)
            #with open('groups.json', 'w',encoding = 'UTF-8') as f:
            #    json.dump(merged,f,ensure_ascii = False)            

            return gotten_groups

Evg = USER(TOKEN)
print(Evg.get_grups())
#print(Evg.get_json())