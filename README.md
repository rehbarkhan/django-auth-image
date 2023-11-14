# django-auth-image
React , DRF and Auth File Download

# How to run this project locally
- clone this project
- cd into the project
- start the virtualenv
```
python3 -m venv env
sourc env/bin/activate

```
- install the packages
```
pip install -r requirement.txt
```

### It is very import to build the react project first before starting the django server
```
cd ui
npm i
npm run build
cd ..
```
## Start the djanog server and enjoy.
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8080


## Or you can just execute magic.sh
```
chmod +x magic.sh
./magic.sh

```

# Start the Django Server only.
## If you have already build the project, then from here onward you just need to start the django server

- first activate the virtual env
```
cd 'into_the_project'
source env/bin/activate

```
- run the django server on port 8080
```
python manage.py runserver 0.0.0.0:8080
```