# Makefile for Stat 159 Final Project (Assumes conda is installed)

ENV_NAME = stat159-project

.PHONY: env
env:
	conda env update -f environment.yml --prune
	bash -ic 'conda activate $(ENV_NAME) && python -m ipykernel install --user --name $(ENV_NAME) --display-name "Python ($(ENV_NAME))"'

.PHONY: all
all:
	bash -ic 'conda activate $(ENV_NAME) && \
	jupyter nbconvert --to notebook --execute final-group23/data_processing.ipynb --output /tmp/data_processing_out.ipynb && \
	jupyter nbconvert --to notebook --execute final-group23/data_analysis_1.ipynb --output /tmp/data_analysis_1_out.ipynb && \
	jupyter nbconvert --to notebook --execute final-group23/data_analysis_2.ipynb --output /tmp/data_analysis_2_out.ipynb && \
	jupyter nbconvert --to notebook --execute main.ipynb --output /tmp/main_out.ipynb'

.PHONY: pdf
pdf:
	myst build --pdf

.PHONY: html
html:
	myst build

.PHONY: clean
clean:
	rm -f outputs/*.png
	rm -f outputs/*.csv
	rm -rf _build/html/