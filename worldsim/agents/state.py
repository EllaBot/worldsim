class State(object):
    """
    :param distance: the distance to the goal
    :param omega: the counterclockwise angle from the goal
    """
    def __init__(self, distance, omega):
        self.distance = distance
        self.omega = omega

    def __str__(self):
        return "Distance to goal: " + str(self.distance) + " Angle to target: " + str(self.omega)