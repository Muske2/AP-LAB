class Bank:
    def __init__(self, name, age, account_number, account_type, balance=0):
        
        self.name = name
        self.age = age
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        if 18 <= age <= 100:
            self.age = age
        else:
            raise ValueError("Age must be between 18 and 100")
        
        if isinstance(account_number, int) and 10000 <= account_number <= 99999:
            self.account_number = str(account_number)
        else:
            raise ValueError("Account number must be a 5-digit integer")
        
        if account_type in ['S', 'C']:
            self.account_type = account_type
        else:
            raise ValueError("Account type must be 'S' for Savings or 'C' for Current")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def print_account_details(self):
        print(f"Account Details for Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}\n")

    def __del__(self):
        print(f"Account {self.account_number} has been closed.")

# Create sample accounts
account1 = Bank("P1", 30, 12345, "S", 1000)
account2 = Bank("P2", 25, 67890, "C", 500)
account3 = Bank("P3", 35, 24680, "S", 1500)
account4 = Bank("P4", 28, 13579, "C", 200)
account5 = Bank("P5", 22, 97531, "S", 3000)

# Menu-driven program
accounts = [account1, account2, account3, account4, account5]
try:
    while True:
        print("\nBank Operations Menu:")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Print Account Details")
        print("5. Exit")
    
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            account_number = int(input("Enter account number: "))
            account_type = input("Enter account type: ")
            initial_balance = float(input("Enter initial balance: "))
        
            new_account = Bank(name, age, account_number, account_type, initial_balance)
            accounts.append(new_account)
            print("New account created successfully.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter the deposit amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
                else:
                    print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
                else:
                    print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.account_number == account_number:
                    account.print_account_details()
                    break
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
            
except ValueError as ve:
    print(f"Error: {ve}")


