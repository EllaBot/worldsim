import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def plot(episode_rewards):
    fig = plt.gcf()

    x = [x for x in range(0, len(episode_rewards))]
    y = episode_rewards
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.plot(x, y, 'r')

    axes.set_xlabel('Episodes')
    axes.set_ylabel('Total reward')

    plt.draw()


def begin():
    plt.ion()
    plt.show()
    plt.figure()


def clear():
    plt.clf()