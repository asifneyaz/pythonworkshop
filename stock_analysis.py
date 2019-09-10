import csv
from datetime import datetime
path = '/Users/tech/code/pythonworkshop/google_stock_data.csv'
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
print(header) #print header of CSV
data = []
for item in reader:
    #item = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    date = datetime.strptime(item[0], '%m/%d/%Y') #convert string datetime to datetime format
    open_price = float(item[1]) #convert price from string to float
    high = float(item[2]) #convert high from string to float
    low = float(item[3]) # " 
    close = float(item[4])
    volume = float(item[5])
    adj_close_price = float(item[6])
    data.append([date, open_price, high, low, close, volume, adj_close_price])
print(data[0])

#calculate daily stock return
#daily return = (todays price - yesterdays price)/yesterdays price
#write daily returns to a new csv file
returns_csv_path = '/Users/tech/code/pythonworkshop/returns_google_stock.csv'
file = open(returns_csv_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Daily stock Return"]) #write header of csv file
#calculate and write data to csv file
for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0] # first element 
    todays_adj_close_price = todays_row[-1] #last element
    yesterdays_row = data[i + 1] #dates sorted in descending in source csv
    yesterdays_date = yesterdays_row[0]
    yesterdays_adj_close_price = yesterdays_row[-1]
    daily_return = (todays_adj_close_price - yesterdays_adj_close_price)/yesterdays_adj_close_price
    #formate date to strip time and write in m/d/y format
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])


