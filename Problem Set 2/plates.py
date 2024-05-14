"""
Vanity Plates

it's possible to request a vanity license plate for your car, with your choice
of letters and numbers instead of random ones. Among the requirements, though,
are:

“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and
a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be
acceptable. The first number used cannot be a '0'.”

“No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and
then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user's input will be uppercase. Structure your
program per the below, wherein is_valid returns True if s meets all
requirements and False if it does not. Assume that s will be a str. You're
welcome to implement additional functions for is_valid to call (e.g., one
function per requirement).
"""

def checkPlate(plate):
    n = len(plate)
    
    if not plate.isalnum():
        print("Invalid")
        return
        
    if n < 2 or n > 6:
        print("Invalid")
        return
        
    for i in range(2):
        if not plate[i].isalpha():
            print("invalid")
            return
    
    num_seen = False
    
    for i in range(2, n):
        if num_seen and plate[i].isalpha():
            print("Invalid")
            return
        
        if plate[i].isnumeric():
            if not num_seen and plate[i] == '0':
                print("Invalid")
                return
            
            num_seen = True

    print("Valid")


if __name__ == "__main__":
    plate = input("Plate: ").strip()
    checkPlate(plate)