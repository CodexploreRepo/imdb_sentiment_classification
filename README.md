# IMDB Sentiment Classification

## Installation

From the source directory run the following commands

#### Virtual Env Creation & Activation

- `python -m venv venv` for initialising the virtual environment
- `source venv/bin/activate` for activating the virtual environment
- `pip install --upgrade pip` for upgrading the pip

#### Dependency Installation

The following commands shall be ran **after activating the virtual environment**.

- `pip install -r requirements.txt` for the functional dependencies
- `pip install -r requirements-dev.txt` for the development dependencies. (should include `pre-commit` module)
- `pre-commit install` for installing the precommit hook
