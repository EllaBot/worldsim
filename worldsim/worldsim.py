import math

class WorldSim(object):
    TICK_DURATION = 0.10

    """Simulates a world with an agent.

    The agent is controlled by specifying angular and linear velocities
    at small time intervals.

    The world is represented as an NxM closed rectangle.

    Parameters
    ----------
    width: float
        The width (N) of the world in meters

    height: float
        The height (M) of the world in meters

    initial_x: float, optional
        The initial x position in meters, where the origin is the top left corner

    initial_y: float, optional
        The initial y position in meters, where the origin is the top left corner
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.goal_y = 5.0
        self.goal_x = 5.0

        self.agents = list()


    def tick(self):
        """Tick the clock once based on TICK_DURATION
        """
        for agent in self.agents:
            agent.theta = (agent.theta + agent.angular_velocity * WorldSim.TICK_DURATION) % (math.pi / 2.0)
            agent.x += math.sin(agent.theta + math.pi / 2.0) * agent.linear_velocity * WorldSim.TICK_DURATION
            agent.y += math.cos(agent.theta + math.pi / 2.0) * agent.linear_velocity * WorldSim.TICK_DURATION

            # Check for boundary overstepping
            agent.x = min(max(agent.x, 0.0), self.width)
            agent.y = min(max(agent.y, 0.0), self.height)

