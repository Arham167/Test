print("Welcome")

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

add_task("Learn Git")

def show_tasks():
    print("Current tasks:")
    for task in tasks:
        print(f"- {task}")

add_task("Practice Git")
show_tasks()
