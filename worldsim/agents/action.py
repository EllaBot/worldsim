class Action(object):
    def __init__(self, linear_velocity, angular_velocity):
        self.linear_velocity = linear_velocity
        self.angular_velocity = angular_velocity

    def __str__(self):
        return str(self.linear_velocity) + " " + str(self.angular_velocity)