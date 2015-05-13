from random import random
import math

from worldsim import VisualizedWorldSim
from worldsim.agents import PGAgent
from worldsim.tasks import SearchTask
from worldsim.experiments.reward_plot import RewardPlot


EPISODES = 600000
GOODRANDOMPOSITION = [0.575, -0.13, 0.0287, -0.897, -0.3881, 0.02335]


def main():
    task = SearchTask(None, None, max_x=10.0, max_y=10.0)
    world = VisualizedWorldSim(10.0, 10.0, 8.0, 3.0, task)
    agent = PGAgent(world, task, initialtheta=GOODRANDOMPOSITION, epsilon=0.4)
    world.agent = agent
    graph = RewardPlot()

    for episode in range(0, EPISODES):
        #world.x = 8.0
        #world.y = 3.0
        task = SearchTask(None, None, max_x=10.0, max_y=10.0)
        world.task = task
        agent.task = task

        reward, steps = executeepisode(world, agent)
        graph.plot(reward)

    graph.freeze()


MAXSTEPS = 2500


def executeepisode(world, agent):
    tasksolved = False
    steps = 0
    returnreward = None
    world.set_target(agent.task.target_x, agent.task.target_y)
    while tasksolved is not True:
        agent.act()
        steps += 1
        state_prime = agent.getstate()
        tasksolved = agent.task.stateisfinal(state_prime)
        if steps > MAXSTEPS:
            tasksolved = True
            print "Terminated episode early"
            returnreward = agent.totalreward
            agent.terminate()
        if steps % 200 is 0:
            world.plot()
            pass
    world.plot()
    world.reset()
    world.clear_plot()
    if returnreward is None:
        returnreward = agent.prevtotalreward
    return returnreward, steps


def distance(world, task):
    d = (task.target_x - world.x) ** 2
    d += (task.target_y - world.y) ** 2
    d = math.sqrt(d)
    return d

if __name__ == '__main__':
    main()