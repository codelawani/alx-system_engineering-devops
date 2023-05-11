#!/usr/bin/python3
"""This script queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after_url=''):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1{}'.format(
        subreddit, after_url)
    response = requests.get(url, allow_redirects=False, headers={
                            "User-Agent": "Nico@alx/1.0"})
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        title = data['data']['children'][0]['data']['title']
        hot_list.append(title)
        if data['data'].get('after'):
            after_url = '&after={}'.format(data['data']['after'])
            recurse(subreddit, hot_list, after_url)
        return hot_list
