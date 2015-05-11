from action import Action
import math
from state import State
from agent import Agent
import random


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
        """Pick a random action and learn nothing.


        """
        state = self.getstate()
        action = self.chooseaction(state)
        self.world.applyaction(action)

        if self.prevstate is not None:
            self.episode_reward += self.task.reward(self.prevstate, action, state)

        self.prevstate = state

    def chooseaction(self, state):
        """Choose an action uniformly at random.

        :param state: The state to act from. Not used.
        :return: The random action.
        """
        linear_action = random.uniform(Action.RANGES[0][0], Action.RANGES[0][1])
        angular_action = random.uniform(Action.RANGES[1][0], Action.RANGES[1][1])
        return Action(linear_action, angular_action)

    def getstate(self):
        State.frompoints(self.world.x, self.world.y, self.world.theta,
                         self.task.x, self.task.y)