#!/usr/bin/python
"""Api implementation using Reddit"""
import requests
import json


def top_ten(subreddit):
    """Returns the Title of top 10 hot post"""
    # print(subreddit)
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "0-subs-script/0.1"}
    req = requests.get(f'{url}{subreddit}/hot.json',
                       headers=headers, allow_redirects=False)
    content_type = req.headers.get('Content-Type', '')
    print(content_type)
    # print(req.json())
    # print(json.dumps(req.json(), indent=4))
    posts = req.json()
    for post in posts['data']['children'][:10]:
        print(f'{post["data"]["title"]}')


if __name__ == '__main__':
    top_ten('programming')
