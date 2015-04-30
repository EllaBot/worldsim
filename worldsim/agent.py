class Agent(object):
    def __init__(self, initial_x = 0, initial_y = 0):
        self.angular_velocity = 0
        self.linear_velocity = 0
        self.theta = 0
        self.x = initial_x
        self.y = initial_y