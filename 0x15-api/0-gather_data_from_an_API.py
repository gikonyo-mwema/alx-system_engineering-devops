#!/usr/bin/python3
"""
This module uses requests to interact with the JSONPlaceholder API.
It accepts an employee ID as a command-line argument and prints the
employee's TODO list progress in a specific format.
"""

import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Fetches and prints the TODO list progress for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    done_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee ID>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_list(employee_id)
