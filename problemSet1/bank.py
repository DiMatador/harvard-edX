def main():
    """Returns Greetings"""
    greeting = money(input("Greetings: "))
    print(greeting)
    
def money(n):
    """str > str
    Return $0 if the greeted with a 'Hello', $100 if not greeted with a 'Hello', but kramer agrees to $20
    if the greeting starts with an 'H'
    >>>money("Hello")
    >>>money("How your doing? ")
    "$20"
    >>>money("Hey")
    "$100"
    """
    greet = n.strip(' ').lower()
    if greet == 'Hello'.lower() or greet == 'Hello, Newman'.lower():
        return '$0'
    elif greet == 'How your doing?'.lower():
        return '$20'
    else:
        return '$100'
        
main()