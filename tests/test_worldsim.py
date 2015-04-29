from worldsim import WorldSim

from nose.tools import assert_equal

class TestWorldSim(object):

    def test_tick(self):
        world = WorldSim(10.0, 10.0, 5.0, 5.0)

        world.linear_velocity = 1.0
        world.angular_velocity = 0.0
        world.tick()

        assert_equal(world.x, 5.0 + WorldSim.TICK_DURATION)
