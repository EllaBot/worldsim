from worldsim import WorldSim
import matplotlib.pyplot as plt
import time

class VisualizedWorldSim(WorldSim):

    """Runs provided world simulator, while adding visualization capabilities

        Parameters
        ----------
        worldsim: WorldSim
            The base world simulator to run
    """
    def __init__(self, *args, **kwargs):
        super(VisualizedWorldSim, self).__init__(*args, **kwargs)
        self.x_history = [self.x]
        self.y_history = [self.y]
        plt.axis((0.0, self.width, 0.0, self.height))
        plt.ion()
        plt.show()

    def applyaction(self, action):
        super(VisualizedWorldSim, self).applyaction(action)
        self.x_history.append(self.x)
        self.y_history.append(self.y)

    def reset(self):
        super(VisualizedWorldSim, self).reset()
        self.x_history = [self.x]
        self.y_history = [self.x]

    def plot(self):
        """Plots the x_history and y_history
        """
        plt.plot(self.x_history, self.y_history, color='k')
        plt.draw()
        time.sleep(0.04)
