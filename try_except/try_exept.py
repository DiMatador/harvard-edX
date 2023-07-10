# buid a script that ask for a number, try to catch any wrong entries

#=== use a while loop ===

def get_int():
    while True:
        try:
            num = int(input("What's the value of X? "))
        except ValueError:
            print("X: Not an integer")
        else:
            break
    print(f"Value of X {num}")



# call number
get_int()
