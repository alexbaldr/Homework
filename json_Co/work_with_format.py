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
                        c = [w.rstrip().lower() for w in result_in_str if len(w.rstrip()) > 6]
                        #print(*sorted(set(c), key=c.count, reverse=True)[:10], sep='\n')
                        words_count = Counter(c).most_common(1)
                        print(words_count )



top_often_words('newsafr.json')




"""
def top_often_words():
    with open('newsafr.json', encoding = "utf-8") as file:
        data = json.load(file)
        #print(data)
        result_list=[]
        for value in data.values():
            if 'channel' in value.keys():
                x = value.get("channel")
                if "items" in x:
                    z = x.get("items") 
                    #c = Counter(z.split()) 
                    #print(c.most_common(10))
                    print(z)
                    #for item in z:
                        #result_list.append(item["description"])
                        #result_in_str = str(result_list).split(' ')
                        #sort_of_result = sorted(result_in_str )

                        #print(result_in_str)


    #with open('newsafr_write.json', "w", encoding = "utf-8") as file:
        #json.dump(data,file, ensure_ascii=False, indent = 2)
top_often_words()
"""