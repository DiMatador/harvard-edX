from num2words import num2words

'''
Returns a number in letter form
>>> 653
Six Hundred Fifty Three
'''
num = int(input("Enter a number: "))
word_number = num2words(num)
print(word_number)


