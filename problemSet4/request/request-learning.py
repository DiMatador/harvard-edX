import requests
import sys

"""
	(number) -> float
	Return the sys.argv[1](amount) * (Bitcoin_rate) the current price of Bitcoin in dollars to four decimal places
	>>> bitcoin.py
	"Missing command-line argument"
	>>> bitcoin.py nn
	"Comman-line argument is not a number"
	>>> bitcoin.py 2
	$33,186.6172
	>>> bitcoin.py 1
	$16,589.4813
"""

if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
    except:
        print("Comman-line argument is not a number")
        sys.exit(1)
        
else:
    print("Missing command-line argument")
    sys.exit(1)
    
    
    
try:
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bpi = res.json()
    bitcoin_rate = bpi["bpi"]["USD"]["rate_float"] # float value of bitcoin price
    total = bitcoin_rate * amount
    
except requests.RequestException:
    pass

# cost of n Bitcoin in USD to four decimal places
print(F"${total:,.4f}")