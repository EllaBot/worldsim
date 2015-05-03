from worldsim import WorldSim
from worldsim.agents import RandomAgent
from worldsim.agents import State
from worldsim.tasks import SearchTask


def main():
    task = SearchTask(5.0, 5.0)
    world = WorldSim(10.0, 10.0, 0, 0, task)
    agent = RandomAgent(world, task)
    agent.linear_velocity = 1.0
    agent.angular_velocity = 0.0
    world.agent = agent

    tasksolved = False
    actions_taken = 0
    while tasksolved is False:
        agent.act()
        agent_state = agent.getstate()
        tasksolved = world.task.stateisfinal(agent_state)
        actions_taken += 1

    print("Random agent took " + str(actions_taken) + " steps to reach the goal.")

if __name__ == '__main__':
    main()
