#!/bin/bash

# . ./venv/bin/activate
echo 
DIRNAME="$(dirname -- "$(readlink -f "${BASH_SOURCE}")")" # /home/kvogel/projects/general/projects/repos/tabsutra
# echo "$(readlink -f "${BASH_SOURCE}")"

# echo DIRNAME=$DIRNAME
source $DIRNAME/venv/bin/activate

# $DIRNAME/src/test.py
$DIRNAME/src/dev.py
