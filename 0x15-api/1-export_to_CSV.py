#!/usr/bin/python3
"""
Exports the to-do list for a given employee to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvf:
        writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, i.get("completed"), i.get("title")])
            for i in todo]
