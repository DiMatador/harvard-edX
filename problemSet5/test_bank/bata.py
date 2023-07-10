def main():
    user_input = input("Greetings: ").lower()
    print(F"${value(user_input)}")
    
def value(greeting):
    greetin = greeting.strip()
    # starts with hello
    if 'hello' in greeting:
        return 0
    # start with 'h' but not hello
    elif greeting.startswith('h') and 'hello' not in greeting:
        return 20
    else:
        return 100
    return greeting
    
    
if __name__ == "__main__":
    main()