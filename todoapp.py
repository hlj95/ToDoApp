
tasks = []
try:

    while True: 
    
        print("1 - Add Task")
        print("2 - Delete Task")
        print("3 - View All Tasks")
        print("q - Quit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Please enter task title: ")
            priority = input("Please enter task priority: ")
            task = {"Task": title, "TaskID": len(tasks) +1, "Priority": priority}
            tasks.append(task)
            print(task)
            
        elif choice == 2:

            idtodelete = int(input("Which task do you wnat to delete?"))
            task = {"Task": title, "Priority": priority}
            print("DELETING FROM A DICTIONARY")
            task = {"Task": title, "Priority": priority}
            print(task)
            del tasks[int(idtodelete) - 1]
            print(tasks)
    
        elif choice == 3:
            print(tasks)
            
        
except ValueError:
    print("Goodbye")