from worldsim.agents import State
import math
from nose.tools import assert_almost_equal


class TestState(object):

    def test_state(self):
        # Agent will always start facing east (theta = 0)
        state = self.generate_state(0, 0)
        assert_almost_equal(state.distance, 0)
        assert_almost_equal(state.omega, 0)

        state = self.generate_state(0, 1)
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi / 2.0)

        state = self.generate_state(-1, 0)
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, math.pi)

        state = self.generate_state(0, -1)
        assert_almost_equal(state.distance, 1)
        assert_almost_equal(state.omega, 3.0 * math.pi / 2.0)

        state = self.generate_state(1, 1)
        assert_almost_equal(state.distance, math.sqrt(2))
        assert_almost_equal(state.omega, math.pi / 4.0)

        state = self.generate_state(1, -1)
        assert_almost_equal(state.distance, math.sqrt(2))
        assert_almost_equal(state.omega, 7.0 * math.pi / 4.0)

    def generate_state(self, x_diff, y_diff, agent_x=5.0, agent_y=5.0):
        return State.frompoints(agent_x, agent_y, 0.0, agent_x + x_diff, agent_y + y_diff)




