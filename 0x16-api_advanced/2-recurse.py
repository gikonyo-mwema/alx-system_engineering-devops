#!/usr/bin/python3
"""
Recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    headers = {'User-Agent': 'My User Agent 1.0'}
    base_url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    url = base_url.format(subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get('data')
        for post in data.get('children'):
            hot_list.append(post.get('data').get('title'))
        after = data.get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)


    if __name__ == '__main__':
        import sys
        if len(sys.argv) < 2:
                print("Please pass an argument for the subreddit to search.")
        else:
            result = recurse(sys.argv[1])
            if result is not None:
                print(len(result))
            else:
                print("None")
