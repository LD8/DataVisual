from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# create 2 dice
die_1 = Die()
die_2 = Die()

# roll dice for some times and store the sum in a list
results = []
for i in range(1000):
    sum = die_1.roll() + die_2.roll()
    results.append(sum)

# analyse the results
frequencies = []
max_num = die_1.sides+die_2.sides
for i in range(2, max_num+1):
    frequency = results.count(i)
    frequencies.append(frequency)

print(frequencies)

# ------------------ visualise the results ------------------ 

# plotly doesn't recognise range() as a list, hence the list() method
x_values = list(range(2, max_num+1))
# create a list of bars, stored in data
data = [Bar(x=x_values, y=frequencies)]

# config x and y axis
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

# create a Layout object, setting the title and utilising the configs above
my_layout = Layout(title='Results of Rolling Two D6 Dice 1000 Times', xaxis=x_axis_config, yaxis=y_axis_config)

# render the {data and layout}, storing the interactive figure as an html file
offline.plot({'data': data, 'layout': my_layout}, filename='d6_dice.html')