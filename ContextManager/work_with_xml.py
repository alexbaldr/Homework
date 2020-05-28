import xml.etree.ElementTree as ET
from collections import Counter
from contextlib import contextmanager
from datetime import datetime


parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item")
result_list=[]

@contextmanager
def get_time():
    try:
        start_time = datetime.utcnow()
        print(f'Начало работы: {start_time}')
        end_time = datetime.utcnow()
 

        for item in xml_items:
            list_of_description = item.find("description").text
            result_list.append(list_of_description)
            result_in_str = str(result_list).split()

        c = [w.rstrip().lower() for w in result_in_str if len(w.rstrip()) > 6]
        words_count = Counter(c).most_common(10)
        #for i in words_count:
            #print(i)
        end_time = datetime.utcnow()
        print(f'Конец работы: {end_time}')
        yield  

    finally:
        print(end_time- start_time)
with get_time():
    print('Было затрачено: ' )