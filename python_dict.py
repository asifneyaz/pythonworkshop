stocks = {'Apple' : 191.10, 'Shell' : 67.50, 'AMD' : 32.50, 'Starbucks' : 10.00}
print(stocks)
#find minimum of stocks
print(min(stocks)) #prints only min of keys and not values
print(max(stocks)) #prints only max of keys and not values
#invert key value pairs to find min of values using zip
stocks_inverted = zip(stocks.values(), stocks.keys())
print(stocks_inverted)
#sort stocks on the basis of price
sorted_stocks = sorted(stocks_inverted)
print(sorted_stocks)
#find minimum of stock prices
print(min(sorted_stocks)) 
print(max(sorted_stocks))
inverted_dictionary_stocks = dict(sorted_stocks)
print(inverted_dictionary_stocks) #dictionary sorted on the basis of stock_price
