#!/usr/bin/python3
"""This script exports data retrieved
from an api request in JSON format"""
import json
import requests as rq
from sys import argv

user_id = argv[1] if argv[1:] else 1
FILENAME = user_id + ".json"

url = 'https://jsonplaceholder.typicode.com/'
user = rq.get(url + 'users/{}'.format(user_id)).json()
tasks = rq.get(url + 'users/{}/todos'.format(user_id)).json()
data = {user_id: [{'task': task.get('title'),
                   'completed': task.get('completed'),
                   'username': user.get('name')} for task in tasks]}
with open(FILENAME, 'w', newline='') as f:
    json.dump(data, f)
