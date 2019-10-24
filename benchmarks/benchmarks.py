# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import numpy as np

import SMPyBandits
from SMPyBandits import Policies
from SMPyBandits import Arms
from SMPyBandits.Environment import MAB

algorithm_map = {
    "Uniform": Policies.Uniform,
    "UCB": Policies.UCB,
    "EpsilonDecreasing": Policies.EpsilonDecreasing,
    "SoftmaxDecreasing": Policies.SoftmaxDecreasing,
    "Exp3PlusPlus": Policies.Exp3PlusPlus,
    "Thompson": Policies.Thompson,
    "klUCB": Policies.klUCB,
    "BESA": Policies.BESA,
    "RCB": Policies.RCB,
    "PHE": Policies.PHE,
    "BayesUCB": Policies.BayesUCB,
}

values_algorithm = tuple(algorithm_map.keys()),
values_nbArms = (2, 3, 4) #, 8, 12, 16, 24, 32, 48, 64)
values_horizon = (100),  #, 250, 500, 750, 1000, 2000),


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
        configuration = {
            'arm_type': Arms.Bernoulli,
            'params':   tuple(np.arange(0.1, 0.9, nbArms)),
        }
        self.MAB = SMPyBandits.Environment.MAB(configuration)

    def mem_createAlgorithm(self, algorithm, nbArms, horizon):
        alg = self.algorithm(self.nbArms)
        alg.startGame()
        return alg

    def time_choice(self, algorithm, nbArms, horizon):
        alg = self.algorithm(self.nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            # reward = 0  # FIXME
            reward = self.MAB.draw(arm)
            alg.getReward(arm, reward)

