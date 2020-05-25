import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item")
result_list=[]
for item in xml_items:
    list_of_description = item.find("description").text
    result_list.append(list_of_description)
    result_in_str = str(result_list).split()

c = [w.rstrip().lower() for w in result_in_str if len(w.rstrip()) > 6]
words_count = Counter(c).most_common(10)
for i in words_count:
    print(i)
