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
    def __init__(self, width, height,  initial_x=None, initial_y=None, task=SearchTask(5.0, 5.0), randomizeposition=False):
        self.width = width
        self.height = height
        self.task = task

        self.x = initial_x
        self.y = initial_y
        self.theta = 0.0

        self._default_x = initial_x
        self._default_y = initial_y
        self._randomizeposition = randomizeposition

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