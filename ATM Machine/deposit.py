import data
data.balance += 500

def deposit():
    amount = float(input("Enter amount to deposit: ₹"))
    
    if amount > 0:
        data.balance += amount
        data.transactions.append(f"Deposited ₹{amount}")
        print("Deposit successful.")
    else:
        print("Invalid amount: ")