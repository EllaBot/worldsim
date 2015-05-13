from worldsim import VisualizedWorldSim, WorldSim
from worldsim.agents import PGAgent
from worldsim.tasks import SearchTask
from reward_plot import RewardPlot

EPISODES = 600000


def main():
    task = SearchTask(5.0, 5.0)
    # world = VisualizedWorldSim(10.0, 10.0, 8.0, 5.0, task)
    world = WorldSim(10.0, 10.0, 8.0, 5.0, task)
    agent = PGAgent(world, task, initialtheta=[0.3865, 0.007, 0.084, 0.36, -0.0465, 0.01479])
    world.agent = agent
    graph = RewardPlot()
    rewards = []
    for episode in range(0, EPISODES):
        #world.x = 8.0
        #world.y = 3.0
        reward = executeepisode(world, agent)
        graph.plot(reward)


MAXSTEPS = 2500


def executeepisode(world, agent):
    tasksolved = False
    steps = 0
    returnreward = None
    # world.set_target(agent.task.target_x, agent.task.target_y)
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
        if steps % 10 is 0:
            # world.plot()
            pass
    world.reset()
    # world.clear_plot()
    if returnreward is None:
        returnreward = agent.prevtotalreward
    if returnreward == 0:
        print "hi"
    return returnreward


if __name__ == '__main__':
    main()