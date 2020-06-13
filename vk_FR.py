import requests
from urllib.parse import urlencode

OAUTH_URL = "https://oauth.vk.com/authorize"
OAUTH_PARAMS = {
    'client_id': '7495532',
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': 5.107
}

print('?'.join(
    (OAUTH_URL, urlencode(OAUTH_PARAMS))
    ))

Token = "89fa88c0ab3ca79b7dba67d6f159b4466bb6a71011c76eb726147a84b881d2205f6f2e7041c00d0f560ac" #&expires_in=86400&user_id=18526683

class USER:

    def __init__(self):
        return 

    def get_friends(self,user1,user2):
        self.user1 = user1
        self.user2 = user2
        params = {"access_token":Token,
                    "v":5.107,
                    "user_id":user1,
        }

        response = requests.get("https://api.vk.com/method/friends.get",params)
        res = response.json()["response"]["items"]
        user1 = set(res)

        params = {"access_token":Token,
                    "v":5.107,
                    "user_id":user2,
        }

        response = requests.get("https://api.vk.com/method/friends.get",params)
        res1 = response.json()["response"]["items"]
        user2 = set(res1)

        result = user1 & user2
        for i in result:
            user = (f"https://vk.com/id{i}")
        return user

    

USER_id = USER()
print(USER_id.get_friends(18526683,3136163))


