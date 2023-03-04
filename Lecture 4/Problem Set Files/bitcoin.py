import requests
import sys


def main():
    coins = get_buy_quantity()  # get quantity of coins user wants to buy
    data = get_json_data()  # request json data from coindesk api
    rate = extract_rate_float(data)  # extract current bitcoin price rate
    value = coins * rate  # calculate value user wants to buy
    print(f"${value:,.4f}")  # format and display


def get_buy_quantity():
    """Searches through the argv for the quantity of coins a user wants to buy"""
    try:
        return float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_json_data():
    """Returns the json data from coindesk api"""
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Could not get json data")

    return response.json()  # extract json object from response


def extract_rate_float(data):
    """Returns the bitcoin rate as a float value"""
    rate = data['bpi']['USD']['rate']  # find rate value
    rate = rate.replace(",", "")  # remove comma separator
    return float(rate)  # return float type version


if __name__ == "__main__":
    main()
