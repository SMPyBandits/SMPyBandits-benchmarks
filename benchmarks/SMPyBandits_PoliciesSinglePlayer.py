#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A benchmark of SMPyBandits Policies, for Single-Players multi-armed Bandits algorithms.

- Homepage for the benchmarks: https://github.com/Naereen/SMPyBandits-benchmarks/
- Homepage: https://SMPyBandits.GitHub.io/
- Author: Lilian Besson and contributors
- License: MIT
- Date: October 2019
"""
from __future__ import division, print_function  # Python 2 compatibility

__author__ = "Lilian Besson"
__version__ = "0.1"

# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import numpy as np

import SMPyBandits
from SMPyBandits import Arms
from SMPyBandits.Environment import MAB
from SMPyBandits import Policies


# Tries to know number of CPU
try:
    from multiprocessing import cpu_count
    CPU_COUNT = cpu_count()  #: Number of CPU on the local machine
except ImportError:
    CPU_COUNT = 1


# ------------------------------------------------
# ----------------- For Policies -----------------

min_arm, max_arm = 0.1, 0.9
make_MAB = lambda nbArms: SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(min_arm, max_arm, nbArms))})


algorithm_map = {
    "Uniform": Policies.Uniform,
    "Exp3": Policies.EpsilonDecreasing,
    "UCB": Policies.UCB,
    "Thompson": Policies.Thompson,
    "kl-UCB": Policies.klUCB,
    "MOSS-Anytime": Policies.MOSSAnytime,
    "AdBandits": Policies.AdBandits,
    "ApproximatedFHGittins": Policies.ApproximatedFHGittins,
}
if CPU_COUNT >= 8:
    algorithm_map.update({
        "Softmax": Policies.SoftmaxDecreasing,
        "Exp3++": Policies.Exp3PlusPlus,
        "Discounted-UCB": Policies.DiscountedUCB,
        "Discounted-Thompson": Policies.DiscountedThompson,
        "kl-UCB+": Policies.klUCBPlus,
        "kl-UCB++": Policies.klUCBPlusPlus,
        "kl-UCB-Switch": Policies.klUCBswitchAnytime,
        "BESA": Policies.BESA,
        "RCB": Policies.RCB,
        "PHE": Policies.PHE,
        "OC-UCB": Policies.OCUCB,
        "OSSB": Policies.OSSB,
        "Bayes-UCB": Policies.BayesUCB,
        "Tsallis-Inf": Policies.TsallisInf,
        "UCBoostEpsilon": Policies.UCBoostEpsilon,
    })

values_algorithm = list(algorithm_map.keys())

values_nbArms = [
    2,
]
if CPU_COUNT >= 8:
    values_nbArms += [
        3, 4, 5, 6, 7, 8, 9,
        # 12, 16, 24, 32, 48, 64,  # TODO
    ]
    # max_nbArms = 32  # XXX
    # values_nbArms = list(range(2, max_nbArms + 1))  # XXX

values_horizon = [100, 250, 500, 750]
# values_horizon += [
#     1000, 1250, 1500, 1750,
# ]
if CPU_COUNT >= 8:
    values_horizon += [
        2000, 2500,  # XXX
        3000, 3500,  # XXX
        4000, 4500,  # XXX
        5000, 5500,  # XXX
        6000, 6500,  # XXX
        7000, 7500,  # XXX
        8000, 8500,  # XXX
        9000, 9500,  # XXX
        # 10000, 15000,  # XXX
        # 20000, 25000,  # XXX
        # 30000,  # XXX
    ]

print("values_algorithm =", values_algorithm)  # DEBUG
print("values_nbArms =", values_nbArms)  # DEBUG
print("values_horizon =", values_horizon)  # DEBUG



class SP:
    """
    A benchmark of SMPyBandits Policies. In progress.

    - https://asv.readthedocs.io/en/stable/benchmarks.html#timing-benchmarks
    """
    processes = CPU_COUNT
    # repeat = (10, 200 if CPU_COUNT >= 8 else 20, 4800)
    # # number = 100
    # timeout = 4800

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
        self.MAB = make_MAB(nbArms)
        self.algorithm = algorithm_map[algname]
        self.nbArms = nbArms
        self.horizon = horizon

    # ------- Simulation function -------

    def full_simulation(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        sumReward = 0
        choices = [-1] * horizon
        for t in range(horizon):
            arm = alg.choice()
            reward = MAB.draw(arm)
            sumReward += reward
            alg.getReward(arm, reward)
            choices[t] = arm
        bestArmChoice = len([c for c in choices if c == (nbArms - 1)])
        return alg, sumReward, bestArmChoice

    # ------- Memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#memory

    mem_createAlgorithm = full_simulation

    # ------- Peak memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#peak-memory

    peakmem_createAlgorithm = full_simulation

    # ------- Timing benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#timing

    time_choice_and_getReward = full_simulation

    # ------- Tracking benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#tracking

    def track_sumReward(self, algname, nbArms, horizon):
        _, sumReward, _ = self.full_simulation(algname, nbArms, horizon)
        return sumReward
    track_sumReward.unit = "Sum reward"

    def track_meanReward(self, algname, nbArms, horizon):
        _, sumReward, _ = self.full_simulation(algname, nbArms, horizon)
        return sumReward / horizon
    track_meanReward.unit = "Mean reward"

    def track_regret(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        sumReward = self.track_sumReward(algname, nbArms, horizon)
        sumBestReward = MAB.maxArm * horizon
        return max(0, sumBestReward - sumReward)
    track_regret.unit = "Sum regret"

    def track_meanRegret(self, algname, nbArms, horizon):
        return self.track_regret(algname, nbArms, horizon) / horizon
    track_meanRegret.unit = "Mean regret"

    def track_normalizedRegret(self, algname, nbArms, horizon):
        return self.track_regret(algname, nbArms, horizon) / np.log(horizon)
    track_normalizedRegret.unit = "Normalized regret"

    def track_bestArmChoice(self, algname, nbArms, horizon):
        _, _, bestArmChoice = self.full_simulation(algname, nbArms, horizon)
        return bestArmChoice
    track_bestArmChoice.unit = "Best arm selections"

    def track_bestArmChoiceRate(self, algname, nbArms, horizon):
        _, _, bestArmChoice = self.full_simulation(algname, nbArms, horizon)
        return bestArmChoice / horizon
    track_bestArmChoiceRate.unit = "Best arm sample rate"
