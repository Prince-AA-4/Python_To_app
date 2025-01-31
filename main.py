print("****Welcome to my to_do app****")

todos=[]
while True:
    user_option = input("Choose an option below: \n1.Add Task \n2.View \n3.Edit \n4.Delete \n5. Clear \n6.Exit \n")
    if user_option=="1":
        # add a task
        todo =input("Enter to-do:\n")
        todos.append(todo) 
        print(f"{todo} added succesfully")
    elif user_option=="2":
        # viewing added task
      if not todos:
        print("Todo list is empty! ")
      else:
        print("to-do list")
        for idx, item in enumerate(todos, start= 1):
            print(f"{idx}. {item}")
    elif user_option=="3":
        # editing task list
        if not todos:
            print("There are no items to edit")
        else:
            try:
                task_number = int(input("Enter task number to edit:\n"))
                new_todo = input("Enter new to-do:\n")
                todos[task_number - 1] = new_todo
                print(f"Task {task_number} has been edited")
            except (ValueError, IndexError):
                print("Invalid task number")
    elif user_option=="4":
        # deleting a task
        if not todos:
            print("there is no item to delete")
        else:
            try:
                task_number = int(input("Enter task number to delete: \n"))
                todos.pop(task_number - 1)
                print(f"{todo} is successfully deleted")
            except(ValueError, IndexError):
                print('Invalid task number')
    elif user_option == "5":
        # clearing the list
        if not todos:
            print("To-do list is empty!")
        else:
            todos.clear()
            print("All tasks cleared succesfully")
    elif user_option == "6":
        print("Goodbye....")
        exit()
    else:
        print("wrong entry")