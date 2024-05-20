#!/usr/bin/python3
"""Script returns todo list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            a.get("id"): [{
                "task": b.get("title"),
                "completed": b.get("completed"),
                "username": a.get("username")
            } for b in requests.get(url + "todos", params={"userId": a.get("id")}).json()] for a in users}, jsonfile)
