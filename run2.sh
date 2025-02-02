#!/bin/zsh
echo "Cron job started at $(date)" >>/tmp/cron.log
env >>/tmp/cron.log
# ./run.sh 2>&1 >>/tmp/cron.log
echo "Cron job ended at $(date)" >>/tmp/cron.log
