from worldsim import WorldSim
from worldsim.agents import RandomAgent
from worldsim.agents import Action
from worldsim.tasks import SearchTask
import math

from nose.tools import assert_equal
from nose.tools import assert_almost_equal

class TestRandomAgent(object):

    def test_state(self):
        # Agent will always start facing east (theta = 0)
        task = SearchTask(5, 5)
        world = WorldSim(10, 10, 6, 5, task)
        agent = RandomAgent(world, task)
        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi)

        world = WorldSim(10, 10, 5, 4, task)
        agent = RandomAgent(world, task)
        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi/2)

        world = WorldSim(10, 10, 5, 6, task)
        agent = RandomAgent(world, task)

        state = agent.getstate()
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, 3 * math.pi/2)

        world = WorldSim(10, 10, 0, 0, task)
        agent = RandomAgent(world, task)

        state = agent.getstate()
        assert_almost_equal(state.distance, 5 * math.sqrt(2))
        assert_almost_equal(state.omega, math.pi/4.0)

        world = WorldSim(10, 10, 10, 10, task)
        agent = RandomAgent(world, task)

        state = agent.getstate()
        assert_almost_equal(state.distance, 5 * math.sqrt(2))
        assert_almost_equal(state.omega, 5 * math.pi/4.0)

