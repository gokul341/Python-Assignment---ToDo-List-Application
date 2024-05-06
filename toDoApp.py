class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task '{}' added successfully.".format(task))

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print("Task '{}' deleted successfully.".format(deleted_task))
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += " (Completed)"
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print("{}. {}".format(index, task))
        else:
            print("No tasks.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter index of task to delete: "))
            todo_list.delete_task(index)
        elif choice == '3':
            index = int(input("Enter index of task to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
