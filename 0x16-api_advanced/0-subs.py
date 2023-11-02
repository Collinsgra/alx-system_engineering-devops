#!/usr/bin/python3
"""
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    # custom agent
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    # Define the Reddit API URL for the given subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers)

    # Checks out if success
    if response.status_code == 200:

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:

        return 0
