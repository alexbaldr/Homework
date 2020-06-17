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
#
#print('?'.join(
#    (OAUTH_URL, urlencode(OAUTH_PARAMS))
#   ))

Token = "81ff236956418c97c8adda143b74ed17c8cab00b5b96d913000bf2004735bad2d4d440946d2f785cf8a41"

class USER:

    def __init__(self, user):
        self.user = user
        self.params = {"access_token": Token, "v": 5.107, "user_id": self.user}

    def get_friends(self):

        response = requests.get("https://api.vk.com/method/friends.get", params=self.params)
        res = set(response.json()["response"]["items"])
        return res

    def __and__(self, other_user):
        result = self.get_friends() & other_user.get_friends()
        common_list = []
        for id in result:
            common_list.append(USER(id))
        return common_list

    def __str__(self):
        return f"https://vk.com/id{str(self.user)}"


user1 = USER(18526683)
user2 = USER(3345683)

users = user1 & user2
for user in users:
    print(user)
