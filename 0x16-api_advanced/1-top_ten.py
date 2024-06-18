#!/usr/bin/python3
"""
    top 10 posts in subreddit module
"""
import requests


def top_ten(subreddit):
    """
        input subreddit and returns sub numbers
    """
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:Python (by/Troyzuwara)"}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print(None)
        return
    value = req.json().get("data")
    if value is None:
        print(None)
        return
    for post in value.get("children")[0:10]:
        print(post.get("data").get("title"))
