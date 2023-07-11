def main():
    convert()
    
def convert():
    """ str > str with amoji
    Returns a str with a corespondig amoji
    >>> convert("Hello")
    "Hello 🙂"
    >>> convert("Goodbye")
    "Goodbye 🙁"
    """
    user = input("Enter the slight smiling face or slightly frowing face amojies ")
    if user == 'Hello :)':
        print("Hello" + ' 🙂')
    elif user == 'Goodbye :(':
        print("Goodbye" + " 🙁")
    else:
        print("Hello 🙂 goodbye 🙁")
        
main()