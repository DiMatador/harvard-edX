def main():
    meal_cost = dinner_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("Tip percentage: "))
    
    tip = float(meal_cost) * float(percent)
    print(F"Leave ${tip:.2f}")
    
    
def dinner_to_float(d):
    """float > float
    Returns a real number after removing the dollar sign if it was provided
    >>>dinner_to_float("$45")
    45
    >>>dinner_to_float("97")
    97
    """
    dollars = d.strip('$')
    return dollars
    
def percent_to_float(p):
    """int > int
    Returns an int with out the percentage symble if it is provided
    >>>percent_to_float("%13")
    13
    >>>percent_to_float("15")
    15
    """
    tip = p.strip('%')
    return float(tip)/100
    
main()