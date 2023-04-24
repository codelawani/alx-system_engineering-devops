#!/usr/bin/python3
"""This script makes an api request"""
import requests as rq
from sys import argv
import csv

user_id = argv[1] if argv[1:] else 1
FILENAME = user_id + ".json"

url = 'https://jsonplaceholder.typicode.com/'
user = rq.get(url + 'users/{}'.format(user_id)).json()
tasks = rq.get(url + 'users/{}/todos'.format(user_id)).json()
with open(FILENAME, 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    header = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
    [writer.writerow([user_id, user.get('name'), task.get('completed'),
                      task.get('title')]) for task in tasks]
