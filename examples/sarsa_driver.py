import sys
import numpy as np
from worldsim import VisualizedWorldSim
from worldsim.agents import SarsaAgent
from worldsim.tasks import SearchTask
from worldsim.experiments.reward_plot import RewardPlot
from true_online_td_lambda import learner_plotting_utilities


EPISODES = 100


def main():
    task = SearchTask(None, None, max_x=10.0, max_y=10.0)
    world = VisualizedWorldSim(10.0, 10.0, 8.0, 5.0, task)
    agent = SarsaAgent(world, task)
    world.agent = agent

    if len(sys.argv) > 1 and sys.argv[1] == '--load':
        theta = np.load('weights_file.npy')
        agent.learner.theta = theta

    learner_plotting_utilities.begin()
    graph = RewardPlot()

    for i in xrange(0, EPISODES):
        task = SearchTask(None, None, max_x=10.0, max_y=10.0)
        world.task = task
        agent.task = task
        reward, steps = executeepisode(world, agent)
        graph.plot(reward)

    np.save('weights_file', agent.learner.theta)
    graph.freeze()


def executeepisode(world, agent):
    steps = 0
    tasksolved = False
    world.set_target(agent.task.target_x, agent.task.target_y)
    while tasksolved is False:
        agent.act()
        agent_state = agent.getstate()
        # learner_plotting_utilities.plot_four_feature_value_function(agent.learner, 0, agent_state.distance, 1, agent_state.omega)
        steps += 1
        tasksolved = world.task.stateisfinal(agent_state)
        if steps % 200 is 0:
            world.plot()
            pass

    world.plot()
    reward = agent.episode_reward
    agent.logepisode()
    agent.episode_reward = 0
    world.reset()
    return reward, steps


if __name__ == '__main__':
    main()
