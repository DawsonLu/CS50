if __name__ == "__main__":
    get_input = input().lower().strip()

    if get_input.startswith("hello"):
        print("$0")

    elif get_input.startswith('h'):
        print("$20")

    else:
        print("$100")