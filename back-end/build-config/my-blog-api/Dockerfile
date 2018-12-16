FROM python:3.7-stretch
# `dev` or `prod`
ARG mode="dev"
WORKDIR /srv/app
COPY ./ .
RUN pip install -r requirements/${mode}.txt
CMD python /srv/app/app.py
