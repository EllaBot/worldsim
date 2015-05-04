from action import Action
import math
from random import random
from state import State


class Agent(object):
    """
    An agent takes actions from the action space and applies them to the
    world. Its knowledge comes from the states returned by the world.
    """
    def __init__(self, world, task):
        self.world = world
        self.task = task
        self.episode_reward = 0

    def act(self):
        pass

    def chooseaction(self, state):
        pass


def doubleunitrandom():
    return 2.0 * (random() - 0.5)