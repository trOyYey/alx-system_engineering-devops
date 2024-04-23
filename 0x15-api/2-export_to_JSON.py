#!/usr/bin/python3
"""
    gather data from API script
"""
import requests as RQ
from sys import argv
from json import dump


if __name__ == "__main__":
    id = argv[1]
    user = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    user = RQ.get(user).json().get("username")
    todo = RQ.get(todo).json()
    final = {id: []}
    for key in todo:
        final.get(id).append({
            "task": key.get("title"),
            "completed": key.get("completed"),
            "username": user
            })
    with open(f"{id}.json", "w+", newline='\n') as File:
        dump(final, File)
