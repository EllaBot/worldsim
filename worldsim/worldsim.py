import math
from tasks import SearchTask
from agents import RandomAgent
from agents import State
from random import random


class WorldSim(object):
    TICK_DURATION = 0.10

    """Simulates a world with an agent.

    The agent is controlled by specifying angular and linear velocities
    at small time intervals.

    The world is represented as an NxM closed rectangle.

    Parameters
    ----------
    width: float
        The width (N) of the world in meters

    height: float
        The height (M) of the world in meters

    initial_x: float, optional
        The initial x position in meters, where the origin is the bottom left corner

    initial_y: float, optional
        The initial y position in meters, where the origin is the bottom left corner
    """
    def __init__(self, width, height, default_x=None, default_y=None, randomizeposition=None):
        if randomizeposition is None and (default_x is None and default_y is None):
            randomizeposition = True
        self.width = width
        self.height = height

        self._default_x = default_x
        self._default_y = default_y

        self.x = default_x
        self.y = default_y
        self.theta = 0.0

        self._randomizeposition = randomizeposition
        self.reset()

    def applyaction(self, action):
        """Tick the clock once based on TICK_DURATION
        """
        self.theta = (self.theta + action.angular_velocity * WorldSim.TICK_DURATION) % (math.pi * 2.0)
        self.x += math.sin(self.theta + math.pi / 2.0) * action.linear_velocity * WorldSim.TICK_DURATION
        self.y += -math.cos(self.theta + math.pi / 2.0) * action.linear_velocity * WorldSim.TICK_DURATION

        # Check for boundary overstepping
        self.x = min(max(self.x, 0.0), self.width)
        self.y = min(max(self.y, 0.0), self.height)

    def reset(self):
        if self._randomizeposition:
            self.x = random() * self.width
            self.y = random() * self.height
        else:
            self.x = self._default_x
            self.y = self._default_y
        self.theta = 0.0