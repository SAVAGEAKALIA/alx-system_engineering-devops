#!/usr/bin/python3
"""Module to count keyword occurrences in Reddit hot posts"""

import requests
import re


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API for the hot posts in the given subreddit,
    counts occurrences of each keyword in the post titles, and prints the results.

    Parameters:
    - subreddit (str): The subreddit to query.
    - word_list (list): A list of keywords to count in the post titles.
    - word_count (dict, optional): A dictionary to keep track of keyword counts.
    - after (str, optional): Pagination token for fetching the next set of posts.
    """
    # Initialize the word_count dictionary if not provided
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    # Define the URL and headers for the API request
    ur = "https://www.reddit.com/r/"
    url = f"{ur}{subreddit}/hot.json"
    headers = {"User-Agent": "count-words-script/0.1"}
    params = {"after": after}

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the response is successful
        if response.status_code != 200:
            return

        # Parse the JSON response
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Collect titles from the response
        titles = [post['data'].get('title', '') for post in posts]

        # If no posts, end recursion and print results
        if not titles:
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                if count > 0:
                    print(f'{keyword}: {count}')
            return

        # Process each title to count keyword occurrences
        for title in titles:
            # Split title into words and clean them from non-alphanumeric characters
            words = re.findall(r'\b\w+\b', title.lower())
            for keyword in word_count:
                word_count[keyword] += words.count(keyword)

        # Check if there is a next page to process
        after_token = data.get('data', {}).get('after')
        if after_token:
            # Recursive call to process the next page
            count_words(subreddit, word_list, word_count, after_token)
        else:
            # Finalize and print results if no more pages
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                if count > 0:
                    print(f'{keyword}: {count}')

    except requests.RequestException:
        return
