# Simple ATM Transaction with PIN Authentication

balance = 5000  # Initial balance
pin = "1234"    # Default ATM PIN

def atm():
    global balance
    
    # PIN verification
    for attempt in range(3):
        entered_pin = input("Enter your ATM PIN: ")
        if entered_pin == pin:
            print("\n✅ PIN Verified Successfully!\n")
            break
        else:
            print("❌ Incorrect PIN. Try again.")
    else:
        print("\n🚫 Too many wrong attempts. Card blocked.")
        return
    
    # ATM Menu
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"\nYour Current Balance: ₹{balance}")
        
        elif choice == "2":
            amount = float(input("\nEnter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
                print(f"Updated Balance: ₹{balance}")
            else:
                print("Invalid deposit amount.")
        
        elif choice == "3":
            amount = float(input("\nEnter amount to withdraw: ₹"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                print(f"Remaining Balance: ₹{balance}")
            else:
                print("Insufficient balance or invalid amount.")
        
        elif choice == "4":
            print("\nThank you for using our ATM. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run ATM
atm()
