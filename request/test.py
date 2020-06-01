import requests
import json

TOKEN = 'OAuth AgAAAAADScWgAADLW17-JyB090H2r6MQTtWBsYQ'
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
    headers = {'Accept': 'application/json', 'Authorization':TOKEN}
    response = requests.get(URL, params=params, headers=headers)
    print(response.text)
    put_url = response.json().get('href')
    print(put_url)
    
    

    files = {'file': open(name_file,'rb')}
    response = requests.put(put_url, files=files)
    print (response.json)

    return get_URL



get_URL("DEinRUS.txt")
get_URL("FRinRUS.txt")
get_URL("ESinRUS.txt")


