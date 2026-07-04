application_name = "Todo Application"
options = """Options:
1. Create a Todo 
2. Display all the Todos 
3. Display a single todo 
4. Mark a Todo as completed 
5. Edit a Todo 
6. Delete a Todo  
7. Display Summary of all Todos
8. Exit"""
todos = [] 
tid = 1 
while True:
    print(application_name)
    print(options)
    choice = int(input("Enter your choice (1-7): "))
    print("-"*15)
    match choice:
        case 1:
            print("Adding Todo: ")
            title = input("Title: ")
            description = input("Description: ")
            todo = {
                "id":tid,
                "title":title,
                "description":description,
                "status":False, # default considering it as pending
            }
            todos.append(todo)
            tid += 1 
            print("Todo Added Success")
        case 2:
            print("Displaying All The Todos:")
            for t in todos:
                print(f"ID: {t["id"]}")
                print(f"Title: {t["title"]}")
                print()
        case 3:
            print("Displaying single Todo: ")
            target_id = int(input("ID: "))
            todo = None # we are assuming the todo is not there in our list by 
                        # default 
            for t in todos:
                if t["id"] == target_id:
                    # we found the todo 
                    todo = t 
                    break 
            
            if todo == None: 
                print("Not found")
            else:
                """
                if todo["status"]:
                    status = "completed"
                else:
                    status = "pending"
                """
                status = "completed" if todo["status"] else "pending"
                print(f"ID: {todo["id"]}")
                print(f"Title: {todo["title"]}")
                print(f"Description: {todo["description"]}")
                print(f"Status: {status}")
        case 4:
            print("Marking Todo as Completed: ")
            target_id = int(input("ID: "))
            todo = None 
            for t in todos:
                if t["id"] == target_id:
                    todo = t 
                    break 
            if todo == None: 
                print("Not found.")
            elif todo["status"]:
                print("Cannot change the status.It is already completed.")
            else:
                todo["status"] = True 
                print("Todo marked as completed.")
        case 5:
            print("Editing a Todo: ")
            target_id = int(input("ID: "))
            todo = None 
            for t in todos:
                if t["id"] == target_id:
                    # we found the todo 
                    todo = t 
                    break 
            if todo == None:
                print("Not found")
            else:
                print("Options:\n1.Title\n2.Description\n3.Reset Status")
                edit_choice = int(input("Enter your choice: "))
                match edit_choice:
                    case 1:
                        title = input("Title: ")
                        todo["title"] = title
                        print("Title updated succesfully.")
                    case 2:
                        description = input("Description: ")
                        todo["description"] = description
                        print("Description updated succesfully.")
                    case 3:
                        todo["status"] = False 
                        print("Status reset succesfully")
                    case _ :
                        print("Invalid input. Try again.")
        case 6:
            print("Deleting a Todo: ")
            target_id = int(input("ID: "))
            index = -1 # indicating index not found
            for i in range(len(todos)):
                if todos[i]["id"] == target_id:
                    index = i 
                    break 
            if index == -1:
                print("Not found.")
            else:
                todos.pop(index)
                print("Todo deleted succesfully.")
        case 7:
            print("Summarzing todos")
            completedcount = 0
            pendingcount = 0
            for todo in todos:
                if todo["status"]:
                    completedcount += 1
                else:
                    pendingcount += 1
            totalcount = len(todos)
            print("Summary of Todo List")
            print(f"{completedcount} Todos Completed")
            print(f"{pendingcount} Todos Pending")
            print(f"{totalcount} Total Todos")
        case 8:
            print("Exiting...")
            break 
        case _ :
            print("Invalid choice, Try again.")
    choice = input("Do you want to continue(y/n)? ")
    if choice == "y":
        print("-"*15)
        continue
    else:
        print("Exiting...")
        break
