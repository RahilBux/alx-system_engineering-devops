#!/usr/bin/python3
"""
Returns to-do list information for an employee
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    complete = [i.get("title") for i in todo if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todo)))
    [print("\t {}".format(j)) for j in complete]
