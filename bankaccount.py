from account import BankAccount
from saving_account import SavingAccount
from overdraft_account import OverdraftAccount
def check_private_access(account):
    try:
        print(account.__balance)
        raise RuntimeError(f"[FAIL] Direct access to {account.owner}'s __balance should not be allowed.")
    except AttributeError:
        print(f"[OK] Direct access to {account.owner}'s __balance is blocked (as expected).")
    #Try name mangling-based access

def main():
    accounts = [
        BankAccount("BaseUser", 100),
        SavingAccount("Saver", 200, min_balance=50),
        OverdraftAccount("OvdUser", 50, overdraft_limit=75)
    ]
# Attempt to directly access private attribute to verify encapsulation
    for acc in accounts:
        check_private_access(acc)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balances")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            for i, acc in enumerate(accounts, 1):
                print(f"{i}. {acc.owner}")
            idx = int(input("Select account number: ")) - 1
            amount = float(input("Amount to deposit: "))
            try:
                accounts[idx].deposit(amount)
                print(f"Deposited {amount} to {accounts[idx].owner}. New balance: {accounts[idx].getBalance()}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            for i, acc in enumerate(accounts, 1):
                print(f"{i}. {acc.owner}")
            idx = int(input("Select account number: ")) - 1
            amount = float(input("Amount to withdraw: "))
            try:
                accounts[idx].withdraw(amount)
                print(f"Withdrew {amount} from {accounts[idx].owner}. New balance: {accounts[idx].getBalance()}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            for acc in accounts:
                print(repr(acc))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select 1-4.")
if __name__ == "__main__":
    main()