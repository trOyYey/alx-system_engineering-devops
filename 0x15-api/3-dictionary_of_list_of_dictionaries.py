#!/usr/bin/python3
"""
    gather data from API script
"""
import requests as RQ
from json import dump


if __name__ == "__main__":
    user = f"https://jsonplaceholder.typicode.com/users"
    todo = f"https://jsonplaceholder.typicode.com/todos"
    users = RQ.get(user).json()
    todos = RQ.get(todo).json()
    result = {}
    for key in todos:
        id = str(key.get("userId"))
        new = {"username": users[int(id) - 1].get("username"),
               "task": key.get("title"),
               "completed": key.get("completed")}
        if id in result:
            result.get(id).append(new)
        else:
            result.update({id: [new]})
    with open("todo_all_employees.json", "w+", newline='\n') as File:
        dump(result, File)
