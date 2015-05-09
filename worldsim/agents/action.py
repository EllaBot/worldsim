import math


class Action(object):
    RANGES = [(-1.5, 1.5), (-1.5, 1.5)]

    def __init__(self, linear_velocity, angular_velocity):
        self.linear_velocity = linear_velocity
        self.angular_velocity = angular_velocity

    def __str__(self):
        return "Linear velocity: " + str(self.linear_velocity) + " Angular velocity: " + str(self.angular_velocity)