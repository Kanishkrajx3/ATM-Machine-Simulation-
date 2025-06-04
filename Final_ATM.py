import datetime

class ATM:
    def __init__(self, pin, balance=0.0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, max_attempts=3):
        """Verify PIN with limited attempts."""
        attempts = 0
        while attempts < max_attempts:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                print("Incorrect PIN.")
                attempts += 1
        print("Too many incorrect attempts. Exiting...")
        return False

    def show_menu(self):
        """Display the ATM options menu."""
        print("\n--- ATM MENU ---")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

    def balance_inquiry(self):
        """Display current account balance."""
        print(f"Your current balance is: ₹{self.balance:.2f}")
        self.add_transaction("Balance Inquiry", 0)

    def withdraw_cash(self):
        """Withdraw cash from the account after validation."""
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
                self.add_transaction("Withdrawal", -amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def deposit_cash(self):
        """Deposit cash into the account."""
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                self.balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
                self.add_transaction("Deposit", amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def change_pin(self):
        """Allow user to securely change their PIN."""
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter new 4-digit PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if (len(new_pin) == 4 and new_pin.isdigit()) and (new_pin == confirm_pin):
                self.pin = new_pin
                print("PIN changed successfully.")
                self.add_transaction("PIN Change", 0)
            else:
                print("PIN mismatch or invalid format. Must be 4 digits.")
        else:
            print("Incorrect current PIN.")

    def show_transaction_history(self):
        """Display a list of all recorded transactions."""
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for entry in self.transaction_history:
                print(entry)

    def add_transaction(self, transaction_type, amount):
        """Record a transaction with timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {transaction_type:<15} | ₹{amount:>8.2f}"
        self.transaction_history.append(entry)

def run_atm():
    atm = ATM(pin="1234", balance=10000.0)  # Initialize ATM with default PIN and balance

    print("Welcome to the ATM Machine Simulation!")

    if not atm.check_pin():
        return

    while True:
        atm.show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            atm.balance_inquiry()
        elif choice == '2':
            atm.withdraw_cash()
        elif choice == '3':
            atm.deposit_cash()
        elif choice == '4':
            atm.change_pin()
        elif choice == '5':
            atm.show_transaction_history()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_atm()
