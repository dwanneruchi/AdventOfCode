# advent_of_code_2019
Location for storing output from: https://adventofcode.com/


## Working in virtual env: 
```bash
# create venv in dir
python -m venv advent

#activate
source advent/Scripts/activate

# install stuff once activated
pip install -r requirements.txt

```

## Build kernel for virtual env to use in jupyter notebook: Run within venv

```bash
pip install ipykernel
pip install jupyter
python -m ipykernel install --user --name=advent
jupyter notebook
```

## Basic Testing

Attempting to hold myself accountable to unit testing. I am just storing tests within specific day's challenge folder. Once pytest is installed testing is pretty easy: 

```bash
# basic test
python -m pytest test_day01.py

# below could be used to help with 
python -m pytest test_day01.py -x -v
```
