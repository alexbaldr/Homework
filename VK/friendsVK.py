
import requests

from pprint import pprint

TOKEN = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

USER_id = 171691064
list_of_friends = []


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
        a = set(get_items)     
        print(a)

        return response

    def get_friends(self):
        
        params = {
        'access_token': TOKEN,
        'v': 5.107,
        "user_id": USER_id, 
        "order" : "name",
        "fields": "domain"
                }

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
        #return #list_of_friends

        for id_f in list_of_friends:   
            params = {
                'access_token': TOKEN,
                'v': 5.107,
                "user_id": id_f,
                "extended": 0,
                "count": 3
                    }


            #response = requests.get(
            #    'https://api.vk.com/method/groups.get', 
            #    params)
            #ВЫВОД ЗАПРОСА ПРИ ПОМОЩИ EXECUTE. САМ МЕТОД НАЧИНАЯ С RETURNа РАБОТАЕТ, 
            r = requests.get('https://api.vk.com/method/execute?access_token='+TOKEN+',&code=return API.groups.get({"user_id":"171691064","extended":"0","count":"3"});')
            #r = requests.get('https://api.vk.com/method/execute?access_token='+TOKEN+',"v":"5.107",&code= return API.groups.get({"user_id": {API.friends.get({"user_id":'+ USER_id+',"order" : "name"}),"extended": 0});')
            #a = set(response)
            list_fds = r.json()#["response"]
            #get_items = list_fds.get("items")
            print(list_fds)      

    
    def exeptions_of_grups(self):
        return


    def get_json(self):
        return


Evg = USER(TOKEN)

#print(Evg.get_grups())
print(Evg.get_friends())
#print(Evg.exeptions_of_grups())
