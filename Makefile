#!/usr/bin/env make
# A benchmark of SMPyBandits Policies, for Single-Players multi-armed Bandits algorithms.
#
# - Homepage for the benchmarks: https://github.com/Naereen/SMPyBandits-benchmarks/
# - Homepage: https://SMPyBandits.GitHub.io/
# - Author: Lilian Besson and contributors
# - License: MIT
# - Date: October 2019
SHELL=/usr/bin/env /bin/bash

default:	pull run_stderr publish send preview
quick:	pull run_quick

send:	send_zamok
send_zamok:
	CP --exclude=.git ./.asv/html/ ${Szam}phd/SMPyBandits-benchmarks/

pull:
	git pull
help:
	asv help
# quickstart:
# 	asv quickstart
machine:
	asv machine
setup:
	asv setup
run:
	asv run --verbose
run_profile:
	asv run --profile
run_profile_stderr:
	asv run --profile --show-stderr --verbose
run_stderr:
	asv run --show-stderr --verbose
run_quick:
	asv run --quick --show-stderr --verbose
dev:
	asv dev
continuous:
	asv continuous
find:
	asv find
rm:
	asv rm
publish:
	asv publish --verbose
preview:
	asv preview --verbose
profile:
	asv profile
update:
	asv update
show:
	asv show
compare:
	asv compare
check:
	asv check
gh-pages:
	asv gh-pages
