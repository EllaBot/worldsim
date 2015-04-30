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

    def act(self):
        # learn, assess, act
        state = self.world.getstate()
        action = self.chooseaction()

        self.world.applyaction(action)

    def chooseaction(self):
        return Action(10 * (random() - 0.5), 10 * (random() - 0.5))

    def getstate(self):
        x_diff = self.world.x - self.task.target_x
        y_diff = self.world.y - self.task.target_y

        distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
        omega = math.atan2(y_diff, x_diff)
        return State(distance, omega)
