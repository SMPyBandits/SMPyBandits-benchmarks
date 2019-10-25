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
    "MOSSAnytime": Policies.MOSSAnytime,
    "AdBandits": Policies.AdBandits,
    "BESA": Policies.BESA,
    "RCB": Policies.RCB,
    "RCB": Policies.RCB,
    "PHE": Policies.PHE,
    "BayesUCB": Policies.BayesUCB,
}

values_algorithm = list(algorithm_map.keys())

values_nbArms = [2, 3, 4, 5, 6, 7, 8, 9, 12, 16, 24, 32, 48, 64]
# max_nbArms = 32
# values_nbArms = list(range(2, max_nbArms + 1))

values_horizon = [100, 250, 500, 750]  #, 250, 500, 750, 1000, 2000],
values_horizon += [
    1000, 1250, 1500, 1750,
    2000, 2500,
    3000, 3500,
    4000, 4500,
    5000, 5500,
    6000, 6500,
    7000, 7500,
    8000, 8500,
    9000, 9500,
]

print("values_algorithm =", values_algorithm)  # DEBUG
print("values_nbArms =", values_nbArms)  # DEBUG
print("values_horizon =", values_horizon)  # DEBUG


class SMPyBandits_Policies:
    """
    A benchmark of SMPyBandits Policies. In progress.

    - https://asv.readthedocs.io/en/stable/benchmarks.html#timing-benchmarks
    """
    # processes = 32
    # repeat = (10, 50, 1200)
    # number = 100
    timeout = 1200

    params = [
        values_algorithm,
        values_nbArms,
        values_horizon,
    ]
    param_names = [
        "algorithm",
        "nbArms",
        "horizon",
    ]

    def setup(self, algname, nbArms, horizon):
        self.MAB = SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(0.1, 0.9, nbArms))})
        self.algorithm = algorithm_map[algname]
        self.nbArms = nbArms
        self.horizon = horizon

    def mem_createAlgorithm(self, algname, nbArms, horizon):
        alg = algorithm_map[algname](self.nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            reward = self.MAB.draw(arm)
            alg.getReward(arm, reward)
        return alg

    peakmem_createAlgorithm = mem_createAlgorithm

    def time_choice(self, algname, nbArms, horizon):
        self.MAB = SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(0.1, 0.9, nbArms))})
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            reward = self.MAB.draw(arm)
            # alg.getReward(arm, reward)

    def time_choice_and_getReward(self, algname, nbArms, horizon):
        self.MAB = SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(0.1, 0.9, nbArms))})
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            reward = self.MAB.draw(arm)
            alg.getReward(arm, reward)

    def time_getReward(self, algname, nbArms, horizon):
        self.MAB = SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(0.1, 0.9, nbArms))})
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = np.random.randint(nbArms)
            reward = self.MAB.draw(arm)
            alg.getReward(arm, reward)

    def track_sumReward(self, algname, nbArms, horizon):
        self.MAB = SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(0.1, 0.9, nbArms))})
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        sumReward = 0
        for t in range(horizon):
            arm = alg.choice()
            reward = self.MAB.draw(arm)
            sumReward += reward
            alg.getReward(arm, reward)
        return sumReward
    track_sumReward.unit = "reward"

    def track_regret(self, algname, nbArms, horizon):
        sumReward = self.track_sumReward(algname, nbArms, horizon)
        sumBestReward = self.MAB.maxArm * horizon
        return sumBestReward - sumReward
    track_regret.unit = "regret"

    def track_bestArmChoice(self, algname, nbArms, horizon):
        self.MAB = SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(0.1, 0.9, nbArms))})
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        choices = [-1] * horizon
        for t in range(horizon):
            arm = alg.choice()
            reward = self.MAB.draw(arm)
            choices[t] = arm
            alg.getReward(arm, reward)
        bestArmChoice = sum(c == (nbArms - 1) for c in choices)
        return bestArmChoice
    track_bestArmChoice.unit = "number"

