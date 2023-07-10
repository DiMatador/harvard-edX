import inflect

"""
Returns a number in letter form
>>> 7
seven
"""

number = int(input("Enter the number : "))
p = inflect.engine()
word = p.number_to_words(number)

# print(number,":",word)
print(word)
