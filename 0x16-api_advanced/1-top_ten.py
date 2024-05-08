#!/usr/bin/python3
"""
This script uses the Reddit API to get the titles of the first 10 hot posts
for a given subreddit.
"""

# We import the requests module to make HTTP requests.
import requests


def top_ten(subreddit):
    """
    This function takes a subreddit name as input, makes a GET request to the
    Reddit API, and prints the titles of the first 10 hot posts.
    """
    # We set the User-Agent header to identify our application.
    headers = {'User-Agent': 'My User Agent 1.0'}

    # We construct the URL for the subreddit's hot posts page in JSON format.
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # We make a GET request to the URL.
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the response status code is not 200 (OK), the subreddit is invalid.
    if response.status_code != 200:
        print(None)
    else:
        # Otherwise, we parse the JSON response and get the list of posts.
        data = response.json().get('data').get('children')

        # We iterate over each post and print its title.
        for post in data:
            print(post.get('data').get('title'))


# This is the main part of our script.
if __name__ == '__main__':
    # We import the sys module to access command-line arguments.
    import sys

    # If no subreddit was provided as a command-line argument...
    if len(sys.argv) < 2:
        # We print a usage message.
        print("Please pass an argument for the subreddit to search.")
    else:
        # Otherwise, we call our function with the subreddit as an argument.
        top_ten(sys.argv[1])
