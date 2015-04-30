from worldsim import WorldSim
from worldsim import Agent
from worldsim import State
from worldsim import SearchProblem

def main():
    problem = SearchProblem(5,5)
    world = WorldSim(10.0, 10.0, 0, 0, problem)
    agent = Agent(world, problem)
    agent.linear_velocity = 1.0
    agent.angular_velocity = 0.0
    world.agent = agent

    problemsolved = False
    while problemsolved is False:
        agent.act()
        agent_state = world.getstate()
        print(agent_state)
        problemsolved = world.problem.stateisfinal(agent_state)


if __name__ == '__main__':
    main()