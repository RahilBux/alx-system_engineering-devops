#!/usr/bin/python3
"""
Contains the number_of_subscribers function to use
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a given subreddit user"""
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
