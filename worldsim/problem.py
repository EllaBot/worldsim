class Problem(object):
    def __init__(self):
        raise NotImplementedError("Should have implemented this")

    def stateisfinal(self, state):
        raise NotImplementedError("Should have implemented this")

    def reward(self, state_prime):
        raise NotImplementedError("Should have implemented this")
