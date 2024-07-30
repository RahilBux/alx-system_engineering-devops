#!/usr/bin/python3
"""
Exports the to-do list for a given employee to CSV
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"user_Id": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": i.get("title"),
            "completed": i.get("completed"),
            "username": username
            } for i in todo]}, jsonfile)
