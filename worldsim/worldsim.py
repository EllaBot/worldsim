class WorldSim(object):
    """Simulates a world with an agent.

    The agent is controlled by specifiying angular and linear velocities
    at small time intervals.

    The world is represented as an NxM closed rectangle.

    Parameters
    ----------
    width: float
        The width (N) of the world in meters

    height: float
        The height (M) of the world in meters

    initial_x: float, optional
        The initial x position in meters, where the origin is the top left corner

    initial_y: float, optional
        The initial y position in meters, where the origin is the top left corner
    """
    def __init__(self, width, height, initial_x = 0.0, initial_y = 0.0):
        self.width = width
        self.height = height
        self.x = initial_x
        self.y = initial_y
