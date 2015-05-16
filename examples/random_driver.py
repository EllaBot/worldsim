from worldsim import WorldSim
from worldsim.agents import RandomAgent
from worldsim.tasks import SearchTask
from worldsim.experiments import reward_plot

EPISODES = 100


def main():
    task = SearchTask(5.0, 5.0)
    world = WorldSim(10.0, 10.0, 0, 0, task)
    agent = RandomAgent(world, task)
    world.agent = agent

    tasksolved = False

    episode_rewards = []
    actions_taken = 0
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

    import matplotlib.pyplot as plt
    reward_plot.plot(episode_rewards)
    plt.show()

if __name__ == '__main__':
    main()
