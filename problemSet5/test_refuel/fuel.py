def main():
    error_occurred = None
    user = convert("Fraction: ")
    result = gauge(user)
    print(result)

    if error_occurred:
        sys.exit(1)  # Exit with a status code of 1 to indicate an error
def convert(fraction):
    '''(str) > str
    convert the x and y to a percentage rounded to the nearest int,
    if x or y not and interger == ValueError
    x is greater than y, convert
    y == 0 ZeroDivisionError
    '''
    x, y = 0,0
    avg = 0
    while True:
        try:   
            nums = input(fraction)
            distribute = nums.split('/')
            x, y = int(distribute[0]), int(distribute[1])
        except ValueError:
            continue
        try:
            if y == 0 or x > y:
                continue
            else:
                avg = (x / y) * 100           
        except (ZeroDivisionError):
            continue

        break
        
    return round(int(avg))

def gauge(percentage):
    while True:
        try:
            if percentage <= 1:
                return "E"
            if percentage >= 99:
                return "F"
        except ValueError:
            pass

        break

    return f"{percentage}%"

if __name__ == "__main__":
	main()