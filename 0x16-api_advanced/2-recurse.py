#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function that calls next result page"""
    ur = "https://www.reddit.com/r/"
    url = f"{ur}{subreddit}/hot.json"
    headers = {"User-Agent": "0-subs-script/0.1"}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
