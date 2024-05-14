"""
Coke Machine

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only
accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a
coin, one at a time, each time informing the user of the amount due. Once the
user has inputted at least 50 cents, output how many cents in change the user
is owed. Assume that the user will only input integers, and ignore any integer
that isn't an accepted denomination.
"""

if __name__ == "__main__":
    amount_due = 50
    
    while amount_due > 0:
        print("Amount Due: ", amount_due)
        get_input = input("Insert Coin: ").strip()
        
        if not get_input.isdigit:
            raise Exception("Invalid input: Not a digit")
        
        if get_input != "5" and get_input != "10" and get_input != "25":
            continue
        
        amount_due -= int(get_input)
        
    print("Change Due: ", abs(amount_due))