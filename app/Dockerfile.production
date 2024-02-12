FROM python:3.8-bullseye 

WORKDIR /app
COPY requirements-live.txt .

ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONPATH /app/src

# RUN apt-get update && apt-get upgrade && apt-get install -y netcat

# COPY ./docker-entrypoint.production.sh .
# RUN sed -i 's/\r$//g' /app/docker-entrypoint.production.sh
# RUN chmod +x /app/docker-entrypoint.production.sh

RUN \
     pip install --no-cache-dir -r requirements-live.txt         

COPY . .

# ENTRYPOINT ["/app/docker-entrypoint.production.sh"]