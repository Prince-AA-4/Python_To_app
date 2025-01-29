print("****Welcome to my to_do app****")

todos=[]
while True:
    user_option = input("Choose an option below: \n1.Add Task \n2.View \n3.Edit \n4.Delete \n5. Exit \n")
    if user_option=="1":
        # add a task
        todo =input("Enter to-do:\n")
        todos.append(todo) 
        print(f"{todo} added succesfully")
    elif user_option=="2":
        pass
    elif user_option=="3":
        pass
    elif user_option=="4":
        pass
    elif user_option == "5":
        print("Goodbye....")
        exit()
    else:
        print("wrong entry")