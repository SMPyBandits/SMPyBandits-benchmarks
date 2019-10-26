#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A benchmark of SMPyBandits Policies, for Multi-Players multi-armed Bandits algorithms.

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


# Tries to know number of CPU
try:
    from multiprocessing import cpu_count
    CPU_COUNT = cpu_count()  #: Number of CPU on the local machine
except ImportError:
    CPU_COUNT = 1


# ------------------------------------------------------------
# ----------------- For PoliciesMultiPlayers -----------------

min_arm, max_arm = 0.1, 0.9
make_MAB = lambda nbArms: SMPyBandits.Environment.MAB({'arm_type': Arms.Bernoulli, 'params': tuple(np.linspace(min_arm, max_arm, nbArms))})


from SMPyBandits.Policies import UCB, klUCB, Thompson
from SMPyBandits.Policies import SIC_MMAB


algorithmMP_map = {
    "CentralizedCycling": lambda nbPlayers, nbArms: PoliciesMultiPlayers.CentralizedCycling(nbArms, nbPlayers),
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
    "Selfish-UCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.Selfish(nbPlayers, nbArms, UCB),
    "Selfish-klUCB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.Selfish(nbPlayers, nbArms, klUCB),
    # "Selfish-Thompson": lambda nbPlayers, nbArms: PoliciesMultiPlayers.Selfish(nbPlayers, nbArms, Thompson),
    "SIC_MMAB": lambda nbPlayers, nbArms: PoliciesMultiPlayers.Selfish(nbPlayers, nbArms, SIC_MMAB),
}
values_algorithmMP = list(algorithmMP_map.keys())

values_nbArmsMP = [
    9,
]

values_nbPlayers = [
    2, 3, 6, 9
]

values_horizonMP = [100, 250, 500, 750]
# values_horizonMP += [
#     1000, 1250, 1500, 1750,
# ]
if CPU_COUNT >= 8:
    values_horizonMP += [
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

print("values_algorithmMP =", values_algorithmMP)  # DEBUG
print("values_nbArmsMP =", values_nbArmsMP)  # DEBUG
print("values_nbPlayers =", values_nbPlayers)  # DEBUG
print("values_horizonMP =", values_horizonMP)  # DEBUG


class SMPyBandits_PoliciesMultiPlayers:
    """
    A benchmark of SMPyBandits PoliciesMultiPlayers. In progress.

    - https://asv.readthedocs.io/en/stable/benchmarks.html#timing-benchmarks
    """
    processes = CPU_COUNT
    # repeat = (10, 200 if CPU_COUNT >= 8 else 20, 4800)
    # # number = 100
    # timeout = 4800

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
        self.my_policy_MP = algorithmMP_map[algname](nbPlayers, nbArms)
        self.nbArms = nbArms
        self.nbPlayers = nbPlayers
        self.horizon = horizon

    # ------- Memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#memory

    def mem_createAlgorithms(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = algorithmMP_map[algname](nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ i for i in range(nbPlayers) if choices[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    children[i].getReward(k, reward)
        return my_policy_MP

    # ------- Peak memory benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#peak-memory

    peakmem_createAlgorithms = mem_createAlgorithms

    # ------- Timing benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#timing

    def time_choice_and_getReward(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = algorithmMP_map[algname](nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ i for i in range(nbPlayers) if choices[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    children[i].getReward(k, reward)

    # ------- Tracking benchmarks -------
    # https://asv.readthedocs.io/en/stable/writing_benchmarks.html#tracking

    def track_sumRewards(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = algorithmMP_map[algname](nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        sumRewards = [0] * nbPlayers
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ i for i in range(nbPlayers) if choices[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    children[i].getReward(k, reward)
                    sumRewards[i] += reward
        return sum(sumRewards)
    track_sumRewards.unit = "sum rewards"

    def track_centralizedRegret(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        sumRewards = self.track_sumRewards(algname, nbArms, nbPlayers, horizon)
        sumBestRewards = sum(MAB.Mbest(nbPlayers))
        return sumBestRewards - sumRewards
    track_centralizedRegret.unit = "centralized regret"

    def track_collisions(self, algname, nbArms, nbPlayers, horizon):
        MAB = make_MAB(nbArms)
        my_policy_MP = algorithmMP_map[algname](nbPlayers, nbArms)
        children = my_policy_MP.children             # get a list of usable single-player policies
        for one_policy in children:
            one_policy.startGame()                       # start the game
        collisions = [0] * nbPlayers
        for t in range(horizon):
            # chose one arm, for each player
            choices = [ children[i].choice() for i in range(nbPlayers) ]
            for k in range(nbArms):
                players_who_played_k = [ i for i in range(nbPlayers) if choices[i] == k ]
                reward = MAB.draw(k) if len(players_who_played_k) == 1 else 0  # sample a reward
                for i in players_who_played_k:
                    if len(players_who_played_k) > 1:
                        collisions[i] += 1
                    children[i].getReward(k, reward)
        return sum(collisions)
    track_collisions.unit = "collisions"

