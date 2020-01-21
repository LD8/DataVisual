import csv # so we can read csv files using csv.reader() function
import matplotlib.pyplot as plt
from datetime import datetime

with open('data/death_valley_2018_simple.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    # for index, text in enumerate(header):
    #     print(index, text)

    highs, lows, dates = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            highs.append(int(row[4]))
            lows.append(int(row[5]))
            dates.append(date)
        except ValueError:
            print('Something wrong with the data on {}'.format(date))
        
    
    # print(highs, dates)

plt.style.use('seaborn')
fig, ax = plt.subplots() # remember it's subplotS not subplot...

ax.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
ax.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='cyan', alpha=0.1)

ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate() # this draws the date labels diagonally

ax.set_ylabel('Temperature (F)', fontsize=12)

ax.set_title('Daily High and Low Temperatures\nDeath Valley - 2018', fontsize=20)

plt.show()