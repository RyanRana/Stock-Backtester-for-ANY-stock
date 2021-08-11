import matplotlib.pyplot as plt
import requests
import json

def get_average(averages_list):
    """
    Gets the average of some numbers
    """
    total = 0 
    for data_set in averages_list:
        total += float(data_set["close"])
    return total/len(averages_list)

ticker = raw_input("Enter ticker: ").upper()
cash = raw_input("Enter initial investment: ")

data_url = 'https://min-api.cryptocompare.com/data/histominute?fsym=' + ticker + '&tsym=USD&limit=2000&aggregate=1'
response = requests.get(data_url)
try:
    data = response.json()['Data']
except:
    print "Error: Crypto Ticker Does Not Exist"
    quit()
historical_data = data

initial = int(cash)
cash = int(cash)

crypto = 0
x_values = []
y_values = []

for place, data_set in enumerate(historical_data[5:-1]):
  
       five_day_average = get_average([
       historical_data[place-1],
       historical_data[place-2],
       historical_data[place-3],
       historical_data[place-4],
       historical_data[place-5]]
         
       three_day_average = get_average([
       historical_data[place-1],              
       historical_data[place-2], 
       historical_data[place-3]])
         
       if three_day_average > five_day_average:
            cash_used_to_buy = cash/2
            price = float(data_set["close"])
            number_of_crypto_we_just_bought = cash_used_to_buy/price
            crypto += number_of_crypto_we_just_bought
            cash -= cash_used_to_buy
            print "Just bought: " +    str(number_of_crypto_we_just_bought) + " " + ticker

       
        if crypto > 1 and three_day_average < five_day_average:
            price = float(data_set["close"])
            number_of_crypto_being_sold = crypto/2
            new_cash = number_of_crypto_being_sold * price
            cash += new_cash
            crypto -= number_of_crypto_being_sold
            print "Just sold: " + str(number_of_crypto_being_sold) + " " + ticker
         
        portfolio_value = cash + (crypto * float(data_set["close"]))
        x_values.append(place)
        y_values.append(portfolio_value)
        print "Final portfolio value:" + str(portfolio_value)
        plot_graph(x_values, y_values)
         
        plt.plot(x, y)
        plt.xlabel("Day")
        plt.ylabel("Portfolio Value")
        plt.show()


    
