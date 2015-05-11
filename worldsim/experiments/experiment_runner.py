from worldsim.tasks import SearchTask
from random import random

def run_experiment(agent, world, episodes, maximize=None):
    task = SearchTask(5.0, 5.0)
    world.task = task
    agent.task = task
    episode_rewards = []
    for i in range(episodes):
        tasksolved = False
        # Run an episode
        while tasksolved is False:
            agent.act(maximize=maximize)
            agent_state = agent.getstate()
            tasksolved = world.task.stateisfinal(agent_state)

        # Store the episode reward
        episode_rewards.append(agent.episode_reward)

        # Reset world and task
        agent.episode_reward = 0
        world.reset()
        task.target_x = random() * world.width
        task.target_y = random() * world.height

    return episode_rewards
