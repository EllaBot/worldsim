from worldsim.tasks import SearchTask
from random import random

def run_experiment(agent, world, episodes, maximize=None):
    task = SearchTask(5.0, 5.0)
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

    return episode_rewards


def run_experiment_capped(agent, world, episodes, maxsteps=None):
    task = SearchTask(None, None, max_x=world.width, max_y=world.height)
    agent.task = task
    episode_rewards = []
    for i in range(episodes):
        task = SearchTask(None, None, max_x=world.width, max_y=world.height)
        agent.task = task
        reward, steps = _executeepisode(agent, world, maxsteps)
        episode_rewards.append(reward)

    return episode_rewards


def _executeepisode(agent, world, maxsteps=None):
    tasksolved = False
    steps = 0
    returnreward = None
    while tasksolved is not True:
        agent.act()
        steps += 1
        state_prime = agent.getstate()
        tasksolved = agent.task.stateisfinal(state_prime)
        if maxsteps is not None and steps > maxsteps:
            tasksolved = True
            returnreward = agent.totalreward
            agent.terminate()

    world.reset()

    if returnreward is None:
        returnreward = agent.prevtotalreward
    return returnreward, steps
