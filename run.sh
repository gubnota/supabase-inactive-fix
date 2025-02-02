#!/bin/zsh
##!/bin/bash
# Change to the directory where the script is located
cd "$(dirname "$0")" || exit
echo "$(dirname "$0")"
# source "$HOME"/.bash_profile
# Export necessary environment variables for cron
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export TERM=xterm-256color

# Suppress unnecessary terminal-specific commands
source "$HOME"/.zprofile >/dev/null 2>&1
source "$HOME"/.zshrc >/dev/null 2>&1

# Remove old log file
rm -f cron_env.log

# Run the script with poetry
poetry run python3 main.py >>cron_env.log 2>&1
