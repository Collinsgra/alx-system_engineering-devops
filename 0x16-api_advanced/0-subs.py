#!/usr/bin/python3
""" function that queries the Reddit
API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ functions to return subscribers to a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.RequestException, KeyError):
        return 0
