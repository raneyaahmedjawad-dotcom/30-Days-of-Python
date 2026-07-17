print("=" * 50)
print("PYTHON BANKING SYSTEM")
print("=" * 50)

# User information
user_name = input("Enter your name: ")
balance= 5000.0  # Initial balance
transactions = []  # List to store transaction history

print("\nWelcome,", user_name)
print("Your current balance is: $", balance)

while True:
    print("\n" + "=" * 50)
    print("MAIN MENU")
    print("=" * 50)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    # Option 1 - Check Balance
    if choice == 1:
        print("Your current balance is: $", balance)    

    # Option 2 - Deposit Money
    elif choice == 2:
        try:
            amount = float(input("Enter the amount to deposit: $"))
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
            continue
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: ${amount}")
            print("Deposit successful!")
            print("Your new balance is: $", balance)
        else:
            print("Invalid deposit amount! Please enter a positive value.") 

    # Option 3 - Withdraw Money
    elif choice == 3:
        try:
            amount = float(input("Enter the amount to withdraw: $"))
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
            continue
        if amount <= 0:
            print("Invalid withdrawal amount! Please enter a positive value.")
        elif amount > balance:
            print("Insufficient funds! Your current balance is: $", balance)
        else:
            balance -= amount
            transactions.append(f"Withdrew: ${amount}")
            print("Withdrawal successful!")
            print("Your remaining balance is: $", balance)

    # Option 4 - View Transaction History
    elif choice == 4:
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in transactions:
                print("-", transaction)

    # Option 5 - Exit
    elif choice == 5:
        print("Thank you for using the Python Banking System. Goodbye!")
        break         

    # Invalid Choice
    else: 
        print("Invalid choice! Please select a valid option (1-5).")

