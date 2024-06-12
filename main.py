from todo import ToDoList

def print_menu():
    print("To-Do List Application")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as done")
    print("4. List tasks")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
        elif choice == '3':
            task = input("Enter the task to mark as done: ")
            todo_list.mark_task_done(task)
        elif choice == '4':
            tasks = todo_list.list_tasks()
            for task in tasks:
                print(task)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
