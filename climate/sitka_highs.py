import csv # so we can read csv files using csv.reader() function
import matplotlib.pyplot as plt
from datetime import datetime

with open('data/sitka_weather_2018_simple.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    # for index, text in enumerate(header):
    #     print(index, text)

    highs, dates = [], []
    for row in reader:
        highs.append(int(row[5]))
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
    
    # print(highs, dates)

plt.style.use('seaborn')
fig, ax = plt.subplots() # remember it's subplotS not subplot...

ax.plot(dates, highs, c='red')

ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate() # this draws the date labels diagonally

ax.set_ylabel('Temperature (F)', fontsize=12)

ax.set_title('Sitka - Highest Temperature of the day (2018)', fontsize=20)

plt.show()