# Installation


## Chrome Web Driver setup for selenium

    wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    mkdir -p /opt/WebDrivers
    mv chromedriver /opt/WebDrivers/chromedriver
    export PATH=$PATH:/opt/WebDrivers/


## Install python packages

    pipenv install


## Run pizza-hut script

    pipenv run python pizza-hut.py [--headless]


# Running using Docker

## Build container

    docker build -t pizzahut:latest .

## Run container

    docker run -it pizzahut

## Get screenshot in case of error

    # get container id
    docker ps -a | grep pizzahut | head -1 | cut -d' ' -f 1

    # copy screenshot from the container
    docker cp <CONTAINER_ID>::/usr/src/app/christmass-pizza/error.png ./error.png

    # open screenshot
    xdg-open ./error.png

