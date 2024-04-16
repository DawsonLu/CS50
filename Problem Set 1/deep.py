"""
Deep Thought

In deep.py, implement a program that prompts the user for the answer to the
Great Question of Life, the Universe and Everything, outputting Yes if the user
inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

if __name__ == "__main__":
    get_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

    if get_input == '42' or get_input == 'fourty-two' or get_input == 'fourty two':
        print('Yes')

    else:
        print('No')