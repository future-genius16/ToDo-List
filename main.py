from todo import ToDoList


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to remove: "))
            todo_list.remove_task(index)
        elif choice == '3':
            tasks = todo_list.show_tasks()
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
