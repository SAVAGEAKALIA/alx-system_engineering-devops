#!/usr/bin/python3
"""Api implementation using Reddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the Title of top 10 hot post"""
    # print(subreddit)
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "0-subs-script/0.1"}
    req = requests.get(f'{url}{subreddit}/about.json',
                       headers=headers, allow_redirects=False)
    content_type = req.headers.get('Content-Type', '')

    if 'application/json' in content_type:
        try:
            if req.status_code == 200:
                data = req.json()
                count = data['data']['subscribers']
                # print(type(count))
                return count
            else:
                # print(f"Error: status code {req.status_code}")
                return 0
        except Exception as e:
            print(f"Error: {e}")
    else:
        # print("Error: not in json format")
        return 0
