import matplotlib.pyplot as plt


class RewardPlot():

    def __init__(self):
        plt.ion()
        plt.show()
        plt.figure()
        plt.grid()
        fig = plt.gcf()
        ax = fig.gca()
        #ax.set_yscale('symlog')
        ax.set_xlabel('Episodes')
        ax.set_ylabel('Total reward')
        ax.set_title('Agent learning')

        self.lastreward = None
        self.episode_number = 0

    def plot(self, reward):
        fig = plt.gcf()
        x = [self.episode_number, self.episode_number + 1]
        y = [self.lastreward, reward]
        if self.lastreward is None:
            self.lastreward = reward
            self.episode_number += 1
            return

        ax = fig.gca()
        ax.plot(x, y, 'b')
        self.lastreward = reward
        self.episode_number += 1
        plt.draw()

    def clear(self):
        plt.clf()

    def freeze_plot(self):
        plt.ioff()
        plt.show()