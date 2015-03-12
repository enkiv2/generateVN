#!/usr/bin/env zsh

if [[ $# -lt 1 ]] ; then
	echo "Usage: $0 VN_NAME"
	exit 1
fi

mkdir $1
mkdir $1/game
python options.py $1 > $1/game/options.rpy
python screens.py $1 > $1/game/screens.rpy
python generateRandomVN.py $1 > $1/game/script.rpy

