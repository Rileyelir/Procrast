# task_manager.py
# Creates, stores, and retrieves tasks while managing their status.

import json_util as jsut

class Task:
    title = ""
    completed = False

    def __init__(self, title: str):
        self.title = title
    
    def toggle(self, option = None):
        """Toggle completion status of this task, or set a specific value."""
        if type(option) is bool:
            self.completed = option
        else:
            self.completed = not self.completed

def load():
    loadedValue = jsut.get_value("procrast.json", ["tasks"])
    if loadedValue == None:
        return []

    current: [Task] = []
    for task in loadedValue:
        new = Task(task["title"])
        new.toggle(task["completed"])
        current.append(new)
    return current

tasks: [Task] = load()

def save():
    current = []
    for t in tasks:
        current.append({
            "title": t.title,
            "completed": t.completed
        })
    jsut.set_value("procrast.json", "tasks", current)

def create(title: str):
    new = Task(title)
    tasks.append(new)
    save()

if __name__ == "__main__":
    for t in tasks:
        print(f"{t.title}: {"Completed" if t.completed else "Not Completed"}")