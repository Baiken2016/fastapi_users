FROM python:3.11

RUN mkdir /fastapi_users

WORKDIR /fastapi_users

COPY requirements.txt .


RUN apt-get update \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

COPY . .


RUN chmod a+x docker/*.sh

ENTRYPOINT ["/fastapi_users/docker/app.sh"]
