import matplotlib.pyplot as plt
from random_walk import RandomWalk
import time

steps_number = int(input('How many steps: '))

while True:
    # create an object]
    rw = RandomWalk(steps_number)
    # generate the steps within the object
    rw.generate_steps()
    
    # style and print out the figure
    plt.style.use('classic')
    # add figsize argument to set the size
    fig, ax = plt.subplots(figsize=(16,9))
    step_num = range(rw.n_steps)
    ax.scatter(rw.xpos, rw.ypos, s=1, c=step_num, cmap=plt.cm.Blues, edgecolors='none')
    # ax.plot(rw.xpos, rw.ypos, linewidth=1)

    # emphasize the first and last dot
    ax.scatter(rw.xpos[0], rw.ypos[0], s=15, c='green', edgecolors='none')
    ax.scatter(rw.xpos[-1], rw.ypos[-1], s=15, c='red', edgecolors='none')

    title = 'Random Walk Pattern (' + str(steps_number) + ' steps)'
    ax.set_title(title)

    # axes invisible
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    again = input('Generate another walk? (y/n): ')
    if again == 'n':
        break