FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt


