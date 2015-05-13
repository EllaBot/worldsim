from random import random
import math

from worldsim import VisualizedWorldSim
from worldsim.agents import PGAgent
from worldsim.tasks import SearchTask
from worldsim.experiments.reward_plot import RewardPlot


EPISODES = 100000
GOODRANDOMPOSITION = [0.575, -0.13, 0.0287, -0.897, -0.3881, 0.02335]


def main():
    task = SearchTask(None, None, max_x=10.0, max_y=10.0)
    world = VisualizedWorldSim(10.0, 10.0, randomizeposition=True)
    agent = PGAgent(world, task, initialtheta=GOODRANDOMPOSITION, epsilon=0.4)
    world.agent = agent
    graph = RewardPlot()

    for episode in range(0, EPISODES):
        task = SearchTask(None, None, max_x=10.0, max_y=10.0)
        #task = SearchTask(5.0, 5.0)
        agent.task = task
        d = task.distance(world.x, world.y)
        reward, steps = executeepisode(world, agent)
        assert d/float(steps) <= world.TICK_DURATION * 1.5
        graph.plot(d/float(steps))

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

    if returnreward is None:
        returnreward = agent.prevtotalreward
    return returnreward, steps


if __name__ == '__main__':
    main()