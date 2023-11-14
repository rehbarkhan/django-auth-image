#!/bin/sh
set -e
# this script will only run in macOS or Linux/Unix
# check and creat the virtualenv
echo 'This script is only for macOS or Linux/Unix.'
echo 'setting up the virtual enviornment'

if [ -d './env' ]; then
    echo 'env dir already present'
else
    python3 -m venv env
fi

echo 'Activating the virtual env'
source env/bin/activate

echo 'Installing the required packages'
pip install -r requirements.txt

echo 'Building the React App for Django'
cd ui
npm i
npm run build
cd ..

echo 'Starting the Django Process Chain'
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo 'Starting the django server on port 8080'
python manage.py runserver 0.0.0.0:8080