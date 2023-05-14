#!/usr/bin/bash

sudo docker compose down -v

if [ $1 = "clean" ]
then
  # sudo rm -rf /event/volumes/static/*
  sudo docker compose up --build -d --scale web=3
else
  sudo docker compose up -d --scale web=3
fi

sudo docker exec progetto_las-web-1 python3 manage.py collectstatic --noinput
