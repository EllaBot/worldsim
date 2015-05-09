from worldsim import WorldSim
from worldsim.agents import SarsaAgent, State
from worldsim.tasks import SearchTask
from true_online_td_lambda import learner_plotting_utilities
import time
import plot_utils
import matplotlib.pyplot as plt

EPISODES = 300


def main():
    task = SearchTask(5.0, 5.0)
    world = WorldSim(10.0, 10.0, 8.0, 5.0, task)
    agent = SarsaAgent(world, task)
    world.agent = agent
    # learner_plotting_utilities.begin()
    plot_utils.begin()
    tasksolved = False

    episode_rewards = []
    for i in xrange(0, EPISODES):
        while tasksolved is False:
            agent.act()
            agent_state = agent.getstate()
            # learner_plotting_utilities.plot_four_feature_value_function(agent.learner, 0, agent_state.distance, 1, agent_state.omega)
            tasksolved = world.task.stateisfinal(agent_state)

        episode_rewards.append(agent.episode_reward)

        plot_utils.plot(episode_rewards)
        agent.episode_reward = 0
        tasksolved = False
        world.reset()
    plot_utils.freeze_plot()


if __name__ == '__main__':
    main()
