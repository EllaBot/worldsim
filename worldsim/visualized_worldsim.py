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

    def set_target(self, target_x, target_y):
        plt.plot([target_x], [target_y], 'ro')
        plt.draw()

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

        # Only plot what hasn't been plotted
        # So that it doesn't have to plot everything
        # on every plot method call
        x_to_plot = []
        y_to_plot = []
        # Keep the last point in the list since
        # two points are required for a line
        for i in range(len(self.x_history) - 1):
            x_to_plot.append(self.x_history.pop(0))
        x_to_plot.append(self.x_history[0])

        for i in range(len(self.y_history) - 1):
            y_to_plot.append(self.y_history.pop(0))
        y_to_plot.append(self.y_history[0])

        plt.plot(x_to_plot, y_to_plot, color='k')
        plt.draw()

    def freeze_plot(self):
        self.plot()
        plt.ioff()
        plt.show()

    def clear_plot(self):
        plt.clf()
        plt.axis((0.0, self.width, 0.0, self.height))