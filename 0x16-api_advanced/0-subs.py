#!/usr/bin/python3
"""
Contains the number_of_subscribers function to use
"""
import requests

def number_of_subscribers(subreddit):
    """returns the num of subscribers for given"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    req = requests.get('https://www.reddit.com/r/{}/about.json',format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = req.get("data", {}).get("subscribers", 0)
    return subs
