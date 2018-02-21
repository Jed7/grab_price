from django.shortcuts import render
import requests

# Create your views here.
# Comment
def index(request):
    return render(request,'app_grab/index.html')


# Grab the BTC value
url = "https://api.bitfinex.com/v1/pubticker/btcusd"

response = requests.request("GET", url)

data = response.json()
last_price = float(data.get('last_price'))

# Function for balance value calculation
btc_amount = 1
def calc_bal(amount=btc_amount, value=last_price):
    bal = amount * value
    return bal

# function to insert the btc price and the balance in the html page
def index(request):
    my_dict = {'insert_btc_price': last_price, 'insert_balance': calc_bal() }
    return render(request,'app_grab/index.html', context=my_dict)
