import requests
import datetime

def get_latest_btc_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
    response = requests.get(url)
    data = response.json()
    btc_price = float(data['bpi']['USD']['rate'].replace(',', ''))
    return btc_price

def calculate_profit_loss(btc_price, purchase_date, purchase_amount):

    usd_rate = btc_price


    initial_usd_amount = btc_price * purchase_amount
    current_usd_amount = btc_price * purchase_amount * usd_rate

    print("Profit/Loss calculation:")
    print(f"საწყისი USD: ${initial_usd_amount:.2f}")
    print(f"მიმდინარე USD: ${current_usd_amount:.2f}")
    print(f"მოგება/წაგება: ${current_usd_amount - initial_usd_amount:.2f}")

purchase_year = int(input("შეიყვანეთ შესყიდვის წელი : "))
purchase_month = int(input("შეიყვანეთ შესყიდვის თვე : "))
purchase_day = int(input("შეიყვანეთ შესყიდვის რიცხვი : "))
purchase_amount = float(input("შესყიდული Bitcoin-ის რაოდენობა: "))

purchase_date = datetime.datetime(purchase_year, purchase_month, purchase_day)


btc_price = get_latest_btc_price()

calculate_profit_loss(btc_price, purchase_date, purchase_amount)
