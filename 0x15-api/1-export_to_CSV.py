#!/usr/bin/python3
"""
Exports the to-do list for a given employee to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"user_Id": u_id}).json()

    with open("{}.csv".format(u_id), "w", newline="") as csvf:
        writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [u_id, username, i.get("completed"), i.get("title")])
            for i in todo]
