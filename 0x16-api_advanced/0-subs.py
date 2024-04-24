#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
  """Queries Reddit API for subscriber count of a subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., "learnpython").

  Returns:
      The number of subscribers for the subreddit, or 0 if invalid.
  """
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()
    data = response.json()
    return data.get('data', {}).get('subscribers', 0)
  except requests.exceptions.RequestException:
    return 0  # Return 0 on any errors
