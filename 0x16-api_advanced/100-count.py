#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    headers = {'User-Agent': 'My User Agent 1.0'}
    base_url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    url = base_url.format(subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get('data')
    for post in data.get('children'):
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            word_dict[word] = word_dict.get(word, 0) +
            title.count(word.lower())
    after = data.get('after')
    if after is None:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print("{}: {}".format(word, count))
    else:
        count_words(subreddit, word_list, after, word_dict)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
