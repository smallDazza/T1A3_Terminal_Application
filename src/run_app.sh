#!/bin/bash

# check if python 3 exists. If not displays where users can install from.
if ! command -v python3 &> /dev/null;
then
    echo "Error Found: 
    This application needs Python3 to run. Python3 in not found.
    Please install from this location: https://www.python.org/downloads/" >&2
exit 1
fi

# check if a virtual environment exists. If not = it will create one.
if [ ! -d "../venv" ]; 
then
    echo "Error Found: a virtual environment not found.
    A venv will now be created." >&2
    python3 -m venv ../venv
fi

# activate the virtual environment
source ../venv/bin/activate

# install the python libraries required.
pip install -r requirements.txt


# run the application.
python3 main.py


