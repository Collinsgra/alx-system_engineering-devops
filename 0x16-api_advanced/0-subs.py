#!/usr/bin/python3
"""
 returns the number of subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit Api and returns the no of subs
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
