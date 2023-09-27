#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if user_response.status_code != 200:
        return None, None

    if todo_response.status_code != 200:
        return None, None

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])
    completed_task_titles = [task["title"] for task in todo_data if task["completed"]]

    return employee_name, total_tasks, completed_tasks, completed_task_titles

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_name, total_tasks, completed_tasks, completed_task_titles = get_employee_todo_progress(employee_id)

    if employee_name is None:
        print("Employee not found")
        sys.exit(1)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    for task_title in completed_task_titles:
        print(f"\t{task_title}")
