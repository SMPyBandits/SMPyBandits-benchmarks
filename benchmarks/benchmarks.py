# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


import SMPyBandits
import SMPyBandits.Policies

algorithm_map = {
    "Uniform": SMPyBandits.Policies.Uniform,
    "UCB": SMPyBandits.Policies.UCB,
    "EpsilonDecreasing": SMPyBandits.Policies.EpsilonDecreasing,
    "SoftmaxDecreasing": SMPyBandits.Policies.SoftmaxDecreasing,
    "Exp3PlusPlus": SMPyBandits.Policies.Exp3PlusPlus,
    "Thompson": SMPyBandits.Policies.Thompson,
    "klUCB": SMPyBandits.Policies.klUCB,
    "BESA": SMPyBandits.Policies.BESA,
    "RCB": SMPyBandits.Policies.RCB,
    "PHE": SMPyBandits.Policies.PHE,
    "BayesUCB": SMPyBandits.Policies.BayesUCB,
}

values_algorithm = list(algorithm_map.keys()),
values_nbArms = [2, 3, 4] #, 8, 12, 16, 24, 32, 48, 64]
values_horizon = [100],  #, 250, 500, 750, 1000, 2000],


class SMPyBanditsSuite:
    """
    A benchmark of SMPyBandits Policies. In progress.
    """
    params = (
        values_algorithm,
        values_nbArms,
        values_horizon,
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

