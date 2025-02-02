#!/bin/zsh
echo "Cron job started at $(date)" >>/tmp/cron.log
env >>/tmp/cron.log
# /path/to/your/actual/command 2>&1 >>/tmp/cron.log
echo "Cron job ended at $(date)" >>/tmp/cron.log
