import csv
from datetime import datetime
path = '/Users/tech/code/pythonworkshop/google_stock_data.csv'
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
print(header)
data = []
for item in reader:
    #item = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    date = datetime.strptime(item[0], '%m/%d/%Y')
    open_price = float(item[1])
    high = float(item[2])
    low = float(item[3])
    close = float(item[4])
    volume = float(item[5])
    adj_close = float(item[6])
    data.append([date, open_price, high, low, close, volume, adj_close])
print(data[0])

#calculate daily stock return
returns_path = '/Users/tech/code/pythonworkshop/google_returns.csv'
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]
    daily_return = (todays_price - yesterdays_price)/yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%y')
    writer.writerow([formatted_date, daily_return])


    