"""
Playback Speed

In a file called playback.py, implement a program in Python that prompts the
user for input and then outputs that same input, replacing each space with ...
(i.e., three periods).
"""


# Function to replace space with '...'
def replaceSpace(input):
    return input.replace(' ', '...')


if __name__ == "__main__":
    print(replaceSpace(input()))