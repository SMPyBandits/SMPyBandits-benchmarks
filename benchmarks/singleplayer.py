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


# ------------------------------------------------
# ----------------- For Policies -----------------

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

values_nbArms = [
    2,
    # 3, 4, 5, 6, 7, 8, 9,
    # 12, 16, 24, 32, 48, 64,  # TODO
]
# max_nbArms = 32  # XXX
# values_nbArms = list(range(2, max_nbArms + 1))  # XXX

values_horizon = [100, 250, 500, 750]  #, 250, 500, 750, 1000, 2000],
values_horizon += [
    1000, 1250, 1500, 1750,
    # 2000, 2500,  # XXX
    # 3000, 3500,  # XXX
    # 4000, 4500,  # XXX
    # 5000, 5500,  # XXX
    # 6000, 6500,  # XXX
    # 7000, 7500,  # XXX
    # 8000, 8500,  # XXX
    # 9000, 9500,  # XXX
]

print("values_algorithm =", values_algorithm)  # DEBUG
print("values_nbArms =", values_nbArms)  # DEBUG
print("values_horizon =", values_horizon)  # DEBUG

min_arm, max_arm = 0.1, 0.9
make_MAB = lambda nbArms: SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(min_arm, max_arm, nbArms))})



class SMPyBandits_Policies:
    """
    A benchmark of SMPyBandits Policies. In progress.

    - https://asv.readthedocs.io/en/stable/benchmarks.html#timing-benchmarks
    """
    # processes = 32
    # repeat = (50, 1000, 1200)
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
        self.MAB = make_MAB(nbArms)
        self.algorithm = algorithm_map[algname]
        self.nbArms = nbArms
        self.horizon = horizon

    # ------- Memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#memory

    def mem_createAlgorithm(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            reward = MAB.draw(arm)
            alg.getReward(arm, reward)
        return alg

    # ------- Peak memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#peak-memory

    peakmem_createAlgorithm = mem_createAlgorithm

    # ------- Timing benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#timing

    def time_choice_and_getReward(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        for t in range(horizon):
            arm = alg.choice()
            reward = MAB.draw(arm)
            alg.getReward(arm, reward)

    # ------- Tracking benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#tracking

    def track_sumReward(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        sumReward = 0
        for t in range(horizon):
            arm = alg.choice()
            reward = MAB.draw(arm)
            sumReward += reward
            alg.getReward(arm, reward)
        return sumReward
    track_sumReward.unit = "reward"

    def track_regret(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        sumReward = self.track_sumReward(algname, nbArms, horizon)
        sumBestReward = MAB.maxArm * horizon
        return sumBestReward - sumReward
    track_regret.unit = "regret"

    def track_bestArmChoice(self, algname, nbArms, horizon):
        MAB = make_MAB(nbArms)
        alg = algorithm_map[algname](nbArms)
        alg.startGame()
        choices = [-1] * horizon
        for t in range(horizon):
            arm = alg.choice()
            reward = MAB.draw(arm)
            choices[t] = arm
            alg.getReward(arm, reward)
        bestArmChoice = len([c for c in choices if c == (nbArms - 1)])
        return bestArmChoice
    track_bestArmChoice.unit = "number"
