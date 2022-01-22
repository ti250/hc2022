FROM node:16.2-alpine as build_client
WORKDIR /client
COPY ./client/package.json .
COPY ./client/package-lock.json .
# Installs node modules
RUN npm install -g npm@7.21.0
RUN npm ci
COPY ./client .
# Compiles svelte app into vanilla JS
RUN npm run build

FROM python:3.8-alpine as build_server

# Install dependencies
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --update add --no-cache \
    lapack-dev \
    gcc \
    freetype-dev
RUN apk add --no-cache --virtual .build-deps \
    gfortran \
    musl-dev \
    g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h


WORKDIR /app
COPY requirements.txt .
RUN python -m venv venv
# https://pythonspeed.com/articles/multi-stage-docker-python/
ENV PATH="./venv/bin:$PATH"
RUN pip install -r requirements.txt

FROM python:3.8-alpine as executor
WORKDIR /app
COPY --from=build_client /client/public ./client/public
COPY --from=build_server /app/venv ./venv
ENV PATH="./venv/bin:$PATH"
COPY app.py .
COPY server/ server

EXPOSE 80
ENV FLASK_APP="app"
ENTRYPOINT flask run --host="0.0.0.0" --port=80
