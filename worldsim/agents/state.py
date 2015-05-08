import math

class State(object):
    """
    :param distance: the distance to the goal
    :param omega: the counterclockwise angle from the goal
    """
    RANGES = [(0.0, 10.0 * math.sqrt(2.0)), (0.0, math.pi * 2.0)]
    def __init__(self, distance, omega):
        assert State.RANGES[0][0] <= distance < State.RANGES[0][1]
        assert State.RANGES[1][0] <= omega < State.RANGES[1][1]
        self.distance = distance
        self.omega = omega

    def __str__(self):
        return "Distance to goal: " + str(self.distance) + " Angle to target: " + str(self.omega)