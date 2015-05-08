from true_online_td_lambda import TrueOnlineTDLambda
import math
import random
from action import Action
from state import State
from agent import Agent
import numpy as np

class SarsaAgent(Agent):
    """
    An agent takes actions from the action space and applies them to the
    world. Its knowledge comes from the states returned by the world.
    """
    def __init__(self, world, task):
        self.world = world
        self.task = task
        self.epsilon = 0.05
        self.previousaction = None
        self.previousstate = None
        self.learner = TrueOnlineTDLambda(4, State.RANGES + Action.RANGES)
        super(SarsaAgent, self).__init__(world, task)

    def act(self):

        state = self.getstate()
        action = self.chooseaction(state)
        value_guess = self.learner.value(self._compose(state, action))

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

        # optimal_params = self.learner.maximize_value([state.distance, state.omega])

        return self._brute_force_search(state)

    def getstate(self):
        x1 = self.world.x
        y1 = self.world.y
        x2 = self.task.target_x
        y2 = self.task.target_y

        x_diff = x2 - x1
        y_diff = y2 - y1
        distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))

        if x_diff < 0 and y_diff > 0:
            omega = math.atan(y_diff / x_diff) + math.pi
        elif x_diff < 0 and y_diff < 0:
            omega = math.atan(y_diff / x_diff) + math.pi
        elif x_diff > 0 and y_diff < 0:
            omega = math.atan(y_diff/x_diff) + 2.0 * math.pi
        elif x_diff > 0 and y_diff > 0:
           omega = math.atan(y_diff/x_diff)
        elif x_diff == 0 and y_diff == 0:
            omega = 0
        elif x_diff == 0 and y_diff > 0:
            omega = math.pi / 2.0
        elif x_diff == 0 and y_diff < 0:
            omega = 3.0 * math.pi / 2.0
        elif x_diff > 0 and y_diff == 0:
            # could be 2pi
            omega = 0
        elif x_diff < 0 and y_diff == 0:
            omega = math.pi

        if omega > self.world.theta:
            omega -= self.world.theta
        else:
            omega = self.world.theta - omega

        assert omega >= 0

        return State(distance, omega)

    def _compose(self, state, action):
        return [state.distance, state.omega, action.linear_velocity, action.angular_velocity]

    def _learn(self, state_prime, action_prime):
        state = self.previousstate
        action = self.previousaction
        reward = self.task.reward(state, action, state_prime)
        assert reward < 0
        # print("Prev state: " + str(state))
        # print("Prev action: " + str(action))
        # print("Next state: " + str(state_prime))
        # print "reward received:" + str(reward)
        # print "----"

        # The learner is smart; it keeps copies of the previous states and actions.
        # We don't need to pass them in.
        self.learner.step(reward, self._compose(state_prime, action_prime))
        self.episode_reward += reward

    def _reset(self):
        self.previousaction = None
        self.previousstate = None

    def _brute_force_search(self, state):
        max_value = np.finfo(np.float64).min
        max_l = 0
        max_a = 0
        l = Action.RANGES[0][0]
        a = Action.RANGES[1][0]
        while a < Action.RANGES[0][1]:
            while l < Action.RANGES[1][1]:
                value = self.learner.value(self._compose(state, Action(l,a)))
                if value > max_value:
                    max_l = l
                    max_a = a
                    max_value = value
                l += 0.05
            l = Action.RANGES[0][0]
            a += 0.05
        action = Action(max_l, max_a)
        print Action(max_l, max_a)
        return action
