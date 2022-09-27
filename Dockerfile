FROM python:latest



RUN apt -qq update && apt install -yqq pip 



COPY Python/  /opt/apps

WORKDIR /opt/apps

RUN pip install -r requirement.txt

ENV PYTHONUNBUFFERED 1

EXPOSE 8001



CMD python3 ./main.py

