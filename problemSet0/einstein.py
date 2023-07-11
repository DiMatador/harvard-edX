def calc_mass():
    """ int > int
    Return the amount of energy generates by mass
    no error checking only ints are allowed
    >>>calc_mass(3)
    270000000000000000
    >>>calc_mass(2)
    180000000000000000
    """
    mass = int(input("Enter a value for mass: "))
    e = mass * 300000000**2
    print(e)
    
calc_mass()