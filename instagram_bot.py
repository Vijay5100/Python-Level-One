import random
from tabulate import tabulate
accounts = []
male_names = ["Vijay", "Jack", "Jacob", "David", "Michael"]
female_names = ["Emma", "Sofia", "Olivia", "Sashi", "Ria"]

def generate_name(gender: str = "Male"):
    if gender.lower() == "female":
        return random.choice(female_names)
    else:
        return random.choice(male_names)
        
def generate_username(name: str):
    number = random.randint(10, 99)
    username = name.lower() + str(number)
    return username
    
def generate_dob():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1996, 2006)
    dob = f"{day}/{month}/{year}"
    return dob
    
def generate_email():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    random_name = ""
    for i in range(8):
        random_name += random.choice(characters)
    email = random_name + "@gmail.com"
    return email

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(10):
        password += random.choice(characters)
    return password

def create_account(name: str, gender: str = "Male"):
    account = {
        "username": generate_username(name),
        "name": name,
        "gender": gender,
        "dob": generate_dob(),
        "email": generate_email(),
        "password": generate_password()
    }
    accounts.append(account)
    return account

def generate_accounts(n: int):
    for i in range(n):
        gender = random.choice(["Male", "Female"])
        name = generate_name(gender)
        create_account(name, gender)
        
def display_accounts():
    if len(accounts) == 0:
        print("No accounts found.")
    else:
        rows = []
        for account in accounts:
            rows.append([
                account["username"],
                account["name"],
                account["gender"],
                account["dob"],
                account["email"],
                account["password"]
            ])
        headers = ["Username", "Name", "Gender", "Date of Birth", "Email", "Password"]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
def display(*args: int):
    if len(accounts) == 0:
        print("No accounts found.")
        return
    else:
        number = args[0]
    if number > len(accounts):
        number = len(accounts)
    rows = []
    for i in range(number):
        account = accounts[i]
        rows.append([
            account["username"],
            account["name"],
            account["gender"],
            account["dob"],
            account["email"]
        ])
    headers = ["Username", "Name", "Gender", "Date of Birth", "Email"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

number_of_accounts = int(input("How many accounts do you want to generate? "))
generate_accounts(number_of_accounts)
display_accounts()
number_of_accounts_displayed = int(input("How many accounts do you want to display? "))
display(number_of_accounts_displayed)
