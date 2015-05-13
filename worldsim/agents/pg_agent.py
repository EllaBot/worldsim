from .agent import Agent
from .state import State
from .action import Action
import numpy as np
from pg_ella.pgpe import PGPE


class PGAgent(Agent):
    def __init__(self, world, task, initialtheta=[0.0, 0.0, 0.0, 0.0, 1.0, 1.0]):
        self.world = world
        self.task = task
        self.optimizer = PGPE(6, epsilon=0.05, alphasigma=0.1, alphatheta=0.2)
        self.optimizer.theta = np.array(initialtheta)
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
            self.terminate()

    def chooseaction(self, state):
        theta = self.theta
        # We would expect a good policy to go forward quickly when
        # omega is low, and go slow and turn when omega is high
        # theta[1] will be negative, theta[3] will be high
        # We would
        linearmean = theta[0] * state.distance + theta[1] * state.omega
        angularmean = theta[2] * state.distance + theta[3] * state.omega

        linear_velocity = np.random.normal(linearmean, abs(theta[4]), 1)[0]
        angular_velocity = np.random.normal(angularmean, abs(theta[5]), 1)[0]

        linear_velocity = max(min(1.5, linear_velocity), -1.5)
        angular_velocity = max(min(1.5, angular_velocity), -1.5)
        return Action(linear_velocity, angular_velocity)

    def getstate(self):
        """Build the agent's representation of the state.
        """
        return State.frompoints(self.world.x, self.world.y, self.world.theta,
                                self.task.target_x, self.task.target_y)

    def terminate(self):
        self.logepisode()
        self.currenttheta += 1
        if self.currenttheta == 2:
            self.optimizer.learn(self.prevtotalreward, self.totalreward)
            self.perturbedthetas = self.optimizer.getperturbedthetas()
            self.currenttheta = 0
        self.prevtotalreward = self.totalreward
        self.totalreward = 0
        self.theta = self.perturbedthetas[self.currenttheta]

    def logepisode(self):
        print "Episode reward: " + str(self.totalreward)
        print "Used theta: " + str(self.theta)
        print "Theta std devs: " + str(self.optimizer.sigmalist[0])