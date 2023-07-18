def main():
    """
    Prints the return value from remove_vowels
    """
    no_vowels = remove_vowels()
    print(no_vowels)


def remove_vowels():
    """str > str
    Returns the word with all vowels removed
    >>>remove_vowels()
    word with any vowels removed
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word = input("Input: ")
    # iterate through the word to find vowels
    for letters in word:
        if letters in vowels:
            word = word.replace(letters, '')

    return word


if __name__ == "__main__":
    main()
