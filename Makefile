BUILD_DIR=_build/html
RMDS:=$(wildcard */*.Rmd)
IPYNBS:=$(patsubst %.Rmd,%.ipynb,$(RMDS))

checkout-ipynbs:
	# Reset notebooks to version in repository.
	git checkout */*.ipynb

%.ipynb: %.Rmd
	# Convert .Rmd file to ipynb file.
	jupytext --to ipynb $<

html: bibliography checkout-ipynbs $(IPYNBS)
	# For ucb_pages module
	export PYTHONPATH="${PYTHONPATH}:${PWD}"
	jupyter-book build .

github: html
	# Complain if tree has changes or commit not pushed.
	# My code here.
	ghp-import -n _build/html -p -f

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb

BIBLIOGRAPHIES= bib/data-science-bib/data_science.bib \
				bib/course_refs.bib

bibliography: $(BIBLIOGRAPHIES)
	cat $(BIBLIOGRAPHIES) > _references.bib
