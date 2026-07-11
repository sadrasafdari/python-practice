tasks =[]
while True:
    
    print("ToDoList")
    print("1. add to list")
    print("2. view list")
    print("3. remove")
    print("4. close")

    choice = input("enter number:")

    
    if choice == "1":
        print("add to list")
        task=input("enter new task:")
        tasks.append(task)
    elif choice=="2":
        print("view")
        for task in tasks:
            print(task)
    elif choice=="3":
        print("remove")
        for i in range(len(tasks)):
            print(i+1,tasks[i])
            number=int(input("enter task number: "))
            tasks.pop(number-1)
    elif choice=="4":
        print("goodluck")
        break
    else:
        print("wrong")
        
            
        
    
    


