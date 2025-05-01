class ToDoList:
    def __init__(self):  # Fixed constructor
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def remove_task(self, task_index):
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task index.")
        else:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully.")

# Sample usage
todo_list = ToDoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Do laundry")

todo_list.view_tasks()

todo_list.remove_task(1)

todo_list.view_tasks()
