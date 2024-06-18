#!/usr/bin/python3
"""
    get list of the hottest articles
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        recursive listing of hotest articles
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "ubuntu:Python (by/Troyzuwara)"}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return None
    value = req.json().get("data")
    for post in value.get("children"):
        hot_list.append(post.get("data").get("title"))
    after = value.get("after")
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
