import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# subplots() function can generate one or more plots in the same figure
# fig represents the entire figure
# ax represents a single plot in the figure

ax.plot(squares)

plt.show()
# this function opens Matplotlib's viewer
