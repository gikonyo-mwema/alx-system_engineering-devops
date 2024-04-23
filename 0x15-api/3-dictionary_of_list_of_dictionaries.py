#!/usr/bin/python3
"""
This module uses requests to interact with the JSONPlaceholder API.
It accepts an employee ID as a command-line argument and exports the
employee's TODO list progress in a specific JSON format.
"""

import json
import requests
import sys


def get_employee_todo_list():
    """
    Fetches and exports the TODO list progress for all employees.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = "{}users".format(base_url)
    todos_url = "{}todos".format(base_url)

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    user_tasks = {}
    for user in users:
        username = user.get('username')
        user_id = user.get('id')
        user_tasks[user_id] = [{"username": username,
                                "task": todo.get('title'),
                                "completed": todo.get('completed')}
                               for todo in todos if
                               todo.get('userId') == user_id]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_tasks, jsonfile)


if __name__ == "__main__":
    get_employee_todo_list()
