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


