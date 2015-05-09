import matplotlib.pyplot as plt


def plot(episode_rewards):
    fig = plt.gcf()

    x = [x for x in range(0, len(episode_rewards))]
    y = episode_rewards
    ax = fig.gca()
    ax.plot(x, y, 'r')

    ax.set_xlabel('Episodes')
    ax.set_ylabel('Total reward')
    plt.grid()
    plt.draw()


def begin():
    plt.ion()
    plt.show()
    plt.figure()


def clear():
    plt.clf()