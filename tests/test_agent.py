from worldsim import WorldSim
from worldsim.agents import Agent
from worldsim.agents import Action
from worldsim.tasks import SearchTask
import math

from nose.tools import assert_equal
from nose.tools import assert_almost_equal

class TestWorldSim(object):

    def test_state(self):
        task = SearchTask(5, 5)
        world = WorldSim(10, 10, 6, 5, task)
        agent = Agent(world, task)
        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, 0)

        problem = SearchTask(5, 5)
        world = WorldSim(10, 10, 4, 5, task)
        agent = Agent(world, task)
        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi)

        problem = SearchTask(5, 5)
        world = WorldSim(10, 10, 5, 6, task)
        agent = Agent(world, task)

        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi/2)
