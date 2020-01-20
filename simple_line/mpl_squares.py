import matplotlib.pyplot as plt

# generate data
xv = range(5000)
yv = [x**3 for x in xv]

# use a built-in style
plt.style.use('seaborn')

# start to generate the plot
fig, ax = plt.subplots()
# subplots() function can generate one or more plots in the same figure
# fig represents the entire figure
# ax represents a single plot in the figure

# plot a single line graph
# ax.plot(xv, yv, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# render dots (data, data, size, color, color_mapping)
ax.scatter(xv, yv, s=20, c=yv, cmap=plt.cm.Blues)

# set size of tick marks
ax.tick_params(axis='both', labelsize=14)

# set axis range
ax.axis([0,5000, 0, 140000000000])

# save an image and trim the whitespace around, then exit 
plt.savefig('cubes_plot.png', bbox_inches='tight')

# this function opens Matplotlib's viewer, if plt.savefig(), show() won't execute
plt.show()
