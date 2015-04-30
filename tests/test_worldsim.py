from worldsim import WorldSim
from worldsim import Agent

from nose.tools import assert_equal

class TestWorldSim(object):

    def test_tick(self):
        world = WorldSim(10.0, 10.0)
        agent = Agent(5.0, 5.0)
        agent.linear_velocity = 1.0
        agent.angular_velocity = 0.0
        world.agents.append(agent)
        world.tick()
        # Test just the linear change
        assert_equal(agent.x, 5.0 + WorldSim.TICK_DURATION)

        world = WorldSim(10.0, 10.0)
        agent = Agent(5.0, 5.0)
        agent.linear_velocity = 0.0
        agent.angular_velocity = 1.0
        world.agents.append(agent)
        world.tick()
        # Test just the angular change
        assert_equal(agent.theta, WorldSim.TICK_DURATION)

        world = WorldSim(1.0, 1.0)
        agent = Agent(0.0, 0.0)
        agent.linear_velocity = 1.0
        agent.angular_velocity = 0.0
        world.agents.append(agent)
        world.tick()
        for x in range(12):
            world.tick()
        # Should not have overstepped boundary
        assert_equal(agent.x, 1.0)
