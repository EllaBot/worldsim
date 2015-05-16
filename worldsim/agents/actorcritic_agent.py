from true_online_td_lambda import TrueOnlineTDLambda
from true_online_td_lambda.basis import FourierBasis
import random
import math
import numpy as np
from action import Action
from state import State
from agent import Agent


class ActorCriticAgent(Agent):
    def __init__(self, world, task):
        """
        :param world: The world the agent is placed in.
        :param task: The task in the world, which defines the reward function.
        """
        self.world = world
        self.task = task
        self.action = None
        self.state = None
        self.variance = 10.0
        self.critic_basis = FourierBasis(State.RANGES + Action.RANGES, 4, 3)
        self.actor_basis = FourierBasis(State.RANGES, 2, 3)
        self.e = np.zeros(self.critic_basis.get_num_basis_functions())
        self.w = np.zeros(self.critic_basis.get_num_basis_functions())
        self.theta1 = np.zeros(self.actor_basis.get_num_basis_functions())
        self.theta2 = np.zeros(self.actor_basis.get_num_basis_functions())
        self.episode_reward = 0.0
        self.episode_count = 0.0
        self.begin()
        super(ActorCriticAgent, self).__init__(world, task)

    def begin(self):
        self.state = self.getstate()
        self.action = self.chooseaction(self.state)
        state_action = [self.state.distance, self.state.omega, self.action.linear_velocity, self.action.angular_velocity]
        self.vs = np.dot(self.w, self.critic_basis.compute_features(state_action))

    def act(self, maximize=None):
        """Execute one action on the world, possibly terminating the episode.

        """
        self.world.applyaction(self.action)
        stateprime = self.getstate()
        actionprime = self.chooseaction(stateprime)
        r = self.task.reward(self.state, self.action, stateprime)
        self.episode_reward += r

        statelist = [self.state.distance, self.state.omega]
        stateaction = [self.state.distance, self.state.omega, self.action.linear_velocity, self.action.angular_velocity]
        stateactionprime = [stateprime.distance, stateprime.omega, actionprime.linear_velocity, actionprime.angular_velocity]
        vs_prime = np.dot(self.w, self.critic_basis.compute_features(stateactionprime))

        phi_sa = self.critic_basis.compute_features(stateaction)
        Q_w = np.dot(phi_sa, self.w)

        phi_s = self.actor_basis.compute_features(statelist)
        mean1 = np.dot(self.theta1, phi_s)
        mean2 = np.dot(self.theta2, phi_s)
        pigrad1 = ((self.action.linear_velocity - mean1) * phi_s) / self.variance
        pigrad2 = ((self.action.angular_velocity - mean2) * phi_s) / self.variance

        delta = 0.0
        if self.task.stateisfinal(stateprime):
            delta = r - self.vs
        else:
            delta = r + 0.99 * vs_prime - self.vs

        self.theta1 = self.theta1 + 0.00000003 * pigrad1 * Q_w
        self.theta2 = self.theta2 + 0.00000003 * pigrad2 * Q_w
        self.e = 0.99 * 0.9 * self.e + 0.0001 * (1 - 0.99 * 0.9 * np.dot(self.e, phi_sa)) * phi_sa
        self.w = self.w + delta * self.e + 0.0001 * (self.vs - np.dot(self.w, phi_sa)) * phi_sa

        if self.task.stateisfinal(stateprime):
            self.e = np.zeros(self.critic_basis.get_num_basis_functions())
            self.episode_count += 1.0
            if self.episode_count >= 200:
                self.variance = 10.0 / (1.0 + math.sqrt((self.episode_count - 200.0) + 1.0))

        self.vs = vs_prime
        self.action = actionprime
        self.state = stateprime

    def chooseaction(self, state):
        """Given a state, pick an action according to an epsilon-greedy policy.

        :param state: The state from which to act.
        :return:
        """
        statelist = [state.distance, state.omega]
        phi_s = self.actor_basis.compute_features(statelist)
        action1 = math.sqrt(self.variance) * np.random.randn() + np.dot(self.theta1, phi_s)
        action2 = math.sqrt(self.variance) * np.random.randn() + np.dot(self.theta2, phi_s)

        # print(str(action1) + "\t" + str(action2))

        return Action(max(min(Action.RANGES[0][1], action1), Action.RANGES[0][0]), max(min(Action.RANGES[1][1], action2), Action.RANGES[1][0]))

    def getstate(self):
        """Build the agent's representation of the state.
        """
        return State.frompoints(self.world.x, self.world.y, self.world.theta,
                                self.task.target_x, self.task.target_y)

    @staticmethod
    def _compose(state, action):
        """Creates an array representation of the state-action pair.

        :param state: The state to compose
        :param action: The action to compose
        :return:
        """
        return [state.distance, state.omega,
                action.linear_velocity, action.angular_velocity]

    def _learn(self, state_prime, action_prime):
        """Wraps the learning method of TD-lambda.

        :param state_prime:
        :param action_prime:
        """
        state = self.previousstate
        action = self.previousaction
        reward = self.task.reward(state, action, state_prime)

        # We handle terminal rewards separately, so the reward here should
        # always be negative.
        assert reward < 0

        # The learner is smart; it keeps copies of the previous states and
        # actions. We don't need to pass them in.
        self.learner.step(reward, self._compose(state_prime, action_prime))
        self.episode_reward += reward

    def logepisode(self):
        print "Episode reward: " + str(self.episode_reward)
