#!/usr/bin/python3
"""
Titles of the first 10 hot posts listed for that subreddit.
"""
import requests



def top_ten(subreddit):
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
