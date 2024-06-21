#!/usr/bin/python3
"""
    
"""
import requests


def count_words(subreddit, word_list, count={}, after=''):
    """
        print a sorted count of given keywords of hot posts of subrddit
    """
    req = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "ubuntu:Python (by/AjwadG)"}

    data = requests.get(req, headers=headers, allow_redirects=False)

    if data.status_code != 200:
        return None
    if not count:
        count = {key.lower(): 0 for key in word_list}
    value = data.json().get("data")
    for i in value.get("children"):
        for word in i.get("data").get("title").split():
            for key in count:
                if word.lower() == key:
                    count[key] += 1
    after = value.get("after")
    if after:
        count_words(subreddit, word_list, count, after)
    else:
        count = dict(sorted(count.items()))
        count = dict(sorted(count.items(), key=lambda item: item[1],
                            reverse=True))
        for key in count:
            if count[key] != 0:
                print(f"{key}: {count[key]}")
