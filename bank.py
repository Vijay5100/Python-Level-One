"""
Bank Simulator: 
1. Create an Account 
2. Add money 
3. Withdraw money 
4. Transfer money 
5. Display Account 
6. Transaction history
7. Check Acccount Balance
8. Exit

Structure of Account: 
Account Number: 
Holder Name: 
Account Type: 
Age: 
Balance: 

*Structure of Deposit:
Transaction ID:
Transaction Type: "Deposit"
Amount:

Structure of Transaction:
Transaction ID: 
From Account: 
To Account: 
Amount: 
"""
from tabulate import tabulate
from datetime import datetime
from zoneinfo import ZoneInfo
import random
account_counter = 1
application_name = "Bank Simulator"
options = """Options:
1. Create an Account 
2. Money Deposit 
3. Withdraw money 
4. Transfer money 
5. Display Account 
6. Transaction history
7. Check Acccount Balance
8. Exit
"""
accounts = [] 
transactions = []
account_type = ("checking","savings","corporate")
zone = ZoneInfo("America/Phoenix")
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
            account_number = account_counter
            account_counter += 1
            holder_name = input("Holder Name: ")
            print("Account Types:")
            for i in range(len(account_type)):
                print(f"{i + 1}. {account_type[i]}")
            type_choice = int(input("Choose Account Type (1-3): "))
            while type_choice < 1 or type_choice > len(account_type):
                print("Invalid Account Type. Try again.")
                type_choice = int(input("Choose Account Type (1-3): "))
            selectedaccount_type = account_type[type_choice - 1]
            age = int(input("Age: "))
            pin = input("Enter 4-digit PIN: ")
            while len(pin) != 4 or pin.isdigit() == False:
                print("Invalid PIN. PIN must be exactly 4 digits.")
                pin = input("Enter 4-digit PIN: ")
            balance = 0
            account = {
                "account_number": account_number,
                "holder_name": holder_name,
                "account_type": selectedaccount_type,
                "age": age,
                "balance": balance,
                "pin": pin
            }
            accounts.append(account)
            print(f"Account number: {account['account_number']}")
            print("Account created successfully.")
        case 2:
            print("Money Deposit: ")
            account_number = int(input("Enter the Account Number: "))
            pin = input("Enter the 4-digit PIN: ")
            selected_account = None
            for account in accounts:
                if account["account_number"] == account_number:
                    selected_account = account
                    break
            if selected_account == None:
                print("Account not found.")
            elif selected_account["pin"] != pin:
                print("Incorrect PIN.")
            else: 
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Invalid amount.")
                else:
                    selected_account["balance"] += amount
                    current_datetime = datetime.now(zone)
                    transaction = {
                        "transaction_id": len(transactions) + 1,
                        "type": "deposit",
                        "from_account": None,
                        "to_account": account_number,
                        "amount": amount,
                        "date": str(current_datetime.date()),
                        "time": str(current_datetime.time())[:8]
                    }
                    transactions.append(transaction)
                print("Money deposited successfully.")
                print(f"New Balance: {selected_account['balance']}")
        case 3:
            print("Money Withdraw: ")
            account_number = int(input("Enter the Account Number: "))
            pin = input("Enter the 4-digit PIN: ")
            selected_account = None
            for account in accounts:
                if account["account_number"] == account_number:
                    selected_account = account
                    break
            if selected_account == None:
                print("Account not found.")
            elif selected_account["pin"] != pin:
                print("Incorrect PIN.")
            else:
                amount = float(input("Enter withdraw amount: "))
                if amount <= 0:
                    print("Invalid amount.")
                elif amount > selected_account["balance"]:
                    print("Insufficient balance.")
                else:
                    selected_account["balance"] -= amount
                    current_datetime = datetime.now(zone)
                    transaction = {
                        "transaction_id": len(transactions) + 1,
                        "type": "withdraw",
                        "from_account": account_number,
                        "to_account": None,
                        "amount": amount,
                        "date": str(current_datetime.date()),
                        "time": str(current_datetime.time())[:8]
                    }
                    transactions.append(transaction)
                    print("Money withdrawn successfully.")
                    print(f"New Balance: {selected_account['balance']}")
        case 4:
            print("Transfer Money: ")
            from_account_number = int(input("Enter the From account Number: "))
            to_account_number = int(input("Enter the To account Number: "))
            pin = input("Enter the 4-digit PIN for the From account: ")
            amount = float(input("Enter the amount: "))
            from_account = None
            to_account = None
            for account in accounts:
                if account["account_number"] == from_account_number:
                    from_account = account
                if account["account_number"] == to_account_number:
                    to_account = account
            if from_account == None:
                print("From account not found.")
            elif to_account == None:
                print("To account not found.")
            elif from_account["pin"] != pin:
                print("Incorrect PIN.")
            elif from_account_number == to_account_number:
                print("You cannot transfer money to the same account.")
            elif amount <= 0:
                print("Invalid amount.")
            elif amount > from_account["balance"]:
                print("Insufficient balance.")
            else:
                from_account["balance"] -= amount
                to_account["balance"] += amount
                current_datetime = datetime.now(zone)
                transaction = {
                    "transaction_id": len(transactions) + 1,
                    "type": "transfer",
                    "from_account": from_account_number,
                    "to_account": to_account_number,
                    "amount": amount,
                    "date": str(current_datetime.date()),
                    "time": str(current_datetime.time())[:8]
                }
                transactions.append(transaction)
                print("Money transferred successfully.")
                print(f"To Account New Balance: {to_account['balance']}")
        case 5:
            print("Displaying Account: ")
            account_number = int(input("Enter the Account Number: "))
            pin = input("Enter the 4-digit PIN: ")
            selected_account = None
            for account in accounts:
                if account["account_number"] == account_number:
                    selected_account = account
                    break
            if selected_account == None:
                print("Account not found.")
            elif selected_account["pin"] != pin:
                print("Incorrect PIN.")
            else:
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
        case 6:
            print("Transaction History:")
            account_number = int(input("Enter Account ID: "))
            pin = input("Enter the 4-digit PIN: ")
            selected_account = None
            for account in accounts:
                if account["account_number"] == account_number:
                    selected_account = account
                    break
            if selected_account == None:
                print("Account not found.")
            elif selected_account["pin"] != pin:
                print("Incorrect PIN.")
            else:
                rows = []
                for transaction in transactions:
                    if transaction["type"] == "deposit":
                        if transaction["account_number"] == account_number:
                            rows.append([
                                transaction["transaction_id"],
                                transaction["type"],
                                transaction["from_account"],
                                transaction["to_account"],
                                transaction["amount"],
                                transaction["date"],
                                transaction["time"]
                            ])
                    elif transaction["type"] == "withdraw":
                        if transaction["account_number"] == account_number:
                            rows.append([
                                transaction["transaction_id"],
                                transaction["type"],
                                transaction["from_account"],
                                transaction["to_account"],
                                transaction["amount"],
                                transaction["date"],
                                transaction["time"]
                            ])

                    elif transaction["type"] == "transfer":
                        if (
                            transaction["from_account"] == account_number
                            or transaction["to_account"] == account_number
                        ):
                            rows.append([
                                transaction["transaction_id"],
                                transaction["type"],
                                transaction["from_account"],
                                transaction["to_account"],
                                transaction["amount"],
                                transaction["date"],
                                transaction["time"]
                            ])
                headers = [
                    "Transaction ID",
                    "Type",
                    "From Account",
                    "To Account",
                    "Amount",
                    "Date",
                    "Time"
                ]
                if len(rows) == 0:
                    print("No transactions found for this account.")
                else:
                    print(tabulate(rows, headers=headers, tablefmt="grid"))
        case 7:
            print("Check Account Balance:")
            account_number = int(input("Enter the Account Number: "))
            pin = input("Enter the 4-digit Pin: ")
            selected_account = None
            for account in accounts:
                if account["account_number"] == account_number:
                    selected_account = account
                    break
            if selected_account == None:
                print("Account not found.")
            elif selected_account["pin"] != pin:
                print("Incorrect PIN.")
            else:
                print("Balance:")
                print(selected_account["balance"])
        case 8:
            print("Exiting...")
            break
        case _ : 
            print("Invalid Choice, Try again.")
    if choice != 8:
        continue_choice = input("\nDo you want to continue? (yes/no): ")
        if continue_choice.lower() != "yes":
            print("Exiting...")
            break
