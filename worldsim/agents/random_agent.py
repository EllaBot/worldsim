from action import Action
import math
from state import State
from agent import Agent
import random
import numpy as np


class RandomAgent(Agent):
    """
    An agent takes actions from the action space and applies them to the
    world. Its knowledge comes from the states returned by the world.
    """
    def __init__(self, world, task):
        self.world = world
        self.task = task
        self.prevstate = None
        super(RandomAgent, self).__init__(world, task)

    def act(self):
        # learn, assess, act
        state = self.getstate()
        action = self.chooseaction(state)
        self.world.applyaction(action)

        if self.prevstate is not None:
            self.episode_reward += self.task.reward(self.prevstate, action, state)

        self.prevstate = state

    def chooseaction(self, state):
        linear_action = random.uniform(Action.RANGES[0][0], Action.RANGES[0][1])
        angular_action = random.uniform(Action.RANGES[1][0], Action.RANGES[1][1])
        return Action(linear_action, angular_action)

    def getstate(self):
        x1 = self.world.x
        y1 = self.world.y
        x2 = self.task.target_x
        y2 = self.task.target_y

        x_diff = x1 - x2
        y_diff = y1 - y2
        distance = math.sqrt(x_diff ** 2 + y_diff ** 2)

        if x_diff < 0:
            omega = math.atan(y_diff / x_diff)
        elif x_diff > 0:
            omega = math.atan(y_diff / x_diff) + math.pi
        else:
            if y2 > y1:
                omega = math.pi / 2.0
            else:
                omega = 3.0 * math.pi / 2.0

        return State(distance, omega)