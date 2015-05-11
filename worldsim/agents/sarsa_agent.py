from true_online_td_lambda import TrueOnlineTDLambda
import random
from action import Action
from state import State
from agent import Agent


class SarsaAgent(Agent):
    def __init__(self, world, task):
        """
        :param world: The world the agent is placed in.
        :param task: The task in the world, which defines the reward function.
        """
        self.world = world
        self.task = task
        self.epsilon = 0.05
        self.previousaction = None
        self.previousstate = None
        self.learner = TrueOnlineTDLambda(4, State.RANGES + Action.RANGES, alpha=0.0001)
        super(SarsaAgent, self).__init__(world, task)

    def act(self):
        """Execute one action on the world, possibly terminating the episode.

        """
        state = self.getstate()
        action = self.chooseaction(state)

        self.world.applyaction(action)

        # For the first time step, we won't have received a reward yet.
        # We're just notifying the learner of our starting state and action.
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
            # Reset episode related information
            self.previousaction = None
            self.previousstate = None

    def chooseaction(self, state):
        """Given a state, pick an action according to an epsilon-greedy policy.

        :param state: The state from which to act.
        :return:
        """
        if random.random() < self.epsilon:

            linear_action = random.uniform(Action.RANGES[0][0], Action.RANGES[0][1])
            angular_action = random.uniform(Action.RANGES[1][0], Action.RANGES[1][1])
            return Action(linear_action,angular_action)

        optimal_params = self.learner.maximize_value([state.distance, state.omega])
        return Action(optimal_params[0], optimal_params[1])

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