#!/usr/bin/python3
"""
This module uses requests to interact with the JSONPlaceholder API.
It accepts an employee ID as a command-line argument and exports the
employee's TODO list progress in a specific CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee ID>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, employee_id)
    todos_url = "{}todos".format(base_url)

    users = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = [user['username'] for user in users
                if user['id'] == employee_id][0]

    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])

        for todo in todos:
            if todo['userId'] == employee_id:
                writer.writerow([employee_id, username,
                                 todo['completed'], todo['title']])
