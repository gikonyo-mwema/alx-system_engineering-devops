#!/usr/bin/python3
"""
This script uses the Reddit API to get the number of subscribers
for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function takes a subreddit name as input, makes a GET request to the
    Reddit API, and returns the number of subscribers for that subreddit.
    """
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
