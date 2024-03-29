BUILD_DIR=_build/html
RMDS:=$(wildcard */*.Rmd)
IPYNBS:=$(patsubst %.Rmd,%.ipynb,$(RMDS))

delete-ipynbs:
	# Delete modified ipynb files to force rebuild from .Rmd
	./_scripts/delete_modified.sh

%.ipynb: %.Rmd
	# Convert newer .Rmd file to ipynb file.
	jupytext --to ipynb $<

html: suid bibliography delete-ipynbs $(IPYNBS)
	# For ucb_pages module
	( export PYTHONPATH="${PYTHONPATH}:${PWD}" && jupyter-book build . )

github: html
	ghp-import -n _build/html -p -f
	./_scripts/check_pushed.sh

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb

BIBLIOGRAPHIES= bib/data-science-bib/data_science.bib \
				bib/course_refs.bib

bibliography: $(BIBLIOGRAPHIES)
	cat $(BIBLIOGRAPHIES) > _references.bib

suid:
	git submodule update --init --recursive
