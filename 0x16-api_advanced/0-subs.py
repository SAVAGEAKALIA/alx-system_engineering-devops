#!/usr/bin/python3
"""Api implementation using Reddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the Title of top 10 hot post"""

    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "0-subs-script/0.1"}
    req = requests.get(f'{url}{subreddit}/about.json',
                       headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0

    data = req.json()
    count = data['data']['subscribers']
    # print(type(count))
    return count
