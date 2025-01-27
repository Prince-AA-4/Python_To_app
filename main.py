print("****Welcome to my to_do app****")
user_option = input("Choose an option below: \n1.Add Task \n2.View \n3.Edit \n4.Delete ")


todos=[]
if user_option=="1":
    # add a task
    while True:
        todo =input("Enter to-do:\n")
        todos.append(todo) 
        print(f"{todo} added succesfully")
if user_option=="2":
    pass
if user_option=="3":
    pass
if user_option=="4":
    pass
else:
    print("wrong option")