#!/usr/bin/env zsh

if [[ $# -lt 1 ]] ; then
	echo "Usage: $0 VN_NAME"
	exit 1
fi

mkdir $1
mkdir $1/game
python2 options.py $1 > $1/game/options.rpy
python2 screens.py $1 > $1/game/screens.rpy
python2 generateRandomVN.py $1 | sed 's/\t/    /g' > $1/game/script.rpy

