FROM python:3-alpine


# Installs some utils for debugging
ARG DEV_ENV="0"

# set environment variables
ENV DEV_ENV $DEV_ENV
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add build-base
RUN apk add libffi-dev
RUN apk add python3-dev openssl-dev cargo
RUN apk add jpeg-dev zlib-dev

RUN pip install --upgrade pip


WORKDIR /backend
COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY . /backend

ENTRYPOINT [ "python" ]
CMD [ "backend.py"]