#!/usr/bin/python3
"""
This module uses requests to interact with the JSONPlaceholder API.
It accepts an employee ID as a command-line argument and exports the
employee's TODO list progress in a specific JSON format.
"""

import json
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Fetches and exports the TODO list progress for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    user = requests.get(user_url).json()
    username = user.get('username')
    todos = requests.get(todos_url).json()

    tasks = []
    for task in todos:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        tasks.append(task_dict)

    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee ID>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_list(employee_id)
