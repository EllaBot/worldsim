import math


class Action(object):
    RANGES = [(-10, 10), (0.0, 2.0 * math.pi)]
    def __init__(self, linear_velocity, angular_velocity):
        self.linear_velocity = linear_velocity
        self.angular_velocity = angular_velocity

    def __str__(self):
        return str(self.linear_velocity) + " " + str(self.angular_velocity)