#!/usr/bin/python3
"""
    gather data from API script
"""
import requests as RQ
from sys import argv
import csv

if __name__ == "__main__":
    id = argv[1]
    user = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    user = RQ.get(user).json().get("username")
    todo = RQ.get(todo).json()
    with open(f"{id}.csv", "w+", newline='\n') as File:
        writer = csv.writer(File, quotechar='"', quoting=csv.QUOTE_ALL)
        for key in todo:
            writer.writerow([id, user, key.get("completed"),
                            key.get("title")])
