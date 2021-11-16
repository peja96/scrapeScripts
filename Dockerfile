FROM python

ADD LobEuroleague.py .

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 2.42
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir -p $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
RUN chmod +x $CHROMEDRIVER_DIR/chromedriver


# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

RUN apt-get install libxi6 libgconf-2-4 -y
RUN apt-get install -y wget xvfb unzip

RUN chromedriver --version

CMD ["python","-u","./LobEuroleague.py"]
