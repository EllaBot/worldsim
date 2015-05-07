class VisualizedWorldSim(object):

    """Runs provided world simulator, while adding visualization capabilities

        Parameters
        ----------
        worldsim: WorldSim
            The base world simulator to run
    """
    def __init__(worldsim):
        self.worldsim = worldsim
        self.x_history = [worldsim.x]
        self.y_history = [worldsim.y]

    def applyaction(self, action):
        self.worldsim.applyaction(action)
        self.x_history.append(worldsim.x)
        self.y_history.append(worldsim.y)

    def reset(self):
        worldsim.reset()
        self.x_history = []
        self.y_history = []
