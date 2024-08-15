#!/usr/bin/python3
"""Api implementation using Reddit top 10 posts"""
import requests
import json


def top_ten(subreddit):
    """Returns the Title of top 10 hot post"""
    # print(subreddit)
    url = "https://www.reddit.com/r/"
    payload = {'limit': 10}
    headers = {"User-Agent": "0-subs-script/0.1"}

    try:
        req = requests.get(f'{url}{subreddit}/hot.json',
                           headers=headers, params=payload, allow_redirects=False)

        if req.headers.get('Content-Type', '').startswith('application/json'):
            try:
                req_json = req.json()
                posts = req_json['data']['children']
                for post in posts[:10]:
                    print(post['data']['title'])
            except json.JSONDecodeError:
                print("None")
        else:
            print("None")
    except requests.RequestException as e:
        print(f"Request Error: {e}")
