"""
Bank Simulator: 
1. Create an Account 
2. Add money 
3. Withdraw money 
4. Transfer money 
5. Display Account 
6. Transaction history
7. Exit 

Structure of Account: 
Account Number: 
Holder Name: 
Account Type: 
Age: 
Balance: 

Structure of Transaction:
Transaction ID: 
From Account: 
To Account: 
Amount: 
"""
from tabulate import tabulate
import random
application_name = "Bank Simulator"
options = """Options:
1. Create an Account 
2. Money Deposit 
3. Withdraw money 
4. Transfer money 
5. Display Account 
6. Transaction history
7. Exit 
"""
accounts = [] 
transactions = []
account_type = ("checking","savings","corporate")
"""
storing account types in list is a major security issue 
the data inside the list can be modified at any time.
mutability -> ability to be modified 
immutability -> they cannot be modified they are constant 
list,dictonary -> mutable data structures 
tuple -> immutable data structure
"""
# account_types = ["Check-in","Savings","Corporate"]

# account_types[0] = "Zero Balance Account"
# vijay_account_type = account_types[0]
# print(vijay_account_type)

while True: 
    print(application_name+":")
    print(options)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Creating Account: ")
            account_number = random.randint(100000, 999999)
            holder_name = input("Holder Name: ")
            print("Account Types:")
            for i in range(len(account_type)):
                print(f"{i + 1}. {account_type[i]}")
            type_choice = int(input("Choose Account Type (1-3): "))
            while type_choice < 1 or type_choice > len(account_type):
                type_choice = int(input("Invalid choice. Choose Account Type (1-3): "))
            selectedaccount_type = account_type[type_choice - 1]
            age = int(input("Age: "))
            balance = 0
            account = {
                "account_number": account_number,
                "holder_name": holder_name,
                "account_type": selectedaccount_type,
                "age": age,
                "balance": balance
            }
            accounts.append(account)
            print("Account created successfully.")
            print(account)
        case 2:
            print("Money Deposit: ")
            account_number = int(input("Enter the Account Number: "))
            flag = False
            for account in accounts:
                if account["account_number"] == account_number:
                    amount = float(input("Enter deposit amount: "))
                    if amount > 0:
                        account["balance"] += amount
                        transaction = {
                            "transaction_id": len(transactions) + 1,
                            "from_account": "Cash",
                            "to_account": account_number,
                            "amount": amount
                        }
                        transactions.append(transaction)
                        print("Money deposited successfully.")
                        print(f"New Balance: {account['balance']}")
                    else:
                        print("Invalid amount.")
                    flag = True
                    break
            if flag == False:
                print("Account not found.")
        case 3:
            print("Money Withdraw: ")
            account_number = int(input("Enter the Account Number: "))
            flag = False
            for account in accounts:
                if account["account_number"] == account_number:
                    amount = float(input("Enter withdraw amount: "))
                    if amount <= 0:
                        print("Invalid amount.")
                    elif amount > account["balance"]:
                        print("Insufficient balance.")
                    else:
                        account["balance"] -= amount
                        transaction = {
                            "transaction_id": len(transactions) + 1,
                            "from_account": "Cash",
                            "to_account": account_number,
                            "amount": amount
                        }
                        transactions.append(transaction)
                        print("Money withdrawed successfully.")
                        print(f"New Balance: {account['balance']}")
                    flag = True
                    break
            if flag == False:
                print("Account not found.")
        case 4:
            print("Transfer Money: ")
        case 5:
            print("Displaying Account: ")
            account_number = int(input("Enter the Account Number: "))
            flag = False
            for account in accounts:
                if account["account_number"] == account_number:
                    rows = [
                        [
                            account["account_number"],
                            account["holder_name"],
                            account["account_type"],
                            account["age"],
                            account["balance"]
                        ]
                    ]
                    headers = [
                        "Account Number",
                        "Holder Name",
                        "Account Type",
                        "Age",
                        "Balance"
                    ]
                    print("Account Details:")
                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                    flag = True
                    break
            if flag == False:
                print("Account not found.")
        case 6:
            print("Transactions: ")
        case 7:
            print("Exiting...")
            break 
        case _ : 
            print("Invalid Choice, Try again.")
