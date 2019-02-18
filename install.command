#!/bin/bash
[[ ! -f /usr/local/bin/brew ]] && /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install pygobject3 gtk+3
echo "Installed slydes. You can now open main.py to launch slydes" 