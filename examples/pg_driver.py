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
        executeepisode(world, agent)

MAXSTEPS = 2500

def executeepisode(world, agent):
    tasksolved = False
    steps = 0
    while tasksolved is not True:
        agent.act()
        steps += 1
        state_prime = agent.getstate()
        tasksolved = agent.task.stateisfinal(state_prime)
        if steps > MAXSTEPS:
            tasksolved = True
            print "Terminated episode early"
            agent.terminate()
        if steps % 10 is 0:
            world.plot()
    world.reset()
    world.clear_plot()

if __name__ == '__main__':
    main()