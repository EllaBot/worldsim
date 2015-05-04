from action import Action
import math
from state import State
from agent import Agent, doubleunitrandom


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
        linear_start = Action.RANGES[0][0]
        angular_start = Action.RANGES[1][0]
        linear_range = Action.RANGES[0][1] - Action.RANGES[0][0]
        angular_range = Action.RANGES[1][1] - Action.RANGES[1][0]

        linear_action = linear_range * doubleunitrandom() + linear_start
        angular_action = angular_range * doubleunitrandom() + angular_start
        return Action(linear_action, angular_action)

    def getstate(self):
        x_diff = self.world.x - self.task.target_x
        y_diff = self.world.y - self.task.target_y

        distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
        omega = math.atan2(y_diff, x_diff)
        return State(distance, omega)