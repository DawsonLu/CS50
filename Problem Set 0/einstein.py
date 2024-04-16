"""
Einstein

In a file called einstein.py, implement a program in Python that prompts the
user for mass as an integer (in kilograms) and then outputs the equivalent
number of Joules as an integer. Assume that the user will input an integer.
"""

if __name__ == "__main__":
    mass = int(input("m: "))
    print(mass * 300000000 ** 2)