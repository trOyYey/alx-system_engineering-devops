#!/usr/bin/python3
"""
    subscribers api counter
"""
import requests


def number_of_subscribers(subreddit):
    """
        input subreddit and returns sub numbers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:Python (by/Troyzuwara)"}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.ok:
        value = req.json().get("data").get("subscribers")
        return value if value is not None else 0
    return 0
