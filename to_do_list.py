def to_do_list():
    tasks = []
    
    while True:
        name = input("Enter your name:")

        print("We")
        print("\n --TO DO LIST--")
        print("1- Add Task")
        print("2- Show Tasks")
        print("3- Modify Tasks ")
        print("4- Mark Task as done")
        print("5- Exit")
    

        choice = input("Enter your choice:")

        if choice == 1:
            print()
            n_tasks = input("\n How many tasks do you want to add?")

            for i in range(n_tasks):
                task = input("Enter the task:")
                tasks.append(task)
                
