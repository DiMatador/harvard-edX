def main():
    arithmatic = calculation(input("Expression: "))
    print(arithmatic)

def calculation(n):
    """str > float
    Returns a calculation from user input
    >>>calculation('2 / 3')
    0.66666666666666666
    >>>calculation('2 * 5')
    10.0
    """
    x,y,z = n.split(' ')
    x = float(x)
    z = float(z)
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z
    elif y == '//':
        return x // z

main()