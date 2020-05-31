import requests
import json

API_KEY = 'OAuth AgAAAAADScWgAADLW17-JyB090H2r6MQTtWBsYQ'
URL ="https://cloud-api.yandex.net/v1/disk/resources/upload"

"""
ID: eb63bd25d8d64f04a92407c360079d4b
Пароль: 1d10f66adbca4d8e966835e5400040ff
"""

def get_URL(name_file):

    params = {
        "path": name_file,
        "overwrite": 'true'
    }
    headers = {'Accept': 'application/json', 'Authorization':API_KEY}
    response = requests.get(URL, params=params, headers=headers)
    print(response)
    json_ = response.json()
    print(json_)
    global href
    href = json_['href']
    return get_URL
    

def download_file ():

    response = requests.put(href)

    print (response.json)

    return download_file 

   

get_URL("DEinRUS.txt")
get_URL("FRinRUS.txt")
get_URL("ESinRUS.txt")
download_file()