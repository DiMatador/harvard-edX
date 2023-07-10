def main():
    user = convert("Fraction: ")
    result = gauge(user)
    print(result)


def convert(fraction):
    '''(str) > str
    Convert the x and y to a percentage rounded to the nearest int.
    If x or y is not an integer, raise a ValueError.
    If x is greater than y or y == 0, ignore the input and prompt again.
    '''
    x, y = 0,0
    avg = 0
    while True:
        try:   
            nums = input(fraction)
            distribute = nums.split('/')
            x, y = int(distribute[0]), int(distribute[1])
            avg = (x / y) * 100            
        except ValueError:
            print("Please enter a valid fraction in the format x/y.")
            continue
        except ZeroDivisionError:
            print("The denominator cannot be zero.")
            continue
        if x > y or y == 0:
            print("Please enter a valid fraction in the format x/y.")
            continue

        break
        
    return round(avg)


def gauge(percentage):
    '''x,y are not an integer prompt again....done!x is greater than y or y is 0 prompt again'''
   
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
	main()
