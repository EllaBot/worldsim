from .agent import Agent
from .state import State
from .action import Action
import numpy as np
from pg_ella.pgpe import PGPE


class PGAgent(Agent):
    def __init__(self, world, task):
        self.world = world
        self.task = task
        self.optimizer = PGPE(4)
        self.optimizer.theta = np.array([0.01, 0.01, 0.01, 0.01])
        self.currenttheta = -1
        self.perturbedthetas = self.optimizer.getperturbedthetas()
        self.theta = self.perturbedthetas[0]
        self.prevtotalreward = 0
        self.totalreward = 0
        super(PGAgent, self).__init__(world, task)

    def act(self):
        state = self.getstate()
        action = self.chooseaction(state)
        self.world.applyaction(action)

        state_prime = self.getstate()
        reward = self.task.reward(state, action, state_prime)
        self.totalreward += reward
        if self.task.stateisfinal(state_prime):

            self.currenttheta += 1
            if self.currenttheta == 2:
                self.optimizer.learn(self.prevtotalreward, self.totalreward)
                self.perturbedthetas = self.optimizer.getperturbedthetas()
                self.currenttheta = 0
                self.prevtotalreward = 0
                self.totalreward = 0
            self.prevtotalreward = self.totalreward
            self.totalreward = 0
            self.theta = self.perturbedthetas[self.currenttheta]

    def chooseaction(self, state):
        theta = self.theta
        mean1 = theta[0] * state.distance + theta[1] * state.omega
        mean2 = theta[2] * state.distance + theta[3] * state.omega
        STD_DEV = 1.0
        linear_velocity = np.random.normal(mean1, STD_DEV, 1)[0]
        angular_velocity = np.random.normal(mean2, STD_DEV, 1)[0]

        linear_velocity = max(min(1.5, linear_velocity), -1.5)
        angular_velocity = max(min(1.5, angular_velocity), -1.5)
        return Action(linear_velocity, angular_velocity)

    def getstate(self):
        """Build the agent's representation of the state.
        """
        return State.frompoints(self.world.x, self.world.y, self.world.theta,
                                self.task.target_x, self.task.target_y)

    def terminateearly(self):
        self.currenttheta += 1
        if self.currenttheta == 2:
            self.optimizer.learn(self.prevtotalreward, self.totalreward)
            self.perturbedthetas = self.optimizer.getperturbedthetas()
            self.currenttheta = 0
            self.prevtotalreward = 0
            self.totalreward = 0
        self.prevtotalreward = self.totalreward
        self.totalreward = 0
        self.theta = self.perturbedthetas[self.currenttheta]