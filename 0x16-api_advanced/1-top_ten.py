#!/usr/bin/python3
"""Api implementation using Reddit"""
import requests
# import json


def top_ten(subreddit):
    """Returns the Title of top 10 hot post"""
    # print(subreddit)
    url = "https://www.reddit.com/r/"
    payload = {'limit': 10}
    headers = {"User-Agent": "0-subs-script/0.1"}
    req = requests.get(f'{url}{subreddit}/hot.json',
                       headers=headers, params=payload, allow_redirects=False)
    content_type = req.headers.get('Content-Type', '')
    # print(content_type)
    # print(req.json())
    # print(json.dumps(req.json(), indent=4))
    if 'application/json' in content_type:
        try:
            # data = dir(req)
            # print(data)
            if req.status_code == 200:
                posts = req.json()
                for post in posts['data']['children']:
                    print(f'{post["data"]["title"]}')
            else:
                # print(f"Error: status code {req.status_code}")
                print("None")
        except Exception as e:
            print(f"Error: {e}")
    else:
        # print("Error: not in json format")
        print("None")
