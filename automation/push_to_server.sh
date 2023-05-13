#! usr/bin/bash

project_path="/event/deployment/mockup_the-event/"

read -p "Username on server: " server_username

echo "Ok, now let's pull the main branch from the server"
ssh $server_username@139.144.176.188 -p 22 -t "cd $project_path && git pull && sh automation/deploy.sh clean"

