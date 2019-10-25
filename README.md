# Airspeed Velocity benchmarks for *SMPyBandits*

This repository contains code (and soon, also results) of benchmarks for the [SMPyBandits](https://github.com/SMPyBandits/SMPyBandits/) python package, using the [airspeed velocity](https://asv.readthedocs.io/en/stable/using.html) tool.

This project is written by [Lilian Besson's](https://perso.crans.org/besson/), written in [Python (2 or 3)](https://www.python.org/), to test the quality of [SMPyBandits](https://github.com/SMPyBandits/SMPyBandits/), my open-source Python package for numerical simulations on :slot_machine: *single*-player and *multi*-players [Multi-Armed Bandits (MAB)](https://en.wikipedia.org/wiki/Multi-armed_bandit) algorithms.

A complete Sphinx-generated documentation for [SMPyBandits](https://github.com/SMPyBandits/SMPyBandits/) is on [SMPyBandits.GitHub.io](https://smpybandits.github.io/).

[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/SMPyBandits-benchmarks/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/SMPyBandits-benchmarks/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/SMPyBandits-benchmarks/README.md?pixel)](https://GitHub.com/Naereen/SMPyBandits-benchmarks/)
[![PyPI version](https://img.shields.io/pypi/v/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![PyPI implementation](https://img.shields.io/pypi/implementation/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/smpybandits.svg?logo=python)](https://pypi.org/project/SMPyBandits)
[![PyPI download](https://img.shields.io/pypi/dm/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![PyPI status](https://img.shields.io/pypi/status/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![Documentation Status](https://readthedocs.org/projects/smpybandits/badge/?version=latest)](https://SMPyBandits.ReadTheDocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/SMPyBandits/SMPyBandits.svg?branch=master)](https://travis-ci.org/SMPyBandits/SMPyBandits)
[![Stars of https://github.com/Naereen/SMPyBandits-benchmarks/](https://badgen.net/github/stars/SMPyBandits/SMPyBandits)](https://GitHub.com/Naereen/SMPyBandits-benchmarks/stargazers)
[![Releases of https://github.com/Naereen/SMPyBandits-benchmarks/](https://badgen.net/github/release/SMPyBandits/SMPyBandits)](https://github.com/Naereen/SMPyBandits-benchmarks/releases)

> [I (Lilian Besson)](https://perso.crans.org/besson/) have [started my PhD](https://perso.crans.org/besson/phd/) in October 2016, and this is a part of my **on going** research since December 2016.
>
> I launched the [documentation](https://smpybandits.github.io/) on March 2017, I wrote my first research articles using this framework in 2017 and decided to (finally) open-source my project in February 2018.
> [![Commits of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/commits/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/commits/master) / [![Date of last commit of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/last-commit/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/commits/master)
> [![Issues of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/issues/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/issues) : [![Open issues of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/open-issues/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/issues?q=is%3Aopen+is%3Aissue) / [![Closed issues of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/closed-issues/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/issues?q=is%3Aclosed+is%3Aissue)

----

## About the benchmarks

TODO

----

## How to cite this work?
If you use this package for your own work, please consider citing it with [this piece of BibTeX](SMPyBandits.bib):


```bibtex
@misc{SMPyBandits,
    title =   {{SMPyBandits: an Open-Source Research Framework for Single and Multi-Players Multi-Arms Bandits (MAB) Algorithms in Python}},
    author =  {Lilian Besson},
    year =    {2018},
    url =     {https://github.com/SMPyBandits/SMPyBandits/},
    howpublished = {Online at: \url{github.com/SMPyBandits/SMPyBandits}},
    note =    {Code at https://github.com/SMPyBandits/SMPyBandits/, documentation at https://smpybandits.github.io/}
}
```

I also wrote a small paper to present *SMPyBandits*, and I will send it to [JMLR MLOSS](http://jmlr.org/mloss/).
The paper can be consulted [here on my website](https://perso.crans.org/besson/articles/SMPyBandits.pdf).

> A DOI will arrive as soon as possible! I tried to publish [a paper](docs/paper/paper.md) on both [JOSS](http://joss.theoj.org/) and [MLOSS](http://mloss.org/software/).

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/SMPyBandits/SMPyBandits.svg)](https://github.com/Naereen/SMPyBandits-benchmarks/blob/master/LICENSE)
[MIT Licensed](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).

© 2016-2018 [Lilian Besson](https://GitHub.com/Naereen), with help [from contributors](https://github.com/Naereen/SMPyBandits-benchmarks/graphs/contributors).

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/SMPyBandits-benchmarks/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/SMPyBandits-benchmarks/README.md?pixel)](https://GitHub.com/Naereen/SMPyBandits-benchmarks/)
[![PyPI version](https://img.shields.io/pypi/v/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![PyPI implementation](https://img.shields.io/pypi/implementation/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/smpybandits.svg?logo=python)](https://pypi.org/project/SMPyBandits)
[![PyPI download](https://img.shields.io/pypi/dm/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![PyPI status](https://img.shields.io/pypi/status/smpybandits.svg)](https://pypi.org/project/SMPyBandits)
[![Documentation Status](https://readthedocs.org/projects/smpybandits/badge/?version=latest)](https://SMPyBandits.ReadTheDocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/SMPyBandits/SMPyBandits.svg?branch=master)](https://travis-ci.org/SMPyBandits/SMPyBandits)

[![Stars of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/stars/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/stargazers) [![Contributors of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/contributors/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/graphs/contributors) [![Watchers of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/watchers/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/watchers) [![Forks of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/forks/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/network/members)

[![Releases of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/release/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/releases)
[![Commits of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/commits/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/commits/master) / [![Date of last commit of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/last-commit/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/commits/master)

[![Issues of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/issues/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/issues) : [![Open issues of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/open-issues/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/issues?q=is%3Aopen+is%3Aissue) / [![Closed issues of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/closed-issues/SMPyBandits/SMPyBandits)](https://github.com/SMPyBandits/SMPyBandits/issues?q=is%3Aclosed+is%3Aissue)

[![Pull requests of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/prs/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/pulls) : [![Open pull requests of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/open-prs/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/issues?q=is%3Aopen+is%3Apr) / [![Closed pull requests of https://github.com/SMPyBandits/SMPyBandits/](https://badgen.net/github/closed-prs/SMPyBandits/SMPyBandits)](https://GitHub.com/SMPyBandits/SMPyBandits/issues?q=is%3Aclose+is%3Apr)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
