import matplotlib.pyplot as plt


def plot(episode_rewards):
    fig = plt.gcf()

    x = [x for x in range(0, len(episode_rewards))]
    y = episode_rewards
    ax = fig.gca()
    ax.plot(x, y, 'b')

    plt.draw()


def begin():
    plt.ion()
    plt.show()
    plt.figure()
    plt.grid()
    fig = plt.gcf()
    ax = fig.gca()
    ax.set_yscale('symlog')
    ax.set_xlabel('Episodes')
    ax.set_ylabel('Total reward')
    ax.set_title('Agent learning')


def clear():
    plt.clf()


def freeze_plot():
    plt.ioff()
    plt.show()