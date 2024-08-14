#!/usr/bin/python3
"""Api implementation using Reddit"""
import requests
# import json


def number_of_subscribers(subreddit):
    """Return total number of subscribers"""
    # print(subreddit)
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "0-subs-script/0.1"}
    req = requests.get(f'{url}{subreddit}/about.json',
                       headers=headers, allow_redirects=False)
    content_type = req.headers.get('Content-Type', '')
    # print(content_type)
    # print(req.json())
    # print(json.dumps(req.json(), indent=4))
    if 'application/json' in content_type:
        try:
            # data = dir(req)
            # print(data)
            if req.status_code == 200:
                return int(req.json()['data']['subscribers'])
            else:
                # print(f"Error: status code {req.status_code}")
                return 0
        except Exception as e:
            print(f"Error: {e}")
    else:
        # print("Error: not in json format")
        return 0


# if __name__ == '__main__':
#     number_of_subscribers('programming')
