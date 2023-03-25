import requests
import sys

#Getting input  from the command-line
if len(sys.argv) == 2:
    try:
        input = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

#Getting the current price of bitcoin as a float
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    result = bitcoin * input
    print(f"${result:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)