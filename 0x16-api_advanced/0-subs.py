#!/usr/bin/python3
"""
Subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    """
    url = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={"User-Agent": "Custom"},
    )
    if url.status_code == 200:
        return 0
    return response.json().get('data').get('subscribers')
