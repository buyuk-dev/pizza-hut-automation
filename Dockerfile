FROM python:3.6-stretch

WORKDIR /usr/src/app

# Install dependencies
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update && \
    apt-get install -y git google-chrome-stable
RUN pip install pipenv

# Install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mkdir -p /opt/WebDrivers && \
    mv chromedriver /opt/WebDrivers/

# Configure github deployment ssh keys
RUN mkdir /root/.ssh/ && \
    ssh-keyscan -t rsa github.com > /root/.ssh/known_hosts
ADD git_rsa /root/.ssh/id_rsa

# Prepare env for selenium
ENV PATH="/opt/WebDrivers:${PATH}"
ENV DISPLAY=:99

# Clone project from github
RUN git clone git@github.com:buyuk-dev/christmass-pizza.git

# Setup everything
WORKDIR /usr/src/app/christmass-pizza/
RUN pipenv install

# Copy script config
COPY config.py /usr/src/app/christmass-pizza/

# Run order script
ENTRYPOINT pipenv run ./pizza-hut.py --headless
