#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A benchmark of SMPyBandits Policies, for Single- and Multi-Players multi-armed Bandits algorithms.

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
from SMPyBandits import PoliciesMultiPlayers


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


# ------------------------------------------------------------
# ----------------- For PoliciesMultiPlayers -----------------

algorithmMP_map = {
    "CentralizedCycling": lambda nbPlayers, nbArms: PoliciesMultiPlayers.CentralizedCycling(nbPlayers, nbArms),
    "CentralizedMultiplePlay-UCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.CentralizedMultiplePlay(nbPlayers, nbArms, UCB),
    "CentralizedMultiplePlay-klUCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.CentralizedMultiplePlay(nbPlayers, nbArms, klUCB),
    # "CentralizedMultiplePlay-Thompson": lambda nbPlayers, nbArms: PoliciesMultiPlayers.CentralizedMultiplePlay(nbPlayers, nbArms, Thompson),
    "rhoRand-UCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.rhoRand(nbPlayers, nbArms, UCB),
    "rhoRand-klUCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.rhoRand(nbPlayers, nbArms, klUCB),
    # "rhoRand-Thompson": lambda nbPlayers, nbArms: PoliciesMultiPlayers.rhoRand(nbPlayers, nbArms, Thompson),
    "rhoEst": lambda nbPlayers, nbArms: PoliciesMultiPlayers.rhoEst(nbPlayers, nbArms, UCB),
    # "rhoLearn": lambda nbPlayers, nbArms: PoliciesMultiPlayers.rhoLearn(nbPlayers, nbArms, UCB),
    # "rhoLearnEst": lambda nbPlayers, nbArms: PoliciesMultiPlayers.rhoLearnEst(nbPlayers, nbArms, UCB),
    "RandTopM": lambda nbPlayers, nbArms: PoliciesMultiPlayers.RandTopM(nbPlayers, nbArms, UCB),
    "MCTopM-UCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.MCTopM(nbPlayers, nbArms, UCB),
    "MCTopM-klUCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.MCTopM(nbPlayers, nbArms, klUCB),
    # "MCTopM-Thompson": lambda nbPlayers, nbArms: PoliciesMultiPlayers.MCTopM(nbPlayers, nbArms, Thompson),
    "Selfish-UCB": lambda (*args, **kwargs): PoliciesMultiPlayers.Selfish(UCB),
    "Selfish-klUCB": lambda (*args, **kwargs): PoliciesMultiPlayers.Selfish(klUCB),
    # "Selfish-Thompson": lambda (*args, **kwargs): PoliciesMultiPlayers.Selfish(Thompson),
    "SIC_MMAB": lambda (*args, **kwargs): PoliciesMultiPlayers.Selfish(SIC_MMAB),
}
values_algorithmMP = list(algorithmMP_map.keys())

values_nbArmsMP = [
    9,
]

values_nbPlayers = [
    2, 3, 6, 9
]

values_horizonMP = [100, 250, 500, 750]  #, 250, 500, 750, 1000, 2000],
values_horizonMP += [
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

print("values_algorithmMP =", values_algorithmMP)  # DEBUG
print("values_nbArmsMP =", values_nbArmsMP)  # DEBUG
print("values_nbPlayers =", values_nbPlayers)  # DEBUG
print("values_horizonMP =", values_horizonMP)  # DEBUG


class SMPyBandits_PoliciesMultiPlayers:
    """
    A benchmark of SMPyBandits PoliciesMultiPlayers. In progress.

    - https://asv.readthedocs.io/en/stable/benchmarks.html#timing-benchmarks
    """
    # processes = 32
    # repeat = (50, 1000, 1200)
    # number = 100
    timeout = 1200

    params = [
        values_algorithmMP,
        values_nbArmsMP,
        values_nbPlayers,
        values_horizonMP,
    ]
    param_names = [
        "algorithm",
        "nbArms",
        "nbPlayers",
        "horizon",
    ]

    def setup(self, algname, nbArms, nbPlayers, horizon):
        self.MAB = make_MAB(nbArms)
        self.algorithm = algorithm_map[algname]
        self.nbArms = nbArms
        self.horizon = horizon

    # ------- Memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#memory

    def mem_createAlgorithm(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = Policy_MP(nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ k_t[i] for i in range(nbPlayers) if k_t[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    children[i].getReward(k, reward)
        return my_policy_MP

    # ------- Peak memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#peak-memory

    peakmem_createAlgorithm = mem_createAlgorithm

    # ------- Timing benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#timing

    def time_choice_and_getReward(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = Policy_MP(nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ k_t[i] for i in range(nbPlayers) if k_t[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    children[i].getReward(k, reward)

    # ------- Tracking benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#tracking

    def track_sumReward(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = Policy_MP(nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        sumRewards = [0] * nbPlayers
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ k_t[i] for i in range(nbPlayers) if k_t[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    children[i].getReward(k, reward)
                    sumRewards[i] += reward
        return sum(sumRewards)
    track_sumReward.unit = "sum rewards"

    def track_regret(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        sumRewards = self.track_sumReward(algname, nbArms, horizon)
        sumBestRewards = sum(MAB.Mbest(nbPlayers))
        return sumBestRewards - sumRewards
    track_regret.unit = "regret"

    def track_collisions(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = Policy_MP(nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        collisions = [0] * nbPlayers
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ k_t[i] for i in range(nbPlayers) if k_t[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                if len(players_who_played_k) > 1:
                    collisions[i] += 1
                for i in players_who_played_k:
                    children[i].getReward(k, reward)
        return sum(collisions)
    track_bestArmChoice.unit = "collision"

