"""
Grocery List

In a file called grocery.py, implement a program that prompts the user for
items, one per line, until the user inputs control-d (which is a common way of
ending one’s input to a program). Then output the user’s grocery list in all
uppercase, sorted alphabetically by item, prefixing each line with the number
of times the user inputted that item. No need to pluralize the items. Treat the
user’s input case-insensitively.
"""

if __name__ == "__main__":
    grocery_list = {}
        
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        
        if item == "DONE":
            break
                
        try:
            grocery_list[item] += 1
        except KeyError:
            grocery_list[item] = 1
    
    for key, count in grocery_list.items():
        print(count, key)
        