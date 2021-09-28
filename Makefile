BUILD_DIR=_build/html
RMDS:=$(wildcard */*.Rmd)
IPYNBS:=$(patsubst %.Rmd,%.ipynb,$(RMDS))
CURRENT_BRANCH:=$(shell git rev-parse --abbrev-ref HEAD)

delete-ipynbs:
	# Delete modified ipynb files to force rebuild from .Rmd
	./_scripts/delete_modified.sh

%.ipynb: %.Rmd
	# Convert newer .Rmd file to ipynb file.
	jupytext --to ipynb $<

html: bibliography delete-ipynbs $(IPYNBS)
	# For ucb_pages module
	( export PYTHONPATH="${PYTHONPATH}:${PWD}" && jupyter-book build . )

github: html
	# Complain if tree has changes or commit not pushed.
	# My code here.
	ghp-import -n _build/html -p -f
	echo "Check that you have pushed the '$(CURRENT_BRANCH)' branch up to Github"

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb

BIBLIOGRAPHIES= bib/data-science-bib/data_science.bib \
				bib/course_refs.bib

bibliography: $(BIBLIOGRAPHIES)
	cat $(BIBLIOGRAPHIES) > _references.bib
