#!/usr/bin/python3
"""
Api reddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # reddit url api
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'My Reddit API Client'}

    response = requests.get(url, headers=headers)

    # if request is successful
    if response.status_code == 200:
        # parse the json
        data = response.json()

        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        print(f"Error: Unable to fetch data for subreddit '{subreddit}'")
        return None
