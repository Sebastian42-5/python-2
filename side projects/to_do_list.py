def to_do_list():
    tasks = []
    
    while True:

        print("We")
        print("\n --TO DO LIST--")
        print("1- Add Task")
        print("2- Show Tasks")
        print("3- Modify Tasks ")
        print("4- Mark Task as done")
        print("5- Exit")
    

        choice = input("Enter your choice: ")

        if choice == 1:
            print()
            n_tasks = input("\n How many tasks do you want to add?")

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append(task)
                tasks.append(False)

        elif choice == 2:
            print("Here are your tasks: ")
            print(tasks)

        elif choice == 3:
            print(tasks)
            modify_task = int(input("Enter the number of the task to modify: ")) - 1

            tasks[modify_task] = input("Enter the name of the task you want to modify: ")


        elif choice == 4:
            print(tasks)
            done_task = int(input('Select the number of the task to mark as done')) - 1


        elif choice == 5:
            break
to_do_list()