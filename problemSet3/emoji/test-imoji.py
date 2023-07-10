
from emoji import emojize

# main function
def main():
    emojii = find_emo("Input: ")
    return emojii

 # logical function
def find_emo(prompt):
    ''' (str) -> emoji
    Returns the prompt veriable as an emoji
    >>> :thumbs_up:
    👍
    >>> :1st_place_medal:
    🥇
    '''
    emo = input(prompt)
    print(emojize(F"{emo}", language='alias'))

main()
