from problem import Problem


class SearchProblem(Problem):
    def __init__(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
        super(SearchProblem,self).__init__()

    def reward(self, action, state_prime):
        if state_prime.distance < 0.55 and state_prime.omega < 0.2:
            return 100

        return -0.5 * action.linear_velocity

    def stateisfinal(self, state):
        if state.distance < 0.55:
            return True

        return False