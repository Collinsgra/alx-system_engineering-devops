#!/usr/bin/python3
"""returns information about his/her
to do list progress"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee information
        response_user = requests.get(user_url)
        response_user.raise_for_status()
        employee_data = response_user.json()

        # Fetch employee's TODO list
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos = response_todos.json()

        # Calculate progress
        total_tasks = len(todos)
        completed_tasks = sum(1 
                for todo in todos 
                if todo['completed'])

        # Display the progress
        print(f"Employee {employee_data['name']} 
        is done with tasks 
                ({completed_tasks}/{total_tasks}):")
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    except KeyError:
        print("Invalid employee ID or API response format.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
