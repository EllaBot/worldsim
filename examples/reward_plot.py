import matplotlib.pyplot as plt


class RewardPlot():

    def __init__(self):

        plt.figure("Reward Plot")
        plt.grid()
        #plt.yscale('symlog')
        plt.xlabel('Episodes')
        plt.ylabel('Total reward')
        plt.title('Agent learning')
        plt.ion()
        plt.show()

        self.lastreward = None
        self.episode_number = 0

    def plot(self, reward):
        fig = plt.figure("Reward Plot")
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
        plt.figure("Reward Plot")
        plt.clf()

    def freeze_plot(self):
        plt.ioff()
        plt.show()