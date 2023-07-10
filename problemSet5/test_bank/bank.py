import sys

def main():
    user_input = input("Greetings: ").lower()
    print(F"${value(user_input)}")
    

def value(greeting):
    greeting =  greeting.rstrip()
    if 'hello' in greeting:
        return 0
    elif greeting.startswith('h') and 'hello' not in greeting:
        return 20
    else:
        return 100
        
        
if __name__ == "__main__":
    main()