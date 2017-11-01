#!/usr/bin/env bash
source ~/Desktop/projects/venvs/local/bin/activate
echo “Testing lambda”
python-lambda-local -f $1 $2 $3