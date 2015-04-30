from worldsim import WorldSim
from worldsim import Agent
from worldsim import Action
from worldsim import SearchProblem
import math

from nose.tools import assert_equal
from nose.tools import assert_almost_equal

class TestWorldSim(object):

    def test_state(self):
        problem = SearchProblem(5, 5)
        world = WorldSim(10, 10, 6, 5, problem)
        agent = Agent(world, problem)
        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, 0)

        problem = SearchProblem(5, 5)
        world = WorldSim(10, 10, 4, 5, problem)
        agent = Agent(world, problem)
        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi)

        problem = SearchProblem(5, 5)
        world = WorldSim(10, 10, 5, 6, problem)
        agent = Agent(world, problem)

        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi/2)
