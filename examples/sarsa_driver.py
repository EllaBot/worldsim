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
    world = WorldSim(10.0, 10.0, 0, 0, task)
    agent = SarsaAgent(world, task)
    world.agent = agent

    tasksolved = False

    episode_rewards = []
    actions_taken = 0
    time1 = time.time()
    for i in xrange(0, EPISODES):
        while tasksolved is False:
            agent.act()
            agent_state = agent.getstate()
            tasksolved = world.task.stateisfinal(agent_state)
            actions_taken += 1
        print("Sarsa agent took " + str(actions_taken) + " steps to reach the goal.")
        episode_rewards.append(agent.episode_reward)
        agent.episode_reward = 0
        tasksolved = False
        actions_taken = 0
        world.reset()
        # Hold the distance at 10, hold the omega at 0
        # plot the x as the linear velocity, y as the angular velocity
        learner_plotting_utilities.plot_four_feature_value_function(agent.learner, 0, 10, 1, 0)
        learner_plotting_utilities.show()
        plot_utils.plot(episode_rewards)
        plt.show()


    time2 = time.time()
    print 'function took %0.3f m' % ((time2-time1) / 60.0)


if __name__ == '__main__':
    main()
