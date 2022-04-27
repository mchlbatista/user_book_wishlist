FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine AS builder

WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt
COPY ./app .


# FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine AS tester
# WORKDIR /app
# COPY ./requirements.txt ./requirements.test.txt ./
# RUN pip3 install --upgrade pip \
#     && pip3 install -r requirements.test.txt
# COPY ./tests ./tests
