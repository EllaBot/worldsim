from worldsim import WorldSim
from worldsim.agents import Agent
from worldsim.agents import State
from worldsim.tasks import SearchTask

def main():
    task = SearchTask(5.0, 5.0)
    world = WorldSim(10.0, 10.0, 0, 0, task)
    agent = Agent(world, task)
    agent.linear_velocity = 1.0
    agent.angular_velocity = 0.0
    world.agent = agent

    tasksolved = False
    while tasksolved is False:
        agent.act()
        agent_state = agent.getstate()
        print(agent_state)
        tasksolved = world.task.stateisfinal(agent_state)


if __name__ == '__main__':
    main()
