import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price")

    try:
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except (KeyError, ValueError):
        sys.exit("Error: Unable to parse Bitcoin price")

    total_cost = num_bitcoins * price_per_bitcoin
    print(f"Total cost: ${total_cost:,.2f}")

if __name__ == "__main__":
    main()