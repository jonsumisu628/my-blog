FROM python:3.7-stretch
# `dev` or `prod`
ARG mode="dev"
RUN apt update -y
# bcrypt https://pypi.org/project/bcrypt/
# For Debian and Ubuntu, the following command will ensure that the required dependencies are installed:
RUN apt install -y build-essential libffi-dev python-dev
COPY requirements requirements
RUN pip install -r requirements/${mode}.txt

WORKDIR /srv/app
COPY ./ .
CMD python /srv/app/app.py
