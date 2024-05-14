"""
Just setting up my twttr

When texting or tweeting, it's not uncommon to shorten words to save time or
space, as by omitting vowels, much like Twitter was originally called twttr. In
a file called twttr.py, implement a program that prompts the user for a str of
text and then outputs that same text but with all vowels (A, E, I, O, and U)
omitted, whether inputted in uppercase or lowercase.
"""

if __name__ == "__main__":
    get_input = input("Input: ").strip()
    res = []
    
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    for c in get_input:
        if c not in vowels:
            res.append(c)
            
    print("Output: ", ''.join(res))