from worldsim import WorldSim
from worldsim import VisualizedWorldSim
from worldsim.agents import SarsaAgent, State
from worldsim.tasks import SearchTask
from true_online_td_lambda import learner_plotting_utilities
from random import random
import numpy as np
import sys
import time

def main():
    task = SearchTask(5.0, 5.0)
    world = VisualizedWorldSim(10.0, 10.0, 0, 0, task)
    world.set_target(task.target_x, task.target_y)
    agent = SarsaAgent(world, task)
    world.agent = agent

    tasksolved = False

    if (len(sys.argv) > 1 and sys.argv[1] == '--load'):
        theta = np.load('weights_file.npy')
        agent.learner.theta = theta

    for x in range(0, 100):
        while tasksolved is False:
            for i in range(10):
                agent.act()
                agent_state = agent.getstate()
                tasksolved = world.task.stateisfinal(agent_state)
                if tasksolved:
                    break
            world.plot()

        world.reset()
        task.target_x = random() * world.width
        task.target_y = random() * world.height
        world.set_target(task.target_x, task.target_y)
        tasksolved = False

    world.freeze_plot()

if __name__ == '__main__':
    main()
