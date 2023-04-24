#!/usr/bin/python3
"""This script makes an api request"""
import requests as rq
from sys import argv

FILE_NAME = "USER_ID.csv"

def tasks_done(todos, mode='count'):
    """Return the number of completed tasks or print the titles"""
    done = 0
    for todo in todos:
        if todo.get('completed', False):
            if mode == 'title':
                print("\t " + todo['title'])
            else:
                done += 1
    return done


id = argv[1] if argv[1:] else 1
url = 'https://jsonplaceholder.typicode.com/'
user = rq.get(url + 'users/{}'.format(id))
todos = rq.get(url + '/users/{}/todos'.format(id))
emp_tasks_total = len(todos)
# print('Employee {} is done with tasks({}/{}):'.
    #   format(user.get('name'), tasks_done(todos), emp_tasks_total))
# tasks_done(todos, 'title')
t = rq.get("https://jsonplaceholder.typicode.com/" + "todos", params={"userId": id}).json()
print(t)
