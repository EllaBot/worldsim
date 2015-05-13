from worldsim import VisualizedWorldSim
from worldsim.agents import PGAgent
from worldsim.tasks import SearchTask
import plot_utils

EPISODES = 10000

def main():
    task = SearchTask(5.0, 5.0)
    world = VisualizedWorldSim(10.0, 10.0, 8.0, 5.0, task)
    agent = PGAgent(world, task)
    world.agent = agent

    for episode in range(0, EPISODES):
        tasksolved = False
        steps = 0
        while tasksolved is not True:
            for x in range(0, 10):
                agent.act()
                steps += 1
                state_prime = agent.getstate()
                tasksolved = agent.task.stateisfinal(state_prime)
                if steps > 2500:
                    print agent.totalreward
                    agent.terminateearly()
                    tasksolved = True
                    print "Terminated rollout early"
                if tasksolved:
                    break

            world.plot()
        world.reset()
        world.clear_plot()


if __name__ == '__main__':
    main()