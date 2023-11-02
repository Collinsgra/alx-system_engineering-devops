#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    # redit api
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # custom agent
    headers = {'User-Agent': 'Google Chrome Version 118.0.5993.118'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        posts = data['data']['nature'][:10]
        for post in posts:
            title = post['data']['title']
            print(title)
    elif response.status_code == 404:
        print(None)
    else:
        print(f"Error: Unable to fetch data for subreddit '{subreddit}'")
