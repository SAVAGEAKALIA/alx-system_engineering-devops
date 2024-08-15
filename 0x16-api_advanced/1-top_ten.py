#!/usr/bin/python3
"""Api implementation using Reddit top 10 posts"""
import requests


def top_ten(subreddit):
    """Returns the Title of top 10 hot post"""
    # print(subreddit)
    ur = "https://www.reddit.com/r/"
    url = f"{ur}{subreddit}/hot.json"
    payload = {'limit': 10}
    headers = {"User-Agent": "0-subs-script/0.1"}
    req = requests.get(url,
                       headers=headers, params=payload,
                       allow_redirects=False)

    if req.status_code != 200:
        return None

    posts = req.json()
    for post in posts['data']['children']:
        print(f'{post["data"]["title"]}')
