from worldsim import WorldSim
from worldsim import Agent
from worldsim import Action

from nose.tools import assert_equal

class TestWorldSim(object):

    def test_applyaction(self):
        action = Action(1.0,0.0)
        world = WorldSim(10,10)
        world.applyaction(action)
        # Test just the linear change
        assert_equal(world.x, 5.0 + WorldSim.TICK_DURATION)

        action = Action(0.0,1.0)
        world = WorldSim(10,10)
        world.applyaction(action)
        # Test just the angular change
        assert_equal(world.theta, WorldSim.TICK_DURATION)

        action = Action(1.0,0.0)
        world = WorldSim(1,1)
        for x in range(12):
            world.applyaction(action)
        # Should not have overstepped boundary
        assert_equal(world.x, 1.0)
