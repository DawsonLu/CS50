"""
Nutrition Facts

In a file called nutrition.py, implement a program that prompts consumers users
to input a fruit (case-insensitively) and then outputs the number of calories
in one portion of that fruit, per the FDA's poster for fruits, which is also
available as text. Capitalization aside, assume that users will input fruits
exactly as written in the poster (e.g., strawberries, not strawberry). Ignore 
any input that isn't a fruit.
"""

FDA_GUIDE = {
    "apple": 130,
    "avocado": 50,
    "Banana": 110,
    "blueberries": 80,
    "cantaloupe": 50,
    "cherries": 90,
    "coconut": 140,
    "grapefruit": 60,
    "grapes": 60,
    "kiwi": 50,
    "lemon": 20,
    "lime": 20,
    "mango": 200,
    "orange": 80,
    "papaya": 120,
    "peach": 60,
    "pear": 100,
    "pineapple": 80,
    "plum": 70,
    "pomegranate": 120,
    "raspberries": 60,
    "strawberries": 50,
    "watermelon": 50
}

if __name__ == "__main__":
    get_input = input("Item: ").strip().lower()
    
    if get_input in FDA_GUIDE:
        print("Calories: ", FDA_GUIDE[get_input])
        
    else:
        print("Invalid input: Not a fruit")