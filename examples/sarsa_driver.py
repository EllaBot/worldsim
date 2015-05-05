from worldsim import WorldSim
from worldsim.agents import SarsaAgent, State
from worldsim.tasks import SearchTask
import time
import plot_utils

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
        # print("Random agent took " + str(actions_taken) + " steps to reach the goal.")
        episode_rewards.append(agent.episode_reward)
        agent.episode_reward = 0
        tasksolved = False
        actions_taken = 0
        world.reset()

    time2 = time.time()
    print 'function took %0.3f m' % ((time2-time1) / 60.0)
    import matplotlib.pyplot as plt
    plot_utils.plot(episode_rewards)
    plt.show()

if __name__ == '__main__':
    main()
