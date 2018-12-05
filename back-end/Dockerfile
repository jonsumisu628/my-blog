FROM python:3.7-stretch
WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD python /back-end/api/app.py
