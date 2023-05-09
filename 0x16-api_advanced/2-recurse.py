#!/usr/bin/python3
"""This script queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], url):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1'.format(
        subreddit)
    response = requests.get(url, allow_redirects=False, headers={
                            "User-Agent": "Nico@alx/1.0"})
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        if 'after' in data['data']:
            after = data['data']['after']
            url += '?after={}'.format(after)
            title = data['data']['children']['data']['title']
            recurse(subreddit, hot_list.append(title), url)

        return hot_list
