from worldsim import VisualizedWorldSim, WorldSim
from worldsim.agents import PGAgent
from worldsim.tasks import SearchTask
from reward_plot import RewardPlot
from random import random
import math

EPISODES = 600000
GOODRANDOMPOSITION = [0.575, -0.13, 0.0287, -0.897, -0.3881, 0.02335]


def main():
    task = SearchTask(5.0, 5.0)
    world = VisualizedWorldSim(10.0, 10.0, 8.0, 3.0, task)
    # world = WorldSim(10.0, 10.0, 8.0, 3.0, task)
    agent = PGAgent(world, task, initialtheta=GOODRANDOMPOSITION, epsilon=0.5)
    world.agent = agent
    graph = RewardPlot()

    for episode in range(0, EPISODES):
        #world.x = 8.0
        #world.y = 3.0
        task.target_x = random() * world.width
        task.target_y = random() * world.height
        distance = task.target_x ** 2 + world.x ** 2
        distance += task.target_y ** 2 + world.y ** 2
        distance = math.sqrt(distance)
        reward, steps = executeepisode(world, agent)
        graph.plot(reward)


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
    if returnreward == 0:
        print "hi"
    return returnreward, steps


if __name__ == '__main__':
    main()