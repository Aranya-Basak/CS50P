import sys
import requests
import json

try:
    if len(sys.argv) == 2:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json" )
        rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
        amnt = float(sys.argv[1])
        prz = rate * amnt
        print(f"${prz:,.4f}")
    else:
        sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Failed to request")




