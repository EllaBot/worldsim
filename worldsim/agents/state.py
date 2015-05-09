import math


class State(object):

    RANGES = [(0.0, 10.0 * math.sqrt(2.0)), (0.0, math.pi * 2.0)]

    def __init__(self, distance, omega):
        """
        :param distance: the distance to the goal
        :param omega: the counterclockwise angle from the goal
        """
        assert State.RANGES[0][0] <= distance < State.RANGES[0][1]
        assert State.RANGES[1][0] <= omega < State.RANGES[1][1]
        self.distance = distance
        self.omega = omega

    def __str__(self):
        return "Distance to goal: " + str(self.distance) + \
               " Angle to target: " + str(self.omega)

    @staticmethod
    def frompoints(agent_x, agent_y, agent_theta, goal_x, goal_y):
        x1 = agent_x
        y1 = agent_y
        x2 = goal_x
        y2 = goal_y

        x_diff = x2 - x1
        y_diff = y2 - y1
        distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))

        # This calculates the counter clockwise angle between the goal
        # and the agent. This is a little different than straight atan2
        if x_diff < 0 and y_diff is not 0.0:
            omega = math.atan(y_diff / x_diff) + math.pi
        elif x_diff > 0 and y_diff < 0:
            omega = math.atan(y_diff/x_diff) + 2.0 * math.pi
        elif x_diff > 0 and y_diff > 0:
           omega = math.atan(y_diff/x_diff)
        elif x_diff == 0 and y_diff == 0:
            omega = 0
        elif x_diff == 0 and y_diff > 0:
            omega = math.pi / 2.0
        elif x_diff == 0 and y_diff < 0:
            omega = 3.0 * math.pi / 2.0
        elif x_diff > 0 and y_diff == 0:
            # could be 2pi
            omega = 0
        elif x_diff < 0 and y_diff == 0:
            omega = math.pi

        if omega > agent_theta:
            omega -= agent_theta
        else:
            omega = agent_theta - omega

        return State(distance, omega)