from worldsim import WorldSim

from nose.tools import assert_equal

class TestWorldSim(object):

    def test_tick(self):
        world = WorldSim(10.0, 10.0, 5.0, 5.0)
        world.linear_velocity = 1.0
        world.angular_velocity = 0.0
        world.tick()
        # Test just the linear change
        assert_equal(world.x, 5.0 + WorldSim.TICK_DURATION)

        world = WorldSim(10.0, 10.0, 5.0, 5.0)
        world.linear_velocity = 0.0
        world.angular_velocity = 1.0
        world.tick()
        # Test just the angular change
        assert_equal(world.theta, WorldSim.TICK_DURATION)

        world = WorldSim(1.0, 1.0, 0.0, 0.0)
        world.linear_velocity = 1.0
        world.angular_velocity = 0.0
        for x in range(12):
            world.tick()
        # Should not have overstepped boundary
        assert_equal(world.x, 1.0)
