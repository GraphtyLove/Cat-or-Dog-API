#!/usr/bin/env bash

# Do it one time in the terminal before running this script
# heroku login

heroku container:login
docker build -t registry.heroku.com/test-21-08/web:latest .;
docker push registry.heroku.com/test-21-08/web:latest;
heroku container:release web -a test-21-08;


