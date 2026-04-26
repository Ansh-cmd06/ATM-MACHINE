import data

def show_statement():
    if not data.transactions:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for t in data.transactions:
            print(t)