from validator_collection import validators, checkers, errors

def main():
    email = valid_email(input("What's your emeil address? "))
    print(email)


def valid_email(s):
    """str -> str
    Returns True if an email is verify as correct or False if is not verify email.
    >>> valid_email('duby@dubycom.com')
    True
    >>> valid_email('beer?#_+@___notemail.crap')
    False
    """

    """Mailbox/User name (letters, numbers, and printable characters)
    “@” sign Domain name. So this would look something like this: your_name@example.com1.
    email_add = ("\b^([a-z]+[0-9]?[^!?$%-])\b@\b([a-z]+[^A-Z!@?$%])\.com$\b")
    """

    try:
        #domain = ''
        # validate the email
        s = validators.email(s)
        
        user, domain = s.split("@")
        # extract the second item in the list
        tld = domain.split('.')[-1]
        print(tld)
        # check for valid tld
        allowed_tlds = ['com', 'edu', 'org']
        if tld not in allowed_tlds:
            return "Invalid"
            
        # check that the '@' appears only once
        # if s.count(char_to_remove) > 1:
            # s = s.replace(char_to_remove, "", s.count(char_to_remove) - 1)
        # use, domain = s.split('@')

        """ check if second item is in the list of allowed TLDs
            if the item does not match return invalid
        """
        # if not validators.email(s):
            # return "Invalid"

        return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
