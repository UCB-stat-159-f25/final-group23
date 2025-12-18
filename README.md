[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

# Yelp Review Dataset Analysis
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group23/HEAD?urlpath=%2Fdoc%2Ftree%2Fmain.ipynb)

## Overview

This project uses the Yelp Open Dataset to examine how review text relates to user ratings in online restaurant reviews. We formulate a binary classification task using TF-IDF features and logistic regression to identify linguistic patterns associated with positive and negative reviews. The analysis focuses on reproducibility, interpretability, and transparent comparison of modeling choices rather than optimizing a single predictive model.

## Dataset

The dataset used in this project is the Yelp Open Dataset, available at  
https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/data.  

Example:
```json
{"review_id":"KU_O5udG6zpxOg-VcAEodg","user_id":"mh_-eMZ6K5RLWhZyISBhwA","business_id":"XQfwVwDr-v0ZS3_CbbE5Xw","stars":3.0,"useful":0,"funny":0,"cool":0,"text":"If you decide to eat here, just be aware it is going to take about 2 hours from beginning to end. We have tried it multiple times, because I want to like it! I have been to it's other locations in NJ and never had a bad experience. \n\nThe food is good, but it takes a very long time to come out. The waitstaff is very young, but usually pleasant. We have just had too many experiences where we spent way too long waiting. We usually opt for another diner or restaurant on the weekends, in order to be done quicker.","date":"2018-07-07 22:09:11"}

Because the full Yelp Open Dataset is large, we rely on programmatic subsetting and preprocessing steps to construct a manageable and reproducible analysis dataset. All data processing steps are fully documented in the analysis notebooks, and the final cleaned subset used for modeling is saved locally within the repository to ensure long-term reproducibility.

## Project Website
The project's JupyterBook website can be accessed [here](https://ucb-stat-159-s23.github.io/final-group23.git/main.html)

## Repository Structure

The repository is structured as follows:

* `data/`: Subset of data processed for analysis
* `outputs/`: Contains the generated outputs, including csv files and figures
* `src/`: Contains utility functions and tests for the project
* `main.ipynb`: Main project notebook, providing an overview of the analysis and results
* `data_processing.ipynb`: Notebook containing data cleaning and preprocessing steps
* `data_analysis_1.ipynb` and `data_analysis_2.ipynb`: Notebooks containing data analysis
* `environment.yml`: Environment file with required packages for the project
* `Makefile`: Makefile to build JupyterBook for the repository and manage other tasks

## Setup and Installation

1. Clone this repository:
```python
git clone https://github.com/UCB-stat-159-f25/final-group23.git
cd final-group23
```
2. Create and activate the aemf environment:
```python
conda env create -f environment.yml
conda activate stat159-project
```
3. Set this environment as Jupyter kernel
```python
python -m ipykernel install \
  --user \
  --name stat159-project \
  --display-name "Python (stat159-project)"
```

## Usage

To build the JupyterBook website locally, run:

	make html

To clean up build files, run:

	make clean

To execute all notebooks, run:

	make all

## Testing
To run tests, navigate to the root directory of the project and execute the following command:
	
	PYTHONPATH=./ pytest

## License

This project is licensed under the BSD 3-Clause License.