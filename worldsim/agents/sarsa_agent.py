from true_online_td_lambda import TrueOnlineTDLambda
import math
import random
from action import Action
from state import State
from agent import Agent


class SarsaAgent(Agent):
    """
    An agent takes actions from the action space and applies them to the
    world. Its knowledge comes from the states returned by the world.
    """
    def __init__(self, world, task):
        self.world = world
        self.task = task
        self.epsilon = 0.1
        self.previousaction = None
        self.previousstate = None
        state_ranges = [(0, math.sqrt(2) * 10), (0, math.pi * 2.0)]
        self.learner = TrueOnlineTDLambda(4, state_ranges + Action.RANGES)
        super(SarsaAgent, self).__init__(world, task)

    def act(self):

        state = self.getstate()
        action = self.chooseaction(state)

        self.world.applyaction(action)

        # For the first time step, we won't have received a reward yet. We're just notifying the
        # learner of our starting state and action.
        if self.previousstate is None and self.previousaction is None:
            self.learner.start(self._compose(state, action))
        else:
            # Learn like normal
            self._learn(state, action)

        self.previousaction = action
        self.previousstate = state

        post_action_state = self.getstate()
        if self.task.stateisfinal(post_action_state):
            reward = self.task.reward(self.previousstate, self.previousaction, post_action_state)
            self.learner.end(reward)
            self.episode_reward += reward
            self._reset()

    def chooseaction(self, state):
        if random.random() < self.epsilon:

            linear_action = random.uniform(Action.RANGES[0][0], Action.RANGES[0][1])
            angular_action = random.uniform(Action.RANGES[1][0], Action.RANGES[1][1])
            return Action(linear_action,angular_action)

        optimal_params = self.learner.maximize_value([state.distance, state.omega])
        return Action(optimal_params[0], optimal_params[1])

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

    def _compose(self, state, action):
        return [state.distance, state.omega, action.linear_velocity, action.angular_velocity]

    def _learn(self, state_prime, action_prime):
        state = self.previousstate
        action = self.previousaction
        reward = self.task.reward(state, action, state_prime)

        # The learner is smart; it keeps copies of the previous states and actions.
        # We don't need to pass them in.
        self.learner.step(reward, self._compose(state_prime, action_prime))
        self.episode_reward += reward

    def _reset(self):
        self.previousaction = None
        self.previousstate = None
