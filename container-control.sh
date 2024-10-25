#!/bin/bash

action=$1
service_name=$2

if [ -z "$action" ] || [ -z "$service_name" ]; then
  echo "Usage: $0 {start|stop} <service_name>"
  exit 1
fi

if [ "$action" = "start" ]; then
  echo "Starting service: $service_name in the foreground"
  sudo docker-compose up $service_name
elif [ "$action" = "stop" ]; then
  echo "Stopping service: $service_name and removing containers"
  sudo docker-compose stop $service_name
  sudo docker-compose rm $service_name
else
  echo "Invalid action. Use 'start' or 'stop'."
  exit 1
fi
