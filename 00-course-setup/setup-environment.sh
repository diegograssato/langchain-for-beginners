#!/bin/bash


if [ -d .venv ]; then
    # If a virtual environment exists, activate it
    rm -rf .venv
fi


if [ ! -f .env ]; then
    # If the .env file does not exist, copy the example
    # and prompt the user to fill it in
    echo "Creating .env file from example..."
    cp -v .env.exemplo .env
    echo "Please fill in the .env file with your credentials."
fi

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install ipykernel


# Set up kernel for Jupyter
python -m ipykernel install --user --name langchain --display-name "Python (langchain)"
pip --disable-pip-version-check --no-cache-dir install -r  requirements.txt
