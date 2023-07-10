""" module to remove all vawols from a word """

def main():
    result = input("Imput: ")
    print(shorten(result))
    

def shorten(word):
    """ str > str minus any vowols or numbers
    >>>shorten("twitter")
    twttr
    >>>shorten("Julio")
    Jl
    Returns a word after it removes all vowels from a word
    """
    for vowels in word:
        if vowels.lower() in ['a', 'e', 'i', 'o', 'u']:
            word = word.replace(vowels, '')
    return word
    
if __name__ == "__main__":
    main()