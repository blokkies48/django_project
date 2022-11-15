## Run using virtual env 
### Activate using virtual env
After activating the virtual environment
    cd into political project
    the run server command
        python manage.py runserver 8000

## Using docker
cd into political_project
run the commands if docker is installed
    docker build --tag capstone-3-1 .
    docker run --publish 8000:8000 capstone-3-1
    then go to localhost:8000 in browser 