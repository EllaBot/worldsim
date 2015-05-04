from task import Task

class SearchTask(Task):
    """
    This is the reward function and terminal threshold as set out in
    the search and rescue paper.
    """
    def __init__(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
        super(SearchTask, self).__init__()

    def reward(self, state, action, state_prime):
        if state_prime.distance < 0.55 and state_prime.omega < 0.2:
            return 100.0

        return -0.5 * abs(action.linear_velocity)

    def stateisfinal(self, state):
        if state.distance < 0.55:
            return True

        return False
