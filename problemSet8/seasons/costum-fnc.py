def convert_to_words(num):
	'''
	>>> convert_to_words(50)
	ifty
	'''
    if num == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    num_string = ""
    while num > 0:
        if num < 10:
            num_string += ones[num]
            num = 0
        elif num >= 10 and num < 20:
            num_string += teens[num % 10]
            num = 0
        elif num < 100:
            num_string += tens[num // 10]
            if num % 10 != 0:
                num_string += "-" + ones[num % 10]
                num = 0
        else:  # num < 1000:
            num_string += ones[num // 100] + " hundred "
            num %= 100
        return num_string


    num = int(input("Enter any number less than 1000 : "))

    print(num, " : ", convert_to_words(num))


