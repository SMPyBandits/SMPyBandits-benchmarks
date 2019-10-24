# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


import SMPyBandits
import SMPyBandits.Policies

algorithm_map = {
    "Uniform": SMPyBandits.Policies.Uniform,
    "UCB": SMPyBandits.Policies.UCB,
    "klUCB": SMPyBandits.Policies.klUCB,
    "BESA": SMPyBandits.Policies.BESA,
}

class SMPyBanditsSuite:
    """
    A benchmark of SMPyBandits Policies. In progress.
    """
    params = (
        ("Uniform", "UCB", "klUCB", "BESA"),
        (2, 8, 16, 32, 64),
        (100, 500, 1000, 5000),
    )
    params_names = (
        "algorithm",
        "nbArms",
        "horizon",
    )

    def setup(self, algorithm, nbArms, horizon):
        self.algorithm = algorithm_map[algorithm]
        self.nbArms = nbArms
        self.horizon = horizon

    def mem_createAlgorithm(self, algorithm, nbArms, horizon):
        alg = self.algorithm(self.nbArms)
        alg.startGame()
        return alg

    def time_choice(self, algorithm, nbArms, horizon):
        alg = self.algorithm(self.nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            reward = 0  # FIXME
            alg.getReward(arm, reward)


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    params = [100, 500, 1000, 5000]

    def setup(self, n):
        self.n = n
        self.d = {}
        for x in range(self.n):
            self.d[x] = None

    def time_keys(self, n):
        for key in self.d.keys():
            pass

    def time_range(self, n):
        d = self.d
        for key in range(n):
            x = d[key]


class MemSuite:
    params = [100, 500, 1000, 5000]

    def setup(self, n):
        self.n = n

    def mem_list(self, n):
        return [0] * n
