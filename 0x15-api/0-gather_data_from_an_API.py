#!/usr/bin/python3
"""
    gather data from API script
"""
import requests as RQ
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    user = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    user = RQ.get(user).json()
    todo = RQ.get(todo).json()
    complete = []
    for task in todo:
        if task.get("completed"):
            complete.append(task)
    print(f"Employee {user.get('name')} is done with"
          f"tasks({len(complete)}/{len(todo)}):")
    for key in complete:
        print(f"\t {key.get('title')}")
