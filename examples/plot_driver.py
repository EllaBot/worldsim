from worldsim import WorldSim
from worldsim import VisualizedWorldSim
from worldsim.agents import SarsaAgent, State
from worldsim.tasks import SearchTask
from true_online_td_lambda import learner_plotting_utilities
import time

def main():
    task = SearchTask(5.0, 5.0)
    world = VisualizedWorldSim(10.0, 10.0, 0, 0, task)
    world.set_target(task.target_x, task.target_y)
    agent = SarsaAgent(world, task)
    world.agent = agent

    tasksolved = False

    for x in range(0, 100):
        while tasksolved is False:
            for i in range(10):
                agent.act()
                agent_state = agent.getstate()
                tasksolved = world.task.stateisfinal(agent_state)
                if tasksolved:
                    break
            world.plot()

        world.clear_plot()
        world.reset()
        tasksolved = False

    world.freeze_plot()

if __name__ == '__main__':
    main()
