todo_list = []

while True:
    if not todo_list:
        print("\nYour ToDo list is empty")
    else:
        index = 1
        for task in todo_list:
            print(f"\n{index}. {task}")
            index += 1
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Quit")
    
    choice = input("\nEnter your choice (1, 2, or 3): ")
    
    if choice == "1":
        new_task = input("Enter the new task: ")
        todo_list.append(new_task)
        print("Task has been added to the list")
    elif choice == "2":
        if not todo_list:
            print("Your ToDo list is empty")
        else:
            todo_list.pop(-1)
    elif choice == "3":
        print("Quitting")
        break
    