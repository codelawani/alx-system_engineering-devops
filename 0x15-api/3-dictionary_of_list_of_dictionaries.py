#!/usr/bin/python3
"""This script exports data retrieved
from an api request in JSON format"""

import json
import requests as rq
from sys import argv

FILENAME = "todo_all_employees.json"

url = 'https://jsonplaceholder.typicode.com/'
users = rq.get(url + 'users').json()
tasks = rq.get(url + 'todos').json()
data = {user.get('id'): [{'username': user.get('name'),
                          'task': task.get('title'),
                          'completed': task.get('completed'),
                          }
        for task in tasks if task.get('userId') == user.get('id')]
        for user in users}
with open(FILENAME, 'w', newline='') as f:
    json.dump(data, f)
