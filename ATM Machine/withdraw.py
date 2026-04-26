import data

def withdraw():
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= 0:
        print("Invalid amount.")
    elif amount > data.balance:
        print("Insufficient balance.")
    else:
        data.balance -= amount
        data.transactions.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful.")