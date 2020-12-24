FROM python:3.6-stretch

WORKDIR /usr/src/app

# Configure github deployment ssh keys
RUN apt update && apt install git
RUN mkdir /root/.ssh/
ADD git_rsa /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan -t rsa github.com >> /root/.ssh/known_hosts

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mkdir -p /opt/WebDrivers && \
    mv chromedriver /opt/WebDrivers/

ENV PATH="/opt/WebDrivers:${PATH}"
ENV DISPLAY=:99

# Clone repo and setup pipenv
RUN git clone git@github.com:buyuk-dev/christmass-pizza.git
WORKDIR /usr/src/app/christmass-pizza/
RUN pip install pipenv && \
    pipenv install

# Copy config file
COPY config.py /usr/src/app/christmass-pizza/

# Run order script
ENTRYPOINT pipenv run ./pizza-hut.py --headless

