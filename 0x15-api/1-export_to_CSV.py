#!/usr/bin/python3
"""Script returns todo list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userid": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, qouting=csv.QOUTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
            ) for t in todo]
