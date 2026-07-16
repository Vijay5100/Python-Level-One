from tabulate import tabulate

todos = []
tid = 0

def generate_todo_id() -> int:
    """
    increases and returns the todo ID.
    Returns:
    - tid (int): new todo ID.
    """
    global tid
    tid += 1
    return tid

def add_todo() -> None:
    """
    takes the todo title and description from the user and adds the new todo to the todos list.
    Returns:
    - None
    """
    title = input("Title: ")
    description = input("Description: ")
    todo = {
        "id":generate_todo_id(),
        "title":title,
        "description":description,
        "status":False,
        "priority":"normal"
    }
    todos.append(todo)

def display_todos() -> None:
    """
    displays all todos from the todos list in a table.
    Returns:
    - None
    """
    if len(todos) == 0:
        print("No todos found.")
    else:
        rows = []
        for todo in todos:
            status = "Completed" if todo["status"] else "Pending"
            rows.append([
                todo["id"],
                todo["title"],
                todo["description"],
                status,
                todo["priority"]
            ])
        headers = [
            "ID",
            "Title",
            "Description",
            "Status",
            "Priority"
        ]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
def display_todo(todo: dict) -> None:
    """
    displays one todo in a table.
    Args:
    - todo (dict): todo that will be displayed.
    Returns:
    - None
    """
    status = "Completed" if todo["status"] else "Pending"
    rows = [[todo["id"], todo["title"], todo["description"], status, todo["priority"]]]
    headers = ["ID", "Title", "Description", "Status", "Priority"] 
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    
def search_todo(target_id: int) -> dict | None:
    """
    searches for a todo using its ID.
    Args:
    - target_id (int): ID of the todo being searched for.
    Returns:
    - todo (dict): matching todo when it is found.
    - None: returns None when no matching todo is found.
    """
    for todo in todos:
        if todo["id"] == target_id:
            return todo
    return None

def edit_todo(todo: dict, key: str, value: str | bool) -> None:
    """
    changes one value inside a todo
    Args:
    - todo (dict): todo that will be changed.
    - key (str): dictionary key that will be changed.
    - value (str | bool): new value assigned to the key.
    returns:
    - None
    """
    todo[key] = value
    print("Todo updated successfully.")

def display_todos_summary() -> None:
    """
    displays the number of completed, pending, and total todos.
    Returns:
    - None
    """
    completed_count = 0
    pending_count = 0
    for todo in todos:
        if todo["status"]:
            completed_count += 1
        else:
            pending_count += 1
    total_count = len(todos)
    rows = [
        ["Completed", completed_count],
        ["Pending", pending_count],
        ["Total", total_count]
    ]
    headers = ["Todo Type", "Count"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def display_pending_todos() -> None:
    """
    displays all todos that have pending status.
    Returns:
    - None
    """
    pending_todos = []
    for todo in todos:
        if todo["status"] == False:
            pending_todos.append(todo)
    if len(pending_todos) == 0:
        print("No pending todos found.")
    else:
        rows = []
        for todo in pending_todos:
            rows.append([
                todo["id"],
                todo["title"],
                todo["description"],
                todo["priority"]
            ])
        headers = [
            "ID",
            "Title",
            "Description",
            "Priority"
        ]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
def mark_todo_completed(todo: dict) -> None:
    """
    changes a todo's status from pending to completed.
    Args:
    - todo (dict): todo that will be marked as completed.
    Returns:
    - None
    """
    if todo["status"]:
        print("This todo is already completed.")
    else:
        todo["status"] = True
        print("Todo marked as completed.")
        
application_name = "Todo Application"
options = """Options:
1. Create a Todo
2. Display all Todos
3. Display a single Todo
4. Mark a Todo as completed
5. Edit a Todo
6. Delete a Todo
7. Display Summary of all Todos
8. Display Pending Todos
9. Exit
"""
while True:
    print(application_name)
    print(options)
    choice = int(input("Enter your choice (1-9): "))
    print("-" * 15)
    match choice:
        case 1:
            print("Adding Todo:")
            add_todo()
        case 2:
            print("Displaying All Todos:")
            display_todos()
        case 3:
            print("Displaying a Single Todo:")
            target_id = int(input("ID: "))
            todo = search_todo(target_id)
            if todo is None:
                print("Todo not found.")
            else:
                display_todo(todo)
        case 4:
            print("Marking Todo as Completed:")
            target_id = int(input("ID: "))
            todo = search_todo(target_id)
            if todo is None:
                print("Todo not found.")
            else:
                mark_todo_completed(todo)
        case 5:
            print("Editing a Todo:")
            target_id = int(input("ID: "))
            todo = search_todo(target_id)
            if todo is None:
                print("Todo not found.")
            else:
                print("""Edit Options:
                        1. Title
                        2. Description
                        3. Reset Status
                        4. Change Priority
                        """)
                edit_choice = int(input("Enter your choice: "))
                match edit_choice:
                    case 1:
                        title = input("New Title: ")
                        edit_todo(todo, "title", title)
                    case 2:
                        description = input("New Description: ")
                        edit_todo(todo, "description", description)
                    case 3:
                        edit_todo(todo, "status", False)
                    case 4:
                        priority = input("New Priority: ")
                        edit_todo(todo, "priority", priority)
                    case _:
                        print("Invalid input. Try again.")
        case 6:
            print("Deleting a Todo:")
            target_id = int(input("ID: "))
            todo = search_todo(target_id)
            if todo is None:
                print("Todo not found.")
            else:
                todos.remove(todo)
                print("Todo deleted successfully.")
        case 7:
            print("Summary of Todos:")
            display_todos_summary()
        case 8:
            print("Displaying Pending Todos:")
            display_pending_todos()
        case 9:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Try again.")
    continue_choice = input("Do you want to continue (y/n)? ")
    if continue_choice.lower() != "y":
        print("Exiting...")
        break
    print("-" * 15)
