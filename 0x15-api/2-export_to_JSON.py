#!/usr/bin/python3
"""Script returns todo list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userid": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": t.get("title"), "completed": t.get(
            "completed"), "username": username) for t in todo]}, jsonfile)
