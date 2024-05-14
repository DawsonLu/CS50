"""
Camel

In a file called camel.py, implement a program that prompts the user for the
name of a variable in camel case and outputs the corresponding name in snake
case. Assume that the user’s input will indeed be in camel case.
"""

if __name__ == "__main__":
    get_input = input("camelCase: ").strip()
    
    if not get_input.isidentifier():
        raise Exception("Invalid input given: not a valid identifier")
    
    char_list = []
    
    for c in get_input:
        if c.isupper():
            char_list.append(f"_{c.lower()}")
        
        else:
            char_list.append(c)
            
    print(''.join(char_list))