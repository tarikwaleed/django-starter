FROM python:3.8-bullseye 

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONPATH /app/src

COPY Pipfile Pipfile.lock ./
COPY ./docker-entrypoint.sh .
# this sed command removes carriage return characters from the file
RUN sed -i 's/\r$//g' /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
RUN pip install -U pipenv
RUN pipenv install --system

COPY . .