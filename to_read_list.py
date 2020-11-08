import json
import os
from xml.etree import ElementTree

import requests

with open(os.path.expanduser("~/Desktop/code/api_keys/goodreads_api_key.json")) as f:
    api_key = json.loads(f.read())

shelves_url = "https://www.goodreads.com/shelf/list.xml"
reviews_url = "https://www.goodreads.com/review/list?v=2"
user_id = "119459640"
shelves_params = {"key": api_key["key"], "user_id": user_id}
reviews_params = {"shelf": "read", "key": api_key["key"]}

# get my shelves
shelves_response = requests.get(shelves_url, params=shelves_params)
shelves_tree = ElementTree.fromstring(shelves_response.content)

for shelf in shelves_tree.find("shelves").findall("user_shelf"):
    name = shelf.find("name").text
    book_count = shelf.find("book_count").text
    print(name, book_count)

      
print()
