#!/bin/bash

# 1. create virtual env
# we use 'if' statement to check if directory already exits.
# -d flag checks for directories

if [-d ".mlops"]; then
    echo "python venv exists"

else
    echo "u need to create one"

fi

echo "setup complete"
