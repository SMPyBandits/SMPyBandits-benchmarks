default:	pull run_stderr publish preview

pull:
	git pull
help:
	asv help
quickstart:
	asv quickstart
machine:
	asv machine
setup:
	asv setup
run:
	asv run
run_profile:
	asv run --profile
run_profile_stderr:
	asv run --profile --show-stderr
run_stderr:
	asv run --show-stderr
dev:
	asv dev
continuous:
	asv continuous
find:
	asv find
rm:
	asv rm
publish:
	asv publish
preview:
	asv preview
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
