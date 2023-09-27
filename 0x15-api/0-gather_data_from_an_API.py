#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import requests
import sys


employee_id = sys.argv[1]

try:
    employee_id = int(employee_id)
except ValueError:
    print("Invalid employee ID")
    sys.exit()


base_url = "https://jsonplaceholder.typicode.com/"
user_url = base_url + "users/" + str(employee_id)
todo_url = base_url + "todos?userId=" + str(employee_id)
user_response = requests.get(user_url).json()
user_name = user_response.get("name")
todo_response = requests.get(todo_url).json()
total_tasks = 0
done_tasks = 0
done_titles = []


for todo in todo_response:

    total_tasks += 1

    completed = todo.get("completed")
    title = todo.get("title")

    if completed:
        done_tasks += 1
        done_titles.append(title)

print("Employee {} is done with tasks({}/{})".format(user_name, done_tasks, total_tasks))
for title in done_titles:
    print("\t {}".format(title))