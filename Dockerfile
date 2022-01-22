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
COPY server.py .
COPY server/ server

EXPOSE 80
ENV FLASK_APP="server"
ENTRYPOINT flask run --host="0.0.0.0" --port=80
