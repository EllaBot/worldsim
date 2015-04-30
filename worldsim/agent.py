from action import Action
import math


class Agent(object):
    """
    An agent takes actions from the action space and applies them to the
    world. Its knowledge comes from the states returned by the world.
    """
    def __init__(self, world, problem):
        self.world = world
        self.problem = problem

    def act(self):
        # learn, assess, act
        state = self.world.getstate()
        action = self.chooseaction()

        self.world.applyaction(action)

    def chooseaction(self):
        return Action(1, 1)