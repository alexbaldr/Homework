import json
from collections import Counter


def top_often_words(filename):
    with open(filename, encoding = "utf-8") as file:
        data = json.load(file)
        result_list=[]
        for value in data.values():
            if 'channel' in value.keys():
                channel = value.get("channel")
                if "items" in channel:
                    items = channel.get("items") 
                    for item in items:
                        result_list.append(item["description"])
                        result_in_str = str(result_list).split()
                        #sort_of_result = sorted(result_in_str )
                        c = [w.rstrip("[]").lower() for w in result_in_str if len(w.rstrip("[]")) > 6]
        words_count = Counter(c).most_common(10)
        for i in words_count:
            print(i)



top_often_words('newsafr.json')
