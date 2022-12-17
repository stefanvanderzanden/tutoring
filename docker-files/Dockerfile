# This is the dev version
FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV USER appuser
ENV HOME /home/$USER
ENV APP_HOME $HOME/app

RUN apt update
# Install supporting packages
RUN apt install -y vim netcat lsof
# Requirements for psycopg2 package
RUN apt install -y libpq-dev python3-dev
RUN apt install -y build-essential python-dev libpq-dev

# Set work directory
WORKDIR $APP_HOME

RUN pip install --upgrade pip
RUN pip install pipenv

# Copy over the pipfiles
COPY ./Pipfile .
COPY ./Pipfile.lock .

# Install required packages
RUN pipenv install --system --deploy --ignore-pipfile --dev

# Add user
RUN useradd -m $USER && echo $USER:$USER | chpasswd && adduser $USER sudo
# Make home directory owned by $USER
RUN chown -R $USER:$USER $HOME

COPY . $APP_HOME
RUN chown -R $USER:$USER $APP_HOME

USER $USER