from todo import ToDoList


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Show done tasks")
        print("5. Mark task as done")
        print("6. Edit task")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to remove: "))
            todo_list.remove_task(index)
        elif choice == '3':
            tasks = todo_list.list_tasks()
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '4':
            done_tasks = todo_list.show_done_tasks()
            for idx, task in enumerate(done_tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '5':
            task = input("Enter task to mark as done: ")
            todo_list.mark_task_done(task)
        elif choice == '6':
            index = int(input("Enter task number to edit: ")) - 1
            new_task = input("Enter new task description: ")
            todo_list.edit_task(index, new_task)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
